# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Tests for the I/O schema types.

Validates Pydantic model construction, serialization, and defaults.
"""

import pytest
from biokernel.schema.io_types import (
    AgentRequest,
    AgentResponse,
    EvalCase,
    ExecutionMode,
    FinishReason,
    LLMRequest,
    LLMResponse,
    ProviderName,
    SkillMetadata,
    SkillType,
    ToolCall,
    ToolDefinition,
    ToolResult,
    WorkflowDefinition,
    WorkflowStep,
    WorkflowStatus,
)


class TestLLMModels:
    """Test LLM request and response models."""

    def test_llm_request_defaults(self):
        req = LLMRequest(query="What is EGFR?")
        assert req.temperature == 0.7
        assert req.max_tokens == 4096
        assert req.tools is None

    def test_llm_response_defaults(self):
        resp = LLMResponse(text="EGFR is a gene.", provider="anthropic", model="claude-3")
        assert resp.finish_reason == FinishReason.STOP
        assert resp.usage["prompt_tokens"] == 0
        assert resp.request_id  # Should auto-generate UUID

    def test_tool_call_auto_id(self):
        tc = ToolCall(name="search", arguments={"query": "BRCA1"})
        assert tc.id  # Auto-generated

    def test_tool_definition(self):
        td = ToolDefinition(
            name="pubmed_search",
            description="Search PubMed",
            input_schema={"type": "object", "properties": {"query": {"type": "string"}}},
        )
        assert td.name == "pubmed_search"

    def test_tool_result(self):
        tr = ToolResult(tool_call_id="abc", output="Found 10 results", is_error=False)
        assert not tr.is_error


class TestAgentModels:
    """Test agent request/response models."""

    def test_agent_request_defaults(self):
        req = AgentRequest(query="analyze my data")
        assert req.mode == ExecutionMode.AUTONOMOUS
        assert req.provider_preference == ProviderName.ANTHROPIC
        assert req.max_steps == 10
        assert req.session_id  # Auto-generated

    def test_agent_response_construction(self):
        resp = AgentResponse(
            response="Analysis complete.",
            skill_used="bioinformatics-singlecell",
            provider_used="anthropic",
            model_used="claude-sonnet-4-20250514",
            execution_time_ms=1234.5,
        )
        assert resp.skill_used == "bioinformatics-singlecell"
        assert resp.safety_flags == []


class TestSkillMetadata:
    """Test skill metadata model."""

    def test_skill_metadata(self):
        skill = SkillMetadata(
            skill_id="test-skill",
            name="Test Skill",
            description="A test skill",
            skill_type=SkillType.SKILL_MD,
            file_path="/path/to/SKILL.md",
            tags=["test"],
        )
        assert skill.version == "1.0.0"
        assert skill.embedding is None

    def test_skill_types(self):
        assert SkillType.SKILL_MD.value == "skill_md"
        assert SkillType.PYTHON_AGENT.value == "python_agent"
        assert SkillType.USDL.value == "usdl"


class TestWorkflowModels:
    """Test workflow definition models."""

    def test_workflow_step(self):
        step = WorkflowStep(step_id="s1", skill_id="my-skill")
        assert step.status == WorkflowStatus.PENDING
        assert step.depends_on == []

    def test_workflow_definition(self):
        wf = WorkflowDefinition(
            name="Test Pipeline",
            steps=[
                WorkflowStep(step_id="a", skill_id="skill-a"),
                WorkflowStep(step_id="b", skill_id="skill-b", depends_on=["a"]),
            ],
        )
        assert wf.status == WorkflowStatus.PENDING
        assert len(wf.steps) == 2
        assert wf.workflow_id  # Auto-generated


class TestEvalModels:
    """Test evaluation models."""

    def test_eval_case(self):
        case = EvalCase(
            name="test_safety",
            input="Is aspirin safe?",
            assertions=[],
        )
        assert case.timeout_seconds == 60
        assert case.tags == []

    def test_provider_names(self):
        assert ProviderName.ANTHROPIC.value == "anthropic"
        assert ProviderName.OPENAI.value == "openai"
        assert ProviderName.GEMINI.value == "gemini"
        assert ProviderName.LOCAL.value == "local"

    def test_execution_modes(self):
        assert ExecutionMode.AUTONOMOUS.value == "autonomous"
        assert ExecutionMode.INTERACTIVE.value == "interactive"
        assert ExecutionMode.MANUAL.value == "manual"
