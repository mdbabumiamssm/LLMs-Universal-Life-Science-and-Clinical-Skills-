# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Unified Runtime Adapter — convenience wrapper around the LLM Factory.

Provides a simple ``llm`` singleton for legacy code that expects a
direct ``complete()`` interface. New code should use the factory directly.
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

from biokernel.adapters.factory import LLMFactory
from biokernel.interface.llm_provider import LLMProvider
from biokernel.schema.io_types import LLMRequest


class RuntimeLLMAdapter:
    """
    Convenience adapter that delegates to the best available LLM provider.

    Tries providers in preference order: anthropic → openai → gemini → local.
    """

    def __init__(self) -> None:
        self._provider: Optional[LLMProvider] = None
        self._initialize()

    def _initialize(self) -> None:
        """Try to initialize the best available provider."""
        LLMFactory.register_defaults()

        preference_order = ["anthropic", "openai", "gemini", "local"]
        for name in preference_order:
            try:
                config = self._get_config_for(name)
                provider = LLMFactory.create_provider(name, config)
                if provider.is_available:
                    self._provider = provider
                    return
            except Exception:
                continue

    @staticmethod
    def _get_config_for(name: str) -> Dict[str, Any]:
        """Build config from environment variables."""
        env_keys = {
            "anthropic": "ANTHROPIC_API_KEY",
            "openai": "OPENAI_API_KEY",
            "gemini": "GOOGLE_API_KEY",
        }
        config: Dict[str, Any] = {}
        if name in env_keys:
            config["api_key"] = os.getenv(env_keys[name], "")
        return config

    def complete(self, system: str, user_prompt: str, model: str = "default") -> str:
        """
        Synchronous completion for legacy compatibility.

        For new code, use the async LLMProvider.generate() interface instead.
        """
        import asyncio

        if self._provider is None:
            return "[No LLM provider available. Set ANTHROPIC_API_KEY, OPENAI_API_KEY, or GOOGLE_API_KEY.]"

        req = LLMRequest(
            query=user_prompt,
            system_instruction=system,
            temperature=0.3,
        )

        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as pool:
                    resp = pool.submit(asyncio.run, self._provider.generate(req)).result()
            else:
                resp = asyncio.run(self._provider.generate(req))
            return resp.text
        except Exception as exc:
            return f"[LLM Error: {exc}]"


# Singleton for backward compatibility
llm = RuntimeLLMAdapter()
