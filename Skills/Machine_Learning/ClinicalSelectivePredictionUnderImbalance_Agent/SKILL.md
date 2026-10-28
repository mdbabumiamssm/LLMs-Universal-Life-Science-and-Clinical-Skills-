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
name: 'clinical-selective-prediction-under-imbalance'
description: 'Evaluate clinical deferral under class imbalance using class-conditional risk, coverage, minority errors, calibration, and paper-supported threshold-aware policy comparisons.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Clinical Selective Prediction Under Class Imbalance

## Overview

Evaluate whether uncertainty-based deferral improves retrospective predictive performance while retaining useful automation for both outcome classes. Global performance can conceal minority exclusion; this skill pairs explicit denominators and calibration diagnostics with controlled policy comparisons. Outputs support research evaluation, not clinical deployment authorization or evidence of improved patient outcomes.

## When to Use This Skill

- Auditing binary clinical prognosis models with rare outcomes and human-review deferral.
- Investigating improved aggregate accuracy alongside declining minority retention or sensitivity.
- Comparing entropy, decision-margin, and class-conditioned rejection policies at a fixed review budget.
- Assessing whether recalibration, threshold changes, or site differences alter deferral behavior.
- Preparing a retrospective evaluation for subsequent external and prospective validation.

## Core Capabilities

1. **Establish an auditable evaluation contract.** Identify the outcome, prediction time, outcome horizon, positive label, minority label, and intended review capacity. Require held-out or out-of-fold probabilities with patient identifiers and split provenance. Check label completeness, repeated records, probability bounds, and class counts. Keep training, calibration, policy selection, and final evaluation separate; never select thresholds using final-test outcomes. Define a fixed decision threshold `tau` in `(0,1)` from the intended decision context rather than automatically equating it with prevalence.

