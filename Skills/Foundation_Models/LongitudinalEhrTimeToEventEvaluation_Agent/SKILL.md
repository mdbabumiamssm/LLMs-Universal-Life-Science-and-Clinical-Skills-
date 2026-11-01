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
name: 'longitudinal-ehr-time-to-event-evaluation'
description: 'Evaluate longitudinal EHR foundation models across health systems and prediction horizons, emphasizing censoring, leakage prevention, calibration, and disease detection at low false-positive rates.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Longitudinal EHR Time-to-Event Evaluation

## Overview

Evaluate longitudinal EHR foundation models for incident diagnosis prediction across institutions and time horizons, with explicit attention to detection and false-alert burden. Inspired by the TRACER finding, this skill pairs discrimination metrics with clinically relevant operating points and checks cohort construction, censoring, calibration, and subgroup performance. It produces an auditable evaluation or a clearly labeled protocol when data or model access is unavailable.

## When to Use This Skill

- Assess incident disease predictions at 1-, 2-, or 5-year horizons, or other prespecified horizons.
- Compare performance in health systems excluded from model development.
- Investigate stable AUROC alongside changing sensitivity, positive predictive value, or false-alert burden.
- Audit temporal leakage, incomplete follow-up, competing events, or differences in diagnosis ascertainment.
- Plan calibration and subgroup analyses before considering a screening application.

## Core Capabilities

1. **Separate source evidence from proposed practice.**
   The supplied summary and linked abstract report a decoder-based model pretrained on over 4.5 million patients from four systems, evaluated on 16 incident diseases at 1-, 2-, and 5-year horizons in over 2 million patients from two systems excluded from development. At 95% specificity, flagged patients were up to eight times more likely to receive a diagnosis within one year than unselected patients; this is a maximum reported enrichment, not a universal effect or a causal benefit. The abstract reports variation in detection and false-alert burden despite retained discrimination. The workflow below is proposed evaluation guidance; do not attribute its censoring, calibration, threshold-selection, or subgroup methods to TRACER without checking the full text. Checkpoint availability, access conditions, and clinical deployment suitability remain unestablished by the supplied finding.

2. **Define the prediction contract and temporal cohort.**
   Specify each disease phenotype, code-set version, index date, minimum lookback, incident-case exclusion window, prediction horizon, and eligible population. Distinguish first recorded diagnosis from biological onset. Freeze a cohort manifest with patient counts and exclusions by site, disease, and horizon. Use one prespecified index per patient or define repeated landmark sampling and account for within-patient dependence. Do not select patients using future survival or future visit frequency unless explicitly evaluating that selected population.

3. **Prevent temporal and institutional leakage.**
   Permit only information available at the index time, checking result-availability timestamps as well as encounter dates. Exclude later diagnoses, retrospectively finalized notes, and preprocessing fitted on evaluation records. Define an index-day ordering or exclusion rule when timestamps are ambiguous. Keep patients disjoint across splits, assess cross-system overlap where feasible, and fit vocabularies, imputation, calibration, and thresholds using development partitions. Document all systems used for pretraining, fine-tuning, and model selection; a site used in any of these stages is not fully external.

4. **Handle follow-up, censoring, and competing events.**
   Record event time, last reliable observation, administrative cutoff, and death or other competing events separately. A patient censored before a horizon without the disease has unknown horizon status and must not automatically become a negative. Prespecify whether the target is cumulative incidence in the presence of competing events or a different survival estimand; do not silently censor death when estimating real-world disease incidence. Use appropriate survival estimators and, where justified, inverse-probability-of-censoring weighting for horizon metrics. State the censoring model, conditional independence and positivity assumptions, weight diagnostics, and truncation sensitivity. Treat inadequate follow-up or unstable weights as a limitation, and report complete-follow-up analyses only as explicitly selected sensitivity analyses.

