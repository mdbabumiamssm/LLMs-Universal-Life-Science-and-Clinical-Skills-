# Scanpy: Single-Cell Analysis in Python

**Source:** [scverse/scanpy](https://github.com/scverse/scanpy)
**Local Repository:** `./repo`

## Overview
Scanpy is a scalable toolkit for analyzing single-cell gene expression data. It handles preprocessing, visualization, clustering, and differential expression analysis. It is designed to work efficiently with AnnData objects.

## Installation
To install from the local repository:
```bash
cd repo
pip install .
```
Or via PyPI: `pip install scanpy`

## Basic Usage
```python
import scanpy as sc

# Read 10x Genomics data
adata = sc.read_10x_mtx(
    'data/hg19/',
    var_names='gene_symbols',
    cache=True
)

# Preprocessing
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# Analysis
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata)

# Visualization
sc.pl.umap(adata, color=['leiden', 'CST3'])
```

## Tutorials & Examples
We have downloaded the official Scanpy tutorials for you.
- **Location:** `./tutorials/repo`
- **Contents:** Jupyter notebooks covering clustering, trajectory inference, spatial analysis, and integration.
- **How to use:**
  ```bash
  cd tutorials/repo
  jupyter notebook
  ```
