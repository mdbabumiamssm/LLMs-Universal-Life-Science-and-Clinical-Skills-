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
name: 'synthetic-cancer-multiomics-evaluation'
description: 'Evaluate synthetic paired cancer RNA-expression and CNV cohorts for biological fidelity, cross-modality coherence, patient-disjoint validity, and training-data proximity.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Synthetic Cancer Multi-Omics Evaluation

## Overview

Evaluate synthetic paired RNA-expression and copy-number variation (CNV) cohorts using the supplied study's biology-informed framework, beginning with longitudinal high-grade serous ovarian cancer. Assess modality fidelity and paired coherence against real training–held-out agreement, alongside training-data proximity; synthetic cohorts are complementary resources, not automatically valid replacements for observed patients.

## When to Use This Skill

- Compare generators producing matched RNA and CNV profiles.
- Audit patient partitioning in cohorts with repeated biopsies or treatment phases.
- Investigate biologically implausible synthetic pairs despite plausible marginal distributions.
- Prepare an evaluation report that distinguishes fidelity, proximity, and evidential limits.

## Core Capabilities

1. **Establish a reproducible evaluation contract.** Inspect matrix dimensions, sample identifiers, gene identifiers, units, missingness, and generator provenance. Require explicit sample-to-patient mapping and verify one-to-one RNA–CNV pairing. Record whether inputs are raw, transformed, or reconstructed; never infer compatible CNV units from similar numerical ranges. Stop affected analyses when identifiers or measurement scales cannot be reconciled.

2. **Audit leakage before scoring.** Assign every longitudinal sample from a patient to one partition, including samples with different site labels or treatment phases. Check patient intersections, duplicate sample identifiers, and repeated profiles across partitions. Fit transformations and feature selection without held-out access; for new tuning runs, repeat these operations inside each inner training split. If a supplied generator used evaluation patients during fitting or selection, label its evaluation contaminated and require a clean refit before generalization claims.

3. **Apply the study-specific metric map.** The following compact specification comes from [Section 3 and Appendix C](https://arxiv.org/html/2611.08394v1#S3); consult their complete definitions before implementation.

   - Design: three patient-disjoint outer folds; patient-grouped inner tuning; treatment cohorts evaluated separately.
   - CNV: amplification/deletion G-scores average thresholded, capped amplitudes; threshold 0.7, cap 2.5 on adjusted log2 ratios. Compare Pearson correlation, absolute errors, and top-50 overlap.
   - RNA: mean Wasserstein-1 and Jensen–Shannon distances, gene-mean correlation, median variance ratio, PCA-space RBF MMD², and discriminator score `2*abs(AUC-0.5)`.
   - Co-expression: Fisher-transformed correlation agreement, edge F1, Leiden-module adjusted Rand index, and top-50 hub Jaccard. Edges require Pearson `r >= 0.70` and BH-adjusted `p < 0.05`; match cohort sizes.
   - Cis coherence: regress RNA on CNV per shared gene; compare slopes by absolute differences, Pearson/Spearman correlation, and sign agreement.
   - Proximity: median synthetic-to-training / synthetic-to-held-out nearest-neighbor distance ratio, plus membership AUC, in RNA, CNV, and paired spaces. Equalize reference sizes and use Appendix C.3 scaling.

4. **Make metric execution reviewable.** Build a configuration recording the source equation or section, feature panel, scaling, estimator, random seed, comparison cohorts, and missing-value policy for each metric. Resolve histogram bins, kernel settings, and classifier folds from the full study or verified implementation; explicitly label unspecified choices as adaptations. Preserve paired row order throughout. Report undefined correlations, zero-variance denominators, and empty networks as unavailable with reasons rather than replacing them with favorable scores.

5. **Interpret biology and dependence.** Inspect feature-level errors as well as aggregate values; annotate biomarkers selected before evaluation and retain their identifiers in the report. Do not treat cis agreement within selected genes as proof of genome-wide regulation, causality, treatment response, or longitudinal trajectory preservation. Keep model comparisons paired by split and retain seed-level results so variability is visible. Avoid an invented universal passing threshold or an unvalidated composite ranking.

6. **Deliver a bounded, honest evaluation.** For the 15-minute workflow, use supplied synthetic cohorts and prepared evaluation inputs; model fitting and exhaustive network analysis require a separately scoped run. First validate inputs and splits, then execute feasible configured metrics, and finish with a report marking each analysis complete, blocked, or deferred. A partial run must not be labeled a completed benchmark. Strong fidelity does not establish privacy; proximity diagnostics alone neither prove copying nor authorize unrestricted data release.

## Inputs / Outputs

**Inputs**

- Real training and held-out RNA/CNV matrices, synthetic paired matrices, and feature annotations.
- Patient/sample map with longitudinal time or treatment phase, sampling site, and split assignments.
- Preprocessing and feature-selection provenance, generation settings, seeds, and fitted-model training membership.
- Full study text, metric configuration, available software, runtime budget, and requested output location.

**Outputs**

- Input and leakage audit with patient/sample counts, alignment checks, exclusions, and blocking issues.
- Metric table containing `model`, `phase`, `fold`, `seed`, `metric`, `comparison`, `value`, `n_samples`, `n_patients`, `n_features`, and `status`.
- Real training–held-out reference values beside synthetic comparisons; optional plots of feature errors, slopes, and proximity distributions.
- Reproducibility manifest recording versions, transformations, seeds, source sections, and adaptations.
- Brief interpretation identifying supported findings, unresolved diagnostics, and limits of cohort transfer or downstream use.

An acceptable result has traceable inputs, explicit split validity, interpretable metric status, and no fabricated values. Missing patient identifiers permit a schema audit but prevent verification of patient-disjoint evaluation.

## References

- [Synthesis of Ovarian Cancer Multi-Omics Datasets: A Biology-Informed Evaluation Framework, arXiv:2611.08394v1](http://arxiv.org/abs/2611.08394v1) — source finding; [full study](https://arxiv.org/html/2611.08394v1), especially Section 3 and Appendix C for implementation details.
