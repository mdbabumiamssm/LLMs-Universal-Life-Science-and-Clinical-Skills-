---
name: cohere-platform-operations-2026
description: Integrate and operate Cohere APIs with current model, rerank, embedding, transcribe, and SDK guidance. Use when selecting Cohere models, building search or agent workflows, or planning migration across Cohere platform updates.
keywords:
  - cohere
  - rerank
  - embeddings
  - transcribe
  - sdk
measurable_outcome: Produce a working Cohere operating plan with model family, endpoint choice, compatibility notes, and safeguards documented within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
  upstream_repo: https://github.com/cohere-ai/cohere-python
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Guidance is grounded in Cohere docs, model pages, and changelog entries checked on 2026-04-20.
  - source: official_repositories
    score: 0.97
    rationale: SDK and connector guidance is cross-checked against Cohere-maintained repositories.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Cohere Platform Operations (2026)

Use this skill when Cohere is the production platform or ranking/search stack, not just an interchangeable model endpoint.

## Workflow

1. Check current Cohere models and release notes before implementation or migration.
2. Choose the model family by task: generation, embeddings, rerank, or transcription.
3. Prefer official Cohere SDK patterns for auth, request schema, batching, and streaming.
4. Define retry, timeout, and rate-limit behavior before load testing.
5. Validate one representative endpoint per workload before broader rollout.

## Guardrails

- Keep model names pinned in production rather than depending on implicit defaults.
- Treat rerank, embed, and transcription as separate operational surfaces with different latency and cost profiles.
- Record SDK version, endpoint, and region or deployment assumptions in test evidence.
- Keep one fallback path for critical retrieval or generation workflows.

## Output Requirements

- State the chosen Cohere model family and endpoint.
- State one compatibility or migration note.
- State one operational safeguard such as timeout, retry, quota, or fallback.
