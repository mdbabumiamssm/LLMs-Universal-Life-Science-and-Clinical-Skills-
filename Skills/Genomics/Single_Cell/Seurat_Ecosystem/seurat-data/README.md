# Seurat Data: Dataset Manager

**Source:** [satijalab/seurat-data](https://github.com/satijalab/seurat-data)
**Local Repository:** `./repo`

## Overview
SeuratData provides a mechanism to easily install and load datasets for testing and demonstration purposes in Seurat.

## Usage
```r
library(SeuratData)

# Install a dataset
InstallData("pbmc3k")

# Load it
data("pbmc3k")
pbmc3k
```
