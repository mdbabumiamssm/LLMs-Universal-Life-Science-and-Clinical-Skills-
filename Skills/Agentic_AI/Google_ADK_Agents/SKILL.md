---
name: google-adk-agents
description: Build, evaluate, and deploy agents with Google's Agent Development Kit (ADK). Use when you want code-first multi-agent systems, workflow agents, MCP tools, or Google-supported agent deployment paths.
keywords:
  - google
  - adk
  - agent-development-kit
  - multi-agent
  - mcp
measurable_outcome: Deliver a working ADK-based agent plan with runtime choice, tool strategy, and evaluation path within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
  upstream_repo: https://github.com/google/adk-python
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in ADK docs and Google developer announcements checked on 2026-04-13.
  - source: official_repositories
    score: 0.98
    rationale: Implementation details are cross-checked against the official Google ADK repository.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Google ADK Agents

Use this skill when you want Google's agent framework primitives instead of retrofitting agent behavior onto a generic app framework.

## Workflow

1. Pick the runtime language first: Python is the default, but ADK also supports TypeScript, Go, and Java.
2. Decide whether the problem is best modeled as an LLM agent, a workflow agent, or a multi-agent system.
3. Choose the tool surface: function tools, MCP tools, OpenAPI tools, or native integrations.
4. Define evaluation and runtime strategy before deployment, not after.
5. Validate locally, then promote to managed runtime or production infra only after passing a small eval set.

## Guardrails

- Keep agent boundaries explicit; avoid one giant catch-all agent.
- Prefer documented ADK primitives over undocumented framework internals.
- Record the model/provider abstraction used so the workflow stays reproducible.
- Treat third-party integrations as optional until auth, quotas, and failure modes are documented.

## Output Requirements

- State the ADK runtime and language.
- State the agent topology (single, workflow, or multi-agent).
- State the evaluation plan and one production risk.
