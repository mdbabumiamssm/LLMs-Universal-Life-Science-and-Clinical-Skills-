<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'oncology-consult-survival-llm'
description: 'Predict cancer survival from initial oncology consultation documents using zero-shot or fine-tuned LLM workflows with leakage control and calibrated reporting.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Oncology Consultation Survival LLM

## Overview

This skill guides agents through building or evaluating LLM workflows that predict cancer survival from initial oncology consultation documents. It emphasizes reproducible label construction, comparison of zero-shot and fine-tuned general LLMs, strict leakage control, calibration, and clinician-facing reporting suitable for review rather than autonomous care decisions.

## When to Use This Skill

- Predicting mortality, survival time, or survival-risk strata from free-text initial oncology consultation notes.
- Comparing zero-shot prompting against fine-tuning for general LLMs on oncology prognosis tasks.
- Designing a clinically auditable NLP pipeline for consultation-note prognostic modeling.
- Checking survival-label definitions, censoring logic, index dates, and follow-up windows for oncology cohorts.
- Reviewing leakage risks from note timing, copied outcome text, later encounters, hospice/death mentions, or metadata.
- Producing calibrated survival-risk summaries that clinicians can interpret alongside existing clinical context.

## Core Capabilities

1. Cohort and endpoint framing: Define the index note, diagnosis context, survival endpoint, censoring rules, follow-up horizon, and exclusion criteria before modeling.
2. Consultation document preparation: Normalize note text, remove irrelevant boilerplate, preserve clinically meaningful context, and apply required de-identification and data-use controls.
3. Leakage control: Restrict inputs to information available at the initial consultation and inspect text, timestamps, labels, features, and splits for future outcome leakage.
4. Zero-shot baseline design: Create explicit prompts that request structured survival-risk outputs, uncertainty, and evidence snippets without exposing labels or validation examples.
5. Fine-tuning workflow: Build training, validation, and test partitions at the patient level; tune only on training data; and compare against zero-shot baselines using identical endpoints.
6. Fine-tuning versus zero-shot comparison: Treat prompt-only zero-shot prediction as the baseline and justify fine-tuning only through a same-endpoint comparison that preserves leakage control, calibration review, and stratified evaluation across clinically relevant groups.
7. Initial-consult comparison guardrails: For zero-shot versus fine-tuned survival prediction from initial consultation documents, require identical input windows, patient-level splits, leakage checks, calibration assessment, site-specific validation, and reporting of clinically actionable uncertainty before recommending either approach.
8. Zero-shot versus fine-tuned comparison workflow: Predefine the survival endpoint and input window, evaluate both general LLM approaches on the same held-out patient set, repeat leakage checks before scoring, assess calibration, and report cautiously as clinician-reviewed decision support rather than autonomous prognosis.
9. Survival-aware evaluation: Report discrimination, calibration, and clinically meaningful error analysis for the chosen horizon while avoiding unsupported claims about real-world performance.
10. Clinician-facing reporting: Convert model output into concise risk categories, confidence notes, rationale excerpts, and limitations for review by qualified oncology clinicians.
11. Governance and documentation: Record model version, prompt or training recipe, cohort definition, label code, missingness handling, evaluation date, and intended-use boundaries.

## Inputs / Outputs

Inputs:

- Initial oncology consultation documents or de-identified extracts.
- Patient-level index dates, diagnosis context, demographics or clinical variables if approved for use.
- Survival labels, event dates, last-follow-up dates, censoring indicators, and prediction horizons.
- Split definitions that keep all notes from a patient in one partition.
- Candidate zero-shot prompts, fine-tuning datasets, or existing model outputs to audit.

Outputs:

- A reproducible workflow for consultation-note survival prediction.
- Cleaned and leakage-audited model inputs with documented exclusions.
- Zero-shot and, when requested, fine-tuned prediction outputs in a structured schema.
- Evaluation summary covering endpoint definition, cohort counts, discrimination, calibration, subgroup checks when sample size permits, and key error patterns.
- Clinician-facing survival-risk report with uncertainty, caveats, and intended-use limitations.
- Documentation of privacy controls, data provenance, model versioning, and validation boundaries.

## References

- Source finding: Phaterpekar T, Zeng Z, Mali Y, Leung B, Ho C. "Investigating fine-tuning versus zero-shot learning for general large language models when predicting cancer survival from initial oncology consultation documents." PubMed: https://pubmed.ncbi.nlm.nih.gov/42004490/
