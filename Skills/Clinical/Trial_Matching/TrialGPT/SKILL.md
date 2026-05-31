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
- Use a neuro-symbolic multi-agent oncology trial-matching pattern grounded in an oncology-specific knowledge graph: reason at the eligibility-criterion level, carry patient cohort-scale prospective evaluation context from the 3804-patient study, resolve conflicting agent judgments, and preserve audit trails for human trial-navigation review.
- For prospective oncology trial matching, coordinate neuro-symbolic, multi-agent review over an oncology-specific knowledge graph; attach criterion-level evidence to each inclusion/exclusion judgment, document patient-scale validation context from the 3804-patient evaluation, reconcile agent conflicts before final recommendations, and require human review checkpoints before matches are acted on.
- Use neuro-symbolic multi-agent oncology trial matching patterns that ground patient facts and trial criteria in an oncology-specific knowledge graph, run criterion-level symbolic reasoning, preserve prospective patient-scale evaluation context, resolve conflicts among agents, and retain audit trails for each match recommendation.
- Incorporate neuro-symbolic, multi-agent oncology trial matching grounded in an oncology-specific knowledge graph, with criterion-level eligibility reasoning, prospective cohort evaluation context, audit trails, and human review for ambiguous inclusion or exclusion criteria.
- Coordinate multi-agent criteria extraction for oncology patient-trial recommendations by grounding extracted patient facts and trial criteria in an oncology-specific knowledge graph, producing criterion-level explanations, capturing prospective evaluation metrics, and requiring human review before recommendations are acted on.
- Ground neuro-symbolic multi-agent oncology trial matching in an oncology-specific knowledge graph for large patient cohorts, with criterion-level eligibility reasoning, prospective evaluation metric capture, confidence scoring, and audit trails for each patient-trial decision.
- Decompose oncology trial eligibility criteria across neuro-symbolic agents grounded in an oncology-specific knowledge graph, preserve prospective cohort evaluation context from the 3804-patient study, score match confidence, and route eligibility conflicts or low-confidence decisions to human review.
- Apply neuro-symbolic, multi-agent oncology trial matching for large patient cohorts by grounding criteria in oncology-specific knowledge graphs, reasoning at the eligibility-criterion level, preserving prospective evaluation context, assigning confidence scores, and routing results through human review.
- For oncology trial matching informed by the 2026 prospective evaluation in 3804 patients, coordinate neuro-symbolic agents over an oncology-specific knowledge graph to reason at the eligibility-criterion level, preserve provenance for every match decision, track prospective evaluation metrics, and escalate uncertain criteria to human reviewers.
- Implement neuro-symbolic, multi-agent oncology trial matching grounded in an oncology-specific knowledge graph, with criterion-level evidence packets, prospective evaluation metrics, and human-in-the-loop adjudication informed by the 2026 prospective evaluation in 3804 patients.
- Separate eligibility parsing, patient evidence extraction, symbolic rule execution, discrepancy review, and site-level audit metrics for prospective oncology trial-matching workflows that use neuro-symbolic multi-agent screening with an oncology-specific knowledge graph.
- Apply a neuro-symbolic multi-agent trial-matching pattern for high-volume oncology workflows: ground retrieval and ranking in an oncology-specific knowledge graph, reason at the eligibility-criterion level, arbitrate patient-trial eligibility decisions, attach confidence scores, preserve prospective validation context, and route matches for clinician review.
- Incorporate prospective oncology trial matching patterns from neuro-symbolic multi-agent systems and oncology knowledge graphs: criterion-level reasoning, KG-backed eligibility checks, patient-scale evaluation context, confidence scoring, and oncologist review.
- Support prospective oncology trial matching for large real-world cohorts with neuro-symbolic, multi-agent workflows grounded in an oncology-specific knowledge graph, including criterion-level matching, evidence provenance, unresolved eligibility gaps, and human review flags.
- Apply prospective oncology trial matching patterns from large patient cohorts: neuro-symbolic multi-agent review, oncology knowledge graph grounding, criterion-level evidence extraction, unresolved-data notes, and clinician validation for each screening run.
- Use neuro-symbolic multi-agent trial matching patterns with oncology knowledge graph grounding, criterion decomposition, patient-trial matching across large prospective cohorts, contradiction handling across patient facts and eligibility criteria, and human-reviewable rationales linking evidence to eligibility decisions.
- Combine an oncology-specific knowledge graph with criterion-level eligibility reasoning and neuro-symbolic multi-agent review for high-volume prospective screening, routing patient-trial matches and unresolved eligibility gaps to human reviewers as in the 2026 prospective oncology evaluation in 3804 patients.
- Run criterion-level symbolic checks grounded in oncology knowledge graph context, score match confidence, and emit clinician-facing explanations and audit outputs for prospective cohort oncology trial screening.
- For prospective oncology trial matching, decompose eligibility into criterion-level checks, normalize biomarkers and regimens through the oncology knowledge graph, compare multi-agent judgments for disagreement review, assign confidence scores, retain audit trails, and define prospective validation endpoints before clinician sign-off.
- For large prospective oncology cohorts, coordinate neuro-symbolic agents over an oncology-specific knowledge graph to produce criterion-level eligibility reasoning, patient-level audit trails, confidence scoring, and human-review queues for each candidate match.
- Use a neuro-symbolic multi-agent oncology matching pattern that combines oncology knowledge graph grounding, criterion-level evidence extraction, eligibility conflict resolution, confidence scoring, and prospective audit metrics from patient-scale evaluations.
- Parse eligibility at the criterion level, ground oncology concepts in a knowledge graph, track prospective evaluation metrics, resolve conflicts between matching agents, and retain audit trails for patient-trial recommendations.
- Add clinician review gates to prospective oncology trial-matching runs: coordinate neuro-symbolic multi-agent checks over an oncology-specific knowledge graph, preserve criterion-level audit trails, and report cohort-scale evaluation context before recommendations are acted on.
- Ground neuro-symbolic multi-agent oncology trial matching in ontology and knowledge-graph context, reason over each eligibility criterion, resolve eligibility conflicts across patient evidence and trial rules, document prospective patient-scale evaluation context, and route uncertain matches through human review workflows.
- For high-volume oncology patient screening, design prospective evaluations around neuro-symbolic multi-agent outputs grounded in an oncology-specific knowledge graph: capture criterion-level eligibility reasoning, confidence scores, unresolved criteria, and human-in-the-loop review status before any match is treated as actionable.
- For large patient cohorts, combine neuro-symbolic agents with an oncology-specific knowledge graph to evaluate each inclusion or exclusion criterion, record and resolve agent disagreements, preserve prospective evaluation context, and route unresolved patient-trial decisions to human review.

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
