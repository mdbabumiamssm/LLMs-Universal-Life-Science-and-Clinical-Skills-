# Test & Demonstration Suite

**Purpose:** Validation and demonstration of Universal Biomedical Skills

---

## Overview

This directory contains the validation suite for testing biomedical AI skills. It demonstrates end-to-end workflows using real-world data formats and validates that skill outputs meet quality standards.

The primary demonstration showcases the **Single-Cell RNA-seq Quality Control Skill** using human bone marrow samples from GEO (GSM3901485-GSM3901487).

---

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Demonstration

```bash
# Run QC on sample data
python qc_analysis.py scRNAsedata/GSM3901485_BM1 --output-dir qc_results_demo

# View results
ls qc_results_demo/
```

### 3. Expected Outputs

```
qc_results_demo/
├── GSM3901485_BM1_filtered.h5ad    # Clean dataset
├── GSM3901485_BM1_with_qc.h5ad     # Original with QC annotations
├── qc_metrics_before.png            # Pre-filtering distributions
├── qc_filtering_thresholds.png      # Applied cutoff visualization
├── qc_metrics_after.png             # Post-filtering distributions
└── qc_summary.json                  # Machine-readable summary
```

---

## Components

### Core Pipeline

| File | Description | Entry Point |
|------|-------------|-------------|
| `qc_analysis.py` | Main CLI wrapper | `python qc_analysis.py <input>` |
| `qc_core.py` | QC metric calculation and filtering logic | Library import |
| `qc_plotting.py` | Visualization generation | Library import |

### Utilities

| File | Description |
|------|-------------|
| `generate_dummy_data.py` | Creates synthetic scRNA-seq data for testing |
| `integration_analysis.py` | Downstream analysis demonstration (clustering, UMAP) |

### Data

| Directory | Contents |
|-----------|----------|
| `scRNAsedata/` | Sample 10x Genomics datasets (bone marrow) |
| `qc_results/` | Output from validation runs |
| `analyzed_data/` | Downstream analysis outputs |

---

## Validation Protocol

### 1. Data Ingestion Test

Verify support for multiple input formats:

```bash
# H5AD format
python qc_analysis.py sample.h5ad

# 10x Genomics directory (contains matrix.mtx, genes.tsv, barcodes.tsv)
python qc_analysis.py scRNAsedata/GSM3901485_BM1/

# H5 format (10x v3)
python qc_analysis.py sample.h5
```

### 2. QC Metric Accuracy

Compare calculated metrics against known values:

```python
import anndata as ad
from qc_core import calculate_qc_metrics

adata = ad.read_h5ad("test_data.h5ad")
calculate_qc_metrics(adata, inplace=True)

# Verify metrics exist
assert "n_counts" in adata.obs.columns
assert "n_genes" in adata.obs.columns
assert "pct_mito" in adata.obs.columns
```

### 3. Filtering Validation

Ensure MAD-based filtering produces expected retention rates:

```python
# Expected: 85-95% retention for healthy samples
initial_cells = adata.n_obs
adata_filtered = filter_cells(adata, mad_threshold=5.0)
retention_rate = adata_filtered.n_obs / initial_cells

assert 0.70 <= retention_rate <= 0.98, f"Unexpected retention: {retention_rate}"
```

### 4. Downstream Compatibility

Verify filtered data works with standard pipelines:

```python
import scanpy as sc

# Normalize and cluster
sc.pp.normalize_total(adata_filtered, target_sum=1e4)
sc.pp.log1p(adata_filtered)
sc.pp.highly_variable_genes(adata_filtered)
sc.pp.pca(adata_filtered)
sc.pp.neighbors(adata_filtered)
sc.tl.umap(adata_filtered)
sc.tl.leiden(adata_filtered)

# Should complete without errors
sc.pl.umap(adata_filtered, color="leiden", save="_test.png")
```

---

## Sample Data

### Human Bone Marrow (GEO)

| Sample | GEO ID | Cells | Description |
|--------|--------|-------|-------------|
| BM1 | GSM3901485 | ~10k | Healthy donor 1 |
| BM2 | GSM3901486 | ~10k | Healthy donor 2 |
| BM3 | GSM3901487 | ~10k | Healthy donor 3 |

### Generating Test Data

For quick testing without downloading real data:

```bash
python generate_dummy_data.py --n-cells 5000 --n-genes 20000 --output test_data.h5ad
```

---

## Benchmarks

### Performance (10k cells, 20k genes)

| Operation | Time | Memory |
|-----------|------|--------|
| Load data | ~2s | 500MB |
| Calculate metrics | ~5s | +200MB |
| Filter cells | ~1s | - |
| Generate plots | ~10s | +100MB |
| **Total** | ~18s | ~800MB |

### Quality Metrics

| Dataset | Initial Cells | After QC | Retention |
|---------|---------------|----------|-----------|
| BM1 | 10,234 | 9,156 | 89.5% |
| BM2 | 9,876 | 8,734 | 88.4% |
| BM3 | 10,521 | 9,423 | 89.6% |

---

## Troubleshooting

### Common Issues

**Import Error: No module named 'scanpy'**
```bash
pip install scanpy
```

**Memory Error with large datasets**
```python
# Use backed mode for large files
adata = ad.read_h5ad("large_file.h5ad", backed="r")
```

**Invalid H5AD file**
```bash
# Verify file integrity
python -c "import anndata; print(anndata.read_h5ad('file.h5ad'))"
```

---

## Contributing

To add new validation tests:

1. Create test script in `tests/` directory
2. Add sample data to `test_data/` (or use `generate_dummy_data.py`)
3. Document expected outputs
4. Update this README

---

## Author

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu
