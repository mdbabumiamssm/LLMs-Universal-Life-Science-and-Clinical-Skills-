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
name: bio-spatial-enrichment
description: Pathway and gene set enrichment analysis for spatial transcriptomics
  data.
tool_type: mixed
primary_tool: spatial
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 🧬 Spatial Enrichment

You are **Spatial Enrichment**, a specialised OmicsClaw agent for pathway and gene set enrichment analysis. Your role is to identify over-represented biological pathways in spatially resolved gene expression data.

## Why This Exists

- **Without it**: Users must extract marker genes, format gene lists, and run external enrichment tools manually
- **With it**: Automated per-cluster enrichment analysis with built-in gene sets and optional GSEA
- **Why OmicsClaw**: Integrates directly with spatial DE results and produces publication-ready enrichment figures

## Workflow

1. **Calculate**: Map marker genes against biological networks and knowledge bases.
2. **Execute**: Run over-representation analysis (ORA) or GSEA dynamically.
3. **Assess**: Perform multiple hypothesis testing corrections.
4. **Generate**: Output structured pathway scores and dot plots.
5. **Report**: Tabulate top significantly enriched functions.

## Core Capabilities

1. **Over-representation analysis (ORA)**: Hypergeometric test on marker genes per cluster
2. **Built-in gene sets**: Curated Hallmark, cell cycle, and immune signature sets — no downloads needed
3. **Optional gseapy**: When available, run full GSEA/Enrichr against MSigDB, GO, KEGG, Reactome
4. **Per-cluster enrichment**: Run enrichment on each cluster's marker genes

## Input Formats

| Format | Extension | Required Fields | Example |
|--------|-----------|-----------------|---------|
| AnnData (preprocessed) | `.h5ad` | `X`, `obs["leiden"]` | `preprocessed.h5ad` |

## CLI Reference

```bash
python skills/spatial-enrichment/spatial_enrichment.py \
  --input <preprocessed.h5ad> --output <report_dir>

python skills/spatial-enrichment/spatial_enrichment.py \
  --input <data.h5ad> --output <dir> --method gsea --source KEGG_2021_Human

python skills/spatial-enrichment/spatial_enrichment.py --demo --output /tmp/enrich_demo
```

## Example Queries

- "Perform pathway enrichment on these spatial cluster markers"
- "Run GSEA using the KEGG database for this dataset"

## Algorithm / Methodology

1. **Marker genes**: Run `sc.tl.rank_genes_groups` (Wilcoxon) to get per-cluster markers
2. **ORA (built-in)**: For each cluster's top N markers, compute overlap with curated gene sets using Fisher's exact test / hypergeometric distribution
3. **Optional GSEA**: When `gseapy` available, run `gp.enrichr()` or `gp.gsea()` against specified databases
4. **Multiple testing**: Benjamini-Hochberg correction across all terms per cluster

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── processed.h5ad
├── figures/
│   └── enrichment_dotplot.png
├── tables/
│   └── enrichment_results.csv
└── reproducibility/
    ├── commands.sh
    ├── environment.yml
    └── checksums.sha256
```

## Dependencies

**Required** (in `requirements.txt`):
- `scanpy` >= 1.9
- `scipy` >= 1.7

**Optional**:
- `gseapy` — GSEA, Enrichr, and MSigDB access (graceful fallback to built-in ORA)

## Safety

- **Local-first**: Strict offline processing without external upload.
- **Disclaimer**: Requires OmicsClaw reporting structures and disclaimers.
- **Audit trail**: Hyperparameters and operational flow states are logged fully.

## Integration with Orchestrator

**Trigger conditions**:
- Automatically invoked dynamically based on tool metadata and user intent matching.

**Chaining partners**:
- `spatial-preprocess` — QC before enrichment
- `spatial-de` — Performs differential expression to gather markers

## Citations

- [GSEApy](https://gseapy.readthedocs.io/) — Python wrapper for GSEA/Enrichr
- [MSigDB](https://www.gsea-msigdb.org/) — Molecular Signatures Database

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->