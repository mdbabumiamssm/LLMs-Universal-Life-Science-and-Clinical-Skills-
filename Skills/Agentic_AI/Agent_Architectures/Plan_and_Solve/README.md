# Plan-and-Solve Agent

Implementation of the **Plan-and-Solve Prompting** strategy (Wang et al., 2023), which improves zero-shot reasoning in Large Language Models by explicitly splitting the task into a planning phase and an execution phase.

## Why this matters?
Standard "Chain of Thought" or "ReAct" agents often get lost in the details of complex, multi-step tasks. Plan-and-Solve forces the agent to:
1.  **Zoom Out:** See the whole problem and devise a roadmap.
2.  **Zoom In:** Execute one step at a time, using the context of the plan.

## Contents

### `planner.py`
- `PlanAndSolveAgent`: The core class.
- **Phase 1 (Planning):** Uses an LLM to generate a numbered list of steps.
- **Phase 2 (Execution):** Iterates through steps, passing the context of previous results to the LLM for the current step.

## Usage
```python
from planner import PlanAndSolveAgent, LLMAdapter

agent = PlanAndSolveAgent(LLMAdapter())
result = agent.run("Design a new protocol for CRISPR off-target analysis")
```
