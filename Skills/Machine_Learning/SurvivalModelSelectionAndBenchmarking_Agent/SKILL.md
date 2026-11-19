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
name: 'survival-model-selection-and-benchmarking'
description: 'Select and benchmark survival models across discrimination, prediction error, event-time accuracy, and dataset regimes while treating the model-selection objective as an experimental variable.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Survival Model Selection and Benchmarking

## Overview

Build a reproducible survival-evaluation protocol that separates hyperparameter selection from final evaluation and compares classical, tree-based, and deep learning methods across dataset regimes. The supplied abstract reports a benchmark of 10 methods on 49 datasets in which selection objectives and dataset characteristics materially affect conclusions. The workflow below is proposed guidance, not a verified reproduction of the full paper.

## When to Use This Skill

- Choose a survival model for risk ranking, survival-probability prediction, or event-time prediction.
- Compare C-index, Integrated Brier Score (IBS), and pseudo-observation Mean Absolute Error (MAE-PO) as selection objectives.
- Audit a benchmark that reports only a global ranking or uses C-index for every tuning decision.
- Compare model families under varying sample size, dimensionality, event counts, or censoring.
- Investigate apparently good calibration in heavily censored data.

## Core Capabilities

1. **Define the prediction task and feasible scope.** Record the endpoint, time origin, time units, event encoding, intended population, prediction horizons, and primary use. Start with right-censored, single-event outcomes; competing risks, delayed entry, recurrent events, and time-varying predictors require explicit compatible estimators and metrics. Within 15 minutes, produce a validated protocol or a small pilot using available data and software; a full benchmark is a separately budgeted run. Label planned, executed, failed, and unavailable analyses distinctly.

2. **Audit outcomes and dataset regimes.** Check invalid times, missing outcomes, duplicate subjects, leakage, and event/censoring coding. Describe sample size, feature count after preprocessing, feature-to-sample ratio, observed events, censoring fraction, follow-up support, and missingness. Define regime bins before inspecting model performance, or use continuous descriptors; do not invent universal thresholds for small samples, high dimensionality, or heavy censoring.

3. **Separate tuning from evaluation.** Use nested cross-validation or a held-out test set with inner training/validation splits. Keep subject, site, and temporal dependencies intact where relevant. Fit imputation, encoding, scaling, feature selection, and learned time discretization only on each training partition. Reuse outer splits and seeds across methods and selection objectives. Never choose hyperparameters, horizons, preprocessing, or the reported winner from test results.

4. **Construct fair model-family comparisons.** Include a simple baseline, such as Kaplan–Meier survival curves and a Cox model, alongside representative survival trees or ensembles and deep survival methods when feasible. These are proposed candidates, not a claim about the paper's exact inventory. Record model versions, search spaces, candidate counts, compute limits, early-stopping rules, and failures. Use comparable declared search budgets while allowing appropriate model-specific preprocessing; document omitted families and resource constraints.

5. **Treat the selection objective as an independent factor.** For every tunable method, select separate configurations by maximizing validation C-index, minimizing validation IBS, and minimizing validation MAE-PO when supported. To isolate selection effects, preferably score the same fitted candidate pool under all three criteria; disclose objective-specific training or search changes. Keep fixed baselines fixed. Predeclare tie-breaking and evaluate each selected configuration on all available test metrics, preserving the distinction between selection metric and evaluation metric.

   | Intended use | Primary selection objective | Required interpretation |
   | --- | --- | --- |
   | Discriminative ranking | C-index, higher is better | Ranking does not establish accurate survival probabilities. |
   | Survival probabilities over time | IBS, lower is better | Report integration interval, grid, weighting, and censoring estimator; assess calibration separately. |
   | Event-time prediction | MAE-PO, lower is better | Verify the pseudo-observation construction and time-prediction rule; report time units and truncation. |

