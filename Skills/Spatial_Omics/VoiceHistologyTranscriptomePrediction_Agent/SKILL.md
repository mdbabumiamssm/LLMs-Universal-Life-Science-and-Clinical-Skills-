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
name: 'voice-histology-transcriptome-prediction'
description: 'Prepare H&E images for VOICE single-cell transcriptome prediction, verify model access and spatial alignment, and evaluate predicted expression against held-out measurements.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# VOICE Histology-to-Transcriptome Prediction

## Overview

VOICE predicts single-cell gene expression from H&E images using direct prediction and optional reference-cell retrieval. This skill guides reproducible research inference and independent evaluation while keeping inferred expression explicitly separate from measured RNA abundance.

## When to Use This Skill

- Prepare histology and cell boundaries for VOICE inference.
- Check whether checkpoints, dependencies, and applicable licenses permit a proposed run.
- Generate spatially indexed expression predictions for exploratory spatial omics analysis.
- Compare predictions with matched measurements from held-out patients or tissues.
- Audit reference-bank leakage, gene alignment, or interpretation of prediction scales.

## Core Capabilities

1. **Establish readiness and provenance.** Inspect the current repository README, configuration, inference code, LICENSE, NOTICE, and weights documentation; pin the commit used. The README links `zchx/VOICE-23M` weights and separately gated `MahmoodLab/UNI2-h` weights. Verify actual download access, checkpoint completeness, gene vocabulary, and compatibility before launching. Repository code is labeled MIT; independently inspect checkpoint, encoder, and reference-data terms rather than assuming that code licensing covers them. Record artifact hashes and applicable restrictions. If required assets or terms cannot be established, return a blocked readiness report without fabricating predictions.

2. **Validate image preparation and spatial registration.** The README specifies 55 µm crops resized to 224×224. Confirm actual microns per pixel, image pyramid level, RGB channel handling, normalization, and masking against the pinned loader; do not invent stain normalization. Whole-slide inference accepts cell polygons at the image resolution. Validate coordinate axis order, origin, units, orientation, and any affine transform using overlays at several tissue landmarks. Inspect segmentation quality, clipped cells, background, folds, and blur. Preserve stable cell identifiers and an exclusion log. Stop inference when scale or registration remains ambiguous.

3. **Run a bounded inference pilot.** Choose a small representative region and record its selection before inspecting predictions. Confirm the environment against repository requirements and available accelerator memory. Prepared inputs include `manifest.csv.gz` and `patch_cell_boundaries.npz`; inspect their exact schema in the pinned version. Verify that image rows, boundary indices, and cell identifiers remain aligned. The documented prepared-input invocation is:

   ```bash
   python predict/predict.py --prepared /data/target --release /models/voice-23m --out pred.h5ad --save_embeddings
   ```

   Replace paths with validated local locations and confirm available flags before execution. Use evaluation mode and the repository inference implementation. Treat the 15-minute outcome as a pilot target with assets already available, not a guarantee for downloads, training, whole-slide processing, or full validation. Report elapsed time and incomplete stages honestly; a readiness report alone is not successful inference.

4. **Control retrieval and leakage.** For retrieval, verify reference tissue, measured-gene coverage, model compatibility, and any fusion calibration. The released pooled banks lack source identifiers, limiting exclusion audits. Keep all sections from a patient together; exclude target patients, duplicate sections, and test measurements from reference construction, tuning, and calibration. If pooled-bank provenance cannot establish independence, disclose that limitation and do not claim leakage-free evaluation. Prefer auditable custom banks or direct-only inference where appropriate; direct-only inference still requires assessment of pretraining overlap.

5. **Validate and label outputs.** Documented AnnData output contains spatial coordinates and optional embeddings; direct `X` values are log1p predictions, while fused `X` values are gene-wise scores. Preserve these meanings rather than relabeling either as raw counts. Check matrix dimensions, unique cell and gene identifiers, finite values, coordinate bounds, and expected coverage. Store measured expression separately and label every exported plot or table as predicted or measured. Retain configuration, checkpoint identity, preprocessing decisions, reference provenance, and excluded cells alongside results.

6. **Evaluate generalization against measurements.** Define patient-level splits before preprocessing choices or tuning; use a tissue-held-out test when testing transfer to unseen tissues. Align measured and predicted genes by identifiers, not column position, and compare only genuinely measured genes. Match expression transformations explicitly; evaluate fused scores with metrics appropriate to their scale. Report per-gene Pearson/Spearman correlation and, when scales match, MAE or RMSE against a training-only baseline. Identify undefined correlations for constant genes. Summarize by patient and tissue, with patient-level resampling for uncertainty rather than treating neighboring cells as independent. Select genes and thresholds using training data only. Do not equate within-slide validation with unseen-patient performance or invent accuracy claims when paired measurements are unavailable.

## Inputs / Outputs

**Inputs**

- H&E images, physical resolution, tissue identity, and patient/slide identifiers.
- Cell segmentation or polygons, or repository-compatible prepared crops and manifests.
- Accessible compatible checkpoints, gene vocabulary, configuration, and dependency environment.
- Optional reference bank and fusion calibration with documented provenance.
- For evaluation: independently measured expression, measured-gene masks, cell correspondence, and predefined patient/tissue splits. Spot-level measurements support spot-level assessment only after a justified aggregation; they do not establish single-cell accuracy.

**Outputs**

- A validated pilot prediction artifact with cell-by-gene values, coordinates, and explicit scale and prediction labels.
- A run record containing source revision, artifact hashes, configuration, QC exclusions, runtime, and licensing/access findings.
- When measurements exist, held-out evaluation tables, baseline comparisons, and limitations on independence and generalization.
- When prerequisites fail, a specific blocker report identifying missing assets or alignment evidence; never synthetic replacement measurements or an unsupported success claim.

## References

- [VOICE_HE_ST_Pred repository and documented workflow](https://github.com/Luosanj/VOICE_HE_ST_Pred) — primary source for implementation, model links, preprocessing, and output semantics; recheck at the pinned revision.
- [VOICE repository LICENSE](https://github.com/Luosanj/VOICE_HE_ST_Pred/blob/main/LICENSE) — code licensing; review separately from model and data terms.
- [VOICE repository NOTICE](https://github.com/Luosanj/VOICE_HE_ST_Pred/blob/main/NOTICE) — third-party notices.
- [VOICE weights documentation](https://github.com/Luosanj/VOICE_HE_ST_Pred/tree/main/weights) — checkpoint and reference-bank requirements.
