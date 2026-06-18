<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

---
name: bio-computational-software-development
description: Full-stack computational software development for biomedical and life
  science applications. Use when building or refactoring research software, LLM-enabled
  analysis platforms, scientific web apps, data pipelines, RAG systems, evaluation
  harnesses, or package-quality Python services for translational research.
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# Computational Software Development

Build production-oriented biomedical software with a bias toward reproducibility, clear interfaces, and testable workflows.

## Workflow

1. Clarify the product boundary: analysis script, library, API, web app, pipeline, or multi-agent system.
2. Inspect the local repository before proposing architecture changes; preserve existing conventions unless they are actively harmful.
3. Choose the simplest stack that fits the job: plain Python package first, then API or UI layers only when they solve a real need.
4. Separate scientific logic, orchestration, and presentation so domain code remains testable outside the UI.
5. Add validation around files, schemas, model outputs, and external API calls; fail loudly when assumptions break.
6. Prefer deterministic scripts for repeated scientific tasks and reserve LLM calls for synthesis, extraction, ranking, or planning.
7. Deliver runnable code plus concise usage notes, tests, and environment assumptions.

## Engineering Priorities

- Keep domain logic in importable modules rather than notebooks or route handlers.
- Treat data contracts explicitly: define expected columns, shapes, units, genome builds, and identifier namespaces.
- For LLM features, specify provider fallback rules, timeout budgets, retry policy, and citation or provenance requirements.
- For biomedical applications, avoid hidden PHI flows and minimize access to sensitive fields.
- Prefer small composable services over one large agent script.

## Common Deliverables

- Python packages with `src/` layout, CLI entry points, and tests.
- Flask or FastAPI backends for analysis services or RAG endpoints.
- Data pipelines for omics preprocessing, QC, and result packaging.
- Multi-LLM orchestration with structured outputs, adjudication, and evaluation.
- Research dashboards that expose results without burying the computational workflow.

## References

- Read `references/architecture-patterns.md` for architecture selection and delivery checklists.
- Read `references/biomedical-llm-patterns.md` when the request involves RAG, citations, or multi-provider systems.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->