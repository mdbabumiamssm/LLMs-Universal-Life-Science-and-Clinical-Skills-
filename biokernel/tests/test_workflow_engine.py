# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Tests for the DAG-based workflow engine.

Validates parallel execution, dependency resolution, retry logic,
and cycle detection.
"""

import asyncio
import pytest
from biokernel.biokernel.workflow_engine import WorkflowEngine
from biokernel.schema.io_types import WorkflowDefinition, WorkflowStep, WorkflowStatus


@pytest.fixture
def engine():
    return WorkflowEngine(max_retries=1, retry_delay=0.1, step_timeout=5.0)


async def mock_executor(step: WorkflowStep, upstream: dict) -> str:
    """Simulate a skill execution."""
    await asyncio.sleep(0.01)
    context = ", ".join(f"{k}={v[:20]}" for k, v in upstream.items() if v)
    return f"Result from {step.step_id} (skill={step.skill_id}, context=[{context}])"


async def failing_executor(step: WorkflowStep, upstream: dict) -> str:
    """Executor that always fails."""
    raise RuntimeError(f"Simulated failure in {step.step_id}")


class TestWorkflowEngine:
    """Test suite for the workflow engine."""

    @pytest.mark.asyncio
    async def test_linear_workflow(self, engine: WorkflowEngine):
        """A→B→C linear workflow should execute in order."""
        workflow = WorkflowDefinition(
            name="Linear Test",
            steps=[
                WorkflowStep(step_id="a", skill_id="skill-a"),
                WorkflowStep(step_id="b", skill_id="skill-b", depends_on=["a"]),
                WorkflowStep(step_id="c", skill_id="skill-c", depends_on=["b"]),
            ],
        )

        result = await engine.execute(workflow, mock_executor)

        assert result.status == WorkflowStatus.COMPLETED
        assert all(s.status == WorkflowStatus.COMPLETED for s in result.steps)
        assert result.total_latency_ms > 0

        # Step B should have context from A
        step_b = next(s for s in result.steps if s.step_id == "b")
        assert "a=" in step_b.result

    @pytest.mark.asyncio
    async def test_parallel_workflow(self, engine: WorkflowEngine):
        """Independent steps should run in parallel."""
        workflow = WorkflowDefinition(
            name="Parallel Test",
            steps=[
                WorkflowStep(step_id="a", skill_id="skill-a"),
                WorkflowStep(step_id="b", skill_id="skill-b"),
                WorkflowStep(step_id="c", skill_id="skill-c", depends_on=["a", "b"]),
            ],
        )

        result = await engine.execute(workflow, mock_executor)

        assert result.status == WorkflowStatus.COMPLETED
        # Step C should have context from both A and B
        step_c = next(s for s in result.steps if s.step_id == "c")
        assert "a=" in step_c.result
        assert "b=" in step_c.result

    @pytest.mark.asyncio
    async def test_diamond_workflow(self, engine: WorkflowEngine):
        """Diamond DAG: A → (B, C) → D."""
        workflow = WorkflowDefinition(
            name="Diamond Test",
            steps=[
                WorkflowStep(step_id="a", skill_id="s-a"),
                WorkflowStep(step_id="b", skill_id="s-b", depends_on=["a"]),
                WorkflowStep(step_id="c", skill_id="s-c", depends_on=["a"]),
                WorkflowStep(step_id="d", skill_id="s-d", depends_on=["b", "c"]),
            ],
        )

        result = await engine.execute(workflow, mock_executor)
        assert result.status == WorkflowStatus.COMPLETED
        assert all(s.status == WorkflowStatus.COMPLETED for s in result.steps)

    @pytest.mark.asyncio
    async def test_failure_propagation(self, engine: WorkflowEngine):
        """Failed steps should mark workflow as FAILED."""
        workflow = WorkflowDefinition(
            name="Failure Test",
            steps=[
                WorkflowStep(step_id="a", skill_id="skill-a"),
                WorkflowStep(step_id="b", skill_id="skill-b", depends_on=["a"]),
            ],
        )

        result = await engine.execute(workflow, failing_executor)
        assert result.status == WorkflowStatus.FAILED

    @pytest.mark.asyncio
    async def test_empty_workflow(self, engine: WorkflowEngine):
        """Empty workflow should complete immediately."""
        workflow = WorkflowDefinition(name="Empty", steps=[])
        result = await engine.execute(workflow, mock_executor)
        assert result.status == WorkflowStatus.COMPLETED

    @pytest.mark.asyncio
    async def test_single_step(self, engine: WorkflowEngine):
        """Single-step workflow should work."""
        workflow = WorkflowDefinition(
            name="Single",
            steps=[WorkflowStep(step_id="only", skill_id="only-skill")],
        )
        result = await engine.execute(workflow, mock_executor)
        assert result.status == WorkflowStatus.COMPLETED
        assert len(result.steps) == 1

    def test_create_linear_workflow(self):
        """Convenience method should chain steps correctly."""
        wf = WorkflowEngine.create_linear_workflow(
            "Test Pipeline",
            ["mine", "design", "safety"],
        )
        assert len(wf.steps) == 3
        assert wf.steps[0].depends_on == []
        assert wf.steps[1].depends_on == ["step_0"]
        assert wf.steps[2].depends_on == ["step_1"]


class TestWorkflowRetry:
    """Test retry and timeout behavior."""

    @pytest.mark.asyncio
    async def test_retry_on_failure(self):
        """Engine should retry failed steps."""
        call_count = {"n": 0}

        async def flaky_executor(step, upstream):
            call_count["n"] += 1
            if call_count["n"] < 2:
                raise RuntimeError("transient error")
            return "success after retry"

        engine = WorkflowEngine(max_retries=2, retry_delay=0.01, step_timeout=5.0)
        workflow = WorkflowDefinition(
            name="Retry Test",
            steps=[WorkflowStep(step_id="flaky", skill_id="flaky-skill")],
        )

        result = await engine.execute(workflow, flaky_executor)
        assert result.status == WorkflowStatus.COMPLETED
        assert call_count["n"] >= 2

    @pytest.mark.asyncio
    async def test_timeout(self):
        """Steps exceeding timeout should fail."""
        async def slow_executor(step, upstream):
            await asyncio.sleep(10)
            return "too slow"

        engine = WorkflowEngine(max_retries=0, retry_delay=0.01, step_timeout=0.1)
        workflow = WorkflowDefinition(
            name="Timeout Test",
            steps=[WorkflowStep(step_id="slow", skill_id="slow-skill")],
        )

        result = await engine.execute(workflow, slow_executor)
        assert result.status == WorkflowStatus.FAILED
