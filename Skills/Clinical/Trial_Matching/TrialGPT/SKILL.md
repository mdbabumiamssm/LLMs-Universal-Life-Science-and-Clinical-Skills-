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
name: trialgpt-matching
description: Trial shortlist
keywords:
  - retrieval
  - ranking
  - ClinicalTrials
  - patient-profile
measurable_outcome: Produce ≥5 ranked trials (when available) with rationale + missing-data notes within 3 minutes of receiving a patient query.
license: MIT
metadata:
  version: "1.0.0"
compatibility:
  - system: Python 3.9+
allowed-tools:
  - run_shell_command
  - read_file
---

# TrialGPT Matching

Run the locally checked-out TrialGPT pipeline to retrieve, rank, and explain candidate trials for a patient before deeper eligibility review.

## Core Capabilities
- Separate eligibility parsing, patient evidence extraction, symbolic rule execution, discrepancy review, and site-level audit metrics for prospective oncology trial-matching workflows that use neuro-symbolic multi-agent screening with an oncology-specific knowledge graph.
- Apply a neuro-symbolic multi-agent trial-matching pattern for high-volume oncology workflows: ground retrieval and ranking in an oncology-specific knowledge graph, reason at the eligibility-criterion level, arbitrate patient-trial eligibility decisions, attach confidence scores, preserve prospective validation context, and route matches for clinician review.
- Incorporate prospective oncology trial matching patterns from neuro-symbolic multi-agent systems and oncology knowledge graphs: criterion-level reasoning, KG-backed eligibility checks, patient-scale evaluation context, confidence scoring, and oncologist review.
- Support prospective oncology trial matching for large real-world cohorts with neuro-symbolic, multi-agent workflows grounded in an oncology-specific knowledge graph, including criterion-level matching, evidence provenance, unresolved eligibility gaps, and human review flags.
- Apply prospective oncology trial matching patterns from large patient cohorts: neuro-symbolic multi-agent review, oncology knowledge graph grounding, criterion-level evidence extraction, unresolved-data notes, and clinician validation for each screening run.
- Use neuro-symbolic multi-agent trial matching patterns with oncology knowledge graph grounding, criterion decomposition, patient-trial matching across large prospective cohorts, contradiction handling across patient facts and eligibility criteria, and human-reviewable rationales linking evidence to eligibility decisions.
- Combine an oncology-specific knowledge graph with criterion-level eligibility reasoning and neuro-symbolic multi-agent review for high-volume prospective screening, routing patient-trial matches and unresolved eligibility gaps to human reviewers as in the 2026 prospective oncology evaluation in 3804 patients.
- Run criterion-level symbolic checks grounded in oncology knowledge graph context, score match confidence, and emit clinician-facing explanations and audit outputs for prospective cohort oncology trial screening.

## Inputs
- Patient summary (structured JSON or free text) with condition keywords.
- Optional filters: geography, phase, intervention, biomarker.
- Up-to-date ClinicalTrials.gov dump or API access.

## Outputs
- Ranked trial table with NCT ID, title, score, and short justification.
- Parsed inclusion/exclusion text ready for downstream eligibility agents.
- Missing data checklist (e.g., "ECOG not provided").
- Prospective oncology screening packet using neuro-symbolic criteria parsing, oncology-specific knowledge graph context, multi-agent eligibility review, criterion-level evidence, confidence scoring, and human review flags for high-volume patient matching.

## Workflow
1. **Setup:** `cd repo && pip install -r requirements.txt` (or reuse env).
2. **Trial retrieval:** Run TrialGPT retriever to pull candidate trials for the indication.
3. **Criteria parsing:** Convert eligibility blocks to structured criteria JSON.
4. **Patient profiling:** Summarize patient facts (labs, prior therapies, biomarkers).
5. **Ranking:** Execute TrialGPT ranking script to score each trial and emit explanations.
6. **Handoff:** Export ranked list + structured criteria for `trial-eligibility-agent`.

## Guardrails
- Refresh ClinicalTrials.gov metadata regularly to avoid stale trials.
- Label scores as AI-generated suggestions pending clinician validation.
- Retain prompt/config metadata for audit trails.

## References
- Detailed usage instructions and repo layout live in `README.md`.
- Coordinate with `Skills/Clinical/Trial_Eligibility_Agent` for criterion-level review.
- https://pubmed.ncbi.nlm.nih.gov/42004487/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
