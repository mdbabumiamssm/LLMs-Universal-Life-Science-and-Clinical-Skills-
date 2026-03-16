<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

---
name: rna-velocity
description: Infer transcriptional dynamics from spliced/unspliced layers using scVelo with latent time, driver gene ranking, and velocity graph exports.
measurable_outcome: Deliver annotated .h5ad files containing velocity layers, latent time, confidence metrics, and ranked driver genes with Markdown + PNG diagnostics.
allowed-tools:
  - read_file
  - run_shell_command
  - python
reliability:
  - source: https://github.com/theislab/scvelo
    score: 0.93
    rationale: >-
      Canonical scVelo implementation maintained by Theis Lab with validated dynamical/stochastic models and active release cadence.
  - source: https://github.com/scverse/single-cell-best-practices
    score: 0.90
    rationale: >-
      Community maintained best-practices playbook from the scverse consortium covering velocity QC, parameter defaults, and benchmarking datasets.
---

## At-a-Glance
- **description (10-20 chars):** Velocity mapper
- **keywords:** scRNAseq, velocity, scVelo, latent-time, kinetics

## Workflow
1. **Input audit** – Accept `.h5ad` or `.loom` matrices with `layers['spliced']` / `layers['unspliced']`. Validate counts (non-negative) and gene overlap.
2. **Preconditioning** – Apply `scv.pp.filter_and_normalize(min_shared_counts=30, n_top_genes=4000)` and `scv.pp.moments(n_pcs=30, n_neighbors=30)` to stabilize kinetics as recommended by scVelo maintainers.
3. **Model selection** – Default to `mode="dynamical"`; auto-fallback to `stochastic` if latent time convergence stalls (>30 iterations without likelihood improvement).
4. **Velocity graph + confidence** – Run `scv.tl.velocity_graph` and `scv.tl.velocity_confidence`, persisting matrices plus summary stats (min/median confidence, percent of cells >0.4).
5. **Latent time + drivers** – Execute `scv.tl.recover_dynamics` and `scv.tl.latent_time`, then `scv.tl.rank_velocity_genes(groupby="leiden")` with CSV/JSON exports of top regulators.
6. **Visualization bundle** – Render `velocity_embedding_stream`, `velocity_embedding_grid`, and per-gene phase portraits for reviewer traceability.

## Guardrails
- Fail fast if `layers` missing or if >20% sparsity after normalization indicates invalid loom conversion.
- Never overwrite raw `.h5ad`; write `*_velocity.h5ad` plus `result.json` capturing parameters + git hash of scVelo commit.
- Document heuristics when trimming divergences (e.g., driver gene count, MT filtering) inside the markdown report for FDA audit trails.

## Integration Hooks
- Upstream: `scrna-qc`, `sc-batch-integration`, doublet workflows.
- Downstream: trajectory agents, ligand-receptor analysis, spatial velocity coupling.

## References
- scVelo GitHub issues/wiki for parameter defaults and troubleshooting.
- scverse best-practices notebook for velocity QC decision trees.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
