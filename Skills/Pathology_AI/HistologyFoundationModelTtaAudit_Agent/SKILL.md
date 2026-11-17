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
name: 'histology-foundation-model-tta-audit'
description: 'Audit whether eight-view geometric TTA improves histology foundation model inference using patient-separated comparisons of prediction quality, uncertainty, and cost at patch and slide levels.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Histology Foundation Model Test-Time Augmentation Audit

## Overview

Evaluate whether identity-only inference, full eight-view D4 test-time augmentation (TTA), or entropy-routed TTA best meets a histology model's quality and compute requirements. The motivating finding reports model-dependent patch benefits and a lack of transfer to slide-level multiple instance learning (MIL), so audit each deployment setting empirically rather than assuming augmentation is always useful or unnecessary. Separate predictive uncertainty, statistical uncertainty, and inference cost in the resulting recommendation.

## When to Use This Skill

- Choosing an inference policy for a histology foundation model or comparing it with a general-purpose backbone.
- Checking whether rotation and reflection sensitivity remains after self-supervised pretraining or task adaptation.
- Reducing TTA compute through uncertainty routing without unacceptable predictive loss.
- Determining whether patch-level improvements survive a specific slide-level MIL pipeline.
- Reassessing an inference policy after a model, tissue, scanner, cohort, or preprocessing change.

## Core Capabilities

1. **Define a bounded, reproducible audit.** Record model and checkpoint identifiers, classifier or MIL head, software versions, device, precision, magnification, patch size, stain processing, and dataset provenance. Freeze the trained weights and inference preprocessing across policies. Predeclare the primary metric, minimum worthwhile gain, acceptable degradation, and latency or memory budget before examining test outcomes.

   Complete a cached-prediction audit or bounded pilot within 15 minutes. Estimate runtime first; when full inference exceeds this budget, use a prespecified patient subset or existing matched predictions and report coverage. If required data are missing or execution cannot finish, return an incomplete audit with explicit missing evidence and a continuation specification; do not claim a completed benchmark.

2. **Enforce patient-separated evaluation.** Require patient, slide, and patch identifiers and disjoint training, validation, and test patient sets. Keep every slide and patch from one patient in the same split; check duplicates and known overlap with task training data. Record any unknown foundation-model pretraining overlap as a limitation. Select routing thresholds, calibration parameters, and operating thresholds on validation patients only, then lock them for test evaluation. Without patient identifiers, do not label a result patient-separated.

3. **Construct and verify D4 inference.** For a square patch, use the eight group operations `R^k(x)` and `R^k(F(x))`, where `k` is 0, 1, 2, or 3, `R` is a 90-degree rotation, and `F` is one fixed-axis reflection. Apply all operations to the same deterministically prepared patch, without random crops or additional stain augmentation. Inspect an asymmetric example to verify that the implementation covers all eight operations, includes identity once, and preserves image content and channel layout.

   Run models in evaluation mode. For patch classification, use arithmetic averaging of per-view class probabilities as the default and record the aggregation domain; averaging logits or embeddings defines a different policy. Keep class order fixed, verify finite normalized probabilities, and reuse the identity prediction. Do not assume that an orientation-invariant representation makes its downstream classifier invariant.

4. **Compare paired predictive quality and uncertainty.** Evaluate identity, full D4, and routed D4 on exactly the same cases. For classification, report the prespecified primary metric plus appropriate AUROC, AUPRC, balanced accuracy, per-class sensitivity and specificity, negative log-likelihood, Brier score, and calibration summaries. State averaging conventions, class prevalence, calibration-bin definitions, and the handling of classes absent from an evaluation subset.

   Report absolute metric values and paired differences with patient-cluster bootstrap confidence intervals, retaining all slides and patches within each resampled patient. Specify whether the estimand weights patches, slides, or patients equally. Treat views and patches from the same patient as correlated observations, not independent replicates. Inspect prespecified tissue, site, scanner, and class strata when sample sizes permit; mark exploratory comparisons and sparse strata explicitly.

