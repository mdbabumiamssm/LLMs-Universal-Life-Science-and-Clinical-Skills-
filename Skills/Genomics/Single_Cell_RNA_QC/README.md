# Single-Cell RNA-seq Quality Control

**ID:** `biomedical.genomics.single_cell_qc`
**Version:** 1.0.0
**Status:** Production
**Category:** Genomics / Single-Cell Analysis

---

## Overview

The **Single-Cell RNA-seq Quality Control Skill** provides a production-grade, statistically rigorous workflow for cleaning raw single-cell transcriptomic data. Unlike generic QC pipelines that rely on arbitrary thresholds, this skill implements **adaptive outlier detection** using Median Absolute Deviation (MAD), following the methodology established in Luecken et al. (2019) and adopted by the scverse community.

This skill enables AI agents to autonomously process raw 10x Genomics or H5AD datasets, assess data quality, filter low-quality cells, and produce analysis-ready outputs without manual intervention.

---

## Key Capabilities

### 1. Adaptive MAD-Based Outlier Detection

**Why MAD instead of fixed thresholds?**

Traditional QC uses arbitrary cutoffs (e.g., "filter cells with >10% mitochondrial reads"). This approach fails because:
- A tumor sample may naturally have elevated mitochondrial content due to metabolic stress
- Resting immune cells have lower UMI counts than activated cells
- Different tissues and experimental protocols yield different baseline distributions

**Our approach:** MAD adapts to each dataset's distribution, identifying statistical outliers relative to the sample's own characteristics. This preserves biological heterogeneity while removing technical artifacts.

```
MAD = median(|Xi - median(X)|)
Outlier threshold = median(X) ± n_MAD * MAD
```

### 2. Comprehensive Metric Calculation

| Metric | Description | Biological Significance |
|--------|-------------|------------------------|
| **Library Size (n_counts)** | Total UMIs per cell | Sequencing depth indicator; low values suggest empty droplets or debris |
| **Gene Detection (n_genes)** | Unique genes expressed | Cell complexity; low values indicate poor capture or dying cells |
| **Mitochondrial % (pct_mt)** | Fraction of mitochondrial reads | Elevated in stressed/dying cells (membrane rupture leaks cytoplasmic mRNA) |
| **Ribosomal % (pct_ribo)** | Fraction of ribosomal reads | High in protein-synthesizing cells; artifacts in some protocols |
| **Hemoglobin % (pct_hb)** | Fraction of hemoglobin genes | Red blood cell contamination marker |

### 3. QC Report Generation

Produces publication-ready visualizations:
- **Pre-filtering distributions:** Violin plots of all metrics
- **Threshold visualization:** Scatter plots with MAD-based cutoff lines
- **Post-filtering comparison:** Before/after cell count summaries

---

## Technical Specifications

### Input Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `file_path` | `str` | Required | Path to `.h5ad`, `.h5`, or 10x Genomics directory |
| `mad_counts` | `float` | `5.0` | MAD multiplier for library size filtering |
| `mad_genes` | `float` | `5.0` | MAD multiplier for gene count filtering |
| `mad_mt` | `float` | `3.0` | MAD multiplier for mitochondrial % filtering |
| `mt_threshold` | `float` | `15.0` | Hard safety cap for mitochondrial % (%) |
| `output_dir` | `str` | `<input>_qc_results` | Directory for output files |

### Output Files

| File | Description |
|------|-------------|
| `*_filtered.h5ad` | Clean dataset with low-quality cells removed |
| `*_with_qc.h5ad` | Original dataset with `pass_qc` boolean columns added |
| `qc_metrics_before.png` | Pre-filtering metric distributions |
| `qc_filtering_thresholds.png` | Visualization of applied cutoffs |
| `qc_metrics_after.png` | Post-filtering distributions |
| `qc_summary.json` | Machine-readable summary statistics |

---

## Usage

### Command Line Interface

```bash
python qc_analysis.py /path/to/data.h5ad \
    --output-dir ./qc_results \
    --mad-counts 5.0 \
    --mad-genes 5.0 \
    --mt-threshold 15.0
```

