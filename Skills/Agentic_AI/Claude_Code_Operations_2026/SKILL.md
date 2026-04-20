---
name: claude-code-operations-2026
description: Build and operate Claude Code workflows in the terminal, IDE, and GitHub Actions with hooks, MCP, and approval-aware repo automation. Use when evaluating or deploying Anthropic's coding-agent surface rather than generic Claude API usage.
keywords:
  - anthropic
  - claude-code
  - coding-agent
  - github-actions
  - hooks
  - mcp
measurable_outcome: Produce a tested Claude Code operating plan with install path, repo permissions, automation hooks, and rollback criteria documented within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
  upstream_repo: https://github.com/anthropics/claude-code
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Guidance is grounded in Anthropic Claude Code documentation checked on 2026-04-20.
  - source: official_repositories
    score: 0.99
    rationale: Operational behavior and automation surfaces are cross-checked against maintainer-owned Anthropic repositories.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Claude Code Operations (2026)

Use this skill when Claude Code is the product surface you are rolling out or evaluating, not just a side note in a broader Anthropic integration.

## Workflow

1. Confirm the deployment surface: local terminal, IDE integration, GitHub Actions, or an internal automation wrapper.
2. Prefer Anthropic's current official install and setup path over stale blog posts or deprecated snippets.
3. Define permissions before rollout: repo write scope, shell/network access, hook behavior, MCP servers, and CI secrets.
4. Use official Claude Code features first - hooks, settings, MCP, slash-command setup, and GitHub Action patterns - before building custom wrappers.
5. Validate on a real repository with diff review, branch isolation, and a clear rollback trigger before broader enablement.

## Guardrails

- Treat repo write access, GitHub Action execution, and MCP connections as separate approval surfaces.
- Keep project-level settings and hooks reviewed in source control; keep local overrides out of shared policy.
- Record the account mode, install method, hook config, and automation trigger path in test notes.
- Require explicit human approval for destructive shell commands, credentialed operations, and autonomous PR merges.

## Output Requirements

- State the Claude Code surface being used and why.
- State the install/auth path and repo permission model.
- State the hook or MCP policy and one concrete rollback trigger.
