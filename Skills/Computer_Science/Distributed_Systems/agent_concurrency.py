# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

import asyncio
from typing import List, Dict, Any, Callable, Awaitable
from dataclasses import dataclass
import time

@dataclass
class AgentTask:
    """Represents a unit of work for an agent."""
    id: str
    description: str
    priority: int = 1
    dependencies: List[str] = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

@dataclass
class AgentResult:
    """The result produced by an agent."""
    task_id: str
    output: Any
    execution_time: float
    status: str  # "success", "failed"

class AsyncAgentRuntime:
    """
    A lightweight asynchronous runtime for executing agent tasks concurrently.
    Simulates the behavior of distributed frameworks like Ray or Celery
    but optimized for local agentic workflows.
    """
    
    def __init__(self, max_concurrency: int = 5):
        self.queue = asyncio.PriorityQueue()
        self.results: Dict[str, AgentResult] = {}
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.running = False
        
    async def submit_task(self, task: AgentTask, func: Callable[..., Awaitable[Any]], *args, **kwargs):
        """Submit a task to the runtime."""
        # PriorityQueue uses strictly less-than, so we negate priority for high-priority first
        await self.queue.put((-task.priority, task, func, args, kwargs))
        
    async def _worker(self):
        """Internal worker loop."""
        while self.running and not self.queue.empty():
            try:
                _, task, func, args, kwargs = await self.queue.get()
                
                # Check dependencies
                if not self._are_dependencies_met(task):
                    # Re-queue if dependencies aren't ready (simple spin-wait simulation)
                    await self.queue.put((-task.priority, task, func, args, kwargs))
                    await asyncio.sleep(0.1)
                    continue

                async with self.semaphore:
                    start_time = time.time()
                    try:
                        print(f"[@Runtime] Starting task: {task.description}")
                        result_data = await func(*args, **kwargs)
                        status = "success"
                    except Exception as e:
                        print(f"[@Runtime] Task failed: {task.description} - {e}")
                        result_data = str(e)
                        status = "failed"
                    
                    end_time = time.time()
                    
                    self.results[task.id] = AgentResult(
                        task_id=task.id,
                        output=result_data,
                        execution_time=end_time - start_time,
                        status=status
                    )
                    
                self.queue.task_done()
            except asyncio.CancelledError:
                break

    def _are_dependencies_met(self, task: AgentTask) -> bool:
        """Check if all parent tasks have completed successfully."""
        for dep_id in task.dependencies:
            if dep_id not in self.results or self.results[dep_id].status != "success":
                return False
        return True

    async def run_all(self):
        """Execute all submitted tasks."""
        self.running = True
        workers = [asyncio.create_task(self._worker()) for _ in range(self.semaphore._value)]
        await self.queue.join()
        self.running = False
        for w in workers:
            w.cancel()
            
    def get_result(self, task_id: str) -> Any:
        return self.results.get(task_id)

# --- Example Usage ---
if __name__ == "__main__":
    async def mock_agent_action(name: str, duration: float):
        await asyncio.sleep(duration)
        return f"{name} completed"

    async def main():
        runtime = AsyncAgentRuntime(max_concurrency=3)
        
        # Create a dependency graph
        # Task A -> Task B & C -> Task D
        
        task_a = AgentTask("A", "Research Target", priority=10)
        task_b = AgentTask("B", "Design Molecule", priority=5, dependencies=["A"])
        task_c = AgentTask("C", "Check Toxicity", priority=5, dependencies=["A"])
        task_d = AgentTask("D", "Write Report", priority=1, dependencies=["B", "C"])
        
        await runtime.submit_task(task_a, mock_agent_action, "Researcher", 1.0)
        await runtime.submit_task(task_b, mock_agent_action, "Designer", 0.5)
        await runtime.submit_task(task_c, mock_agent_action, "Toxicologist", 0.8)
        await runtime.submit_task(task_d, mock_agent_action, "Reporter", 0.2)
        
        print("Starting Agent Runtime...")
        await runtime.run_all()
        print("All agents finished.")
        
        print(f"Final Report: {runtime.get_result('D').output}")

    asyncio.run(main())

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
