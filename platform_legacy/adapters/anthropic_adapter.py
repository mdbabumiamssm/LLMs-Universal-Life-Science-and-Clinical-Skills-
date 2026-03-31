# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Anthropic Claude adapter for the BioKernel platform.

Provides real integration with the Anthropic Messages API, supporting:
- Single-turn generation
- Multi-turn agentic tool-use loops
- Streaming responses
- Extended thinking
"""

from __future__ import annotations

import os
import time
from typing import Any, AsyncIterator, Dict, List, Optional

from platform.interface.llm_provider import LLMProvider
from platform.observability import get_logger
from platform.schema.io_types import (
    FinishReason,
    LLMRequest,
    LLMResponse,
    ToolCall,
    ToolDefinition,
    ToolResult,
)

logger = get_logger("anthropic_adapter")

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False


class AnthropicAdapter(LLMProvider):
    """
    LLM provider adapter for Anthropic's Claude models.

    Wraps the ``anthropic`` Python SDK to conform to the BioKernel
    ``LLMProvider`` interface, enabling unified skill execution.
    """

    def __init__(self) -> None:
        self._client: Optional[Any] = None
        self._async_client: Optional[Any] = None
        self._model: str = "claude-sonnet-4-20250514"
        self._available: bool = False
        self._config: Dict[str, Any] = {}

    # -- LLMProvider interface ------------------------------------------------

    @property
    def provider_name(self) -> str:
        return "anthropic"

    @property
    def is_available(self) -> bool:
        return self._available

    def initialize(self, config: Dict[str, Any]) -> bool:
        self._config = config
        api_key = config.get("api_key") or os.getenv(
            config.get("api_key_env", "ANTHROPIC_API_KEY")
        )
        self._model = config.get("model", "claude-sonnet-4-20250514")

        if not HAS_ANTHROPIC:
            logger.warning("anthropic package not installed — run: pip install anthropic")
            return False

        if not api_key:
            logger.warning("No Anthropic API key found")
            return False

        try:
            self._client = anthropic.Anthropic(api_key=api_key)
            self._async_client = anthropic.AsyncAnthropic(api_key=api_key)
            self._available = True
            logger.info("Anthropic adapter initialized", model=self._model)
            return True
        except Exception as exc:
            logger.error("Anthropic initialization failed", error=str(exc))
            return False

    async def generate(self, request: LLMRequest) -> LLMResponse:
        if not self._available or self._async_client is None:
            return self._error_response("Anthropic adapter not available")

        start = time.perf_counter()
        try:
            messages = self._build_messages(request)
            kwargs: Dict[str, Any] = {
                "model": self._model,
                "max_tokens": request.max_tokens,
                "temperature": request.temperature,
                "messages": messages,
            }
            if request.system_instruction:
                kwargs["system"] = request.system_instruction
            if request.stop_sequences:
                kwargs["stop_sequences"] = request.stop_sequences
            if request.tools:
                kwargs["tools"] = self._convert_tools(request.tools)

            response = await self._async_client.messages.create(**kwargs)
            latency = (time.perf_counter() - start) * 1000

            text_parts = []
            tool_calls = []
            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
                elif block.type == "tool_use":
                    tool_calls.append(
                        ToolCall(id=block.id, name=block.name, arguments=block.input)
                    )

            finish = self._map_stop_reason(response.stop_reason)

            return LLMResponse(
                text="\n".join(text_parts),
                tool_calls=tool_calls if tool_calls else None,
                finish_reason=finish,
                usage={
                    "prompt_tokens": response.usage.input_tokens,
                    "completion_tokens": response.usage.output_tokens,
                    "total_tokens": response.usage.input_tokens + response.usage.output_tokens,
                },
                latency_ms=latency,
                provider="anthropic",
                model=response.model,
            )
        except Exception as exc:
            latency = (time.perf_counter() - start) * 1000
            logger.error("Anthropic generate failed", error=str(exc), latency_ms=latency)
            return self._error_response(str(exc), latency)

    async def generate_with_tools(
        self,
        request: LLMRequest,
        tool_executor: Optional[Any] = None,
        max_iterations: int = 10,
    ) -> LLMResponse:
        """
        Multi-turn agentic loop: generate → tool_call → tool_result → generate …

        Keeps running until the model stops requesting tools or we hit the
        iteration limit.
        """
        if not self._available:
            return self._error_response("Anthropic adapter not available")

        messages = self._build_messages(request)
        total_usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        all_text: List[str] = []
        all_tools_used: List[str] = []
        total_start = time.perf_counter()

        for iteration in range(max_iterations):
            kwargs: Dict[str, Any] = {
                "model": self._model,
                "max_tokens": request.max_tokens,
                "temperature": request.temperature,
                "messages": messages,
            }
            if request.system_instruction:
                kwargs["system"] = request.system_instruction
            if request.tools:
                kwargs["tools"] = self._convert_tools(request.tools)

            response = await self._async_client.messages.create(**kwargs)

            # Accumulate usage
            total_usage["prompt_tokens"] += response.usage.input_tokens
            total_usage["completion_tokens"] += response.usage.output_tokens
            total_usage["total_tokens"] += (
                response.usage.input_tokens + response.usage.output_tokens
            )

            # Parse response blocks
            text_parts = []
            tool_calls = []
            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
                elif block.type == "tool_use":
                    tool_calls.append(
                        ToolCall(id=block.id, name=block.name, arguments=block.input)
                    )
                    all_tools_used.append(block.name)

            if text_parts:
                all_text.extend(text_parts)

            # If no tool calls or no executor, we're done
            if not tool_calls or tool_executor is None:
                break

            # Add assistant message with tool use to conversation
            messages.append({"role": "assistant", "content": response.content})

            # Execute tools and add results
            tool_results = []
            for tc in tool_calls:
                try:
                    result = await tool_executor(tc)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": tc.id,
                        "content": str(result.output) if isinstance(result, ToolResult) else str(result),
                    })
                except Exception as exc:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": tc.id,
                        "content": f"Error: {exc}",
                        "is_error": True,
                    })

            messages.append({"role": "user", "content": tool_results})

            # If the model indicated it's done, stop
            if response.stop_reason == "end_turn":
                break

        total_latency = (time.perf_counter() - total_start) * 1000

        return LLMResponse(
            text="\n".join(all_text),
            finish_reason=FinishReason.STOP,
            usage=total_usage,
            latency_ms=total_latency,
            provider="anthropic",
            model=self._model,
        )

    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        if not self._available or self._async_client is None:
            yield "[Error: Anthropic adapter not available]"
            return

        messages = self._build_messages(request)
        kwargs: Dict[str, Any] = {
            "model": self._model,
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
            "messages": messages,
        }
        if request.system_instruction:
            kwargs["system"] = request.system_instruction

        async with self._async_client.messages.stream(**kwargs) as stream:
            async for text in stream.text_stream:
                yield text

    # -- Helpers --------------------------------------------------------------

    def _build_messages(self, request: LLMRequest) -> List[Dict[str, Any]]:
        if request.messages:
            return [{"role": m.role, "content": m.content} for m in request.messages]
        return [{"role": "user", "content": request.query}]

    @staticmethod
    def _convert_tools(tools: List[ToolDefinition]) -> List[Dict[str, Any]]:
        return [
            {
                "name": t.name,
                "description": t.description,
                "input_schema": t.input_schema or {"type": "object", "properties": {}},
            }
            for t in tools
        ]

    @staticmethod
    def _map_stop_reason(reason: str | None) -> FinishReason:
        mapping = {
            "end_turn": FinishReason.STOP,
            "stop_sequence": FinishReason.STOP,
            "max_tokens": FinishReason.LENGTH,
            "tool_use": FinishReason.TOOL_CALLS,
        }
        return mapping.get(reason or "", FinishReason.STOP)

    def _error_response(self, message: str, latency_ms: float = 0.0) -> LLMResponse:
        return LLMResponse(
            text=f"Error: {message}",
            finish_reason=FinishReason.ERROR,
            provider="anthropic",
            model=self._model,
            latency_ms=latency_ms,
        )