5. **Evaluate screening operating points alongside discrimination.**
   Select disease- and horizon-specific thresholds in a designated development validation set, including a 95% specificity target when reproducing the abstract's operating-point concept. Lock thresholds before external testing and report achieved specificity at every external site. A threshold chosen from external test labels to achieve exactly 95% specificity is descriptive and must be labeled as test-selected, not prospective threshold transport. Report time-dependent AUROC with its case/control definition, sensitivity, specificity, positive predictive value, and event incidence at each horizon. Match all metrics to the chosen censoring and competing-risk estimand.

   For fully observed binary outcomes, report alerts per 1,000 eligible patients as `1000 * (TP + FP) / N`, false alerts per 1,000 as `1000 * FP / N`, and enrichment as `PPV / horizon_event_incidence`. Specificity of 95% means a 5% false-positive rate among noncases, not 5% of all patients. For censored data, use consistently weighted or modeled estimates and label them as estimates rather than raw counts. Report zero denominators as undefined. For repeated screening, distinguish unique patients flagged from alert episodes and specify any suppression interval.

6. **Assess calibration and subgroup performance.**
   Verify that outputs represent absolute horizon risks before reporting calibration; ranking scores require a separately fitted mapping. Compare predicted risks with censoring-aware observed risks through calibration plots, calibration-in-the-large, calibration slope where estimable, and horizon-specific Brier scores. Check probability bounds and nondecreasing cumulative risk across horizons for the same endpoint. Evaluate prespecified age, sex, demographic, utilization, and other available clinically relevant strata within each site, documenting missingness and group definitions. Report event and non-event support, uncertainty, and unstable estimates rather than interpreting sparse groups as equivalent. Treat local recalibration as a distinct adapted model and evaluate it on data held apart from the adaptation set.

7. **Quantify external validity and uncertainty.**
   Present site-level results before pooled summaries, including differences in case mix, coding, observation length, disease incidence, and missing data. Use patient-level resampling within sites for confidence intervals, preserving repeated landmarks together; use paired resampling for model comparisons. State whether intervals condition on fixed thresholds or include threshold-selection uncertainty. Keep exploratory disease, horizon, and subgroup comparisons distinct from prespecified comparisons, and document multiplicity handling. Do not infer broad health-system generalizability from a small number of external systems or equate retrospective prediction with screening benefit.

8. **Execute a bounded, reviewable workflow.**
   Within the 15-minute scope, first inspect the schema and model-output contract, then freeze cohort and split rules, audit leakage and follow-up, compute feasible metrics, and assemble the report. Prefer supplied predictions over expensive retraining. If access, runtime, or essential columns prevent analysis, return a protocol with missing inputs and unexecuted checks explicitly listed; never substitute fabricated results. A valid measured output includes reproducible configuration, supported denominators, uncertainty, and limitations. A protocol-only output must not claim that empirical validation succeeded.

## Inputs / Outputs

**Inputs**

- Authorized longitudinal EHR extracts or precomputed predictions with pseudonymous patient identifiers, site identifiers, index times, event times and indicators, observation endpoints, and competing-event information where available.
- Disease definitions, lookback and exclusion rules, timestamp semantics, code mappings, and data provenance.
- Model version, training-system inventory, prediction semantics, horizon definitions, and development/calibration/test split assignments.
- Intended screening population, operational alert constraints, subgroup definitions, and available compute. No TRACER checkpoint is assumed to exist or be accessible.

**Outputs**

- An evaluation report or explicitly labeled protocol containing cohort flow, temporal definitions, split provenance, leakage findings, censoring assumptions, and unresolved inputs.
- A results table keyed by model, site, disease, horizon, subgroup, and threshold policy, with eligible counts, events, censoring and competing-event counts, incidence, discrimination, calibration, detection, alert burden, and confidence intervals. Mark nonestimable values and explain why.
- Threshold provenance and achieved operating points, distinguishing locked external evaluation from test-selected descriptions and separately evaluated local adaptation.
- Reproducibility details: dataset and phenotype versions, model identifier, configuration, software versions, random seeds, and estimator definitions; no patient-level identifiers in shared reports.
- A source-evidence ledger labeling claims as reported in the abstract, verified in full text, proposed practice, or unknown. Retrospective performance alone does not establish clinical utility, safe deployment, or improved patient outcomes.

## References

- [TRACER, a time-to-event EHR foundation model for disease detection across health systems, arXiv:2610.40536v1](http://arxiv.org/abs/2610.40536v1), submitted 2026-10-29. Source for the reported populations, horizons, operating point, and external-evaluation findings; additional workflow recommendations above are not asserted to be methods reported by this paper.
