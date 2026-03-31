# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Tests for the USDL transpiler.

Validates cross-platform compilation of skill specs.
"""

import json
import pytest
from biokernel.optimizer.usdl_transpiler import (
    FieldSpec,
    Provider,
    USDLSpec,
    USDLTranspiler,
)


@pytest.fixture
def sample_spec():
    return USDLSpec(
        name="Variant Classifier",
        description="ACMG-based clinical variant classification",
        inputs=[
            FieldSpec(name="variant", description="Genomic variant (e.g., BRCA1 c.123G>A)", type="string"),
            FieldSpec(name="gene", description="Gene symbol", type="string"),
        ],
        outputs=[
            FieldSpec(name="classification", description="ACMG class", type="string"),
            FieldSpec(name="evidence", description="Supporting evidence codes", type="string"),
        ],
        safety_checks=[
            "Never output definitive clinical diagnoses.",
            "Always recommend genetic counseling.",
        ],
        instructions_body="Classify variants using the ACMG/AMP 2015 guidelines.",
    )


@pytest.fixture
def transpiler():
    return USDLTranspiler()


class TestUSDLTranspiler:
    """Test cross-platform compilation."""

    def test_compile_openai(self, transpiler: USDLTranspiler, sample_spec: USDLSpec):
        result = transpiler.compile(sample_spec, Provider.OPENAI)
        assert result["provider"] == "openai"
        assert "system_message" in result
        assert "Variant Classifier" in result["system_message"]
        assert len(result["function_schemas"]) > 0

    def test_compile_anthropic(self, transpiler: USDLTranspiler, sample_spec: USDLSpec):
        result = transpiler.compile(sample_spec, Provider.ANTHROPIC)
        assert result["provider"] == "anthropic"
        assert "<system>" in result["system_prompt"]
        assert "<role>" in result["system_prompt"]
        assert "variant" in result["system_prompt"]

    def test_compile_gemini(self, transpiler: USDLTranspiler, sample_spec: USDLSpec):
        result = transpiler.compile(sample_spec, Provider.GEMINI)
        assert result["provider"] == "gemini"
        assert "Variant Classifier" in result["prompt"]
        assert "classification" in result["output_constraints"]

    def test_compile_all(self, transpiler: USDLTranspiler, sample_spec: USDLSpec):
        results = transpiler.compile_all(sample_spec)
        assert set(results.keys()) == {"openai", "anthropic", "gemini"}

    def test_safety_checks_included(self, transpiler: USDLTranspiler, sample_spec: USDLSpec):
        for provider in Provider:
            result = transpiler.compile(sample_spec, provider)
            safety = result.get("safety_checks", [])
            if provider == Provider.GEMINI:
                assert "safety" in result["prompt"].lower() or "counsel" in result["prompt"].lower()
            else:
                assert len(safety) == 2

    def test_unsupported_provider(self, transpiler: USDLTranspiler, sample_spec: USDLSpec):
        with pytest.raises(ValueError):
            transpiler.compile(sample_spec, "invalid")


class TestUSDLSpec:
    """Test spec construction."""

    def test_from_dict(self):
        data = {
            "name": "Test Agent",
            "description": "A test agent",
            "inputs": [{"name": "query", "description": "Input query", "type": "string"}],
            "outputs": [],
            "safety_checks": ["Be safe"],
        }
        spec = USDLSpec.from_dict(data)
        assert spec.name == "Test Agent"
        assert len(spec.inputs) == 1
        assert spec.inputs[0].name == "query"

    def test_from_skill_md(self):
        content = """---
name: test-skill
description: A test skill for parsing
---

# Instructions
Do the thing.

## Safety
Be careful.
"""
        spec = USDLSpec.from_skill_md(content)
        assert spec.name == "test-skill"
        assert spec.description == "A test skill for parsing"
        assert "Do the thing" in spec.instructions_body
        assert len(spec.safety_checks) > 0  # Should detect "safety" keyword

    def test_from_skill_md_no_frontmatter(self):
        content = "# Just a plain markdown file\nNo frontmatter here."
        spec = USDLSpec.from_skill_md(content)
        assert spec.name == "Unknown Skill"
        assert "plain markdown" in spec.instructions_body

    def test_minimal_spec(self):
        spec = USDLSpec(name="Minimal", description="Minimal spec")
        assert spec.inputs == []
        assert spec.outputs == []
        assert spec.version == "1.0.0"
