---
name: bulkrna-alignment
description: >-
  Bulk RNA-seq count matrix QC — library size, gene detection rates, and sample correlation.
version: 0.1.0
author: OmicsClaw
license: MIT
tags: [bulkrna, qc, library-size, gene-detection, alignment-stats]
metadata:
  omicsclaw:
    domain: bulkrna
    emoji: "📊"
    trigger_keywords: [bulk rna qc, library size, gene detection, count matrix qc, bulk alignment stats]
---

# Bulk RNA-seq Count Matrix QC

Library size distribution, gene detection rates, and sample correlation analysis for bulk RNA-seq count matrices.

## CLI Reference

```bash
python omicsclaw.py run bulkrna-alignment --demo
python omicsclaw.py run bulkrna-alignment --input <counts.csv> --output <dir>
```

## Why This Exists

- **Without it**: Bulk RNA-seq count matrices are fed directly into differential expression without checking for outlier samples, low-complexity libraries, or batch-driven correlation structure.
- **With it**: Systematic QC flags problematic samples before downstream analysis, preventing false positives from library size imbalance or failed sequencing lanes.
- **Why OmicsClaw**: Provides a standardised, local-first QC report with reproducible figures and machine-readable JSON output that chains into downstream skills.

## Workflow

1. **Load**: Parse the count matrix CSV (genes as rows, samples as columns, first column is gene identifiers).
2. **Library Size**: Compute total counts per sample, mean, median, and coefficient of variation across samples.
3. **Gene Detection**: For each gene, count how many samples detect it (count > 0). Identify globally undetected genes.
4. **Per-Sample Stats**: Calculate detected gene count and detection percentage for each sample.
5. **Sample Correlation**: Compute Pearson correlation matrix across all sample pairs and flag outlier samples with low mean correlation.

## Example Queries

- "Run QC on my bulk RNA-seq count matrix"
- "Check library sizes and gene detection rates"
- "Are there outlier samples in my RNA-seq experiment?"
- "Show sample correlation heatmap for my count data"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── figures/
│   ├── library_sizes.png
│   ├── gene_detection.png
│   └── sample_correlation.png
├── tables/
│   └── sample_stats.csv
└── reproducibility/
    └── commands.sh
```

## Safety

- **Local-first**: All computation runs locally; no data leaves the machine.
- **Disclaimer**: Reports include the standard OmicsClaw research-use disclaimer.
- **Audit trail**: Parameters, input checksums, and commands are logged for reproducibility.

## Integration with Orchestrator

**Trigger conditions**:
- Automatically invoked when the user mentions bulk RNA-seq QC, library size, gene detection, or count matrix quality.

**Chaining partners**:
- `bulkrna-de` -- Downstream differential expression analysis
- `bulkrna-enrichment` -- Downstream pathway enrichment on DE results

## Citations

- [RNA-seq QC best practices (Conesa et al. 2016)](https://doi.org/10.1186/s13059-016-0881-8)
- [A survey of best practices for RNA-seq data analysis (Genome Biology)](https://doi.org/10.1186/s13059-016-0881-8)
