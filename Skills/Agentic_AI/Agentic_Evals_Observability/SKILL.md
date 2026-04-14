---
name: agentic-evals-observability
description: Design evaluation, tracing, monitoring, and rollback discipline for agent systems. Use when an agent workflow is becoming important enough that you need evidence, not vibes, to decide whether it is good.
keywords:
  - evals
  - observability
  - tracing
  - monitoring
  - regression
measurable_outcome: Define an eval and observability plan with offline tests, online monitoring, and rollback thresholds within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in official evaluation and observability documentation checked on 2026-04-13.
  - source: protocol_and_sdk_docs
    score: 0.97
    rationale: Tracing and telemetry expectations are cross-checked against official SDK docs and OpenTelemetry conventions.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Agentic Evals and Observability

Use this skill when the question changes from "can the agent run" to "can we trust it in production".

## Workflow

1. Define the task classes, success criteria, and failure classes before running benchmarks.
2. Instrument traces first so every eval failure can be debugged at the step level.
3. Separate offline evaluation from online monitoring; both are required.
4. Score for correctness, tool behavior, cost, latency, and safety, not just final-answer quality.
5. Set rollback thresholds before deployment so regressions have teeth.

## Guardrails

- Do not ship agent changes without a representative eval set.
- Do not rely on one metric; combine exact checks, LLM judges, human review, and cost telemetry.
- Record model, prompt, tool config, and environment for every major run.
- Prefer OTel-compatible tracing so data is portable across observability stacks.

## Output Requirements

- Include offline eval design.
- Include online monitoring signals.
- Include at least one rollback threshold tied to quality, safety, or cost.
