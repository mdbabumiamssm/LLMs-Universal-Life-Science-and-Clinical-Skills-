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
name: bio-metabolomics-normalization
description: Metabolomics data normalization, scaling and transformation.
tool_type: mixed
primary_tool: metabolomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 📐 Metabolomics Normalization

Data normalization, scaling, and transformation for metabolomics feature tables.

## CLI Reference

```bash
python omicsclaw.py run met-normalize --demo
```

## Why This Exists

- **Without it**: Run-order effects and instrument drift heavily skew analytical variance
- **With it**: Mathematical transformations stabilize distributions and correct intrabatch variations
- **Why OmicsClaw**: Rapid integration of classic techniques (TIC, Median, Pareto) to prepare matrices for statistics

## Workflow

1. **Calculate**: Analyze missing value distribution.
2. **Execute**: Impute missing entries via localized techniques (kNN, RF).
3. **Assess**: Apply transformation (Log, Generalized Log) and scaling (Pareto, Auto).
4. **Generate**: Output structural normalized numerical matrices.
5. **Report**: Synthesize before/after boxplots of sample variance.

## Example Queries

- "Normalize this metabolomics table using QC-RLSC"
- "Log transform and Pareto scale this feature matrix"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── normalized.csv
├── figures/
│   └── normalization_boxplot.png
├── tables/
│   └── normalization_metrics.csv
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
- `peak-detection` — Upstream raw data mapping
- `met-diff` — Downstream statistical execution

## Citations

- [NOREVA](https://doi.org/10.1093/nar/gkx449) — normalization evaluation

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->