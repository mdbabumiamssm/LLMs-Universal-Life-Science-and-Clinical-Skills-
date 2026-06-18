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
name: bio-bulkrna-de
description: Bulk RNA-seq differential expression analysis using PyDESeq2 with optional
  edgeR/limma-voom via rpy2.
tool_type: mixed
primary_tool: bulkrna
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# Bulk RNA-seq Differential Expression

Differential expression analysis for bulk RNA-seq count data. Primary engine is PyDESeq2 (a pure-Python re-implementation of DESeq2); falls back to a scipy Welch's t-test with Benjamini-Hochberg FDR correction when PyDESeq2 is not installed.

## CLI Reference

```bash
python omicsclaw.py run bulkrna-de --demo
python omicsclaw.py run bulkrna-de --input <counts.csv> --output <dir>
python bulkrna_de.py --input counts.csv --output results/ --control-prefix ctrl --treat-prefix treat
python bulkrna_de.py --demo --output /tmp/bulkrna_de_demo
python bulkrna_de.py --input counts.csv --output results/ --method ttest --padj-cutoff 0.01 --lfc-cutoff 1.5
```

## Why This Exists

- **Without it**: Researchers must manually install and configure DESeq2 in R, handle count normalization, dispersion estimation, and multiple-testing correction across thousands of genes.
- **With it**: A single Python command runs the full DESeq2 pipeline (via PyDESeq2), produces publication-ready volcano and MA plots, and exports filtered DE tables ready for downstream enrichment.
- **Why OmicsClaw**: Wraps the gold-standard negative-binomial GLM approach into the OmicsClaw reporting framework with automatic fallback to simpler statistics when dependencies are unavailable.

## Workflow

1. **Load**: Read a genes-by-samples raw count matrix (CSV with a `gene` column and sample columns prefixed by condition).
2. **Partition**: Split sample columns into control and treatment groups by prefix matching.
3. **Model**: Fit a negative-binomial GLM per gene using PyDESeq2 (size-factor normalization, dispersion shrinkage, Wald test). Falls back to Welch's t-test with manual Benjamini-Hochberg FDR if PyDESeq2 is not available.
4. **Filter**: Identify significant genes at the user-specified padj and log2FC cutoffs.
5. **Visualize**: Generate volcano plot, MA plot, and DE summary bar chart.
6. **Report**: Write markdown report, result.json, full and filtered DE tables, and a reproducibility script.

### PyDESeq2 Enhancements Adopted

- **Multi-factor + continuous covariates**: Accept formulas like `~ batch + condition` or `~ age + condition`, mirroring the design support described in the PyDESeq2 repository (v0.5+) so users can adjust for confounders without leaving Python.
- **Installer parity**: `pip install pydeseq2` (PyPI) or `conda install -c bioconda pydeseq2`; OmicsClaw checks for either path at runtime before falling back to the Welch t-test.
- **CI-aligned dependency floor**: Default environment pins to pandas ≥2.0, numpy ≥1.24, scipy ≥1.11, matching PyDESeq2's GitHub Actions matrix to reduce drift.

### Reliability Notes

- Treat `pydeseq2` import failures as actionable warnings; we emit remediation steps sourced from the upstream README (e.g., missing formulaic or anndata dependencies).
- Every packaged report lists the reliability score for the underlying DE engine so downstream orchestration can decide whether to re-run with an alternate method (edgeR/limma) if desired.

## Example Queries

- "Run differential expression on my bulk RNA-seq counts"
- "Find DEGs between control and treatment using DESeq2"
- "Perform bulk RNA DE analysis with a log2FC cutoff of 2"
- "Run bulk DE with t-test fallback on this count matrix"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── figures/
│   ├── volcano_plot.png
│   ├── ma_plot.png
│   └── de_barplot.png
├── tables/
│   ├── de_results.csv
│   └── de_significant.csv
└── reproducibility/
    └── commands.sh
```

## Safety

- **Local-first**: All processing runs locally; no data is uploaded to external services.
- **Disclaimer**: Every report includes the standard OmicsClaw disclaimer.
- **Audit trail**: Parameters, method used (including fallback events), and input checksums are recorded in result.json.

## Integration with Orchestrator

**Trigger conditions**:
- Automatically invoked when user intent matches bulk RNA differential expression keywords.

**Chaining partners**:
- `bulkrna-alignment` — Upstream: aligned BAM to count matrix
- `bulkrna-enrichment` — Downstream: pathway/GO enrichment of significant genes

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--method` | `pydeseq2` | `pydeseq2` or `ttest` |
| `--control-prefix` | `ctrl` | Column name prefix for control samples |
| `--treat-prefix` | `treat` | Column name prefix for treatment samples |
| `--padj-cutoff` | `0.05` | Adjusted p-value significance threshold |
| `--lfc-cutoff` | `1.0` | Absolute log2 fold-change threshold |

## Version Compatibility

Reference examples tested with: PyDESeq2 0.4+, scipy 1.11+, pandas 2.0+, numpy 1.24+

## Dependencies

**Required**: numpy, pandas, scipy, matplotlib
**Optional**: pydeseq2 (recommended; pure-Python DESeq2 implementation)

## Citations

- [DESeq2](https://doi.org/10.1186/s13059-014-0550-8) — Love et al., Genome Biology 2014
- [PyDESeq2](https://doi.org/10.1093/bioinformatics/btad547) — Muzellec et al., Bioinformatics 2023
- [Benjamini-Hochberg](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) — Benjamini & Hochberg, JRSSB 1995

## Related Skills

- `bulkrna-alignment` — Read alignment and counting upstream
- `bulkrna-enrichment` — Pathway enrichment of DE genes downstream
- `bulkrna-coexpression` — Co-expression network analysis

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->