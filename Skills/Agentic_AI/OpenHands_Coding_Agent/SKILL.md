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
name: bio-openhands-coding-agent
description: Run OpenHands headless CLI/SDK missions from BioKernel swarms for autonomous
  software work.
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# OpenHands Coding Agent Skill

OpenHands (formerly OpenDevin) is a 70k+ star open-source coding agent stack that exposes the same engine through a Python SDK, a CLI, a local GUI, a hosted cloud workspace, and a self-hosted enterprise edition.¹ The CLI ships with a **headless mode** so you can script missions, capture JSONL traces, and hand progress back to other agents.²

## When to Trigger This Skill

* You need a persistent IDE-grade coding agent that can run shells, editors, and browsers against your repo while other biomedical agents handle research/safety steps.
* You want to re-use OpenHands’ plan/act/react loop instead of building a sandbox from scratch.
* You must export JSONL traces for downstream reviewers or for ingestion into `platform/compliance/` dashboards.

## Prerequisites

1. Install OpenHands (CLI bundles a uv launcher):
   ```bash
   uv tool install openhands --python 3.12
   # or pip install openhands
   ```
2. Provide an LLM key via env (Claude, GPT-4.1, Gemini, Qwen, etc.). You can also pass them via `--env KEY=value` when using the runner below:
   ```bash
   export OPENAI_API_KEY=sk-...
   ```
3. Ensure your repo mount has git + docker access if you want containerized sandboxes; otherwise use the lightweight local mode.

## Workflow

1. **Define the mission text** that OpenHands should solve (e.g., “Triage KRAS G12D tox notebook failures”).
2. **Run headless CLI** so the agent streams work to stdout and (optionally) JSONL. Use the helper below or invoke the CLI directly:
   ```bash
   # direct
   openhands --headless -t "${MISSION}" --json > traces/${RUN_ID}.jsonl

   # helper script (handles env vars and tee'ing output)
   python Skills/Agentic_AI/OpenHands_Coding_Agent/openhands_runner.py \
     --mission "${MISSION}" \
     --json-out Skills/Agentic_AI/OpenHands_Coding_Agent/runs/${RUN_ID}.jsonl \
     --env OPENAI_API_KEY=sk-xxx CLAUDE_API_KEY=sk-ant-yyy
   ```
3. **Optional task files**: place a multi-step YAML/Markdown brief in `openhands_task.md` and run `openhands --headless -f openhands_task.md`.
4. **Synthesize results**: parse the JSONL (each event has `role`, `tool`, `content`) and feed summaries back into `Multi_Agent_Systems/orchestrator.py` as part of the Reviewer/Safety checkpoints.
5. **Escalate/stop**: send SIGINT (Ctrl+C) to halt the agent; it checkpoints the shell/IDE history so you can resume the same run ID later.

## Swarm Handoff Pattern

*Kick-off from orchestrator*: have the Overmind delegate coding subtasks by writing `MISSION.txt`, then invoke OpenHands via `subprocess.run` (or manually) using the command above.

*Return artifacts*: drop patch files, terminal transcripts, and the JSON trace under `Skills/Agentic_AI/OpenHands_Coding_Agent/runs/<timestamp>/` so other agents (Reviewer, SafetyOfficer) can inspect diffs.

## Assets

| File | Purpose |
| --- | --- |
| `openhands_runner.py` | Wrapper that shells out to the OpenHands CLI with `--headless`, `--json`, optional task files, env injection, and JSONL teeing. |


*Safety hooks*: tail the JSONL stream to automatically look for PHI/PII before allowing patches to merge.

## References

1. GitHub – OpenHands/OpenHands (`README` outlines SDK, CLI, GUI, Cloud, Enterprise surfaces). <https://github.com/OpenHands/OpenHands>
2. GitHub – OpenHands CLI headless usage (`openhands --headless -t ... --json`). <https://github.com/OpenHands/OpenHands?tab=readme-ov-file#openhands-cli>

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->