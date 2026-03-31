# Single-Cell RNA-seq Quality Control

This skill performs comprehensive quality control on single-cell RNA-seq data using
MAD-based filtering. It calculates standard QC metrics (total counts, genes detected,
mitochondrial percentage), identifies outliers using Median Absolute Deviation, and
generates publication-ready visualizations. Follows scverse consortium best practices.


## Capabilities

### calculate_qc_metrics

Calculate standard QC metrics for each cell

**Inputs:**
- `adata` (AnnData) (required): Annotated data matrix with raw counts
- `mito_prefix` (string) (optional): Prefix for mitochondrial genes [default: MT-]

**Outputs:**
- `adata` (AnnData): AnnData with QC metrics in .obs
- `qc_summary` (DataFrame): Summary statistics of QC metrics

### filter_cells

Filter cells based on QC metrics using MAD-based thresholds

**Inputs:**
- `adata` (AnnData) (required): AnnData with QC metrics calculated
- `min_genes` (integer) (required): Minimum genes per cell [default: 200]
- `max_genes` (integer) (required): Maximum genes per cell (None for MAD-based) [default: None]
- `max_mito_pct` (float) (required): Maximum mitochondrial percentage [default: 20.0]
- `n_mads` (float) (required): Number of MADs for outlier detection [default: 5.0]

**Outputs:**
- `filtered_adata` (AnnData): Filtered AnnData object
- `filtering_report` (dict): Report with cells removed per criterion

### generate_qc_plots

Generate comprehensive QC visualization plots

**Inputs:**
- `adata` (AnnData) (required): AnnData with QC metrics
- `output_dir` (string) (required): Directory to save plots [default: ./qc_plots]

**Outputs:**
- `plot_paths` (list): Paths to generated plot files

## System Prompt

```
You are an expert bioinformatician specializing in single-cell RNA sequencing analysis.
You follow scverse best practices and understand the biology behind QC metrics.

Key principles:
1. Always examine data distributions before setting hard thresholds
2. Use MAD-based filtering when possible for adaptive thresholds
3. Consider tissue/cell type when interpreting mitochondrial content
4. Document all filtering decisions for reproducibility
5. Generate visualizations to support QC decisions

```

## Examples

### Example 1

**User:** Run QC on my PBMC dataset at /data/pbmc_10k.h5ad

**Assistant:** I'll perform comprehensive QC on your PBMC dataset. Let me:

1. First, calculate QC metrics (total counts, genes detected, mito %)
2. Examine the distributions to set appropriate thresholds
3. Apply MAD-based filtering (5 MADs from median)
4. Generate visualization plots

[Executes QC pipeline...]

Results:
- Initial cells: 10,000
- Cells removed (low genes): 234
- Cells removed (high mito): 156
- Final cells: 9,610 (96.1% retained)

The filtering thresholds used:
- Min genes: 200
- Max genes: 5,847 (median + 5*MAD)
- Max mito %: 15.2% (median + 5*MAD)


## Dependencies

### Python Packages
```
scanpy>=1.9.0
anndata>=0.8.0
matplotlib>=3.5.0
seaborn>=0.12.0
pandas>=1.5.0
numpy>=1.23.0
```

---

**Skill ID:** `biomedical.genomics.single_cell_qc`
**Version:** 1.0.0
**Category:** genomics/single_cell
**License:** MIT
**Generated:** 2025-12-28
