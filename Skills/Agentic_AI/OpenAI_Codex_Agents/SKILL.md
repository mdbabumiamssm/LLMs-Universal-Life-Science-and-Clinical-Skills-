---
name: openai-codex-agents
description: Build and operate OpenAI-first coding and agent workflows using the Responses API, Codex models, Agents SDK, MCP/connectors, and approval-aware tool execution. Use when you need long-horizon software agents or OpenAI-native multi-agent orchestration.
keywords:
  - openai
  - codex
  - agents-sdk
  - responses-api
  - mcp
measurable_outcome: Stand up a tested OpenAI-first agent workflow with model choice, tool policy, tracing, and rollback criteria documented within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
  upstream_repo: https://github.com/openai/openai-agents-python
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in OpenAI developer docs and API guides checked on 2026-04-13.
  - source: official_repositories
    score: 0.98
    rationale: SDK and skills implementation details are cross-checked against maintainer-owned OpenAI repositories.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# OpenAI Codex Agents

Use this skill when the job is best served by OpenAI-native agent building rather than a generic framework wrapper.

## Workflow

1. Start with the Responses API unless you have a hard compatibility reason not to.
2. Pick the model for the job: frontier GPT models for broad reasoning, Codex models for long-horizon coding, and deep-research models for multi-step research tasks.
3. Use the Agents SDK when you need handoffs, guardrails, sessions, tracing, or multi-agent composition.
4. Use MCP/connectors only with explicit approval policy, domain trust, and auditability in mind.
5. Validate the workflow on a real repo or real task with a small eval set before wider rollout.

## Guardrails

- Default to approval for sensitive MCP or connector actions.
- Record the exact model, reasoning setting, and tool policy used in tests.
- Keep coding agents on a bounded write scope and enforce diff review before merge.
- Prefer official OpenAI SDKs and docs over third-party wrappers when behavior matters.

## Output Requirements

- State the chosen model and why.
- State whether the workflow uses Responses only, Agents SDK, or both.
- State the tool/approval policy and one rollback trigger.
