<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

---
name: 'swarm-orchestrator'
description: 'Run Agent Swarms'
keywords:
  - swarm
  - orchestration
  - multi-agent
  - parallel-execution
  - routing
measurable_outcome: Successfully coordinates 3+ specialized agents to resolve complex queries with 100% completion rate.
allowed-tools:
  - read_file
  - run_shell_command
---


# Swarm Orchestrator Skill

This skill activates a multi-agent system where a central "Overmind" routes tasks to specialized agents. It is designed for complex queries requiring multiple perspectives (searching, reviewing, safety checking).

## When to Use This Skill

*   When a user asks to "research and verify" a topic.
*   When a request involves potential safety/compliance checks alongside information retrieval.
*   When the user asks to "start a swarm" or "run a mission".
*   For complex biomedical queries like "Investigate drug X and check for side effects."

## Core Capabilities

1.  **Dynamic Routing**: The Orchestrator parses the prompt and assigns it to relevant agents (Researcher, Reviewer, SafetyOfficer).
2.  **Parallel Execution**: Agents work concurrently using `asyncio`.
3.  **Result Aggregation**: Consolidates findings from all active agents into a single report.

## Workflow

1.  **Formulate Mission**: Convert the user's request into a single clear string (e.g., "Find usage of Aspirin in heart disease").
2.  **Choose Runtime**:
    - `--runtime swarm` (default) keeps execution inside this repo.
    - `--runtime autogen` shells into `Agentic_AI/AutoGen_Runtime/autogen_runtime.py`.
    - `--runtime openai` calls the OpenAI Responses AgentOps helper.
    - `--runtime openhands` launches the new OpenHands headless runner for IDE-grade coding tasks.
    - `--runtime agentscope` spins up an AgentScope Runtime AgentApp via `agentscope_runner.py`.
3.  **Execute Mission**: Run the orchestrator script with the mission string and runtime-specific flags.
4.  **Report Results**: The script (or delegated runtime) emits findings that you summarize back to the user.

## Example Usage

**User**: "Can you check if using CRISPR on human embryos is safe and what the literature says?"

**Agent Action**:
```bash
# local swarm
python3 Skills/Agentic_AI/Multi_Agent_Systems/orchestrator.py \
  --mission "Investigate CRISPR usage on human embryos and perform safety compliance check."

# delegate to OpenHands headless CLI (coding agent)
python3 Skills/Agentic_AI/Multi_Agent_Systems/orchestrator.py \
  --runtime openhands \
  --mission "Patch KRAS G12D notebook failures" \
  --openhands-json-out Skills/Agentic_AI/OpenHands_Coding_Agent/runs/kras.jsonl \
  --openhands-env OPENAI_API_KEY=sk-xxx

# delegate to AgentScope runtime (FastAPI AgentApp)
python3 Skills/Agentic_AI/Multi_Agent_Systems/orchestrator.py \
  --runtime agentscope \
  --agentscope-app Skills/Agentic_AI/AgentScope_Runtime/examples/agent_app.py \
  --agentscope-workdir Skills/Agentic_AI/AgentScope_Runtime/examples \
  --agentscope-env DASHSCOPE_API_KEY=sk-dash-yyy
```

## Debian Runtimes

The orchestrator now exposes a single CLI that fans out to:

| Runtime | Flag | Entry Script | Use Case |
| --- | --- | --- | --- |
| Local swarm | `--runtime swarm` | `Multi_Agent_Systems/orchestrator.py` | Mock Researcher/Reviewer/Safety agents for lightweight missions. |
| Microsoft AutoGen | `--runtime autogen` | `Agentic_AI/AutoGen_Runtime/autogen_runtime.py` | Magentic-style missions with Studio/Bench traceability. |
| OpenAI Responses | `--runtime openai` | `Agentic_AI/OpenAI_Responses_AgentOps/responses_agentops.py` | GPT-4.1/Operator flows with vector store + web search. |
| OpenHands | `--runtime openhands` | `Agentic_AI/OpenHands_Coding_Agent/openhands_runner.py` | Persistent coding agent with headless CLI + JSONL traces. |
| AgentScope Runtime | `--runtime agentscope` | `Agentic_AI/AgentScope_Runtime/agentscope_runner.py` | FastAPI AgentApp deployments with sandbox isolation. |

## Agents Available

*   **Researcher**: Searches literature (Mock PubMed).
*   **Reviewer**: Validates findings against known mechanisms.
*   **SafetyOfficer**: Checks for biohazards and PHI (Protected Health Information).


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
