---
name: deepseek-api-operations-2026
description: Integrate and operate DeepSeek APIs with current docs and compatibility guidance. Use when implementing DeepSeek chat, reasoning, tool calling, or FIM workflows through its OpenAI-compatible API.
keywords:
  - deepseek
  - openai-compatible
  - reasoning
  - tool-calls
  - fim
measurable_outcome: Produce a DeepSeek integration plan with endpoint choice, model choice, and compatibility assumptions within 60 minutes.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in DeepSeek API docs checked on 2026-04-13.
  - source: official_integrations
    score: 0.95
    rationale: Compatibility guidance is grounded in DeepSeek's documented OpenAI-compatible interface and integrations pages.
allowed-tools:
  - read_file
  - run_shell_command
---

# DeepSeek API Operations (2026)

## Workflow

1. Start from DeepSeek's OpenAI-compatible API assumptions and document the base URL explicitly.
2. Choose between `deepseek-chat`, `deepseek-reasoner`, or beta/FIM paths based on the workload.
3. Validate tool calling, JSON mode, and streaming behavior against the official docs before using the OpenAI SDK as a drop-in.
4. Plan around long-lived requests and server-side timing behavior rather than assuming OpenAI-style latency.
5. Run a smoke test that proves model output, reasoning output, and tool output behave as expected.

## Output Requirements

- State the chosen model and base URL.
- State the compatibility assumptions.
- State one timeout or retry guardrail.
