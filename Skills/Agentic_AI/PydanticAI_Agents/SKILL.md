---
name: pydanticai-agents
description: Build typed, provider-agnostic agents with PydanticAI. Use when structured I/O, dependency injection, MCP support, and OpenTelemetry-friendly observability matter more than framework hype.
keywords:
  - pydanticai
  - typed-agents
  - validation
  - logfire
  - mcp
measurable_outcome: Produce a typed agent design with validated inputs/outputs, tool plan, and observability hooks within 90 minutes.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
  upstream_repo: https://github.com/pydantic/pydantic-ai
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in PydanticAI and Logfire documentation checked on 2026-04-13.
  - source: official_repositories
    score: 0.98
    rationale: Implementation patterns are cross-checked against the maintainer-owned PydanticAI repository.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# PydanticAI Agents

Use this skill when you care about typed contracts, validation, and clean Python engineering as much as raw model output.

## Workflow

1. Define the agent's structured inputs, outputs, and dependencies before writing prompts.
2. Choose the provider model through PydanticAI's model layer so the workflow remains portable.
3. Add tools, dependency injection, and structured outputs only where they simplify the system.
4. Instrument the workflow with Logfire or another OTel-compatible backend before shipping.
5. Back the agent with tests and evals, especially when schema correctness matters.

## Guardrails

- Do not bypass typed outputs for convenience on critical workflows.
- Keep tool schemas strict and explicit.
- Prefer MCP integration through documented interfaces rather than hidden adapters.
- Treat observability as mandatory for production agents.

## Output Requirements

- State the output schema strategy.
- State the provider/model path.
- State the observability path and one failure mode to test.
