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
name: 'dmmr-crc-histopathology-agent'
description: 'Predict and validate colorectal cancer dMMR signals from H&E histopathology, including non-tumor and low-magnification WSI regions.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# dMMR CRC Histopathology Agent

## Overview

This skill guides computational pathology work for predicting mismatch repair deficiency (dMMR) in colorectal cancer from H&E whole-slide histopathology. It emphasizes workflows that consider tumor, non-tumor, and low-magnification tissue context, because the referenced finding specifically highlights the value of regions beyond conventional high-magnification tumor tiles.

Use this skill to structure data intake, region selection, model execution, validation review, and clinical-pathology handoff without treating image-based prediction as a replacement for validated diagnostic testing.

## When to Use This Skill

- A user asks for dMMR, MMR-deficiency, MSI, or Lynch-screening support from colorectal cancer histopathology.
- A colorectal cancer WSI workflow needs tumor, non-tumor, stromal, inflammatory, mucosal, or low-magnification region handling.
- A model or analysis must compare region strategies for biomarker prediction from H&E slides.
- A pathology AI result needs validation framing, failure analysis, or pathologist-facing handoff language.
- A dataset requires slide-level, patient-level, or cohort-level planning for dMMR/MSI labels derived from IHC, PCR, sequencing, or clinical records.

## Core Capabilities

1. **Clinical task framing** - Define the target as dMMR or a closely aligned MSI/MMR biomarker endpoint, identify label provenance, and state that outputs are decision-support signals unless clinically validated.
2. **WSI intake and quality control** - Check slide format, magnification metadata, tissue coverage, blur, folds, staining artifacts, scanner differences, de-identification status, and linkage to patient-level labels.
3. **Region selection strategy** - Build explicit inclusion and exclusion rules for tumor, invasive front, stroma, lymphoid aggregates, mucosa, necrosis, background, and low-magnification tissue context.
4. **Tile and feature pipeline design** - Plan tissue masking, multiscale tile extraction, color handling, feature embedding, multiple-instance learning, transformer/CNN aggregation, or classical feature workflows according to available code and data.
5. **Leakage-aware training and inference** - Enforce patient-level splits, avoid slide or tile leakage, separate development from locked evaluation, and document any cohort enrichment or case-control sampling.
6. **Validation and interpretation review** - Report metrics only when computed from the supplied data, inspect calibration and subgroup behavior, review heatmaps or attention maps cautiously, and summarize failure modes.
7. **Clinical-pathology handoff** - Produce concise notes that describe image evidence, region contributions, uncertainty, limitations, recommended confirmatory testing, and cases needing pathologist review.
8. **Non-tumor and low-magnification dMMR review** - Explicitly sample non-tumor and low-magnification colorectal cancer WSI regions, record region-level contribution to the prediction, validate predictions against available MSI or IHC status, and route uncertain predictions to pathology review.
9. **Tumor-only assumption checks** - When designing WSI region sampling or validation handoff, include non-tumor and low-magnification regions as potential dMMR signal contributors and flag bias risks from workflows that assume only high-magnification tumor tiles are informative.
10. **Region attribution and confirmation controls** - Evaluate tumor, non-tumor, and low-magnification WSI regions separately and jointly; document region-level attribution; control for blur, folds, stain or scanner artifacts, necrosis, background, and annotation errors; require external validation before clinical use; and hand off positive, discordant, or uncertain image-based signals for confirmatory MMR IHC and/or MSI testing.
11. **Evidence-aware multiregion validation** - Treat non-tumor and low-magnification WSI regions as potential contributors to dMMR predictive signal, while testing sensitivity to region sampling, assessing confounding, validating on external cohorts, and defining a clear pathology handoff for review and diagnostic confirmation.
12. **Comparative multiscale region workflow** - Explicitly sample and compare tumor, non-tumor, and low-magnification tissue regions; run region-selection ablations; fuse multiscale features before slide-level aggregation; validate on external cohorts; apply artifact controls; generate interpretability maps; and require pathology review of predictive signals arising outside tumor regions.

## Inputs / Outputs

**Inputs**

- H&E colorectal cancer whole-slide images or derived image tiles.
- Slide, block, case, and patient identifiers with de-identification status.
- dMMR, pMMR, MSI-H, MSS, or related labels with source details, such as IHC, PCR, sequencing, or curated clinical registry fields.
- Optional tumor annotations, tissue masks, region labels, magnification levels, scanner metadata, staining batches, and clinical-pathology covariates.
- User intent: training, inference, validation, region ablation, quality control, interpretability review, or clinical handoff.

**Outputs**

- A workflow plan for dMMR/MSI histopathology analysis, including region strategy and validation design.
- QC summaries for slides, tissue regions, tiles, metadata joins, and label consistency.
- Tile or region manifests documenting tumor, non-tumor, and low-magnification sampling decisions.
- Model-ready feature tables or inference summaries when data and tools are available.
- Patient-level or slide-level prediction reports with uncertainty, calibration notes, and limitations.
- Pathologist-facing handoff text that separates computational signal from diagnostic confirmation.

## References

- PubMed: dMMR prediction from colorectal cancer histopathology: Leveraging non-tumor and low-magnification regions. https://pubmed.ncbi.nlm.nih.gov/41875848/
