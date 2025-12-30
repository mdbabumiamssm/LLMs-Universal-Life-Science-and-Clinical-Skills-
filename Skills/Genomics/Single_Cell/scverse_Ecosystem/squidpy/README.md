# Squidpy: Spatial Omics Analysis

**Source:** [scverse/squidpy](https://github.com/scverse/squidpy)
**Local Repository:** `./repo`

## Overview
Squidpy brings spatial data analysis to the scverse ecosystem. It integrates with Scanpy and AnnData to analyze spatial transcriptomics data (Visium, Slide-seq, MERFISH) and tissue images.

## Key Capabilities
- **Graph Analysis:** Spatial neighbors, centrality, interaction analysis.
- **Image Analysis:** Image segmentation, feature extraction.
- **Interactive Plotting:** Visualizing gene expression on tissue coordinates.

## Basic Usage
```python
import squidpy as sq

# Load a built-in Visium dataset
adata = sq.datasets.visium_fluo_image_crop()

# Calculate spatial neighbors
sq.gr.spatial_neighbors(adata)

# Calculate spatial autocorrelation (Moran's I)
sq.gr.spatial_autocorr(
    adata,
    mode="moran",
    genes=adata.var_names[:10]
)

# Plot
sq.pl.spatial_scatter(adata, color="cluster")
```

## Tutorials & Examples
We have downloaded the official Squidpy notebooks for you.
- **Location:** `./tutorials/repo`
- **Contents:** Notebooks demonstrating spatial graph analysis, image container usage, and interactive visualization.
- **How to use:**
  ```bash
  cd tutorials/repo
  jupyter notebook
  ```
