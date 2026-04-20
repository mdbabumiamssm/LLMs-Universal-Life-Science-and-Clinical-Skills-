---
name: computer-use-agents-2026
description: Design and operate browser and desktop agents that rely on screenshots, mouse and keyboard control, or hybrid bash/editor/computer loops. Use when deciding between DOM automation, browser agents, and full computer-use workflows.
keywords:
  - computer-use
  - browser-agents
  - desktop-agents
  - openai
  - anthropic
  - benchmark
measurable_outcome: Produce a computer-use agent operating plan with runtime choice, isolation model, approval policy, and evaluation path documented within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
source_reliability:
  - source: official_vendor_docs
    score: 1.0
    rationale: Runtime guidance is grounded in official OpenAI and Anthropic computer-use documentation checked on 2026-04-20.
  - source: benchmark_literature
    score: 0.95
    rationale: Evaluation guidance is anchored to benchmark papers rather than anecdotal demos.
  - source: ecosystem_repositories
    score: 0.9
    rationale: Browser Use and OpenHands are treated as ecosystem references, not canonical first-party sources.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Computer Use Agents (2026)

Use this skill when the agent must operate a real browser or desktop surface, not just call APIs or script a DOM.

## Workflow

1. Classify the surface first: deterministic browser automation, screenshot-based browser agent, or full desktop computer use.
2. Prefer deterministic browser tooling when DOM access is sufficient; escalate to computer-use only when visual grounding or arbitrary GUI control is required.
3. Select the runtime deliberately: OpenAI computer use, Anthropic computer-use plus bash/text editor, or a sandboxed browser-agent stack.
4. Run in an isolated VM, container, or controlled browser environment with minimal credentials, explicit checkpoints, and action logging.
5. Evaluate against representative UI tasks and benchmark-style scenarios before production rollout.

## Guardrails

- Separate test and production accounts, cookies, and browser profiles.
- Require human checkpoints for login, payments, destructive actions, and data export.
- Record screenshots, actions, and stop reasons for every validation run.
- Keep display size, action rate, and retry policy explicit so runs are reproducible.

## Output Requirements

- State whether the workflow uses browser automation, browser agenting, or full computer use.
- State the runtime and isolation model.
- State the approval/auth policy and one concrete stop condition.
