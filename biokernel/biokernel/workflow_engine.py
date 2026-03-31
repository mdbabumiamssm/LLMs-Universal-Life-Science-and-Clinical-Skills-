# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
DAG-based Workflow Engine for multi-agent orchestration.

Executes multi-step biomedical workflows as directed acyclic graphs (DAGs),
where each node is a skill invocation and edges encode data dependencies.

Features:
- Automatic parallelization of independent steps
- Configurable retry with exponential backoff
- Step-level timeout enforcement
- Provenance tracking for reproducibility
"""

from __future__ import annotations

import asyncio
import time
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Callable, Coroutine, Dict, List, Optional, Set

from biokernel.observability import get_logger
from biokernel.schema.io_types import (
    WorkflowDefinition,
    WorkflowStatus,
    WorkflowStep,
)

logger = get_logger("workflow_engine")


class WorkflowEngine:
    """
    Executes workflow DAGs with parallel step execution and retry logic.

    Usage::

        engine = WorkflowEngine()
        workflow = WorkflowDefinition(
            name="Drug Discovery Pipeline",
            steps=[
                WorkflowStep(step_id="mine", skill_id="literature-miner"),
                WorkflowStep(step_id="design", skill_id="molecule-designer",
                             depends_on=["mine"]),
                WorkflowStep(step_id="safety", skill_id="safety-officer",
                             depends_on=["design"]),
            ],
        )
        result = await engine.execute(workflow, step_executor=my_executor)
    """

    def __init__(
        self,
        max_retries: int = 2,
        retry_delay: float = 5.0,
        step_timeout: float = 120.0,
    ) -> None:
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.step_timeout = step_timeout

    async def execute(
        self,
        workflow: WorkflowDefinition,
        step_executor: Callable[
            [WorkflowStep, Dict[str, str]], Coroutine[Any, Any, str]
        ],
    ) -> WorkflowDefinition:
        """
        Execute a workflow DAG to completion.

        Args:
            workflow: The workflow definition with steps and dependencies.
            step_executor: Async callable that executes a single step.
                Receives (step, upstream_results_dict) and returns a string result.

        Returns:
            The workflow definition updated with results, status, and timing.
        """
        workflow.status = WorkflowStatus.RUNNING
        total_start = time.perf_counter()

        # Build adjacency and in-degree maps
        step_map: Dict[str, WorkflowStep] = {s.step_id: s for s in workflow.steps}
        dependents: Dict[str, List[str]] = defaultdict(list)
        in_degree: Dict[str, int] = {}

        for step in workflow.steps:
            in_degree[step.step_id] = len(step.depends_on)
            for dep in step.depends_on:
                dependents[dep].append(step.step_id)

        # Validate DAG (no cycles)
        if not self._validate_dag(step_map, in_degree):
            workflow.status = WorkflowStatus.FAILED
            logger.error("Workflow DAG contains a cycle", workflow=workflow.name)
            return workflow

        # Results accumulator
        results: Dict[str, str] = {}
        completed: Set[str] = set()
        failed: Set[str] = set()

        # Topological execution with parallel independent steps
        ready_queue: List[str] = [
            sid for sid, deg in in_degree.items() if deg == 0
        ]

        while ready_queue:
            # Launch all ready steps in parallel
            tasks = []
            batch = list(ready_queue)
            ready_queue.clear()

            for step_id in batch:
                step = step_map[step_id]
                step.status = WorkflowStatus.RUNNING

                # Gather upstream results for this step
                upstream = {dep: results.get(dep, "") for dep in step.depends_on}

                tasks.append(
                    self._execute_step_with_retry(step, step_executor, upstream)
                )

            # Await all parallel steps
            step_results = await asyncio.gather(*tasks, return_exceptions=True)

            for step_id, outcome in zip(batch, step_results):
                step = step_map[step_id]

                if isinstance(outcome, Exception):
                    step.status = WorkflowStatus.FAILED
                    step.error = str(outcome)
                    failed.add(step_id)
                    logger.error(
                        "Step failed",
                        step=step_id,
                        error=str(outcome),
                        workflow=workflow.name,
                    )
                else:
                    step.status = WorkflowStatus.COMPLETED
                    step.result = outcome
                    results[step_id] = outcome
                    completed.add(step_id)

                    # Decrement in-degree of dependents
                    for child_id in dependents[step_id]:
                        in_degree[child_id] -= 1
                        if in_degree[child_id] == 0 and child_id not in failed:
                            ready_queue.append(child_id)

        # Finalize
        total_latency = (time.perf_counter() - total_start) * 1000
        workflow.total_latency_ms = total_latency
        workflow.completed_at = datetime.now(timezone.utc)

        if failed:
            workflow.status = WorkflowStatus.FAILED
        else:
            workflow.status = WorkflowStatus.COMPLETED

        logger.info(
            "Workflow finished",
            workflow=workflow.name,
            status=workflow.status.value,
            steps_completed=len(completed),
            steps_failed=len(failed),
            total_ms=total_latency,
        )

        return workflow

    async def _execute_step_with_retry(
        self,
        step: WorkflowStep,
        executor: Callable,
        upstream: Dict[str, str],
    ) -> str:
        """Execute a single step with retry and timeout."""
        last_error: Optional[Exception] = None

        for attempt in range(self.max_retries + 1):
            step_start = time.perf_counter()
            try:
                result = await asyncio.wait_for(
                    executor(step, upstream),
                    timeout=self.step_timeout,
                )
                step.latency_ms = (time.perf_counter() - step_start) * 1000
                return result

            except asyncio.TimeoutError:
                step.latency_ms = (time.perf_counter() - step_start) * 1000
                last_error = TimeoutError(
                    f"Step '{step.step_id}' timed out after {self.step_timeout}s"
                )
                logger.warning(
                    "Step timeout, retrying",
                    step=step.step_id,
                    attempt=attempt + 1,
                )

            except Exception as exc:
                step.latency_ms = (time.perf_counter() - step_start) * 1000
                last_error = exc
                logger.warning(
                    "Step error, retrying",
                    step=step.step_id,
                    attempt=attempt + 1,
                    error=str(exc),
                )

            if attempt < self.max_retries:
                await asyncio.sleep(self.retry_delay * (2**attempt))

        raise last_error or RuntimeError(f"Step '{step.step_id}' failed after retries")

    @staticmethod
    def _validate_dag(
        step_map: Dict[str, WorkflowStep],
        in_degree: Dict[str, int],
    ) -> bool:
        """Check for cycles using Kahn's algorithm."""
        remaining = dict(in_degree)
        queue = [sid for sid, deg in remaining.items() if deg == 0]
        visited = 0

        while queue:
            node = queue.pop(0)
            visited += 1
            step = step_map[node]
            # Find children
            for other_id, other_step in step_map.items():
                if node in other_step.depends_on:
                    remaining[other_id] -= 1
                    if remaining[other_id] == 0:
                        queue.append(other_id)

        return visited == len(step_map)

    @staticmethod
    def create_linear_workflow(
        name: str,
        skill_ids: List[str],
        description: str = "",
    ) -> WorkflowDefinition:
        """
        Convenience: create a linear (sequential) workflow from skill IDs.

        Args:
            name: Workflow name.
            skill_ids: Ordered list of skill IDs to execute sequentially.
            description: Optional description.

        Returns:
            WorkflowDefinition with steps chained linearly.
        """
        steps = []
        for i, sid in enumerate(skill_ids):
            step = WorkflowStep(
                step_id=f"step_{i}",
                skill_id=sid,
                depends_on=[f"step_{i-1}"] if i > 0 else [],
            )
            steps.append(step)

        return WorkflowDefinition(
            name=name,
            description=description,
            steps=steps,
        )
