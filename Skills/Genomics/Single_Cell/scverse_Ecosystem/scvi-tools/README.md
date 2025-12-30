# scvi-tools: Deep Probabilistic Analysis

**Source:** [scverse/scvi-tools](https://github.com/scverse/scvi-tools)
**Local Repository:** `./repo`

## Overview
scvi-tools (Single-cell Variational Inference) is a library for deep probabilistic analysis of single-cell omics data. It uses PyTorch to implement generative models for tasks like data integration (batch correction), dimensionality reduction, and differential expression.

## Installation
To install from the local repository:
```bash
cd repo
pip install .
```

## Basic Usage (Data Integration)
```python
import scvi
import scanpy as sc

# Assume 'adata' is your concatenated AnnData object
scvi.model.SCVI.setup_anndata(adata, batch_key="batch")

# Train the model
model = scvi.model.SCVI(adata)
model.train()

# Get latent representation (batch-corrected)
adata.obsm["X_scVI"] = model.get_latent_representation()

# Visualize
sc.pp.neighbors(adata, use_rep="X_scVI")
sc.tl.umap(adata)
sc.pl.umap(adata, color=["batch", "cell_type"])
```

## Tutorials & Examples
We have downloaded the official scvi-tools tutorials for you.
- **Location:** `./tutorials/repo`
- **Contents:** Extensive Jupyter notebooks for CITE-seq, spatial data, harmonization, and differential expression using deep generative models.
- **How to use:**
  ```bash
  cd tutorials/repo
  jupyter notebook
  ```
