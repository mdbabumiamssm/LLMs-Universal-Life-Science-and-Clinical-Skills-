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
name: 'cell-painting-domain-shift-evaluation'
description: 'Evaluate Cell Painting models under experimental batch and source shifts using BatchBench, with reproducible dataset preparation, published splits and metrics, adaptation comparisons, and leakage audits.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Cell Painting Domain Shift Evaluation

## Overview

BatchBench evaluates compound identification from JUMP Cell Painting images acquired in unseen experimental sources and batches. This skill prepares reproducible evaluations, checks separation between development and evaluation data, and compares adaptation methods without confusing biological signal with acquisition effects.

## When to Use This Skill

- Evaluate a microscopy model on experimental conditions absent from its training data.
- Prepare a BatchBench-compatible evaluation or inspect an existing result for protocol compliance.
- Compare a fixed model with domain adaptation or test-time adaptation methods.
- Investigate performance differences across sources, batches, plates, and compound groups.
- Audit preprocessing, pretrained encoders, and model selection for evaluation leakage.

## Core Capabilities

1. **Resolve and freeze the evaluation protocol.** Read the versioned paper in References and follow its links to official data and implementation artifacts. Record dataset revision, code commit, label mapping, preprocessing, split manifest, metric definitions, and permitted adaptation inputs before running models. If an essential artifact cannot be verified, produce a readiness report naming the missing item; do not invent an official configuration.

   Published v1 anchors: JUMP-CP-2k uses 2,000 compound classes and five-channel images. Source 2 is validation; sources 4, 6, 9, and 13 are private test sources; the other eight public sources are training. Overall image-level accuracy determines ranking, with POSCON, TARGET, and REST accuracies also reported. Use official subset membership rather than reconstructing it from names or assuming groups are disjoint.

2. **Prepare traceable inputs.** Build a manifest containing image identifier, location or checksum, source, batch, plate, well, available field identifier, label availability, and official split assignment. Use composite identifiers where batch or plate names are only locally unique. Check missing files, duplicates, channel order, dimensions, non-finite values, and metadata joins. Follow the released preprocessing implementation; record any deviations and label the resulting evaluation as custom. Preserve original identifiers through cropping, embedding extraction, and prediction export.

3. **Audit leakage before fitting.** Compare manifests across splits using identifiers and content hashes; flag related crops, duplicate images, and repeated wells. Verify source separation and nested batch/plate separation against the official assignments. Repeated compound labels across domains can be intentional in compound classification; distinguish this from reuse of the same observations.

   Fit learned normalization, feature selection, dimensionality reduction, and batch correction only on permitted development data. Treat joint correction across train and evaluation data as adaptation requiring explicit protocol support. Audit negative-control provenance and all encoder pretraining datasets. V1 excludes held-out sources from training, pretraining, and model selection, while permitting adaptation to unlabeled test inputs through the evaluation interface. Unknown checkpoint provenance means eligibility is unverified, not passed. Keep evaluation labels inaccessible to fitting and adaptation.

4. **Compare methods under matched conditions.** Establish a no-adaptation baseline and compare requested methods using the same splits, input representation, labels, training budget, and validation selection rule. Document differences that prevent a controlled comparison. Tune hyperparameters and stopping rules on validation data; freeze them before final evaluation. For adaptive models, log the adaptation unit, available metadata, sample ordering, update budget, random seeds, and reset policy. Prevent state from carrying across independent runs unless the evaluated protocol explicitly requires it. Include a matched adaptation-disabled ablation when feasible.

5. **Evaluate and diagnose domain-specific performance.** Apply the official evaluator and retain prediction-to-image alignment and class ordering. For v1, report overall accuracy and the three published subset accuracies. Add per-source, per-batch, and per-plate results where labels and access allow, clearly marked as supplemental diagnostics. Include sample counts and class support; use an explicit unavailable value for empty groups. State weighting for any supplemental average and avoid substituting it for the official ranking metric.

   Report adaptation deltas against the matched baseline and inspect whether improvements coincide with changes in class composition. If uncertainty estimates are requested, resample independent experimental units rather than treating related images as independent replicates; record the resampling unit and method. Do not infer successful biological preservation solely from reduced domain separability or visually mixed embeddings.

6. **Package reproducible evidence within the available budget.** Save the configuration, split audit, checkpoint provenance, prediction alignment checks, metric table, and limitations in the requested output location. The published interface uses a `Submission` class with `adapt()` and `predict()`; non-adaptive methods use a no-op adaptation step. Verify exact signatures against the current official template before preparing submission code. Preparing artifacts does not authorize publishing a repository or submitting externally.

   For the 15-minute outcome, prioritize protocol resolution, manifest checks, and a bounded evaluator smoke test using cached inputs or existing predictions. Report the scope as `readiness_only`, `smoke_test`, `local_evaluation`, or `official_evaluation`. Full downloads, training, and private server evaluation may take longer; provide remaining steps and mark incomplete metrics as unavailable. A smoke test validates execution and alignment, not benchmark performance. Stop scoring on split violations, exposed evaluation labels, or prediction/label mapping failures, and report the corrective action.

## Inputs / Outputs

**Inputs**

- Task scope: protocol audit, local evaluation, method comparison, or submission preparation.
- Versioned benchmark artifacts and official split/subset manifests, or an explicitly identified custom protocol.
- Images or protocol-compatible cached representations, acquisition metadata, permitted labels, and control annotations.
- Model checkpoints and pretraining provenance, training/adaptation configurations, or existing predictions.
- Compute and time budget, random seeds, and intended output location.

**Outputs**

- Protocol record identifying verified artifacts, unresolved dependencies, and benchmark deviations.
- Data and leakage audit with pass, fail, or unverified status and supporting evidence for each check.
- Comparison table containing method, checkpoint, split, domain/subset, metric, value, sample count, seed, and adaptation settings.
- Reproducibility record with versions, preprocessing, fitted-data scope, runtime, and evaluation status.
- Concise findings separating official scores, local validation results, supplemental diagnostics, and untested claims.

A valid completion identifies its execution scope, preserves split and prediction alignment evidence, and labels every reported metric by its actual evaluation population. Claim official performance only when returned by the official evaluation process; never manufacture private labels or scores.

## References

- [BatchBench: Benchmarking AI Robustness to Batch Effects and Domain Shift in Biomedical Images - A JUMP Cell Painting Leaderboard](http://arxiv.org/abs/2610.30104v1), arXiv:2610.30104v1. Source for benchmark purpose, task, splits, metrics, and eligibility rules; consult the versioned full text and its official artifact links before execution.
