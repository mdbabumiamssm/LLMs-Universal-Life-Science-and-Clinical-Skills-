# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
OpenAI runtime adapter for the BioKernel platform.

Provides real integration with the OpenAI Chat Completions API, supporting:
- Single-turn generation
- Multi-turn agentic tool-use loops (function calling)
- Streaming responses
"""

from __future__ import annotations

import json
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

logger = get_logger("openai_adapter")

try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


class OpenAIRuntimeAdapter(LLMProvider):
    """
    LLM provider adapter for OpenAI models (GPT-4o, o1, etc.).
    """

    def __init__(self) -> None:
        self._client: Optional[Any] = None
        self._async_client: Optional[Any] = None
        self._model: str = "gpt-4o"
        self._available: bool = False
        self._config: Dict[str, Any] = {}

    @property
    def provider_name(self) -> str:
        return "openai"

    @property
    def is_available(self) -> bool:
        return self._available

    def initialize(self, config: Dict[str, Any]) -> bool:
        self._config = config
        api_key = config.get("api_key") or os.getenv(
            config.get("api_key_env", "OPENAI_API_KEY")
        )
        self._model = config.get("model", "gpt-4o")

        if not HAS_OPENAI:
            logger.warning("openai package not installed — run: pip install openai")
            return False

        if not api_key:
            logger.warning("No OpenAI API key found")
            return False

        try:
            self._client = openai.OpenAI(api_key=api_key)
            self._async_client = openai.AsyncOpenAI(api_key=api_key)
            self._available = True
            logger.info("OpenAI adapter initialized", model=self._model)
            return True
        except Exception as exc:
            logger.error("OpenAI initialization failed", error=str(exc))
            return False

    async def generate(self, request: LLMRequest) -> LLMResponse:
        if not self._available or self._async_client is None:
            return self._error_response("OpenAI adapter not available")

        start = time.perf_counter()
        try:
            messages = self._build_messages(request)
            kwargs: Dict[str, Any] = {
                "model": self._model,
                "messages": messages,
                "max_completion_tokens": request.max_tokens,
                "temperature": request.temperature,
            }
            if request.tools:
                kwargs["tools"] = self._convert_tools(request.tools)
            if request.stop_sequences:
                kwargs["stop"] = request.stop_sequences
            if request.response_format == "json":
                kwargs["response_format"] = {"type": "json_object"}

            response = await self._async_client.chat.completions.create(**kwargs)
            latency = (time.perf_counter() - start) * 1000

            choice = response.choices[0]
            text = choice.message.content or ""
            tool_calls = None

            if choice.message.tool_calls:
                tool_calls = [
                    ToolCall(
                        id=tc.id,
                        name=tc.function.name,
                        arguments=json.loads(tc.function.arguments),
                    )
                    for tc in choice.message.tool_calls
                ]

            return LLMResponse(
                text=text,
                tool_calls=tool_calls,
                finish_reason=self._map_finish_reason(choice.finish_reason),
                usage={
                    "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                    "completion_tokens": response.usage.completion_tokens if response.usage else 0,
                    "total_tokens": response.usage.total_tokens if response.usage else 0,
                },
                latency_ms=latency,
                provider="openai",
                model=response.model,
            )
        except Exception as exc:
            latency = (time.perf_counter() - start) * 1000
            logger.error("OpenAI generate failed", error=str(exc))
            return self._error_response(str(exc), latency)

    async def generate_with_tools(
        self,
        request: LLMRequest,
        tool_executor: Optional[Any] = None,
        max_iterations: int = 10,
    ) -> LLMResponse:
        if not self._available:
            return self._error_response("OpenAI adapter not available")

        messages = self._build_messages(request)
        total_usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        all_text: List[str] = []
        total_start = time.perf_counter()

        for _ in range(max_iterations):
            kwargs: Dict[str, Any] = {
                "model": self._model,
                "messages": messages,
                "max_completion_tokens": request.max_tokens,
                "temperature": request.temperature,
            }
            if request.tools:
                kwargs["tools"] = self._convert_tools(request.tools)

            response = await self._async_client.chat.completions.create(**kwargs)
            choice = response.choices[0]

            if response.usage:
                total_usage["prompt_tokens"] += response.usage.prompt_tokens
                total_usage["completion_tokens"] += response.usage.completion_tokens
                total_usage["total_tokens"] += response.usage.total_tokens

            if choice.message.content:
                all_text.append(choice.message.content)

            if not choice.message.tool_calls or tool_executor is None:
                break

            # Add assistant message to conversation
            messages.append(choice.message.model_dump())

            # Execute tools
            for tc in choice.message.tool_calls:
                tool_call = ToolCall(
                    id=tc.id,
                    name=tc.function.name,
                    arguments=json.loads(tc.function.arguments),
                )
                try:
                    result = await tool_executor(tool_call)
                    content = str(result.output) if isinstance(result, ToolResult) else str(result)
                except Exception as exc:
                    content = f"Error: {exc}"

                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": content,
                })

            if choice.finish_reason != "tool_calls":
                break

        total_latency = (time.perf_counter() - total_start) * 1000
        return LLMResponse(
            text="\n".join(all_text),
            finish_reason=FinishReason.STOP,
            usage=total_usage,
            latency_ms=total_latency,
            provider="openai",
            model=self._model,
        )

    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        if not self._available or self._async_client is None:
            yield "[Error: OpenAI adapter not available]"
            return

        messages = self._build_messages(request)
        stream = await self._async_client.chat.completions.create(
            model=self._model,
            messages=messages,
            max_completion_tokens=request.max_tokens,
            temperature=request.temperature,
            stream=True,
        )
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    # -- Helpers --------------------------------------------------------------

    def _build_messages(self, request: LLMRequest) -> List[Dict[str, Any]]:
        msgs: List[Dict[str, Any]] = []
        if request.system_instruction:
            msgs.append({"role": "system", "content": request.system_instruction})
        if request.messages:
            msgs.extend({"role": m.role, "content": m.content} for m in request.messages)
        else:
            msgs.append({"role": "user", "content": request.query})
        return msgs

    @staticmethod
    def _convert_tools(tools: List[ToolDefinition]) -> List[Dict[str, Any]]:
        return [
            {
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description,
                    "parameters": t.input_schema or {"type": "object", "properties": {}},
                },
            }
            for t in tools
        ]

    @staticmethod
    def _map_finish_reason(reason: str | None) -> FinishReason:
        mapping = {
            "stop": FinishReason.STOP,
            "length": FinishReason.LENGTH,
            "tool_calls": FinishReason.TOOL_CALLS,
            "content_filter": FinishReason.CONTENT_FILTER,
        }
        return mapping.get(reason or "", FinishReason.STOP)

    def _error_response(self, message: str, latency_ms: float = 0.0) -> LLMResponse:
        return LLMResponse(
            text=f"Error: {message}",
            finish_reason=FinishReason.ERROR,
            provider="openai",
            model=self._model,
            latency_ms=latency_ms,
        )
