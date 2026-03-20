# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Unified I/O type system for the BioKernel platform.

Provides Pydantic models for all inter-component communication:
LLM requests/responses, skill definitions, workflow states, and evaluation results.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------

class ProviderName(str, Enum):
    """Supported LLM providers."""
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    GEMINI = "gemini"
    LOCAL = "local"


class FinishReason(str, Enum):
    """LLM generation finish reasons."""
    STOP = "stop"
    LENGTH = "length"
    TOOL_CALLS = "tool_calls"
    CONTENT_FILTER = "content_filter"
    ERROR = "error"


class WorkflowStatus(str, Enum):
    """Workflow execution status."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class SkillType(str, Enum):
    """Types of registered skills."""
    SKILL_MD = "skill_md"
    PYTHON_AGENT = "python_agent"
    USDL = "usdl"
    MCP_TOOL = "mcp_tool"


class ExecutionMode(str, Enum):
    """How a user wants to interact with the system."""
    AUTONOMOUS = "autonomous"
    INTERACTIVE = "interactive"
    MANUAL = "manual"


# ---------------------------------------------------------------------------
# Tool Definitions
# ---------------------------------------------------------------------------

class ToolDefinition(BaseModel):
    """Schema for a tool available to an LLM agent."""
    name: str
    description: str
    input_schema: Dict[str, Any] = Field(default_factory=dict)


class ToolCall(BaseModel):
    """A tool invocation requested by the LLM."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str
    arguments: Dict[str, Any] = Field(default_factory=dict)


class ToolResult(BaseModel):
    """Result from executing a tool call."""
    tool_call_id: str
    output: str
    is_error: bool = False


# ---------------------------------------------------------------------------
# LLM Request / Response
# ---------------------------------------------------------------------------

class LLMMessage(BaseModel):
    """A single message in a conversation."""
    role: str  # "system", "user", "assistant", "tool"
    content: str
    tool_calls: Optional[List[ToolCall]] = None
    tool_call_id: Optional[str] = None


class LLMRequest(BaseModel):
    """Standardized request to any LLM provider."""
    query: str
    system_instruction: Optional[str] = None
    messages: List[LLMMessage] = Field(default_factory=list)
    tools: Optional[List[ToolDefinition]] = None
    temperature: float = 0.7
    max_tokens: int = 4096
    top_p: float = 1.0
    stop_sequences: Optional[List[str]] = None
    context: Dict[str, Any] = Field(default_factory=dict)
    stream: bool = False
    response_format: Optional[str] = None  # "json", "text", None


class LLMResponse(BaseModel):
    """Standardized response from any LLM provider."""
    text: str
    tool_calls: Optional[List[ToolCall]] = None
    finish_reason: FinishReason = FinishReason.STOP
    usage: Dict[str, int] = Field(
        default_factory=lambda: {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    )
    latency_ms: float = 0.0
    provider: str = ""
    model: str = ""
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# ---------------------------------------------------------------------------
# Skill Registry
# ---------------------------------------------------------------------------

class SkillMetadata(BaseModel):
    """Metadata for a registered skill."""
    skill_id: str
    name: str
    description: str
    skill_type: SkillType
    file_path: str
    category: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    version: str = "1.0.0"
    author: Optional[str] = None
    instructions_body: str = ""
    capabilities: List[str] = Field(default_factory=list)
    safety_checks: List[str] = Field(default_factory=list)
    embedding: Optional[List[float]] = None  # For semantic routing


# ---------------------------------------------------------------------------
# Agent Request / Response
# ---------------------------------------------------------------------------

class AgentRequest(BaseModel):
    """Top-level request to the BioKernel."""
    query: str
    context: Dict[str, Any] = Field(default_factory=dict)
    mode: ExecutionMode = ExecutionMode.AUTONOMOUS
    provider_preference: ProviderName = ProviderName.ANTHROPIC
    skill_id: Optional[str] = None  # Force a specific skill
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    max_steps: int = 10
    timeout_seconds: float = 300.0


class AgentStep(BaseModel):
    """A single step in an agentic execution."""
    step_number: int
    action: str  # "thinking", "tool_call", "response"
    content: str
    tool_calls: Optional[List[ToolCall]] = None
    tool_results: Optional[List[ToolResult]] = None
    latency_ms: float = 0.0
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class AgentResponse(BaseModel):
    """Complete response from the BioKernel."""
    response: str
    skill_used: str = ""
    provider_used: str = ""
    model_used: str = ""
    steps: List[AgentStep] = Field(default_factory=list)
    tools_used: List[str] = Field(default_factory=list)
    execution_time_ms: float = 0.0
    token_usage: Dict[str, int] = Field(
        default_factory=lambda: {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    )
    session_id: str = ""
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    safety_flags: List[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Workflow Engine
# ---------------------------------------------------------------------------

class WorkflowStep(BaseModel):
    """A single step in a DAG workflow."""
    step_id: str
    skill_id: str
    depends_on: List[str] = Field(default_factory=list)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    status: WorkflowStatus = WorkflowStatus.PENDING
    result: Optional[str] = None
    error: Optional[str] = None
    latency_ms: float = 0.0


class WorkflowDefinition(BaseModel):
    """A complete DAG workflow specification."""
    workflow_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str = ""
    steps: List[WorkflowStep] = Field(default_factory=list)
    status: WorkflowStatus = WorkflowStatus.PENDING
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
    total_latency_ms: float = 0.0


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

class EvalAssertion(BaseModel):
    """A single assertion in an evaluation test case."""
    assertion_type: str  # "contains", "not_contains", "regex", "safety_check", etc.
    value: Optional[str] = None
    entity_type: Optional[str] = None


class EvalCase(BaseModel):
    """An evaluation test case."""
    name: str
    input: str
    assertions: List[EvalAssertion] = Field(default_factory=list)
    expected_output: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    timeout_seconds: int = 60


class EvalResult(BaseModel):
    """Result of a single evaluation."""
    case_name: str
    passed: bool
    score: float
    assertions_passed: int
    assertions_total: int
    output: str
    latency_ms: float
    error: Optional[str] = None
    details: Dict[str, Any] = Field(default_factory=dict)


class EvalReport(BaseModel):
    """Complete evaluation report."""
    skill_id: str
    platform: str
    timestamp: str
    total_cases: int
    passed_cases: int
    overall_score: float
    results: List[EvalResult]
    metrics: Dict[str, float]
    recommendations: List[str]
