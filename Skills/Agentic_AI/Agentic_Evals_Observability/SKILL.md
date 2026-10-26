---
name: agentic-evals-observability
description: Design evaluation, tracing, monitoring, scope-control, and rollback discipline for agent systems. Use when an agent workflow is becoming important enough that you need evidence, not vibes, to decide whether it is good.
keywords:
  - evals
  - observability
  - tracing
  - monitoring
  - regression
  - scope-control
  - scientific-validation
measurable_outcome: Define an eval and observability plan with offline tests, online monitoring, and rollback thresholds within 2 hours.
metadata:
  author: MD BABU MIA
  version: "2026.05"
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

## Core Capabilities

- Design clinical testing harnesses that evaluate patient trajectories, tool actions, escalation, reproducible traces, and regression gates within a defined scope of practice.

## Workflow

1. Define the task classes, success criteria, and failure classes before running benchmarks.
2. Define the authorized scope: files, tools, networks, datasets, patient records, lab actions, and user-approved side effects.
3. Instrument traces first so every eval failure can be debugged at the step level.
4. Separate offline evaluation from online monitoring; both are required.
5. Score for correctness, tool behavior, scope control, cost, latency, and safety, not just final-answer quality.
6. For scientific agents, score claim boundary discipline, reproducibility, code execution logs, citation quality, and human-checkpoint compliance.
7. Set rollback thresholds before deployment so regressions have teeth.

## Clinical Testing Harnesses

Evidence status: The letter cited in References argues for trajectory-level evaluation, clinical edge-case scenarios, escalation testing, and staged evidence thresholds. It reports no new data generated or analysed; it does not establish experimentally validated harness performance or clinical benefit. The following are conceptual implementation recommendations for this skill, not tested results from the paper.

- **Simulated patient trajectories:** Build versioned scenarios with evolving patient state, missing or conflicting information, and tool failures. Define expected actions and stopping points across the trajectory, not only the final answer.
- **Tool-action assertions:** Check each proposed and executed action against scenario-specific permissions, required inputs, patient identity, ordering constraints, and prohibited side effects in a sandbox.
- **Escalation behavior:** Specify when uncertainty, conflicting evidence, or scope limits require clinician review. Assert timely handoff with relevant context and no further restricted action until review.
- **Reproducible traces:** Capture scenario versions, initial state, model/prompt/tool/environment versions, tool inputs and outputs, state transitions, assertions, and handoffs. Preserve fixtures and seeds where supported for replay; record nondeterminism rather than claiming identical reruns.
- **Regression gates:** Rerun the versioned suite after model, prompt, tool, or scope changes. Predefine acceptance criteria for action safety and escalation; block release on critical assertion failures and require review of regressions. Tie scope expansion to additional evidence, and report measured local results separately from conceptual recommendations.

## Guardrails

- Do not ship agent changes without a representative eval set.
- Do not rely on one metric; combine exact checks, LLM judges, human review, and cost telemetry.
- Record model, prompt, tool config, and environment for every major run.
- Prefer OTel-compatible tracing so data is portable across observability stacks.
- Include benign-task tests that detect out-of-scope edits, tool calls, deletes, network access, or unrelated configuration changes.
- Do not accept scientific-agent outputs without a logged validation endpoint and a clear label for hypothesis versus validated result.

## Output Requirements

- Include offline eval design.
- Include online monitoring signals.
- Include at least one rollback threshold tied to quality, safety, or cost.
- Include one scope-control eval and one human-review checkpoint.

## References

- Waisberg E, Guarnieri JW. *Agentic AI in Medicine: Challenges for Responsible Development and the Case for Clinical Testing Harnesses.* Ann Biomed Eng. Published online 23 September 2026. Letter; conceptual recommendations, no new data generated or analysed. https://pubmed.ncbi.nlm.nih.gov/42776404/
