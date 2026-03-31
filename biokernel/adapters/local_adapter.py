# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Local LLM adapter for the BioKernel platform.

Connects to locally running models via Ollama or any OpenAI-compatible
API endpoint (e.g., vLLM, llama.cpp server, LM Studio).
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

from biokernel.interface.llm_provider import LLMProvider
from biokernel.observability import get_logger
from biokernel.schema.io_types import (
    FinishReason,
    LLMRequest,
    LLMResponse,
    ToolDefinition,
)

logger = get_logger("local_adapter")

try:
    import httpx
    HAS_HTTPX = True
except ImportError:
    HAS_HTTPX = False

try:
    import ollama as ollama_lib
    HAS_OLLAMA = True
except ImportError:
    HAS_OLLAMA = False


class LocalAdapter(LLMProvider):
    """
    LLM provider adapter for locally hosted models.

    Supports two backends:
    1. **Ollama** (preferred): Direct integration via the ollama Python SDK.
    2. **OpenAI-compatible**: Any server exposing ``/v1/chat/completions``
       (e.g., vLLM, llama.cpp, LM Studio).
    """

    def __init__(self) -> None:
        self._model: str = "llama3.1:8b"
        self._api_base: str = "http://localhost:11434"
        self._available: bool = False
        self._backend: str = "none"  # "ollama" or "openai_compat"

    @property
    def provider_name(self) -> str:
        return "local"

    @property
    def is_available(self) -> bool:
        return self._available

    def initialize(self, config: Dict[str, Any]) -> bool:
        self._model = config.get("model", "llama3.1:8b")
        self._api_base = config.get("api_base", "http://localhost:11434")

        if HAS_OLLAMA:
            try:
                # Test connection
                ollama_lib.list()
                self._backend = "ollama"
                self._available = True
                logger.info("Local adapter initialized (Ollama)", model=self._model)
                return True
            except Exception:
                logger.info("Ollama not reachable, trying OpenAI-compat endpoint")

        if HAS_HTTPX:
            try:
                import httpx
                resp = httpx.get(f"{self._api_base}/api/tags", timeout=5)
                if resp.status_code == 200:
                    self._backend = "openai_compat"
                    self._available = True
                    logger.info("Local adapter initialized (OpenAI-compat)", base=self._api_base)
                    return True
            except Exception:
                pass

        logger.warning("No local LLM backend reachable")
        return False

    async def generate(self, request: LLMRequest) -> LLMResponse:
        if not self._available:
            return self._error_response("Local adapter not available")

        start = time.perf_counter()

        if self._backend == "ollama" and HAS_OLLAMA:
            return await self._generate_ollama(request, start)
        elif self._backend == "openai_compat" and HAS_HTTPX:
            return await self._generate_openai_compat(request, start)

        return self._error_response("No backend configured")

    async def generate_with_tools(
        self,
        request: LLMRequest,
        tool_executor: Optional[Any] = None,
        max_iterations: int = 10,
    ) -> LLMResponse:
        # Most local models have limited tool-use support;
        # we embed tool descriptions in the prompt and parse the output.
        tool_desc = ""
        if request.tools:
            tool_desc = "\n\nAvailable tools:\n" + "\n".join(
                f"- {t.name}: {t.description}" for t in request.tools
            )

        enhanced = LLMRequest(
            query=request.query + tool_desc,
            system_instruction=request.system_instruction,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        return await self.generate(enhanced)

    # -- Backend implementations ----------------------------------------------

    async def _generate_ollama(self, request: LLMRequest, start: float) -> LLMResponse:
        try:
            messages = []
            if request.system_instruction:
                messages.append({"role": "system", "content": request.system_instruction})
            messages.append({"role": "user", "content": request.query})

            response = ollama_lib.chat(
                model=self._model,
                messages=messages,
                options={"temperature": request.temperature, "num_predict": request.max_tokens},
            )
            latency = (time.perf_counter() - start) * 1000
            text = response["message"]["content"]

            return LLMResponse(
                text=text,
                finish_reason=FinishReason.STOP,
                usage={
                    "prompt_tokens": response.get("prompt_eval_count", 0),
                    "completion_tokens": response.get("eval_count", 0),
                    "total_tokens": response.get("prompt_eval_count", 0)
                    + response.get("eval_count", 0),
                },
                latency_ms=latency,
                provider="local/ollama",
                model=self._model,
            )
        except Exception as exc:
            return self._error_response(str(exc), (time.perf_counter() - start) * 1000)

    async def _generate_openai_compat(self, request: LLMRequest, start: float) -> LLMResponse:
        try:
            import httpx

            messages = []
            if request.system_instruction:
                messages.append({"role": "system", "content": request.system_instruction})
            messages.append({"role": "user", "content": request.query})

            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    f"{self._api_base}/v1/chat/completions",
                    json={
                        "model": self._model,
                        "messages": messages,
                        "temperature": request.temperature,
                        "max_tokens": request.max_tokens,
                    },
                    timeout=120,
                )
                data = resp.json()

            latency = (time.perf_counter() - start) * 1000
            text = data["choices"][0]["message"]["content"]

            return LLMResponse(
                text=text,
                finish_reason=FinishReason.STOP,
                usage=data.get("usage", {}),
                latency_ms=latency,
                provider="local/openai_compat",
                model=self._model,
            )
        except Exception as exc:
            return self._error_response(str(exc), (time.perf_counter() - start) * 1000)

    def _error_response(self, message: str, latency_ms: float = 0.0) -> LLMResponse:
        return LLMResponse(
            text=f"Error: {message}",
            finish_reason=FinishReason.ERROR,
            provider="local",
            model=self._model,
            latency_ms=latency_ms,
        )
