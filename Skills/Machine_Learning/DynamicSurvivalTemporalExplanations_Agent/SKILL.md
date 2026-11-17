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
name: 'dynamic-survival-temporal-explanations'
description: 'Explain dynamic survival predictions with static and longitudinal covariates using hierarchical Shapley screening and temporal refinement, with checks for temporal availability, stability, and computational cost.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Time-Resolved Explanations for Dynamic Survival Models

## Overview

DynSurvX explains dynamic survival predictions through Shapley-based feature screening followed by adaptive temporal refinement. This skill turns that approach into a reproducible analysis with explicit prediction targets, input-availability checks, and explanation diagnostics. Attributions describe a model's predictions, not causal effects or treatment benefits.

## When to Use This Skill

- Explain a fitted survival model that consumes both static variables and longitudinal histories.
- Identify which historical measurement intervals influence an individual prediction.
- Compare explanations as new observations become available at successive prediction landmarks.
- Evaluate whether temporal resolution improves explanations enough to justify its computational cost.
- Audit attribution stability before presenting model explanations to biomedical collaborators.

## Core Capabilities

1. **Verify method and software before execution.** Read the paper's Sections 3–4 and Appendices A and D.4, then inspect the linked repository. The full paper was accessible during authoring; it identifies `TeamHeKA/survinsights` as public code, but repository retrieval failed, so installation, interfaces, and reproducibility remain unverified. Before supplying executable examples, verify the revision, license, dependencies, masking implementation, threshold selection, and a documented minimal invocation. Do not invent package names or API calls. If verification fails, return a method specification and explicit execution blockers.

2. **Define the prediction contract.** Record the event, time origin, units, landmark `tP`, and horizon `tH > tP`, stating whether the horizon is an absolute time or `tP + duration`. Select one scalar output: conditional survival probability, event risk, or restricted remaining survival time. Record conditioning on survival to the landmark and the output's direction and units. A positive attribution to survival probability has a different interpretation from a positive attribution to event risk. Define competing-event handling if applicable; do not silently substitute a single-event target. If using a median, report it as undefined when the modeled curve never reaches the required probability.

3. **Enforce temporal availability.** Build each patient history using only values available by `tP`, checking both measurement time and result-release time where available. Treat static variables as eligible only if they were known then. Exclude later outcomes and post-landmark measurements from predictor inputs; retain outcome labels separately for evaluation. Split data by patient before fitting preprocessing. Do not backfill, interpolate, or normalize using future patient observations. Document irregular sampling, missingness indicators, padding, sequence masks, and how censored patients enter the eligible landmark cohort.

4. **Specify the attribution game.** Define players, background population, coalition evaluation, and output scale before estimating Shapley values. State whether absent features are handled through conditional sampling or marginal replacement; these choices need not yield identical explanations for correlated trajectories. Use background histories with compatible landmark availability and preprocessing. Check that perturbed histories satisfy the prediction adapter's timestamp and mask requirements. Record the empty-coalition baseline and full-input prediction. Distinguish the paper's mathematical game from any approximation implemented in software.

5. **Apply the two-phase hierarchy.** Phase 1 uses KernelSHAP with each static variable and whole longitudinal trajectory as a player. Normalize absolute feature attributions over all features; retain longitudinal features above an elbow-selected `delta1`. Phase 2 starts each selected trajectory as one window, estimates WindowSHAP contributions, and normalizes absolute values within that trajectory. Split qualifying windows at observation-index midpoints; update `delta2 = min(xi, 1 / window_count)`. Stop when boundaries no longer change or the split limit is reached. These method details follow [the paper, including Algorithm A.1](https://arxiv.org/html/2611.21571v1).

   Implementation checks: preserve signed values separately from normalized importance. Handle zero normalization denominators explicitly as no resolved importance. Require a new interior boundary for a split and settle endpoint ownership so observations are not accidentally duplicated. Return attributions for the final reported partition, recomputing after a final split if needed. Retain static and unselected feature results; label unselected temporal effects as unrefined rather than zero. Do not assume independently normalized window scores are additive across features or that they reconstruct a parent attribution.

6. **Update and compare explanations.** Rebuild the eligible input at each landmark and rerun the verified procedure. Keep model revision, output definition, and background policy fixed for controlled comparisons. Separate changes due to newly observed data from changes due to horizon choice, reference cohort, or model updates. Display observation time and landmark distinctly; do not confuse when a feature was measured with when the survival outcome is predicted. Aggregate across patients only with a documented eligible cohort and compatible time alignment.

7. **Assess stability and cost.** Repeat a bounded pilot across random seeds and background samples; compare signed attribution variation, feature-rank agreement, and interval patterns on a common grid. Vary screening and refinement thresholds and the split budget. Include an unscreened or less aggressively screened subset to detect localized effects missed by screening. Check reconstruction residuals only for compatible games and scales, never by summing normalized scores. Report held-out discrimination, calibration, and censoring-aware prediction error separately from explanation fidelity; flag unavailable model validation.

   Measure wall time, model calls, coalition samples, and resolved windows. If comparing with a temporal baseline, match patients, targets, model, hardware, background policy, and evaluation budget, and disclose differences. Report measured savings only for that experiment; published speedups are not performance guarantees. Distinguish between-patient variability from Monte Carlo uncertainty and model uncertainty.

8. **Return an auditable bounded result.** Within the 15-minute workflow budget, prioritize source/software verification, the prediction contract, leakage checks, and a small pilot when execution is possible. Set patient, coalition, and refinement limits before running. If the budget expires or required artifacts are missing, return a clearly marked partial or blocked report with completed checks and remaining work; do not label an unexecuted specification as a successful explanation run. This time target does not guarantee completion of a full-cohort analysis.

## Inputs / Outputs

**Required inputs**

- A fitted model with revision identifier and a prediction adapter, plus its preprocessing and feature schema.
- Patient identifiers, static covariates, longitudinal values, timestamps, availability information, and missingness masks.
- Event definition, landmark eligibility rules, prediction landmarks, horizons, and scalar output definition.
- A reference/background cohort and an explicit coalition replacement or sampling policy.
- Execution limits, random seeds, feature-screening configuration, refinement controls, and available validation data.

**Produced outputs**

- A verification record identifying paper version, repository/revision status, supported invocation, and unresolved implementation details.
- A prediction contract and temporal-availability audit, including exclusions and preprocessing assumptions.
- Feature attribution rows containing patient, landmark, horizon, target, feature, signed attribution, normalized importance, and refinement status.
- Temporal attribution rows containing patient, feature, window boundaries, observation count, signed contribution, within-feature normalized importance, and stopping reason.
- A diagnostic report containing baseline/output values, applicable reconstruction checks, stability comparisons, runtime, model calls, budget limits, and missing checks.
- An interpretation separating model reliance from causal claims, alongside model-performance limitations and any unsupported conclusions.

**Completion criteria:** A successful pilot has verified software execution, valid landmark inputs, a declared attribution game, finite outputs or explicit degenerate-case statuses, traceable window definitions, and measured diagnostics. A specification-only deliverable must explicitly state that no attributions were computed. Do not fabricate results when inputs, software, or compute are unavailable.

## References

- Nguyen, Van Tuan, and Agathe Guilloux. [DynSurvX: Time-Resolved Explanations for Dynamic Survival Predictions](http://arxiv.org/abs/2611.21571v1), arXiv:2611.21571v1. Source finding; [full text and algorithm appendices](https://arxiv.org/html/2611.21571v1).
- [TeamHeKA/survinsights](https://github.com/TeamHeKA/survinsights). Software location linked by the paper; repository contents and executable interfaces were not independently verified during authoring.
