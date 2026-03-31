# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Meta-Prompter: Cross-platform prompt optimization.

Transforms a generic biomedical prompt into provider-specific formats
that leverage each LLM's unique strengths:

- **Claude (Anthropic)**: XML structure, thinking blocks, pre-fill patterns
- **OpenAI (GPT-4o)**: Concise system messages, JSON mode hints, function schemas
- **Gemini (Google)**: Long-context role cards, structured input, grounding

This optimizer implements the USDL (Universal Skill Description Language)
principle: write once, deploy optimally everywhere.
"""

from __future__ import annotations

from enum import Enum
from typing import Dict, Optional


class ModelTarget(Enum):
    """Target LLM platform for optimization."""
    CLAUDE = "claude"
    OPENAI = "openai"
    GEMINI = "gemini"


class PromptOptimizer:
    """
    Optimizes generic prompts for specific LLM providers.

    Each provider method applies documented best practices from the
    respective platform's prompt engineering guides.
    """

    # Domain-specific system context shared across all platforms
    BIOMEDICAL_PREAMBLE = (
        "You are an expert biomedical AI assistant with deep knowledge in "
        "genomics, clinical medicine, drug discovery, and computational biology. "
        "Provide scientifically accurate, evidence-based responses. "
        "Always cite relevant literature when possible. "
        "Include appropriate safety disclaimers for clinical content."
    )

    def optimize(
        self,
        prompt: str,
        target: ModelTarget,
        *,
        domain: str = "biomedical",
        include_safety: bool = True,
    ) -> str:
        """
        Optimize a prompt for the target platform.

        Args:
            prompt: The generic input prompt.
            target: Target LLM platform.
            domain: Domain context (default: biomedical).
            include_safety: Whether to include safety guardrails.

        Returns:
            Platform-optimized prompt string.
        """
        optimizers = {
            ModelTarget.CLAUDE: self._optimize_for_claude,
            ModelTarget.OPENAI: self._optimize_for_openai,
            ModelTarget.GEMINI: self._optimize_for_gemini,
        }
        optimizer_fn = optimizers.get(target, lambda p, **kw: p)
        return optimizer_fn(prompt, include_safety=include_safety)

    def _optimize_for_claude(self, prompt: str, *, include_safety: bool = True) -> str:
        """
        Anthropic Claude optimization:
        - XML tags for clear structure (Claude excels at XML parsing)
        - Extended thinking encouragement
        - Structured output hints
        - Pre-fill pattern support
        """
        parts = [
            "<system>",
            f"<role>{self.BIOMEDICAL_PREAMBLE}</role>",
        ]

        if include_safety:
            parts.append(
                "<safety_guidelines>"
                "Never provide definitive diagnoses. "
                "Always recommend consulting healthcare professionals for clinical decisions. "
                "Flag any potentially harmful content. "
                "Include evidence levels (e.g., Level 1A, 2B) when discussing clinical evidence."
                "</safety_guidelines>"
            )

        parts.extend([
            "<instructions>",
            "Think step-by-step before responding. "
            "Structure your response with clear sections. "
            "Cite sources with PMIDs or DOIs when available.",
            "</instructions>",
            "</system>",
            "",
            "<user_query>",
            prompt.strip(),
            "</user_query>",
        ])

        return "\n".join(parts)

    def _optimize_for_openai(self, prompt: str, *, include_safety: bool = True) -> str:
        """
        OpenAI GPT optimization:
        - Concise system messages (GPT-4 performs better with brevity)
        - Explicit formatting instructions
        - Markdown output hints
        """
        system = f"ROLE: {self.BIOMEDICAL_PREAMBLE}\n"

        if include_safety:
            system += (
                "\nSAFETY: Include disclaimers for clinical content. "
                "Never suggest self-diagnosis or self-medication.\n"
            )

        system += (
            "\nFORMAT: Use Markdown. Include section headers. "
            "Cite sources when possible. Be concise but thorough.\n"
        )

        return f"### SYSTEM\n{system}\n### USER\n{prompt.strip()}"

    def _optimize_for_gemini(self, prompt: str, *, include_safety: bool = True) -> str:
        """
        Google Gemini optimization:
        - Role card format (Gemini responds well to explicit role definitions)
        - Long-context utilization
        - Structured input with separators
        - Grounding instructions
        """
        parts = [
            f"Role: Expert Biomedical Research Assistant",
            f"Expertise: {self.BIOMEDICAL_PREAMBLE}",
            "",
        ]

        if include_safety:
            parts.extend([
                "Safety Requirements:",
                "- Include medical disclaimers where appropriate",
                "- Never provide definitive clinical diagnoses",
                "- Recommend professional consultation for medical decisions",
                "",
            ])

        parts.extend([
            "Output Requirements:",
            "- Provide detailed, multi-faceted analysis",
            "- Structure with clear sections and headers",
            "- Include citations to primary literature",
            "- Note confidence levels for claims",
            "",
            "=" * 40,
            "QUERY:",
            prompt.strip(),
            "=" * 40,
            "",
            "Please provide a comprehensive, evidence-based response.",
        ])

        return "\n".join(parts)


# ---------------------------------------------------------------------------
# CLI demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    optimizer = PromptOptimizer()
    test_prompt = "Analyze the JAK2 V617F mutation in myeloproliferative neoplasms and its therapeutic implications."

    for target in ModelTarget:
        print(f"\n{'='*60}")
        print(f"  {target.value.upper()} OPTIMIZED")
        print(f"{'='*60}\n")
        print(optimizer.optimize(test_prompt, target))
