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

# Agentic AI (2026)

This directory is the curated home for first-party agent workflows, not a dumping ground for random demos.
Keep skills here when they are repeatedly useful for building, operating, or evaluating production-grade LLM systems.

## Current Focus Areas

- **Core agent patterns:** `Agent_Architectures/Plan_and_Solve`, `Agent_Architectures/ReAct_Agent`, `Agent_Architectures/Self_Correction`
- **Research agents:** `Automated_Web_Research`, `DeepResearch_Swarm`
- **Execution runtimes and coding agents:** `AgentScope_Runtime`, `OpenHands_Coding_Agent`, `OpenAI_Codex_Agents`, `Claude_Code_Operations_2026`, `LangGraph_Self_Hosted`
- **Modern framework coverage:** `OpenAI_Codex_Agents`, `Google_ADK_Agents`, `PydanticAI_Agents`
- **Scientific discovery agents:** `Scientific_Discovery_Agents_2026`
- **Computer and browser control:** `Computer_Use_Agents_2026`
- **Operational quality:** `Agentic_Evals_Observability`, `Memory_Systems`, `Productivity/`
- **Reasoning and multimodality:** `Reasoning_Models/`, `Multimodal_Agents/`

## Curation Rules

- Prefer official docs, official SDK docs, protocol specs, and maintainer-owned repositories.
- Keep `SKILL.md` short and trigger-oriented; move details to `references/`.
- Add `agents/openai.yaml` for curated skills that should surface cleanly in agent UIs.
- Rewrite thin or stale skills before adding more near-duplicates.
- Treat imported external collections as reference material until curated locally.

## High-Value Additions In This Refresh

- `Claude_Code_Operations_2026/` for terminal, IDE, GitHub Action, hooks, and MCP-aware Claude Code rollouts.
- `Computer_Use_Agents_2026/` for browser-vs-desktop agent selection, isolated execution, and benchmark-grounded computer-use operations.
- `OpenAI_Codex_Agents/` for Responses-first coding agents, Codex models, Agents SDK, MCP/connectors, and approval-aware tool execution.
- `Google_ADK_Agents/` for Google's multi-language Agent Development Kit and workflow-agent patterns.
- `PydanticAI_Agents/` for typed agent engineering, dependency injection, MCP integration, and Logfire/OTel observability.
- `Agentic_Evals_Observability/` for offline evals, online monitoring, tracing, rollback criteria, and regression discipline.
- Upgraded `Automated_Web_Research/` and `DeepResearch_Swarm/` to be evidence-first and source-aware.

## May 2026 Agentic Science Refresh

- `Scientific_Discovery_Agents_2026/` captures the new peer-reviewed biomedical discovery-agent layer: Co-Scientist, Robin, CellVoyager, SPARK, and Biomni-style orchestration.
- Updated curation expectations now require scientific claim boundaries, human checkpoints, validation endpoints, reproducibility packages, and explicit rollback triggers for discovery agents.
- MCP and coding-agent skills should treat tool metadata, OAuth/resource discovery, approval policy, and out-of-scope action testing as first-class operational concerns.

## Related Strategy Doc

See `docs/strategy/LLM_AGENTIC_AI_CURATION_2026.md` for the official-source map, literature watchlist, and monthly refresh checklist.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