2. **Implement only verified paper corrections.** The following compact specification follows Sections 2.3 and 2.5 of the [complete paper](https://arxiv.org/html/2610.37561v1):

   Define `H(q) = -q log2(q) - (1-q) log2(1-q)`, with `0 log2(0) = 0`.
   Set `q = p/(2*tau)` for `p <= tau`, otherwise `q = 0.5 + (p-tau)/(2*(1-tau))`; use `H_tau(p)=H(q)`.
   CCR partitions by predicted label `p >= tau`, then rejects the highest-scoring `floor(r*n_j)` cases per partition.
   Compare global entropy, global margin (smallest first), global `H_tau`, entropy+CCR, `H_tau`+CCR, and random+CCR.
   Margin+CCR and `H_tau`+CCR have equivalent within-queue rankings.
   At `tau=0.5`, `H_tau=H`; the supplied summary's contrary threshold statement is erroneous.
   CCR preserves predicted proportions approximately, not true-class coverage, and cannot repair confident errors or provide distribution-free risk guarantees.
   For paper-style ccAUGRC, integrate `E_k/N_k` against true-class coverage using trapezoids; also compare common coverage support.

3. **Make policy comparisons reproducible.** Add a no-deferral reference and hold model probabilities and decision thresholds constant across policies. Predeclare the rejection grid, tie ordering independent of outcomes, random seed, and minimum reportable class counts. Report actual retained and deferred counts: rounding can make nominally equal budgets differ. Compare operational points at matched achieved workload where possible, explicitly marking unmatched points. Labels may score outcomes but must never determine rejection queues. Distinguish retrospective batch ranking from a prospective policy with fixed thresholds or a specified queue window.

4. **Measure class-conditional risk and coverage.** For each policy and operating point, let `a_i=1` denote retention, `yhat_i=1[p_i>=tau]`, and `e_i=1[yhat_i!=y_i]`. For each true class `k`, calculate:

   | Quantity | Definition | Interpretation |
   | --- | --- | --- |
   | Original count | `N_k = sum 1[y_i=k]` | Evaluation denominator before selection |
   | Retained count | `A_k = sum a_i*1[y_i=k]` | Automated cases in that true class |
   | Retained errors | `E_k = sum a_i*e_i*1[y_i=k]` | Residual automated errors |
   | Coverage | `C_k = A_k/N_k` | Fraction of that class automated |
   | Selective risk | `R_k = E_k/A_k` | Error frequency among retained cases |
   | Generalized risk | `G_k = E_k/N_k` | Automated errors per original class member |

   Report global counterparts and predicted-class retention separately. Verify `G_k=C_k*R_k` when denominators exist. Mark zero-denominator metrics undefined, never zero or perfect. Plot both class risk curves and coverage trajectories; a low generalized risk may simply reflect near-total deferral. Report integration bounds and avoid comparing areas over different supports without an explicit qualification.

5. **Expose minority errors and review burden.** Report retained and deferred confusion matrices using the original model predictions. For positive-class outcomes, give retained sensitivity `TP_A/(TP_A+FN_A)`, retained specificity `TN_A/(TN_A+FP_A)`, and retained precision. Separately report automated true-positive yield `TP_A/N_1`, automated false-negative burden `FN_A/N_1`, and positive-class coverage. If class 0 is the minority, provide the corresponding class-0 quantities instead of assuming minority means positive. Include deferred true positives, false negatives, false positives, and true negatives to distinguish useful error capture from exclusion of correct predictions. Deferred outcomes are not automatically corrected outcomes.

6. **Audit calibration independently of ranking.** On held-out data, report Brier score, log loss, and reliability diagrams with bin counts and observed event rates, including the region around `tau`. Examine calibration by site and available clinical subgroups where sample sizes permit. Report Brier and log-loss contributions separately by true class, but do not call conditioning on the realized outcome a conventional reliability analysis. If comparing calibrated and uncalibrated models, fit recalibration only on development data and rerun identical policy evaluations. Assess retained-set calibration separately; good aggregate calibration does not establish safe rejection ordering. The transformed `q` in capability 2 is a ranking construction, not a newly calibrated event probability.

7. **Quantify uncertainty and stress-test conclusions.** Use paired patient-level resampling across policies, preserving patient clusters for repeated observations. State interval method, resample count, seed, and failed or undefined replicates. Resampling fixed predictions estimates sampling variation conditional on the fitted model; training variability needs repeated fitting or an appropriately nested design. Evaluate plausible threshold changes and available temporal or external-site partitions without tuning on their outcomes. Label prevalence reweighting or subsampling as a sensitivity analysis, not independent external validation. Report effect sizes and uncertainty for both classes; small disparity alone is insufficient when both risks are high.

8. **Deliver a bounded retrospective conclusion.** Compare policies against prespecified research acceptance criteria for minority risk, both class coverages, and review capacity. If no policy meets them, report that result rather than choosing one from the global score alone. Separate evidence from the current dataset, hypotheses about failure mechanisms, and untested clinical claims. Clinical validation additionally requires prospective workflow evaluation, review delays and clinician performance, patient outcomes, population transportability, and monitoring of changing prevalence and calibration. Treat unavailable human-review outcomes as a limit on estimating overall system benefit.

## Inputs / Outputs

**Required inputs**

- Patient-level evaluation table containing `patient_id`, binary `y`, predicted event probability `p`, and split provenance.
- Outcome definition and horizon; minority-class identity; decision threshold and its justification.
- Review-budget grid, policy-selection protocol, and any prespecified research acceptance criteria.

**Optional inputs**

- Separate calibration data; uncalibrated probabilities; ensemble member predictions.
- Site, time, subgroup, and cluster identifiers; human-review decisions and delay measurements.

**Outputs**

- Input audit and reproducibility record, including exclusions, thresholds, seeds, tie rules, calibration provenance, and paper version.
- Policy-by-budget table with actual workload, class counts, coverage, selective and generalized risks, confusion counts, minority error measures, and uncertainty intervals.
- Class risk-coverage curves, calibration diagnostics, and integrated-risk summaries with explicit integration domains.
- A short retrospective findings report describing trade-offs, unsupported claims, missing evidence, and the clinical-validation work still needed.

**Execution and completion criteria**

Use the 15-minute target for evaluation of already available predictions, not model retraining or clinical validation. Allocate approximately 3 minutes to input checks and specification, 7 to policy and metric computation, and 5 to validation and reporting; adapt to dataset size. If essential inputs are absent or computation exceeds the budget, return an explicit incomplete evaluation with missing inputs or pending analyses, without fabricating results.

Before declaring completion, verify patient conservation between retained and deferred sets, no outcome leakage into routing, valid class denominators, deterministic ties, and agreement between raw counts and reported metrics. Verify the threshold-aware score peaks at `tau`, matches ordinary entropy when `tau=0.5`, and agrees with margin+CCR selections under identical tie handling. A valid completed output includes both classes and the no-deferral reference, with retrospective limitations stated.

## References

- [When uncertainty quantification fails: structural vulnerabilities and corrections for selective prediction under clinical class imbalance](http://arxiv.org/abs/2610.37561v1), arXiv:2610.37561v1; source finding, posted October 27, 2026. [Complete paper](https://arxiv.org/html/2610.37561v1), especially Sections 2.3, 2.5, 4, and Appendix 10. Paper-specific corrections are identified in capability 2; the remaining workflow supplies general evaluation safeguards rather than additional claimed paper methods.
