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
name: 'promise-ad-progression-survival-agent'
description: 'Progression-aware multi-horizon survival agent that estimates calibrated 1/2/3/5-year risks of CN→MCI and MCI→AD conversion from irregular ADNI/TADPOLE tabular visit histories.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# PROMISE-AD Multi-Horizon Alzheimer's Progression Agent

## Overview

This skill operationalizes the PROMISE-AD framework — a leakage-safe, progression-aware survival model for individualized Alzheimer's disease (AD) trajectory prediction. It transforms irregular pre-index ADNI/TADPOLE tabular visit histories into temporal tokens, fuses them with a Transformer to produce a progression score and discrete-time mixture hazards, and emits calibrated multi-horizon (1-, 2-, 3-, and 5-year) conversion risks for CN→MCI and MCI→AD transitions. It is designed to support clinical decision-support pipelines, cohort enrichment for trials, and dynamic risk tracking across longitudinal follow-up.

## When to Use This Skill

- Estimating individualized risk of conversion from cognitively normal (CN) to mild cognitive impairment (MCI), or from MCI to AD dementia.
- Generating calibrated multi-horizon (1/2/3/5-year) survival probabilities from longitudinal tabular EHR / registry data with right-censoring.
- Building a leakage-safe progression score that excludes diagnostic labels from feature inputs.
- Analyzing ADNI/TADPOLE-style cohorts with irregular visit timing, missingness, and slope/change features.
- Enriching clinical trial cohorts by stratifying patients by predicted progression hazard.
- Dynamic re-scoring of patients as new visits accrue (track risk drift over time).
- Benchmarking new AD progression models against an interpretable, calibrated survival baseline.

## Core Capabilities

1. **Visit Tokenization** — Convert pre-index visits into structured tokens carrying standardized continuous measurements, missingness masks, longitudinal change deltas, time-normalized slopes, visit timing offsets, and non-diagnostic categorical attributes (e.g., demographics, APOE4 status).
2. **Temporal Transformer Encoder** — Fuse a global representation, attention-pooled summary, and the latest-visit embedding to capture both long-range trajectory and recent change dynamics.
3. **Progression Score Head** — Produce a continuous, monotonically interpretable progression score that ranks patients by underlying disease trajectory.
4. **Discrete-Time Mixture Hazards** — Model latent subpopulations via a mixture over discrete-time hazard functions for flexible, multi-modal risk shapes.
5. **Multi-Objective Training** — Combine survival likelihood, horizon-specific focal risk loss, progression ranking loss, hazard smoothness regularization, and mixture-balance regularization.
6. **Isotonic Calibration** — Apply per-horizon isotonic regression on a held-out validation set to deliver calibrated 1-, 2-, 3-, and 5-year risk probabilities.
7. **Leakage-Safe Feature Construction** — Explicitly exclude diagnostic labels from feature inputs to avoid trivial label-leakage during longitudinal token construction.
8. **Censoring-Aware Evaluation** — Report Integrated Brier Score (IBS), Harrell/Antolini C-index, and time-dependent AUROC/AUPRC across horizons.
9. **Interpretability Hooks** — Surface attention weights over visits and feature ablation summaries (e.g., contribution of cognitive, functional, APOE4, and recency-of-visit features).
10. **Dynamic Tracking Mode** — Re-evaluate predictions as new visits arrive and emit horizon-conditioned trajectories of risk over time.

## Inputs / Outputs

**Inputs**
- Longitudinal tabular cohort (ADNI/TADPOLE-format or equivalent) with per-visit:
  - Standardized cognitive (e.g., MMSE, ADAS-Cog, MoCA), functional (e.g., FAQ), and biomarker fields.
  - Visit timestamps (relative to an index visit) and missingness indicators.
  - Non-diagnostic categorical attributes: age, sex, education, APOE4 status.
- Survival labels: time-to-event (conversion to next stage) and right-censoring indicator.
- Configuration: prediction horizons (default 1, 2, 3, 5 years), task choice (CN→MCI or MCI→AD), random seed(s).

**Outputs**
- Per-patient calibrated risk probabilities at each requested horizon.
- Continuous progression score per patient.
- Cohort-level metrics: IBS, C-index, time-dependent AUROC/AUPRC at each horizon.
- Calibration diagnostics (reliability curves, Brier decomposition) per horizon.
- Interpretability artifacts: visit-level attention, feature-group ablation report.
- Optional dynamic-tracking series: risk trajectories as a function of visit index.

## References

- Source paper: Lyu Q, Hudson J, Kawas M, Jiang Y, You C, Whitlow CT. *PROMISE-AD: Progression-aware Multi-horizon Survival Estimation for Alzheimer's Disease Progression and Dynamic Tracking.* arXiv:2604.28055 (2026). http://arxiv.org/abs/2604.28055v1
- ADNI (Alzheimer's Disease Neuroimaging Initiative): https://adni.loni.usc.edu/
- TADPOLE Challenge (Alzheimer's Disease Prediction of Longitudinal Evolution): https://tadpole.grand-challenge.org/
- Lee C, Zame WR, Yoon J, van der Schaar M. *DeepHit: A Deep Learning Approach to Survival Analysis with Competing Risks.* AAAI 2018. https://ojs.aaai.org/index.php/AAAI/article/view/11842
- Katzman JL, Shaham U, Cloninger A, Bates J, Jiang T, Kluger Y. *DeepSurv: Personalized Treatment Recommender System Using a Cox Proportional Hazards Deep Neural Network.* BMC Med Res Methodol (2018). https://doi.org/10.1186/s12874-018-0482-1
- Graf E, Schmoor C, Sauerbrei W, Schumacher M. *Assessment and comparison of prognostic classification schemes for survival data (Integrated Brier Score).* Statistics in Medicine (1999).
- pycox (discrete-time survival models in PyTorch): https://github.com/havakv/pycox
- scikit-survival: https://github.com/sebp/scikit-survival
