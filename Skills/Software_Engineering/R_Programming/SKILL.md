# R Programming for Biomedical Science

## Overview
R is a premier language for statistical computing and graphics, serving as the backbone for much of modern bioinformatics, particularly through the Bioconductor project. Mastery of R is essential for genomic data analysis, rigorous statistical testing, and publication-quality visualization.

## Core Competencies

### 1. Base R & Functional Programming
- **Data Structures:** Vectors, Lists, Data Frames, Matrices, Factors.
- **Control Flow:** Apply family (`lapply`, `sapply`, `tapply`) vs. loops.
- **S3/S4 Classes:** Understanding R's object-oriented systems, critical for Bioconductor packages.

### 2. Tidyverse (Modern Data Science)
- **dplyr:** Data manipulation (filter, select, mutate, group_by, summarize).
- **tidyr:** Tidy data principles (pivot_longer, pivot_wider).
- **readr:** Efficient data import.
- **purrr:** Functional programming tools.
- **magrittr:** Pipe operators (`%>%`, `|>`).

### 3. Data Visualization
- **ggplot2:** Grammar of graphics, layering, themes, and scales.
- **ComplexHeatmap:** Advanced heatmaps for omics data.
- **Patchwork/Cowplot:** Composing multi-panel figures.

### 4. Bioconductor Ecosystem
- **Core Classes:** `SummarizedExperiment`, `SingleCellExperiment`, `GRanges`.
- **Package Management:** `BiocManager`.
- **Workflow:** Integration with downstream tools (DESeq2, edgeR, limma).

### 5. Statistics
- **Hypothesis Testing:** t-tests, ANOVA, linear models (`lm`, `glm`).
- **Dimensionality Reduction:** PCA, t-SNE, UMAP.
- **Correction:** False Discovery Rate (FDR), Benjamini-Hochberg.

### 6. Package Development
- **Structure:** DESCRIPTION, NAMESPACE, R/ directory.
- **Documentation:** roxygen2.
- **Testing:** testthat.
- **Check:** `R CMD check` compliance.

## Learning Path
1.  **Novice:** Master `dplyr` verbs and `ggplot2` basics. Understand factors.
2.  **Intermediate:** Learn to use `Bioconductor` classes (`SummarizedExperiment`). Perform differential expression analysis.
3.  **Advanced:** Build reusable R packages. Optimize code with `Rcpp`. Create interactive Shiny apps.

## Key Resources
- [R for Data Science (2e)](https://r4ds.hadley.nz/)
- [Bioconductor](https://www.bioconductor.org/)
- [Advanced R (Hadley Wickham)](https://adv-r.hadley.nz/)
