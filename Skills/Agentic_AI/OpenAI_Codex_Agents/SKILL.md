---
name: openai-codex-agents
description: Build and operate OpenAI-first coding and agent workflows using Codex app/cloud, the Responses API, current GPT and Codex models, Agents SDK, hosted tools, tool search, MCP/connectors, skills, and approval-aware tool execution. Use when you need long-horizon software agents or OpenAI-native multi-agent orchestration.
keywords:
  - openai
  - codex
  - agents-sdk
  - responses-api
  - mcp
measurable_outcome: Stand up a tested OpenAI-first agent workflow with model choice, tool policy, tracing, and rollback criteria documented within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.05"
  upstream_repo: https://github.com/openai/openai-agents-python
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in OpenAI developer docs, Codex docs, and API guides checked on 2026-05-22.
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

1. Start with the Responses API unless you need the Codex product surface or the Agents SDK orchestration layer.
2. Use Codex app, web, IDE, GitHub, or cloud tasks when the work is repository-scoped, diff-reviewable, and benefits from isolated worktrees or background execution.
3. Pick the model deliberately from the current model catalog; document whether the task needs a Codex-class coding model, a frontier reasoning model, a deep-research model, or a computer-use model.
4. Choose the tool surface explicitly: hosted web/file/code tools, hosted MCP, tool search, shell, apply_patch, computer use, or local runtime tools.
5. Use the Agents SDK when you need handoffs, guardrails, sessions, tracing, hosted containers, skills, shell/apply_patch control, or multi-agent composition.
6. Use MCP/connectors only with explicit approval policy, domain trust, OAuth/resource-discovery review, and auditability in mind.
7. Validate the workflow on a real repo or real task with a small eval set before wider rollout.

## Guardrails

- Default to approval for sensitive MCP or connector actions.
- Record the exact model, reasoning setting, and tool policy used in tests.
- Keep coding agents on a bounded write scope and enforce diff review before merge.
- Prefer official OpenAI SDKs and docs over third-party wrappers when behavior matters.
- Test for out-of-scope file edits, hidden network access, and unrelated config rewrites before granting broader autonomy.

## Output Requirements

- State the chosen model and why.
- State whether the workflow uses Codex, Responses only, Agents SDK, or a specialized research/computer-use surface.
- State the tool/approval policy and one rollback trigger.
