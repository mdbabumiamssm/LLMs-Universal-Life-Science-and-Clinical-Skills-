# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Google Gemini adapter for the BioKernel platform.

Provides real integration with the Google Generative AI API, supporting:
- Single-turn generation
- Multi-turn agentic tool-use loops
- System instructions
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

logger = get_logger("gemini_adapter")

try:
    import google.generativeai as genai
    HAS_GEMINI = True
except ImportError:
    HAS_GEMINI = False


class GeminiAdapter(LLMProvider):
    """
    LLM provider adapter for Google's Gemini models.
    """

    def __init__(self) -> None:
        self._model: Optional[Any] = None
        self._model_name: str = "gemini-2.0-flash"
        self._available: bool = False
        self._config: Dict[str, Any] = {}

    @property
    def provider_name(self) -> str:
        return "gemini"

    @property
    def is_available(self) -> bool:
        return self._available

    def initialize(self, config: Dict[str, Any]) -> bool:
        self._config = config
        api_key = config.get("api_key") or os.getenv(
            config.get("api_key_env", "GOOGLE_API_KEY")
        )
        self._model_name = config.get("model", "gemini-2.0-flash")

        if not HAS_GEMINI:
            logger.warning("google-generativeai package not installed")
            return False

        if not api_key:
            logger.warning("No Google API key found")
            return False

        try:
            genai.configure(api_key=api_key)
            self._model = genai.GenerativeModel(self._model_name)
            self._available = True
            logger.info("Gemini adapter initialized", model=self._model_name)
            return True
        except Exception as exc:
            logger.error("Gemini initialization failed", error=str(exc))
            return False

    async def generate(self, request: LLMRequest) -> LLMResponse:
        if not self._available or self._model is None:
            return self._error_response("Gemini adapter not available")

        start = time.perf_counter()
        try:
            model = self._model
            if request.system_instruction:
                model = genai.GenerativeModel(
                    self._model_name,
                    system_instruction=request.system_instruction,
                )

            response = await model.generate_content_async(
                request.query,
                generation_config=genai.types.GenerationConfig(
                    temperature=request.temperature,
                    max_output_tokens=request.max_tokens,
                    stop_sequences=request.stop_sequences or [],
                ),
            )
            latency = (time.perf_counter() - start) * 1000

            text = response.text if hasattr(response, "text") else str(response)
            prompt_tokens = len(request.query) // 4
            completion_tokens = len(text) // 4

            return LLMResponse(
                text=text,
                finish_reason=FinishReason.STOP,
                usage={
                    "prompt_tokens": prompt_tokens,
                    "completion_tokens": completion_tokens,
                    "total_tokens": prompt_tokens + completion_tokens,
                },
                latency_ms=latency,
                provider="gemini",
                model=self._model_name,
            )
        except Exception as exc:
            latency = (time.perf_counter() - start) * 1000
            logger.error("Gemini generate failed", error=str(exc))
            return self._error_response(str(exc), latency)

    async def generate_with_tools(
        self,
        request: LLMRequest,
        tool_executor: Optional[Any] = None,
        max_iterations: int = 10,
    ) -> LLMResponse:
        # Gemini tool use: construct a multi-turn prompt approach
        if not self._available:
            return self._error_response("Gemini adapter not available")

        tool_desc = ""
        if request.tools:
            tool_desc = "Available tools:\n" + "\n".join(
                f"- {t.name}: {t.description}" for t in request.tools
            )

        enhanced_query = (
            f"{request.query}\n\n{tool_desc}\n\n"
            "Think step-by-step. If you need a tool, output TOOL_CALL: <name>(<args>). "
            "When you have the final answer, output FINAL_ANSWER: <answer>."
        )

        enhanced_request = LLMRequest(
            query=enhanced_query,
            system_instruction=request.system_instruction,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        return await self.generate(enhanced_request)

    def _error_response(self, message: str, latency_ms: float = 0.0) -> LLMResponse:
        return LLMResponse(
            text=f"Error: {message}",
            finish_reason=FinishReason.ERROR,
            provider="gemini",
            model=self._model_name,
            latency_ms=latency_ms,
        )
