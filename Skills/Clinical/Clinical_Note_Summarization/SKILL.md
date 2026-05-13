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
name: clinical-note-summarization
description: Structure raw clinical notes into SOAP-format summaries with explicit contradictions, missing data, and ICD-linked assessments using the provided prompt + usage script.
measurable_outcome: Produce SOAP markdown and JSON outputs covering all four sections with at least 95% note coverage and explicit missing information within 2 minutes per note.
allowed-tools:
  - read_file
  - run_shell_command
---

## At-a-Glance
- **description (10-20 chars):** SOAP builder
- **keywords:** clinical-notes, SOAP, guardrails, ICD10, gaps
- **measurable_outcome:** Produce SOAP markdown + JSON (when requested) covering all four sections with ≥95% note coverage and explicit missing info in ≤2 minutes per note.

## Inputs
- `note_text` (dictation, OCR, or EHR export) and optional `patient_context` metadata.
- `output_format` (`markdown` default, `json` when downstream validators need schema).

## Outputs
1. Structured SOAP summary with Subjective/Objective/Assessment/Plan bulleting.
2. Alerts plus missing-information checklist.
3. Optional JSON payload using schema from README.

## Core Capabilities
- Require clinical-note quality evaluation before AI-generated summaries enter clinical workflows, including note-level rubric scoring for correctness, omissions, and risk of harm, benchmark designs matched to the target note task, and human adjudication of disputed or high-risk outputs.
- Apply a clinical-note quality evaluation module for AI-generated documentation that scores correctness, omissions, hallucination and risk-of-harm, uses note-type-specific rubrics, adjudicates inter-rater disagreements, and reports benchmark methods transparently.
- Evaluate AI-generated clinical notes and SOAP summaries for correctness, omissions, factuality, harm-risk, and structure quality using rubric-based clinician review, benchmark design, inter-rater agreement checks, and regression tests before deployment.
- Build clinical-note quality evaluation modules for AI-generated documentation that check correctness, omissions, harmful hallucinations, note-specific rubric criteria, human reviewer sampling, and transparent benchmark reporting.
- Design dataset- and task-specific clinical-note quality rubrics that assess factual correctness, omissions, hallucinations, harmfulness, structure adherence, completeness, and clinician preference.
- Select evaluation methods for AI-generated clinical notes by pairing rubric-based scoring with experimental benchmark selection and reviewer agreement reporting.
- Evaluate AI-generated clinical notes with methods covering factual correctness, omissions, hallucinations, note completeness, readability, downstream safety risk, inter-rater review, and benchmark reporting templates.
- Require clinician-adjudicated evaluation of AI-generated clinical notes before downstream use, covering correctness, omissions, hallucinations, risk of harm, note completeness, and benchmark design fit for the target note task.
- Evaluate AI-generated clinical notes before deployment for correctness, completeness, harmful omission, factual consistency, and template adherence using clinician rubric review and transparent benchmark reporting.

## Quality Evaluation
- Score generated notes for correctness, omissions, hallucinations, risk of harm, and note completeness using explicit review rubrics; select benchmarks that match the clinical note task being tested, report reviewer agreement when multiple reviewers assess the same outputs, and require clinician adjudication before generated notes are used downstream.
- Before deployment, evaluate AI-generated clinical notes for correctness, completeness, harmful omission, factual consistency, and template adherence; use clinician rubric review and report benchmark methods transparently.

## Workflow
1. **Load system prompt:** `prompt.md` enforces no hallucinations + data gap surfacing.
2. **Normalize input:** Pre-clean vitals, labs, and timeline context when available.
3. **Generate summary:** Call preferred LLM (OpenAI, Anthropic, Gemini, OSS) using `usage.py` as a template.
4. **Validate:** Cross-check extracted values vs. source text and ensure contradictions/missing data are spelled out.
5. **Deliver output:** Provide markdown + JSON as required and log PHI handling steps.

## Guardrails
- Never invent findings; state "not provided" explicitly.
- Mark outputs as documentation support only—not clinical decisions.
- Strip/re-mask PHI before storing prompts/responses.

## References
- For detailed schema, guardrails, and integration snippets see `README.md`, `prompt.md`, and `usage.py`.
- https://pubmed.ncbi.nlm.nih.gov/41955894/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
