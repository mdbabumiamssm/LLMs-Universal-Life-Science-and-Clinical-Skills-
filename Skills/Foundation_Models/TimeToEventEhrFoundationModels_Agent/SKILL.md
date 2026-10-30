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
name: 'time-to-event-ehr-foundation-models'
description: 'Prepare longitudinal EHR cohorts and evaluate time-to-event foundation models for disease screening across health systems, with censoring-aware metrics, calibration, and leakage controls informed by TRACER.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Time-to-Event EHR Foundation Models

## Overview

This research skill prepares temporal EHR records and evaluates incident-diagnosis predictions across health systems, informed by TRACER. It emphasizes censoring, calibration, and screening alert burden because overall discrimination alone does not establish useful screening performance. Its implementation requirements are distinct from verified paper methods and do not establish clinical readiness.

## When to Use This Skill

- Construct landmark-based incident-disease cohorts from longitudinal structured EHRs.
- Evaluate foundation-model representations paired with time-to-event prediction heads.
- Compare detection, calibration, and false alerts across development and external systems.
- Audit temporal leakage, incomplete follow-up, or optimistic screening thresholds.
- Assess whether available TRACER artifacts support reproduction or only a generic research implementation.

## Core Capabilities

1. **Verify evidence and execution prerequisites.** Read the versioned source and record method locations, artifact URLs, licenses, and unresolved details before prescribing model-specific commands.

   Verified source notes: TRACER uses a decoder backbone with frozen representations and endpoint-specific DeepHit heads. UC1–UC4 supported development; UC5–UC6 were external. Endpoints use SNOMED CT sets and first recorded qualifying visits. One prediction visit is sampled per patient and endpoint, strictly more than one year after record start and before event or censoring; its contents are excluded. Noncases are censored at their last visit. Chronic-disease horizons are 52, 104, and 260 weeks; cancers add 26 weeks. Thresholds were cohort-specific retrospective estimates. These details come from Methods 2.1–2.6; they are not a prospective deployment protocol.

   No model checkpoint or official implementation release link was identified in the reviewed v1 text; availability remains unverified. Individual-level study data are restricted. Require a verified checkpoint, tokenizer, preprocessing specification, and compatible prediction head before claiming TRACER inference. Otherwise use supplied predictions or explicitly label a generic implementation; never invent package names, download commands, weights, or endpoint concept lists.

2. **Define the cohort and estimand.** Specify the population, endpoint concept-set version, incident-case exclusion, lookback, index-visit rule, prediction cutoff, follow-up end, and horizon units before constructing labels.

   Distinguish first documented diagnosis from biological disease onset. For source reproduction, implement the verified visit-sampling rule and document exclusions when no eligible visit exists. For a prospective-use simulation, choose landmarks from information available at prediction time and label that design as an adaptation. Preserve natural incidence for screening evaluation; case-control samples require justified population weighting before estimating PPV or workload.

3. **Prepare temporal records without leakage.** Require pseudonymous patient and system identifiers, encounter identifiers, event time, information-availability time where obtainable, vocabulary, concept, and relevant values/units. Harmonize codes and units; audit duplicates, missing dates, timestamp ties, and unmapped concepts.

   Admit features only if available before the declared cutoff. Exclude the landmark visit when reproducing the source protocol, including associated results recorded later. Do not infer safety from causal attention alone: post-index events, retrospectively updated diagnoses, or outcome-derived preprocessing can still leak labels. Fit learned mappings, quantile bins, imputation, and normalization on permitted development data only; freeze them for evaluation. Document sequence truncation, visit grouping, time-gap encoding, padding masks, and pooling rather than guessing checkpoint behavior.

4. **Represent censoring and competing events explicitly.** Store one row per patient, endpoint, and landmark with observed duration, event indicator, censoring reason, and any competing-event indicator. Define observation end from documented coverage, last observation, and administrative cutoff as appropriate to the study; record assumptions about care outside the system.

   Compute duration from landmark to the earliest relevant event or observation end. A patient censored before a horizon is not a known negative. Specify handling of events exactly on a boundary and censoring within discrete bins; retain residual survival probability beyond the final bin. Decide whether death is a competing event or part of a justified censoring estimand, and use compatible cumulative-incidence estimators. Do not treat independent censoring as automatically satisfied.

5. **Separate development and external validation.** Partition by patient before fitting transformations or heads; prevent cross-system duplicates from crossing partitions where linkage permits. Record exposure to pretraining, head training, tuning, calibration, and threshold selection separately for each system.

   Keep external systems out of every development stage for an untouched external evaluation. If local recalibration or head training is performed, reserve separate local evaluation patients and report it as adaptation alongside the unchanged transfer result. Record calendar periods, coding coverage, follow-up distributions, and missingness to characterize transportability.

