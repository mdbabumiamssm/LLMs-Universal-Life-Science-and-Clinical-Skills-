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
name: bio-metabolomics-statistics
description: "Statistical analysis for metabolomics \u2014 PCA, PLS-DA, clustering,\
  \ and univariate tests."
tool_type: mixed
primary_tool: metabolomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 📈 Metabolomics Statistical Analysis

Statistical analysis module for metabolomics data. PCA, PLS-DA, hierarchical clustering, and univariate tests.

## CLI Reference

```bash
python omicsclaw.py run met-stat --demo
```

## Why This Exists

- **Without it**: Metabolomic variance is inherently high-dimensional and non-trivial to dissect
- **With it**: Advanced clustering algorithms and projections distill variance into biologically valid groups
- **Why OmicsClaw**: Wraps complex R/Bioconductor modules into a clear Python execution syntax

## Workflow

1. **Calculate**: Compute distance matrices (Euclidean, Pearson).
2. **Execute**: Project high-dimensional structures via PCA/t-SNE/UMAP.
3. **Assess**: Execute hierarchical clustering mapping samples to metabolic profiles.
4. **Generate**: Output coordinate projections.
5. **Report**: Synthesize scree plots, scatter projections, and heatmaps.

## Example Queries

- "Run PCA on my normalized metabolomics data"
- "Perform hierarchical clustering with Ward's method"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── statistics.csv
├── figures/
│   ├── pca_projection.png
│   └── sample_heatmap.png
├── tables/
│   └── principal_components.csv
└── reproducibility/
    ├── commands.sh
    ├── environment.yml
    └── checksums.sha256
```

## Safety

- **Local-first**: Strict offline processing without external upload.
- **Disclaimer**: Requires OmicsClaw reporting structures and disclaimers.
- **Audit trail**: Hyperparameters and operational flow states are logged fully.

## Integration with Orchestrator

**Trigger conditions**:
- Automatically invoked dynamically based on tool metadata and user intent matching.

**Chaining partners**:
- `met-normalize` — Upstream data scaling
- `met-diff` — Parallel structural differential assessment

## Citations

- [MetaboAnalystR](https://doi.org/10.1093/bioinformatics/bty528)
- [ropls](https://doi.org/10.1021/acs.jproteome.5b00354)

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->