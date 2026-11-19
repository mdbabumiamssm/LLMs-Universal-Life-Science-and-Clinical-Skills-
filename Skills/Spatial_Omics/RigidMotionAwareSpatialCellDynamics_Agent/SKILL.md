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
name: 'rigid-motion-aware-spatial-cell-dynamics'
description: 'Assess spatial transcriptomics time courses for coordinate-frame artifacts and plan or evaluate horizontal flow matching of tissue geometry, molecular state, and cell abundance.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Rigid-Motion-Aware Spatial Cell Dynamics

## Overview

This skill assesses and evaluates spatial cell dynamics when section rotation or translation can masquerade as biological movement. It uses the research-stage HORIZON formulation described in the source finding: horizontal flow matching models tissue geometry, molecular state, and abundance while removing shared rigid motion. Separate reported claims from verified implementation behavior and results measured on the supplied data.

## When to Use This Skill

- Spatial transcriptomics snapshots at multiple times have inconsistent coordinate frames.
- Inferred cell displacement appears dominated by whole-section translation or rotation.
- A study needs to compare rigid alignment with explicit removal of rigid velocity components.
- Tissue generation or interpolation must account for changing cell abundance as well as expression and geometry.
- A HORIZON reproduction needs input checks, baseline design, or evaluation criteria before training.

## Core Capabilities

1. **Validate temporal and spatial inputs.** Check cell identifiers, finite coordinates, coordinate dimension and units, gene identifiers, time ordering, biological replicates, and expression preprocessing. Keep physical coordinate scaling consistent across stages; independently rescaling each tissue can erase biological expansion. Distinguish individual cells from spots and do not silently interpret spot counts as cell abundance.

2. **Diagnose coordinate-frame artifacts.** Visualize snapshots before and after a shared rigid transform per section. Use available anatomical landmarks or robust correspondences to assess translation and rotation, and record residual deformation, tissue overlap, cropping, and landmark uncertainty. Treat reflections, scaling, and nonrigid distortion separately; they are not removed by a translation-and-rotation model. Explicitly document whether global tissue motion is nuisance variation or part of the biological question.

3. **Check implementation readiness.** Retrieve the versioned paper and inspect any implementation linked by the paper or its project page. Verify provenance, license, supported data dimensions, dependencies, example execution, and checkpoint availability before proposing executable commands. Do not invent a repository, package name, command-line interface, or pretrained model. If code or full mathematical details cannot be verified, produce a readiness report and evaluation plan rather than claim a HORIZON run.

4. **Specify horizontal dynamics.** Describe a continuity–reaction model in which transport changes spatial and molecular organization and reaction changes mass. The source formulation assigns no action cost to shared rigid motion; its projector removes that component from spatial prediction errors during training and predicted velocities during generation. Its endpoint problem jointly estimates correspondence and relative pose in Wasserstein–Fisher–Rao geometry, supplying analytic velocity and growth regression targets. Verify the paper's metric, mass weighting, pose convention, and projector equations before implementation; ordinary centering alone does not remove rotation. Theoretical recovery under ideal population conditions is not an empirical guarantee.

5. **Construct fair comparisons.** Compare an unaligned trajectory baseline, the same baseline with rigid alignment, and a horizontal model where available. Include alignment-only and projection-disabled ablations when supported, with shared preprocessing, data splits, feature choices, and comparable tuning budgets. Use a spatial trajectory comparator and an unbalanced comparator capable of changing mass when available. Record unavailable comparisons instead of fabricating results.

6. **Evaluate geometry, state, abundance, and drift.** Report spatial distribution or landmark reconstruction error, expression distribution or marker-pattern error, and total and cell-type abundance error separately. Specify each metric's units, normalization, and evaluation alignment. Measure shared translation and rotation remaining in predicted velocities or trajectories using the verified weighting convention. Test controlled rigid perturbations: rotating or translating an input should transform spatial predictions consistently without changing scalar growth or molecular predictions. Report both original-frame and rigid-aligned geometry errors so evaluation alignment cannot conceal drift.

7. **Test temporal generalization and interpretation.** Hold out an intermediate stage where enough stages exist, and exclude its measurements from fitting, feature selection, alignment tuning, and hyperparameter selection. Generate from the permitted initial snapshot, then compare with the held-out stage. Prefer replicate-level splits and report variability across replicates or seeds when feasible. Treat inferred correspondence as a distribution-level hypothesis, not observed lineage; sampling depth, segmentation, capture efficiency, and section coverage can mimic growth or loss.

8. **Deliver a bounded assessment.** Within 15 minutes, complete input triage, source/implementation status, coordinate diagnostics when feasible, and a concrete comparison plan or small verified execution. Full training is outside this time guarantee. Mark every evaluation as measured, planned, or unavailable; state blockers and the next executable step. Do not equate a completed readiness report with validated biological dynamics.

## Inputs / Outputs

**Required inputs**

- At least two ordered snapshots for learning temporal change: cell-by-gene expression, matching cell coordinates, time labels, and section/sample identifiers.
- Coordinate units and dimension, expression normalization or raw-count status, gene mapping, and the biological interpretation of sampling times.
- Counts or mass weights plus sampling/coverage information if abundance dynamics are to be interpreted quantitatively. If these are missing, restrict conclusions about abundance.

**Optional inputs**

- Tissue images, landmarks, cell-type annotations, replicate labels, quality filters, and known frame transformations.
- Verified source implementation or checkpoint, compute budget, and preselected baselines and metrics.
- A single initial snapshot for generation only when a suitable fitted model already exists; one snapshot alone does not identify temporal dynamics.

**Outputs**

- A concise readiness report recording validated input shapes, units, time structure, mass assumptions, missing metadata, and implementation verification status.
- A coordinate-frame diagnostic with transform conventions, alignment residuals, and remaining biological or technical ambiguities.
- A reproducible run specification containing data splits, preprocessing, baseline/ablation settings, metric definitions, random seeds, and verified software versions or commit identifiers.
- When execution is feasible, predicted tissue states, spatial velocities, molecular states, mass/growth outputs, and measured comparison results with uncertainty where available.
- A limitations statement separating coordinate invariance, predictive reconstruction, and biological interpretation. Require finite predictions, valid output dimensions, and nonnegative generated mass; report failures explicitly.

## References

- Zihan Wang, Jianzhe Li, Zhenyi Zhang, and Peijie Zhou. [Horizontal Flow Matching for Single-Cell Spatiotemporal Dynamics](http://arxiv.org/abs/2611.24764v1). arXiv:2611.24764v1, submitted November 18, 2026. Source finding for horizontal flow matching and HORIZON; treat its performance statements as paper-reported until independently reproduced.
