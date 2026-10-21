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
name: 'direction-aware-spatial-transcriptomics'
description: 'Prepare and evaluate spatial transcriptomics representations using spatially informative genes and directional cellular neighborhoods, with coordinate checks and spatially separated baselines.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Direction-Aware Spatial Transcriptomics

## Overview

This skill turns the Tessera finding into a reproducible research workflow for spatial gene selection and directional neighborhood analysis. It separates documented methodology from proposed controls so that coordinate artifacts, spatial leakage, and implementation uncertainty do not become claims of biological improvement.

## When to Use This Skill

- Expression-only embeddings fail to distinguish cells in different spatial contexts.
- Equally distant neighbors may have different relevance depending on their bearing.
- A study needs spatial gene selection compared with conventional highly variable genes.
- A team wants to assess Tessera reproducibility or transfer across tissue sections and technologies.
- Directional representations need evaluation under translation, rotation, and coordinate perturbation.

## Core Capabilities

1. **Establish method and implementation provenance.** Read the versioned paper, especially Sections 2–3 and Appendices C–E. Verified v1 details: SIR combines TF–IDF and Moran's I ranks with reciprocal-rank fusion, selecting 500 genes per cell; its constants are kappa=60 and lambda=0.6. Frozen scGPT embeddings feed continuous 2D RoPE attention with learned vector frequencies, unrotated values, and a 200-micrometre cutoff. Training masks whole-cell embeddings and uses negative-binomial reconstruction; masked-cell depth is replaced by visible-neighbor median depth. These are paper specifications, not an executable implementation. [Method source](https://arxiv.org/html/2610.28579v1).

   No official Tessera repository or checkpoint link was identified in the inspected v1 text on 2026-10-21; availability remains unverified. Recheck paper-linked resources before execution. Record repository URL, commit, license, checkpoint checksum, vocabulary, dependencies, and supported hardware when found. Never invent installation commands or package names. If unavailable, deliver a method specification and baseline pilot, explicitly labeled as a proposed implementation rather than a Tessera reproduction.

2. **Prepare expression and coordinate inputs.** Require a cells-by-genes count matrix, stable cell and gene identifiers, and matching coordinates. Preserve raw counts separately from transformed encoder inputs. Check identifier uniqueness, row alignment, missing values, negative counts, empty profiles, duplicate coordinates, and panel coverage. Distinguish unmeasured genes from measured zeros; document vocabulary mapping and any losses.

   The paper uses 2D micrometre coordinates; translation invariance does not imply rotation invariance. [Coordinate specification](https://arxiv.org/html/2610.28579v1). Require pixel calibration, axis direction, handedness, section identifiers, and any registration transforms. Do not infer micrometres from coordinate magnitudes. Keep sections separate, preserve physical scale, and flag unknown orientation. Treat spot-level mixtures and 3D inputs as adaptations requiring independent evaluation.

3. **Select spatially informative features without target leakage.** Establish train, development, and test partitions before fitting preprocessing. Implement the exact SIR equations from Appendix C only after checking graph construction, rank direction, tie handling, and zero-expression behavior. Record unspecified choices as assumptions. Compare SIR with highly variable genes and expression-only ranking using matched gene budgets.

   Fit learned transformations and tune settings on training/development data only. In masked-expression experiments, exclude target counts from spatial statistics, feature selection, normalization, and neighbor summaries accessible to the predictor. Use a fixed evaluable target panel rather than target-selected genes for a strict assessment. Label this stricter protocol as an adaptation when it differs from paper reproduction. Declare any test-section adaptation or transductive preprocessing explicitly.

4. **Construct and inspect directional neighborhoods.** Store directed offsets as delta(i,j)=position(j)-position(i), plus distance and section membership. Audit graph density, isolated cells, edge effects, tissue gaps, and accidental links between sections. Match neighborhood support across directional and radial models. A hand-built offset-feature model is a research baseline, not Tessera.

   At inference with deterministic settings, translate all coordinates and compare outputs against a stated numerical tolerance. Rotate and reflect coordinates as sensitivity analyses, recording whether biological axes were retained. Inspect angular responses while controlling distance and cellular content; direction sensitivity alone does not establish useful biology. Apply coordinate shuffling within sections as a negative control.

5. **Compare representations using spatially separated validation.** Prefer held-out donors and complete sections; keep sections from one donor together. If only one section exists, use spatial blocks with exclusion buffers exceeding the model's effective receptive field, including multilayer paths. Build partition-specific neighborhoods and prevent overlapping windows from crossing splits. Mark single-section results as limited evidence of transfer.

   Include expression-only PCA or a verified frozen encoder, a distance-only neighborhood model, and a directional model. Hold gene budgets, training budgets, target masks, preprocessing, and evaluation cells constant. Add a gene-selection-by-geometry ablation to distinguish the two contributions. Prespecify the task and metric: masked reconstruction with error and correlation, or label prediction using independently supplied annotations. Aggregate paired differences by donor or section, with uncertainty at that level; do not treat correlated cells as independent replicates. Inspect platform and batch predictability alongside biological performance. Report failed controls and missing baselines; never substitute published improvements for measured results.

6. **Return a bounded, auditable pilot.** Use the 15-minute target for input validation, provenance review, a small baseline run when dependencies are ready, and a report. It is not a promise to train a foundation-scale model. Select a deterministic subset and record its size, seed, runtime, and hardware. If data, calibration, or code are missing, return an explicit readiness report with blocked steps; do not mark modeling complete. Schedule full training and independent validation as follow-up work outside the pilot budget.

## Inputs / Outputs

**Inputs**

- AnnData or equivalent expression matrix with raw counts and gene identifiers.
- Cell coordinates with physical units, section IDs, and cell-to-coordinate mapping.
- Donor, tissue, platform, batch, and optional independent annotation metadata.
- Analysis objective, resource budget, split policy, and optional verified model artifacts.

**Outputs**

- Readiness and QC report, including coordinate assumptions and missing prerequisites.
- Reproducibility manifest with source version, implementation status, preprocessing, seeds, and split membership.
- When execution is possible: selected gene ranks, neighborhood offsets, and finite cell-aligned embeddings with model provenance.
- Matched baseline results, spatial validation metrics, transformation controls, and limitations; clearly distinguish computed results from proposed experiments.

**Acceptance checks:** Cell IDs remain aligned across all outputs; splits and neighborhood boundaries pass leakage checks; units and transforms are recorded; reported metrics trace to actual runs; every skipped stage has a reason. A readiness-only result is valid triage output but is not successful model execution. Spatial associations and attention patterns are not evidence of causal cell communication or clinical utility.

## References

- [Spatially Informed and Direction Sensitive Representation Learning for Spatial Transcriptomics — arXiv:2610.28579v1](http://arxiv.org/abs/2610.28579v1). Source finding; submitted 2026-10-20.
- [Versioned full text and methodological appendices](https://arxiv.org/html/2610.28579v1). Consult for exact formulas and reproduction settings; no official implementation was verified during authoring.
