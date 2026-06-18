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
name: bio-sc-velocity
description: RNA velocity analysis for single-cell omics. Wraps scVelo to quantify
  spliced/unspliced kinetics, latent time, velocity graphs, and driver gene ranking
  with optional dynamical mode fitting.
tool_type: mixed
primary_tool: singlecell
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# ⚡ Single-Cell RNA Velocity

Quantify transcriptional dynamics by coupling spliced and unspliced matrices using **scVelo**'s stochastic and dynamical models. This skill
ingests AnnData/loom counts, performs preconditioning (normalization, moments, phase portrait checks), computes velocities, and returns
latent time embeddings with driver gene evidence suitable for trajectory-aware downstream workflows.

## When to Trigger

- User mentions "RNA velocity," "latent time," "dynamic gene programs," or "spliced/unspliced layers"
- Input AnnData includes `.layers["spliced"]` and `.layers["unspliced"]`
- Need to compare lineage directionality following clustering/integration steps

## Supported Inputs

| Format | Notes |
|--------|-------|
| `.h5ad` | Preferred; expects `layers["spliced"]`/`["unspliced"]`, `obs` annotations, optional `var` kinetic priors |
| `.loom` | Auto-converted to AnnData; verifies `layers/{spliced,unspliced}` |
| Matrices | Provide `--spliced`/`--unspliced` MTX + metadata to build AnnData wrapper |

## Typical Workflow

1. **Load + QC**
   ```python
   import scvelo as scv
   adata = scv.read("sample.h5ad")
   scv.pp.filter_and_normalize(adata, min_shared_counts=30, n_top_genes=4000)
   scv.pp.moments(adata, n_pcs=30, n_neighbors=30)
   ```
2. **Velocity Computation**
   ```python
   scv.tl.velocity(adata, mode="dynamical")
   scv.tl.velocity_graph(adata)
   scv.tl.velocity_confidence(adata)
   ```
3. **Latent Time & Drivers**
   ```python
   scv.tl.recover_dynamics(adata)
   scv.tl.latent_time(adata)
   scv.tl.rank_velocity_genes(adata, groupby="leiden")
   ```
4. **Visualization & Export**
   ```python
   scv.pl.velocity_embedding_stream(adata, basis="umap", color="leiden")
   adata.write_h5ad("velocity_annotated.h5ad")
   ```

## CLI Examples

```bash
# Run full pipeline with dynamical model, auto-detect PCA/neighbor params
python omicsclaw.py run sc-velocity --input data/sample.h5ad --mode dynamical --out runs/sc_velocity

# Skip recover_dynamics if kinetics already stored
python omicsclaw.py run sc-velocity --input data/sample.h5ad --mode stochastic --skip-latent-time

# Provide loom inputs and metadata
python omicsclaw.py run sc-velocity --loom data/sample.loom --obs-meta obs.csv --var-meta var.csv
```

## Key Parameters

| Flag | Default | Description |
|------|---------|-------------|
| `--mode` | `dynamical` | `stochastic`, `steady_state`, or `dynamical` modeling |
| `--min-shared-counts` | `30` | Genes must appear with this many shared counts during normalization |
| `--n-top-genes` | `4000` | HVG count for kinetics modeling |
| `--n-pcs` | `30` | Principal components for moment calculation |
| `--n-neighbors` | `30` | Neighborhood size for velocity graph construction |
| `--skip-latent-time` | `False` | Disable latent time + driver gene ranking to save runtime |

## Outputs

- Annotated `.h5ad` with velocity layers, confidence, latent time, and driver gene tables
- Summary report (`report.md`) capturing runtime, parameter set, model diagnostics, QC thresholds
- PNG/PDF figures for streamlines, quiver plots, phase portraits, driver gene heatmaps
- `result.json` for orchestrator bookkeeping

## Integration Touchpoints

- **Upstream:** `sc-preprocessing`, `sc-doublet-detection`, `sc-batch-integration`
- **Downstream:** `sc-trajectory` (uses latent time), `sc-cell-communication` (velocity-informed ligand prioritization), `spatial-velocity`

## Troubleshooting Cheatsheet

| Symptom | Fix |
|---------|-----|
| Low velocity confidence (`velocity_confidence` < 0.4) | Increase `min_shared_counts`, rerun normalization/moments, verify layers not log-normalized beforehand |
| Divergent dynamical fit | Initialize with `mode=stochastic`, inspect phase portraits for genes with insufficient kinetics |
| Memory pressure (>32 GB) | Use `--subset-gene-file` to preselect driver genes or run on sparse-backed AnnData |

## Source Reliability

| Source | Score | Notes |
|--------|-------|-------|
| Theis Lab scVelo repo | 0.93 | Active upstream repository with peer-reviewed implementation |
| K-Dense Claude Scientific Skills | 0.90 | Provides standardized skill scaffolding we mirror for metadata/trigger design |

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->