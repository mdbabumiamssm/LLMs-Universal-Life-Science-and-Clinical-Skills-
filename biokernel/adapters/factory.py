# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
LLM Provider Factory — Workflow Abstraction Layer (WAL).

Creates and manages LLM provider instances from configuration,
enabling dynamic provider selection and runtime switching.
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type

from biokernel.interface.llm_provider import LLMProvider
from biokernel.observability import get_logger

logger = get_logger("llm_factory")


class LLMFactory:
    """
    Factory for creating and caching LLM provider instances.

    Supports dynamic provider registration, so plugins can add custom
    providers at runtime.
    """

    _registry: Dict[str, Type[LLMProvider]] = {}
    _instances: Dict[str, LLMProvider] = {}

    @classmethod
    def register_provider(cls, name: str, provider_cls: Type[LLMProvider]) -> None:
        """Register a provider class under a given name."""
        cls._registry[name.lower()] = provider_cls
        logger.info("Provider registered", name=name)

    @classmethod
    def register_defaults(cls) -> None:
        """Register the built-in provider adapters."""
        from biokernel.adapters.anthropic_adapter import AnthropicAdapter
        from biokernel.adapters.openai_runtime_adapter import OpenAIRuntimeAdapter
        from biokernel.adapters.gemini_adapter import GeminiAdapter
        from biokernel.adapters.local_adapter import LocalAdapter

        cls._registry.setdefault("anthropic", AnthropicAdapter)
        cls._registry.setdefault("openai", OpenAIRuntimeAdapter)
        cls._registry.setdefault("gemini", GeminiAdapter)
        cls._registry.setdefault("local", LocalAdapter)

    @classmethod
    def create_provider(
        cls,
        provider_name: str,
        config: Dict[str, Any],
        *,
        cache: bool = True,
    ) -> LLMProvider:
        """
        Create (or return cached) a provider instance.

        Args:
            provider_name: One of the registered provider names.
            config: Provider-specific configuration.
            cache: If True, reuse an existing instance for this name.

        Returns:
            An initialized ``LLMProvider`` instance.

        Raises:
            ValueError: If the provider name is not registered.
        """
        key = provider_name.lower()

        if cache and key in cls._instances:
            return cls._instances[key]

        if not cls._registry:
            cls.register_defaults()

        provider_cls = cls._registry.get(key)
        if provider_cls is None:
            available = ", ".join(cls._registry.keys())
            raise ValueError(
                f"Unknown provider '{provider_name}'. Available: {available}"
            )

        instance = provider_cls()
        success = instance.initialize(config)

        if not success:
            logger.warning("Provider initialization returned False", provider=key)

        if cache:
            cls._instances[key] = instance

        return instance

    @classmethod
    def get_provider(cls, name: str) -> Optional[LLMProvider]:
        """Get a cached provider by name, or None if not initialized."""
        return cls._instances.get(name.lower())

    @classmethod
    def list_providers(cls) -> Dict[str, bool]:
        """Return a dict of provider_name → is_available."""
        if not cls._registry:
            cls.register_defaults()
        result: Dict[str, bool] = {}
        for name in cls._registry:
            instance = cls._instances.get(name)
            result[name] = instance.is_available if instance else False
        return result

    @classmethod
    def reset(cls) -> None:
        """Clear all cached instances (useful for testing)."""
        cls._instances.clear()
