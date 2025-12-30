# Seurat Wrappers: Community Extensions

**Source:** [satijalab/seurat-wrappers](https://github.com/satijalab/seurat-wrappers)
**Local Repository:** `./repo`

## Overview
Seurat Wrappers is a collection of wrapper functions that allow you to run external community tools (like Monocle, Velocyto, LIGER, Harmony) directly on Seurat objects.

## Examples
- **Monocle3:** Trajectory inference.
- **Harmony:** Batch correction.
- **LIGER:** NMF-based integration.

## Usage Example (Harmony)
```r
library(Seurat)
library(SeuratWrappers)
library(harmony)

# Run Harmony integration via wrapper
pbmc <- RunHarmony(pbmc, group.by.vars = "batch")
```
