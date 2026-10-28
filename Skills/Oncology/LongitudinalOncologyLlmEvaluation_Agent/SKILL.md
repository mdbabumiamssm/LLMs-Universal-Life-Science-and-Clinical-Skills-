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
name: 'longitudinal-oncology-llm-evaluation'
description: 'Evaluate longitudinal cancer-care LLM responses using patient-specific, phase-aware rubrics and decision-time evidence, grounded in NPC-RubricBench for nasopharyngeal carcinoma research.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Longitudinal Oncology LLM Evaluation

## Overview

Evaluate LLM responses across a longitudinal cancer-care pathway using patient-specific atomic criteria and evidence available at each decision time. The supplied NPC-RubricBench finding concerns nasopharyngeal carcinoma and motivates separate analysis of care phases, explicit decision errors, omissions, and prompt specificity. This skill supports research evaluation; benchmark performance does not establish clinical deployment readiness or generalization to other cancers.

## When to Use This Skill

- Assess whether diagnostic performance persists across later care responsibilities.
- Organize longitudinal nasopharyngeal carcinoma records into evaluable patient-phase units.
- Construct or audit patient-specific rubrics for evidence leakage and clinical relevance.
- Compare model responses to broad versus detailed prompts on identical clinical evidence.
- Investigate phase-specific errors and omissions before proposing safeguards for further evaluation.

## Core Capabilities

1. **Establish scope and provenance.** Record disease, cohort, sites, evaluation purpose, model versions, and source version. The supplied finding describes 405 patients from two centers, 941 patient-phase units across six phases, and 17,688 criteria across five dimensions. Treat these as reported benchmark characteristics, never as counts for a new dataset. Obtain the full methods and rubric definitions before claiming an exact reproduction; if unavailable, label the work an adapted protocol based on the supplied summary.

2. **Build decision-time snapshots.** For each pseudonymous patient and phase, define a decision timestamp and assemble only evidence available by that cutoff. Distinguish event time from information availability time; exclude later results, subsequent treatment decisions, outcomes, and retrospective annotations that reveal them. Flag uncertain timestamps and exclude affected evidence pending review. Keep all phases from a patient together in any development/test split.

3. **Map care phases explicitly.** Use verified benchmark phase definitions when available, recording phase order and inclusion rules. The summary names initial work-up, anatomical staging, and post-treatment follow-up but does not enumerate all six phases; do not invent the remaining labels. For a local adaptation, document the supplied phase mapping and mark absent or unevaluable phases without creating clinical events.

4. **Construct patient-specific atomic rubrics.** Define one assessable requirement per criterion, tied to the patient's phase and decision-time evidence. Record criterion ID, dimension, expected behavior, evidence locator, applicability rule, and scoring rule. Separate actions required by available evidence from conditional actions and requests for missing information. Have qualified oncology reviewers establish or adjudicate clinical expectations before treating scores as validated judgments.

5. **Preserve dimension definitions.** The finding names Decision Quality, Evidence Faithfulness, and Safety Adherence, while reporting five total dimensions. Retrieve the remaining names and scoring definitions from verified materials before reporting the complete benchmark. Otherwise report only explicitly defined local dimensions, identify their adapted status, and avoid presenting a partial score as the official benchmark metric.

6. **Compare prompt granularity fairly.** Evaluate broad and checklist-like prompts against identical snapshots and frozen rubrics. Record exact prompts, response text, model/version, generation settings, and repeats when available. Keep expected answers and evaluator-only rubrics out of model inputs. Report changes in Decision Quality separately from Evidence Faithfulness and Safety Adherence: more detailed prompts can improve one dimension while worsening others, as reported in the supplied finding.

7. **Score and classify failures.** Apply verified benchmark rules when available. For an adapted rubric, use transparent labels such as met, explicit error, omission, not applicable, and unresolved. An explicit error requires an incorrect asserted decision; an omission requires an applicable expected decision that is absent. Do not equate missing clinical evidence with a model omission. Preserve response excerpts and evidence locators, record unsupported claims and safety violations separately, and adjudicate disagreements rather than forcing uncertain labels.

8. **Aggregate without hiding phase differences.** Report criterion counts, applicable denominators, exclusions, and unresolved cases for each model, phase, dimension, and prompt condition. For local descriptive rates, divide each failure count by the stated applicable, resolved criterion count and separately report unresolved coverage. Distinguish pooled criterion rates from patient-level or phase-level averages; if estimating uncertainty, account for repeated phases within patients. Do not copy published percentages into local results or compare model families without documenting how membership and evaluation conditions were determined.

9. **Produce a bounded research report.** Within 15 minutes, complete a scoped pilot using supplied records and responses, or deliver an executable evaluation specification with explicit missing inputs. State which units were actually scored, summarize phase-specific failures and prompt trade-offs, and propose safeguards as hypotheses requiring further testing. If data, responses, or rubric definitions are missing, return an unscored specification rather than invented results; a full benchmark run is not implied by the time target.

## Inputs / Outputs

**Inputs**

- Authorized, de-identified longitudinal records with patient identifiers, phase assignments, event timestamps, availability timestamps, and evidence locators.
- Benchmark methods and rubric materials, or an explicitly identified local phase map and clinician-reviewed evaluation protocol.
- Model responses or an authorized inference setup, exact prompt variants, model identifiers, and generation settings.
- Scope of the pilot, comparison groups, scoring definitions, and any supplied adjudications.

**Outputs**

- Evaluation manifest: source version, disease scope, included patients/phases, model settings, rubric version, prompt variants, and reproduction-versus-adaptation status.
- Patient-phase inventory: `patient_id`, `phase`, `decision_time`, `included_evidence`, `excluded_evidence`, and `exclusion_reason`.
- Atomic criterion ledger: `patient_id`, `phase`, `criterion_id`, `dimension`, `expected_behavior`, `evidence_locator`, `applicability`, and `scoring_rule`.
- Scoring ledger: `model`, `prompt_variant`, `criterion_id`, `rating`, `response_excerpt`, `rationale`, and `adjudication_status`, linked to patient-phase identifiers.
- Phase-by-model report with denominators, error and omission rates, dimension-specific prompt effects, unresolved cases, and evidence-leakage checks.
- Limitations and proposed phase-specific safeguards, clearly separating reported source findings, locally observed results, and untested hypotheses.

Use only authorized environments for patient records and inference; do not send identifiable records through web retrieval tools. A valid output preserves traceability to decision-time evidence, explicitly marks missing definitions and unscored units, and makes no patient-care recommendations or deployment claims from benchmark scores alone. Extension beyond nasopharyngeal carcinoma requires a separately defined and validated disease-specific rubric.

## References

- [Patient-specific rubric-based evaluation of large language models across longitudinal cancer care — arXiv:2610.35847v1](http://arxiv.org/abs/2610.35847v1), published October 26, 2026. Source for NPC-RubricBench and the reported phase-dependent failure and prompt-granularity findings. This skill is grounded in the supplied source summary; the full text was not retrievable during authoring, so unspecified phase names, dimension names, and official scoring rules remain unverified.
