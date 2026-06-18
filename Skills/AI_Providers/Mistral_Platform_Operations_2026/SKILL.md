---
name: mistral-platform-operations-2026
description: Integrate and operate Mistral APIs with current model catalog, SDKs, and agent features. Use when implementing Mistral chat, agents, conversations, files, or coding workflows.
keywords:
  - mistral
  - agents
  - conversations
  - sdk
  - coding
measurable_outcome: Deliver a Mistral integration plan with model choice, SDK path, and operational guardrails within 90 minutes.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in Mistral documentation checked on 2026-04-13.
  - source: official_repositories
    score: 0.97
    rationale: SDK and implementation details are cross-checked against the official Mistral repositories.
allowed-tools:
  - read_file
  - run_shell_command
---

# Mistral Platform Operations (2026)

## Workflow

1. Confirm the target feature set: plain chat, reasoning, agents/conversations, files, OCR, or coding.
2. Select the model from the current catalog and note whether open-weight or hosted behavior is required.
3. Choose the official Python or TypeScript client before considering wrappers.
4. Decide whether to use first-class Agents/Conversations or keep orchestration in your own app layer.
5. Validate auth, retries, streaming, and observability before scaling traffic.

## Output Requirements

- State the chosen model or agent surface.
- State the SDK path.
- State one operational guardrail and one rollback condition.
