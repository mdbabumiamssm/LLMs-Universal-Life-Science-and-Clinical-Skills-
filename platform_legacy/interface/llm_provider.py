# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Abstract base class for all LLM providers.

Every provider (Anthropic, OpenAI, Gemini, Local) must implement this
interface to participate in the BioKernel orchestration layer.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Dict, List, Optional

from platform.schema.io_types import (
    LLMRequest,
    LLMResponse,
    ToolCall,
    ToolDefinition,
    ToolResult,
)


class LLMProvider(ABC):
    """
    Abstract base class for LLM provider adapters.

    Each adapter normalizes a specific provider's API into the BioKernel's
    unified ``LLMRequest`` / ``LLMResponse`` schema, enabling write-once
    skills to execute on any supported backend.
    """

    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> bool:
        """
        Configure the provider with API keys, model names, and parameters.

        Args:
            config: Provider-specific configuration dictionary.

        Returns:
            True if initialization succeeded, False otherwise.
        """
        ...

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Canonical name of this provider (e.g., 'anthropic', 'openai')."""
        ...

    @property
    @abstractmethod
    def is_available(self) -> bool:
        """Whether the provider is initialized and ready to serve requests."""
        ...

    @abstractmethod
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """
        Generate a response for a single-turn request.

        Args:
            request: Standardized LLM request.

        Returns:
            Standardized LLM response.
        """
        ...

    @abstractmethod
    async def generate_with_tools(
        self,
        request: LLMRequest,
        tool_executor: Optional[Any] = None,
        max_iterations: int = 10,
    ) -> LLMResponse:
        """
        Execute a multi-turn agentic loop with tool use.

        The provider sends a request, checks for tool calls, executes them
        via ``tool_executor``, and feeds results back until the model stops
        requesting tools or ``max_iterations`` is reached.

        Args:
            request: The initial LLM request (must include tool definitions).
            tool_executor: Callable that maps ToolCall → ToolResult.
            max_iterations: Safety bound on agentic loop depth.

        Returns:
            Final LLM response after all tool iterations.
        """
        ...

    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        """
        Stream response tokens. Default implementation falls back to generate().

        Yields:
            Individual text chunks as they arrive.
        """
        response = await self.generate(request)
        yield response.text

    async def check_health(self) -> Dict[str, Any]:
        """
        Probe whether the provider is reachable and responding.

        Returns:
            Dict with 'healthy' bool and optional diagnostics.
        """
        if not self.is_available:
            return {"healthy": False, "reason": "Provider not initialized"}
        try:
            test_req = LLMRequest(query="Hello", max_tokens=5, temperature=0.0)
            resp = await self.generate(test_req)
            return {"healthy": True, "latency_ms": resp.latency_ms, "model": resp.model}
        except Exception as exc:
            return {"healthy": False, "reason": str(exc)}
