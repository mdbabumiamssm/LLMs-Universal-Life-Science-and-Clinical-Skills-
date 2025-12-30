# Azimuth: Reference Mapping

**Source:** [satijalab/azimuth](https://github.com/satijalab/azimuth)
**Local Repository:** `./repo`

## Overview
Azimuth is a Seurat-based tool for mapping query datasets to high-quality reference atlases. It automates annotation by projecting your data onto a pre-computed reference, transferring cell type labels and embeddings.

## Key Features
- **Fast Mapping:** Uses PCA projection for speed.
- **Reference Atlases:** Access to Human PBMC, Cortex, Lung, etc.
- **Web App:** Can be run as a Shiny app or via R command line.

## Basic Usage (R)
```r
library(Seurat)
library(Azimuth)

# Run Azimuth on a query dataset using a built-in reference
pbmc.query <- RunAzimuth(pbmc.query, reference = "pbmcref")
```