6. **Handle censoring and metric support explicitly.** Specify the C-index variant, risk-score orientation, tie handling, and any time truncation. For inverse-probability-of-censoring-weighted metrics, document the censoring model, its fitting partition, and assumptions about independent censoring conditional on modeled information. Avoid test-data fitting except where the documented evaluation estimator explicitly requires it; never feed evaluation estimates back into selection. Restrict evaluation to adequately supported horizons, inspect unstable weights, and report clipping or truncation choices. Do not treat censored times as event times or substitute uncensored-only MAE for MAE-PO. Verify MAE-PO and X-CAL definitions against source methods and code before computing them; mark unsupported metrics unavailable rather than inventing formulas. Specify how curves yield an event-time estimate and how an undefined median or truncated mean is handled.

7. **Evaluate discrimination, error, and calibration together.** Report C-index, IBS, MAE-PO, and X-CAL where validated implementations and model outputs support them. Risk scores alone do not provide survival probabilities; document any training-fitted conversion. Check that survival curves stay within [0, 1] and are nonincreasing on a consistent time grid. Pair scalar calibration summaries with censoring-aware calibration plots, numbers at risk, and uncertainty at declared horizons. Under heavy censoring, small absolute calibration errors or non-rejected calibration tests may reflect weak information and must not be presented as proof of calibration.

8. **Compare paired results within dataset regimes.** Show per-dataset and per-regime results before any global summary. Compare selection objectives using paired differences on identical outer splits, with uncertainty respecting repeated subjects and resampling dependence. Do not pool raw MAE across incompatible time units or IBS across incompatible integration windows. For sufficiently rich multi-dataset results, optionally fit a documented hierarchical model with dataset effects and method-by-objective or regime interactions; specify likelihoods, priors, diagnostics, and limitations. This is a proposed analysis option, not a reproduction of the paper's Bayesian model. Avoid causal interpretations of observational dataset characteristics and do not declare a universal winner from aggregate ranks.

9. **Keep evidence and recommendations separate.** The supplied abstract reports improved probabilistic accuracy and calibration when flexible models are selected by IBS rather than C-index, with little loss of ranking performance; it also reports benefits of larger samples and difficulties with high dimensionality for deep models. Treat these as abstract-reported findings, not guarantees for a new dataset. Exact effect sizes, method-specific claims, dataset composition, metric formulas, and hierarchical-model specifications require full-paper verification. The linked repository was accessible during authoring, but the arXiv page could not be retrieved; repository descriptions do not replace full-paper verification.

## Inputs / Outputs

**Inputs**

- Dataset or existing benchmark results, outcome schema, feature definitions, subject/group identifiers, and data-access constraints.
- Prediction task, time horizon, censoring information, primary selection objective, and any required external validation setting.
- Candidate methods, available libraries, compute and time budget, seeds, splits, and search configurations when provided.
- Source paper and repository version or commit when attempting reproduction.

**Outputs**

- A protocol recording endpoint assumptions, preprocessing boundaries, splits, candidate methods, selection objectives, metric definitions, censoring treatment, and compute budget.
- A dataset-regime inventory and a result table with one row per dataset, outer split, seed, method, and selection objective. Include selected configuration, evaluation metrics, horizon, runtime, execution status, and reasons for missing values.
- Paired objective comparisons, regime-specific summaries, uncertainty estimates, and calibration diagnostics when executed results support them.
- A task-specific recommendation supported by held-out evidence, or an explicitly provisional recommendation when only a protocol or pilot is feasible.
- A limitations and provenance record separating source-reported findings, locally observed results, proposed guidance, and details awaiting verification.

**Completion criteria:** Within the stated time budget, deliver either a complete protocol with unresolved prerequisites identified or a clearly bounded pilot with valid outputs. Confirm that every reported score has a metric definition and split provenance, missing metrics are explicit, and no test observations influenced model selection. Never label a protocol, partial pilot, or timed-out run as a completed large-scale benchmark.

## References

- [What Survival Benchmarks Don't Tell You: Impact of Model Selection and Dataset Regimes, arXiv:2611.24837v1](http://arxiv.org/abs/2611.24837v1) — supplied source finding; abstract-level evidence unless the full paper is retrieved and checked.
- [Survival benchmark study repository](https://github.com/sdening/surv-bench-study) — accompanying implementation and experiment configuration reference; inspect and pin the relevant revision before reproduction.
