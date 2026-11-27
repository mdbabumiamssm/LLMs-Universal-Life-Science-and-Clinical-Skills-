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
name: 'scatter-spatial-cell-state-deconvolution'
description: 'Estimate cell-type proportions and spatial cell-state expression with SCATTER from mixed spatial counts, coordinates, and annotated single-cell references, with reference-mismatch checks.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# SCATTER Spatial Cell-State Deconvolution

## Overview

SCATTER estimates cell-type proportions and spot-specific relative expression profiles using spatial transcriptomic counts, coordinates, and an annotated single-cell reference. This skill guides input harmonization, implementation verification, fitting, and interpretation to distinguish changes in tissue composition from expression variation within cell types. The method description is supported by the supplied preprint; an official executable implementation was not verified during skill authoring.

## When to Use This Skill

- Mixed spatial capture spots require both cell-type composition estimates and within-cell-type expression analysis.
- Spatial neighborhoods may influence cell states, and an appropriately annotated single-cell reference is available.
- Tumor interfaces, lesions, or other tissue regions need exploratory cell-type-specific expression maps.
- Existing deconvolution results require checks for missing reference populations, weak cell-type support, or composition-driven signals.

## Core Capabilities

1. **Verify the implementation before execution.** Follow the paper's code-availability statement to an official repository and inspect its installation instructions, examples, input schema, and output definitions. Record the repository URL, release or commit, dependencies, and hardware requirements. Do not guess a package name, command, API, or parameter default from the acronym. If code or essential documentation remains unavailable, return a blocked execution report with input-readiness findings; do not claim a completed SCATTER fit.

2. **Harmonize counts, annotations, and coordinates.** Preserve raw spatial counts separately from any transformed matrices and use the input scale required by the verified implementation. Align species, gene identifiers, gene order, spot identifiers, and coordinate rows explicitly. Resolve duplicate gene identifiers with a documented rule, report shared-gene coverage and exclusions, and check finite nonnegative counts, empty spots, missing labels, and reference cell counts per type. Keep tissue sections separate when constructing neighborhoods so unrelated coordinate systems cannot create artificial neighbors.

3. **Check reference suitability.** Compare tissue, assay, condition, and annotation granularity between the spatial sample and reference. Review marker coverage and populations expected from independent tissue knowledge. Flag missing types, rare reference groups, and closely related types that may be difficult to separate. Use a justified coarser annotation or a better reference where needed; do not silently force an absent population into the nearest available label.

4. **Prepare proportion regularization.** Obtain compatible cell2location estimates using the verified SCATTER workflow. Match their spot and cell-type axes to the analysis inputs, and confirm the documented conversion from abundance estimates to the quantities SCATTER expects. Preserve these estimates and their provenance for comparison with fitted proportions; do not substitute arbitrary normalized abundance values without implementation support.

5. **Fit with spatial context.** Run the verified example on a small, representative subset before scaling up. SCATTER weights reference profiles using local spatial context and jointly fits profiles and proportions to reconstruct spot counts, with cell2location estimates regularizing proportions. Record neighborhood settings, seed, stopping criteria, runtime, and convergence diagnostics using the actual implementation. Treat the 15-minute outcome as a bounded pilot target on a prepared environment, not a promise for installation or a complete tissue-scale fit; report unfinished runs honestly.

6. **Validate fitted and allocated outputs.** Check documented dimensions, label alignment, finite values, and nonnegativity. Check proportion normalization against the implementation's definition and inspect reconstructed-count residuals by spot, gene, and tissue region. Keep relative expression profiles distinct from observed counts allocated after fitting using learned gene-specific calibration factors and proportions. For allocated counts, check conservation against observed counts over the documented modeled gene and cell-type universe, accounting for any explicitly documented residual component.

7. **Interpret states with sensitivity checks.** Map cell-type proportions alongside relative expression for the same type, marking low-support spot–type combinations as unreliable rather than biological zeros. Investigate structured residuals, implausible marker allocation, and strong dependence on the reference or regularization as possible mismatch signals. Where resources permit, compare plausible reference annotations, neighborhood settings, or seeds. Interpret neighborhood associations and ligand–receptor rankings as exploratory associations; inferred expression does not directly measure single-cell expression or establish signaling or causality.

## Inputs / Outputs

**Required inputs**

- Spatial spot-by-gene count matrix with stable spot and gene identifiers.
- Coordinates keyed to spots, with coordinate units and sample or tissue-section identifiers.
- Annotated single-cell reference expression data with gene identifiers, cell-type labels, and tissue, assay, and condition metadata.
- Compatible cell2location estimates, or inputs and resources needed to generate them through the verified workflow.
- Verified SCATTER implementation and documentation before numerical execution, plus a defined analysis subset and compute budget.

**Optional inputs**

- Tissue-region annotations, histology, marker sets, and independent imaging measurements for biological checks.
- Alternative reference annotations or samples for assessing sensitivity to reference mismatch.

**Expected outputs after a successful fit**

- Spot-by-cell-type proportion matrix with explicit labels and scale definitions.
- Spot-by-gene relative expression profiles for each cell type, preserving the implementation's normalization semantics.
- Separately labeled cell-type allocations of observed counts, with modeled-gene coverage and calibration provenance.
- Reconstruction diagnostics and spatial maps showing proportions, expression, and low-support regions.
- A concise run report recording implementation version, input alignment, exclusions, settings, convergence, elapsed time, validation results, and reference limitations.

**Completion criteria:** A pilot succeeds only when fitting completes and the labeled outputs pass dimensional, numerical, and reconstruction checks. Report a blocked or incomplete status with the precise missing dependency or failed check otherwise; input validation alone is not a successful deconvolution. Keep downstream differential-expression or pathway conclusions provisional until appropriate replication and statistical analysis are performed.

## References

- [Resolving cell states in spatial transcriptomics with SCATTER, arXiv:2611.34798v1](http://arxiv.org/abs/2611.34798v1) — source finding and method description; consult its code-availability statement to verify the executable implementation.
