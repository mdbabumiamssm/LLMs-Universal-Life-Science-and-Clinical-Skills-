# edgePython

## Overview
This directory contains a Python implementation of differential gene expression analysis methods, porting functionality traditionally found in the R package `edgeR`.

## Source
- **Origin:** Local import from `edgePython-main`.
- **Purpose:** To provide Python-native workflows for RNA-seq analysis, enabling integration with other Python-based machine learning and data science tools.

## Key Components
- **`edgepython/`**: Core library code.
    - `dgelist.py`: Data structure for gene expression counts.
    - `exact_test.py`: Exact tests for differences between two groups of negative-binomial counts.
    - `glm_fit.py`: Genewise Negative Binomial Generalized Linear Models.
- **`examples/`**: Jupyter notebooks demonstrating usage (e.g., `hoxa1_tutorial.ipynb`).
- **`tests/`**: Unit tests comparing Python results against R benchmarks.

## Integration Status
This codebase has been integrated into the Universal Biomedical Skills platform to support:
1.  Python-based transcriptomics pipelines.
2.  Benchmarking between R and Python implementations of edgeR.
3.  Development of hybrid AI/Statistical workflows.