5. **Audit entropy routing without test leakage.** Compute baseline class entropy as `H(p) = -sum_c p_c log(p_c)`, with `0 log(0) = 0`. On validation patients, choose a threshold that trades predictive quality against cost under the declared budget. Route a case when `H(p) > threshold`; retain its baseline probability otherwise. For routed cases, combine the cached identity probability with the seven additional views using the same full-D4 rule.

   Freeze the threshold before test evaluation and report the realized routed fraction, overall quality, and routed versus unrouted subgroup behavior. Do not interpret entropy as a guarantee of error detection. Compare several validation operating points if useful, but do not import the source study's routing fraction as a universal target. Report recovered gain only when the full-D4 gain is positive and sufficiently stable for the ratio to be meaningful.

6. **Measure actual inference cost.** Warm up the model, synchronize accelerator timing, and repeat measurements on matched hardware and batching settings. Report sample counts, batch size, median and tail latency, throughput, peak device memory, and total wall time, stating whether decoding, transforms, transfers, feature extraction, and MIL aggregation are included. Distinguish cold execution from cached replay; cached predictions cannot establish current end-to-end speed.

   With identity reuse and routed fraction `r`, the nominal encoder evaluation count is `1 + 7r` per patch versus 1 for baseline and 8 for full D4. This count is a compute proxy, not a measured speedup: batching, routing, and I/O can change latency substantially. Include routing overhead and do not describe selective augmentation as zero-cost inference.

7. **Evaluate slide-level MIL separately.** Keep tissue masks, patch coordinates, bag membership, patch sampling, and MIL weights fixed across policies. Specify whether TTA averages embeddings per patch before MIL or averages slide probabilities from eight view-specific bags; these are distinct experiments and need separate results. If transforming whole-slide geometry, define how coordinates and positional features transform as well.

   Evaluate slide endpoints using patient-clustered uncertainty estimates. A patch classifier's entropy is not automatically a valid slide-routing signal; define and validate any slide-level routing score on validation patients. Never transfer a patch-level recommendation to MIL without a measured slide-level comparison. If the MIL head is retrained for a different feature distribution, label that as a separate training experiment rather than a pure inference audit.

8. **Issue an evidence-based decision.** Recommend baseline, full D4, routed D4, or further evaluation against the predeclared quality and cost criteria. Distinguish lack of evidence for improvement from evidence that any gain is too small to matter; an interval spanning important benefit and harm warrants an inconclusive decision. Keep patch and slide conclusions separate, explain subgroup failures, and list the evidence needed to resolve uncertainty. This audit supports model evaluation and does not establish clinical validity.

## Inputs / Outputs

**Inputs**

- A trained histology model, preprocessing specification, and classifier or MIL head; optional general-purpose comparators evaluated under matched conditions.
- An authorized labeled cohort with patient, slide, and patch identifiers, split assignments, and relevant site or scanner metadata.
- Raw patches or WSIs with extraction metadata, or matched per-view probability or embedding caches with sufficient provenance to verify aggregation and splits.
- Validation and held-out test partitions; task definition, primary metric, decision margins, compute budget, and available hardware.

**Outputs**

- An audit report stating scope, completion status, patient separation checks, coverage, model configuration, transform definitions, aggregation policy, and limitations.
- A comparison table with one row per model, endpoint level, and policy: patient/slide/patch counts, primary and secondary metrics, paired differences and confidence intervals, calibration measures, routed fraction, latency, throughput, memory, and total runtime. Use `not measured` for missing evidence.
- A routing specification containing entropy definition, validation-selected threshold, selection criterion, and held-out routed fraction.
- A reproducibility record containing split and checkpoint identifiers, seeds, software and device details, timing protocol, and per-case predictions with internal patient/slide/patch keys when permitted.
- Separate patch and slide recommendations tied to the declared acceptance criteria. A pilot or incomplete audit must state what remains untested and must not present its conclusion as a full-cohort result.

**Completion check:** Verify matched case sets, patient-disjoint splits, eight correct D4 operations, normalized outputs, validation-only threshold selection, patient-clustered comparisons, and explicit cost measurement status. If any required check fails, identify it in the report and withhold a definitive policy recommendation.

## References

- [When Do Histology Foundation Models Need Geometric Test-Time Augmentation?](http://arxiv.org/abs/2611.21565v1), arXiv:2611.21565v1, submitted November 16, 2026. Source finding motivating the audit; its reported outcomes are specific to the evaluated settings.
- [Accompanying histology TTA repository](https://github.com/lars-chen/histology-tta). Inspect and pin a commit before using implementation details; the audit procedures above are recommendations, not a claim of exact experimental replication.
