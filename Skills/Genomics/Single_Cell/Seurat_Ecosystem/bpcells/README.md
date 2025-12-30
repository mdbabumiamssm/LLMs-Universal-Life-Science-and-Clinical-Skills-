# BPCells: High-Performance Single Cell Analysis

**Source:** [bnprks/BPCells](https://github.com/bnprks/BPCells)
**Local Repository:** `./repo`

## Overview
BPCells is an R package for high-performance single-cell analysis. It utilizes bit-packed compression and disk-backed storage to analyze millions of cells with minimal memory usage. It is a core dependency for the scalability features in Seurat v5.

## Key Features
- **Bit-packing:** Ultra-efficient storage of count matrices.
- **Disk-backed:** Analysis does not require loading everything into RAM.
- **Speed:** C++ backend for rapid computation.

## Basic Usage (R)
```r
library(BPCells)
library(Seurat)

# Write a matrix to BPCells format on disk
write_matrix_dir(mat = raw_counts, dir = "counts_bpcells")

# Load it back (instant)
mat <- open_matrix_dir(dir = "counts_bpcells")

# Create a Seurat object
obj <- CreateSeuratObject(counts = mat)
```