6. **Validate survival predictions and calibration.** Accept cumulative horizon risks or a documented survival distribution. For discrete probability-mass outputs, cumulative risk is the sum of event masses through the horizon; for conditional hazards, use one minus the product of interval survival probabilities. Do not confuse these parameterizations.

   Check finite probabilities in [0, 1], nondecreasing cumulative risk, consistent units and bin boundaries, and alignment with patient labels. Estimate horizon-specific calibration curves and censoring-adjusted Brier scores, plus integrated scores only over supported follow-up. Use survival-aware observed incidence within calibration groups, switching to competing-risk estimators when required. Fit any recalibration using designated calibration data, preserve horizon coherence, and freeze it before test evaluation. These calibration checks are workflow requirements, not claims that the paper established calibrated deployment risks.

7. **Measure screening performance and alert burden.** Report cumulative/dynamic AUROC, a declared survival concordance estimator, and partial AUROC over a prespecified low-FPR range. Identify raw versus standardized partial area. Add sensitivity, achieved specificity, PPV, horizon incidence, enrichment, case yield, and false-alert estimates by endpoint, horizon, and system.

   Choose operating thresholds on development validation data, save the values and tie rule, then apply unchanged to external cohorts. Treat retrospective cohort-specific thresholds as a separate matched-specificity analysis; they do not demonstrate threshold transport. A 95% specificity target is a source-motivated comparison point, not a universal clinical requirement.

   Use consistent censoring-aware case/control definitions and weights for horizon metrics. State where the censoring distribution is estimated, assumptions behind inverse probability of censoring weighting (IPCW), weight truncation, and follow-up support; mark estimates unavailable when support is inadequate. Do not silently drop early censoring and report ordinary classification accuracy.

   With N scored patients and weighted true/false positives TPw and FPw, report estimated detected cases as 10,000 × TPw/N and false alerts as 10,000 × FPw/N. Report actual selected patients separately as count(risk ≥ threshold)/N, including patients with incomplete follow-up. PPV uses TPw/(TPw + FPw); enrichment divides PPV by compatible horizon incidence. Label weighted quantities as estimates, retain denominator definitions, and return undefined values when denominators vanish. Do not interpret specificity as the proportion of all patients spared alerts or enrichment as absolute diagnostic certainty.

8. **Quantify uncertainty and finish with an auditable result.** Use patient-level resampling, retaining all repeated landmarks together if present; pair resamples for model comparisons. Report confidence intervals, case counts, censoring counts, and sparse-subgroup limitations rather than ranking unstable estimates. Keep validation-selected thresholds fixed when estimating uncertainty for the frozen deployment rule; disclose threshold reselection in retrospective analyses.

   For a 15-minute execution, prioritize source/artifact checks, a cohort and leakage audit, and evaluation of existing predictions on a bounded sample. Full pretraining, multi-million-patient inference, and clinical validation are outside that time target. Return a valid feasibility report with explicit blockers when data or artifacts are missing; do not fabricate results or describe incomplete evaluation as successful model validation.

## Inputs / Outputs

**Inputs**

- Authorized, de-identified longitudinal EHR tables or a documented cohort with precomputed horizon risks; retain patient-level records within the approved environment.
- Endpoint concept sets and versions, index and eligibility rules, follow-up and death information, and requested horizons.
- Patient/system split manifest, model artifact provenance, preprocessing configuration, and prediction-output semantics.
- Intended screening operating points, calibration partition, and available compute/time budget.

**Outputs**

- Evidence and artifact manifest distinguishing verified source facts, implementation choices, unavailable assets, and deviations from reproduction.
- Cohort audit with counts by exclusion reason, system, endpoint, split, and horizon; leakage checks and censoring/competing-event assumptions.
- Prediction schema: `patient_id`, `system_id`, `endpoint`, `landmark`, `duration`, `event`, `horizon`, `risk`, `split`, and model/configuration identifier.
- Evaluation table with population size, observed events, follow-up support, threshold origin/value, achieved specificity, sensitivity, PPV, incidence, enrichment, actual selection rate, estimated case/false-alert yield, discrimination, calibration, and uncertainty.
- Reproducibility record covering seeds, package/artifact versions, preprocessing state, runtime, missing estimates, and remaining validation work. Share aggregate results without exporting identifiable records.

**Completion checks:** Temporal cutoffs and patient separation pass; early censoring is not labeled negative; probability semantics and units are validated; external threshold/calibration provenance is explicit; every metric has a denominator and support assessment. A blocked run must identify missing inputs and distinguish completed checks from unexecuted steps.

## References

- [TRACER, a time-to-event EHR foundation model for disease detection across health systems — arXiv:2610.40536v1](http://arxiv.org/abs/2610.40536v1). Source finding and versioned research context.
- [TRACER full text, Methods 2.1–2.7 and Supplementary Methods S4](https://arxiv.org/html/2610.40536v1). Cohort construction, survival modeling, evaluation, and availability statements; reviewed 2026-10-30.
