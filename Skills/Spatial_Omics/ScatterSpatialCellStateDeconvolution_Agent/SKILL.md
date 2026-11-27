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
description: 'Prepare and validate SCATTER analyses of mixed spatial transcriptomic spots to estimate cell-type proportions and spot-specific relative expression using coordinates and annotated single-cell references.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# SCATTER Spatial Cell-State Deconvolution

## Overview

SCATTER estimates cell-type proportions and spot-specific relative expression from mixed spatial transcriptomic counts, coordinates, and annotated single-cell references. It uses local spatial context to weight reference profiles, jointly fits profiles and proportions with cell2location regularization, and allocates observed counts using fitted proportions and learned gene-specific calibration factors. This skill guides preparation, execution, and validation so that composition changes can be distinguished from expression variation within a cell type.

## When to Use This Skill

- Analyze capture spots or spatial bins containing mixtures of cell types.
- Investigate whether regional expression differences reflect composition, within-type expression, or both.
- Map cell-type-specific programs near tumors, lesions, or tissue boundaries using a suitable single-cell reference.
- Validate inferred expression against imaging-derived pseudo-spots or independent spatial measurements.

## Core Capabilities

1. **Verify the implementation before execution.** Follow the source paper's code-availability link to its official repository and inspect the README, environment specification, and executable examples. Record the repository URL, release or commit, dependency versions, exact commands, and parameter choices. No official SCATTER repository or API was verified when this skill was authored; do not invent package names, installation commands, flags, defaults, or model equations. If the implementation remains inaccessible, finish input validation and report fitting as blocked rather than substitute another method under the SCATTER name.

2. **Prepare aligned counts and coordinates.** Preserve unnormalized count matrices and stable spot, cell, and gene identifiers. Check nonnegative finite counts, duplicate identifiers, empty spots, missing coordinates, and one-to-one alignment of spatial rows with count rows. Reconcile gene identifiers between spatial and reference data, document the intersection and exclusions, and reorder explicitly. Apply normalization and gene selection only as required by the verified implementation; do not silently use log-transformed values in a count likelihood.

3. **Match the reference to the tissue.** Check species, tissue, disease context, sequencing modality, cell-type labels, and representation of relevant states. Review cell counts and marker support per reference label, and flag absent or poorly sampled populations. Resolve inconsistent label granularity before fitting; retain sample and donor metadata to assess batch effects and reference mismatch. Treat expression outside the reference's supported states as uncertain rather than evidence of a newly discovered state.

4. **Supply compatible composition regularization.** Obtain cell2location estimates using the documented SCATTER workflow, or validate supplied estimates. Align their spots and cell-type labels exactly with the SCATTER inputs. Confirm which abundance summary and transformation the implementation expects; absolute abundance estimates and normalized proportions are not interchangeable. Record prior settings and provenance, and flag disagreement with independent marker or histology evidence.

5. **Model local spatial context and fit jointly.** Confirm coordinate units, section identifiers, and the documented neighborhood construction. Prevent neighborhoods from connecting unrelated tissue sections; inspect graph edges near gaps and boundaries. Run the official workflow that weights reference cells using local context and jointly fits expression profiles and proportions to reconstruct spot counts. Save the random seed, neighborhood settings, optimization diagnostics, and stopping criteria. Where feasible, compare documented neighborhood settings and seeds to assess sensitivity without replacing SCATTER with generic spatial smoothing.

6. **Export distinct expression products.** Keep fitted proportions, relative within-type profiles, reconstructed spot counts, and calibrated allocations of observed counts separate. Use the official post-fit allocation procedure and retain calibration factors when exposed. Do not approximate allocation as observed counts multiplied only by proportions, or interpret allocated counts as per-cell absolute expression. Label all output axes, units, normalization conventions, and any unsupported or low-abundance entries.

7. **Validate composition and expression separately.** Inspect reconstruction residuals by spot, gene, library size, and tissue region, while recognizing that reconstruction alone does not establish correct deconvolution. Check finite, nonnegative estimates and the implementation's normalization conventions; test that allocations sum to observed counts for the modeled genes when the documented allocation guarantees this. Compare proportions with independent abundance evidence and compare expression within each supported cell type across spots. For pseudo-spot validation, exclude benchmark cells from the reference, report gene-by-cell-type cross-spot correlations and errors, and identify constant or insufficiently observed pairs rather than assigning misleading correlations.

8. **Interpret neighborhoods with abundance-aware checks.** Examine relative expression alongside the focal cell type's abundance, total counts, and neighboring cell composition. Mask or flag estimates where the focal type has insufficient support, using explicit documented thresholds. Account for spatial dependence and biological replication in association tests; individual spots are not independent donors. Treat regulon scores and ligand-receptor rankings as downstream hypotheses, not direct evidence of regulatory activity or signaling. Report sensitivity to reference choice, composition regularization, and spatial context when those checks are available.

### Execution scope and acceptance

Use the 15-minute target for a bounded smoke run on a documented example or representative subset when dependencies and reference estimates are ready. Record elapsed time, hardware, subset selection, and whether convergence was reached; full datasets, environment setup, and cell2location training may exceed this budget. A partial or blocked run is not a successful fit.

Accept a smoke run only when identifiers remain aligned, the documented fitting and allocation stages complete, output dimensions and numerical checks pass, and diagnostics are available for inspection. Report unresolved residual patterns, unstable estimates, missing reference types, and unsupported cell-type/spot combinations. Do not transfer the paper's benchmark performance to a new dataset without validation.

## Inputs / Outputs

### Inputs

- Spatial raw counts: spots or bins by genes, with unique identifiers and count provenance.
- Coordinates: one aligned row per spot, coordinate units, section/sample identifiers, and optional tissue masks or histology.
- Single-cell reference: cells by genes, annotated cell types, raw counts or the representation required by the official workflow, and donor/batch metadata.
- cell2location estimates: aligned abundance summaries or inputs needed to generate the documented regularizer.
- Run specification: verified implementation version, documented parameter settings, available compute, output location, and target tissue comparison.
- Optional validation data: independent imaging counts, pseudo-spot ground truth, tissue annotations, or replicate samples.

### Outputs

- An input-validation report covering alignment, reference coverage, gene overlap, exclusions, and unresolved mismatches.
- A spot-by-cell-type proportion table, with the implementation's scale and normalization documented.
- Spot-by-cell-type-by-gene relative expression and calibrated allocated counts, exported separately in suitable sparse or chunked form when needed.
- Reconstructed spot counts, residual summaries, fit diagnostics, and calibration factors if exposed by the implementation.
- Spatial maps and comparison tables that show abundance and within-type expression separately, with low-support estimates flagged.
- A reproducibility record containing commands, versions, seeds, parameters, elapsed time, validation results, and completion status. If execution is blocked, provide the prepared-input report and precise missing prerequisite without fabricated estimates.

## References

- [Resolving cell states in spatial transcriptomics with SCATTER, arXiv:2611.34798v1](http://arxiv.org/abs/2611.34798v1). Source finding for the method and applications; consult its code-availability statement for implementation details.
