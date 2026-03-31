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
name: end-to-end-agentic-ai-lab
description: Deploy MDalamin5's End-to-End Agentic AI Automation Lab to prototype lab automation swarms that span LangChain/LangGraph agents, MCP servers, and n8n-run experiment control.
keywords:
  - lab-automation
  - multi-agent
  - langgraph
  - n8n
  - mcp
measurable_outcome: Stand up one multi-agent workflow plus an MCP-backed automation pipeline from the lab within a single working day.
license: MIT
metadata:
  author: Lab Automation Guild
  version: "2026.03"
compatibility:
  - system: Python 3.10+
  - system: Docker + docker-compose
  - system: AWS (optional for cloud deploy)
allowed-tools:
  - run_shell_command
  - web_fetch
  - python
  - docker
---

# End-to-End Agentic AI Automation Lab Skill

Use this skill when you need a ready-made set of blueprints for building autonomous assay agents, notebook copilots, or workflow directors that can escalate to physical lab equipment via n8n or MCP bridges.

## What You Get from the Repository
- **Framework coverage:** LangChain, LangGraph, CrewAI, AutoGen, Agno, LangFlow UI modules.
- **Automation fabric:** n8n workflows plus GitHub Actions CI/CD for continuous deployment.
- **Protocol adapters:** Model Context Protocol (MCP) server examples for standardized tool calls.
- **Deployment targets:** Docker Compose stacks, AWS (ECR/ECS, EC2), BentoML serving templates.
- **Observability:** LangSmith, Opik, ClearML dashboards for tracing agent behavior.

## Quickstart
1. Clone the lab portfolio:
   ```bash
   git clone https://github.com/MDalamin5/End-to-End-Agentic-Ai-Automation-Lab.git
   cd End-to-End-Agentic-Ai-Automation-Lab
   ```
2. Create `.env` from `env.example` and populate keys:
   - `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `LANGSMITH_API_KEY`
   - `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` if deploying to AWS
   - `N8N_PERSONAL_API_KEY` when chaining to instrument endpoints.
3. Bootstrap the base environment (Anaconda or `uv`):
   ```bash
   conda env create -f envs/core.yml
   conda activate agentic-lab
   pre-commit install
   ```
4. Launch LangFlow or n8n canvases from `automation/` to visually edit workflows before exporting YAML/JSON definitions for CI.

## Recommended Build Path
| Phase | Module | Outcome |
|-------|--------|---------|
| Architecture dry run | `frameworks/langgraph_orchestrator/` | Supervisor-worker multi-agent plan for protocol optimization.
| Retrieval | `rag/adaptive_rag_pipeline/` | Agentic RAG that routes to domain-specific vector DBs (FAISS, Chroma).
| MCP + lab hooks | `mcp/bench-bot/` | Standardized tool contracts that trigger Opentrons, plate readers, or ELN updates.
| Automation | `automation/n8n/` | Low-code flows for QC scripts, Slack alerts, or instrument macros.
| Deployment | `deploy/aws_bentoml/` | Containerized services with GitHub Actions for nightly refresh.

## Usage Notes
- **CrewAI vs AutoGen:** start with CrewAI for deterministic role definitions; switch to AutoGen for dynamic agent spawning.
- **LangGraph memory patterns:** reuse `memory/episodic_graph_state.py` to capture reagent history and avoid redundant experiments.
- **MCP alignment:** use `.well-known/mcp/manifest.json` templates to register new assay tools so agents can call them uniformly.
- **n8n bridging:** import the provided JSON flows, then swap placeholder webhooks with your instrument endpoints or LIMS REST calls.

## Operational Checklist
- Pin framework versions using the lab's `uv.lock` or `poetry.lock` snapshot to avoid breaking agent compatibility.
- Use GitHub Actions recipes in `ci/` to lint prompts, run notebook smoke-tests, and push Docker images to ECR.
- Connect LangSmith tracing to Anthropic/OpenAI keys so wet-lab safety reviews can replay agent decisions.
- When moving to AWS, provision S3 buckets for artifact exchange plus Secrets Manager entries for API keys; the repo's Terraform stubs cover this.

## Security Notes
- **Patch LangChain/LangGraph dependencies:** February 2026 fixes addressed remote-code-execution flaws triggered by malicious tool definitions. Update `langchain>=0.3.12`, `langgraph>=0.1.22`, and rebuild Docker images before exposing new endpoints. https://www.techradar.com/pro/security/langchain-fixes-serious-vulnerabilities-that-gave-hackers-the-ability-to-run-malicious-code
- **Secrets hygiene:** rotate `.env` values whenever you share the automation stack, and prefer your secrets manager to populate runtime variables.

## References
1. GitHub – *MDalamin5/End-to-End-Agentic-Ai-Automation-Lab*. https://github.com/MDalamin5/End-to-End-Agentic-Ai-Automation-Lab
2. MCP Cow catalog – *End-to-End Agentic AI Automation Lab* overview. https://mcpcow.com/zh/service/end-to-end-agentic-ai-automation-lab/
3. Ecosyste.ms topic feed – repository telemetry (stars, sync time). https://repos.ecosyste.ms/topics/agentic-rag

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
