---
name: xai-grok-operations-2026
description: Integrate and operate xAI Grok APIs with current documentation and SDK guidance. Use when implementing Grok tool use, Responses-style workflows, files or collections search, or migration from other provider SDKs.
keywords:
  - xai
  - grok
  - responses
  - tools
  - sdk
measurable_outcome: Produce an xAI integration plan with model, tool strategy, and SDK path within 90 minutes.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in xAI docs checked on 2026-04-13.
  - source: official_repositories
    score: 0.97
    rationale: SDK behavior is cross-checked against the official xAI Python SDK repository.
allowed-tools:
  - read_file
  - run_shell_command
---

# xAI Grok Operations (2026)

## Workflow

1. Confirm whether you want native xAI SDK usage or OpenAI-compatible client usage against `https://api.x.ai/v1`.
2. Choose the Grok model and built-in tool set based on the task.
3. Define whether the workflow needs web search, X search, code execution, collections search, or remote MCP tools.
4. Document regional endpoint, throughput, and migration expectations before production rollout.
5. Validate citations, streaming, and tool billing behavior with a small end-to-end test.

## Output Requirements

- State the chosen model and client path.
- State the tool plan.
- State one operational risk and mitigation.