### Python Library Integration

```python
import anndata as ad
from qc_core import calculate_qc_metrics, detect_outliers_mad, filter_cells

# Load data
adata = ad.read_h5ad("sample.h5ad")

# Calculate QC metrics
calculate_qc_metrics(adata, inplace=True)

# Detect outliers using MAD
outlier_mask = detect_outliers_mad(
    adata,
    mad_counts=5.0,
    mad_genes=5.0,
    mad_mt=3.0,
    mt_threshold=15.0
)

# Filter cells
adata_clean = filter_cells(adata, outlier_mask)
print(f"Retained {adata_clean.n_obs}/{adata.n_obs} cells ({100*adata_clean.n_obs/adata.n_obs:.1f}%)")

# Save results
adata_clean.write("sample_filtered.h5ad")
```

### LLM Agent Integration (LangChain)

```python
from langchain.tools import tool
import anndata as ad
from qc_core import calculate_qc_metrics, detect_outliers_mad, filter_cells

@tool
def run_scrna_qc(
    file_path: str,
    mad_threshold: float = 5.0,
    mt_threshold: float = 15.0
) -> str:
    """
    Performs automated quality control on single-cell RNA-seq data.

    Uses MAD-based adaptive outlier detection following scverse best practices.
    Filters cells based on library size, gene count, and mitochondrial content.

    Args:
        file_path: Path to .h5ad file
        mad_threshold: Number of MADs for outlier detection (default: 5.0)
        mt_threshold: Hard cap for mitochondrial % (default: 15.0)

    Returns:
        Summary string with filtering results and output path
    """
    adata = ad.read_h5ad(file_path)
    initial_cells = adata.n_obs

    calculate_qc_metrics(adata, inplace=True)
    outlier_mask = detect_outliers_mad(
        adata,
        mad_counts=mad_threshold,
        mad_genes=mad_threshold,
        mad_mt=3.0,
        mt_threshold=mt_threshold
    )
    adata_clean = filter_cells(adata, outlier_mask)

    output_path = file_path.replace(".h5ad", "_qc_filtered.h5ad")
    adata_clean.write(output_path)

    removed = initial_cells - adata_clean.n_obs
    pct = 100 * removed / initial_cells

    return f"QC complete. Removed {removed} cells ({pct:.1f}%). Output: {output_path}"
```

---

## Methodology

This implementation follows the best practices established in:

> Luecken, M.D., Theis, F.J. **Current best practices in single-cell RNA-seq analysis: a tutorial.** *Molecular Systems Biology* 15, e8746 (2019). https://doi.org/10.15252/msb.20188746

Key methodological decisions:

1. **MAD over IQR:** MAD is more robust to extreme outliers than interquartile range methods
2. **Asymmetric filtering:** High mitochondrial content is always problematic; low values may be biologically relevant
3. **No doublet detection in QC:** Doublet removal is a separate downstream step (scrublet, DoubletFinder)
4. **Gene filtering deferred:** Minimum gene/cell thresholds applied after cell QC to avoid bias

---

## Dependencies

```
anndata>=0.9.0
scanpy>=1.9.0
scipy>=1.10.0
matplotlib>=3.7.0
seaborn>=0.12.0
numpy>=1.24.0
```

Install with:
```bash
pip install anndata scanpy scipy matplotlib seaborn numpy
```

---

## Validation

This skill has been validated on:

- **10x Genomics PBMC datasets** (3k, 10k cell benchmarks)
- **Human Bone Marrow samples** (GSM3901485-GSM3901487)
- **Tumor microenvironment samples** (high mitochondrial baseline)

Expected retention rates: 85-95% of cells for healthy samples; 70-85% for tumor/stressed samples.

---

## Related Skills

- **CRISPR Design Agent:** For gene knockout experiments on identified marker genes
- **Spatial Transcriptomics:** For tissue-context analysis after cell type annotation
- **Clinical Trial Eligibility:** For patient stratification based on single-cell biomarkers

---

## Author

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu
