# CellAgent (CellTypeAgent)

**Source:** [jianghao-zhang/CellTypeAgent](https://github.com/jianghao-zhang/CellTypeAgent)
**Local Repository:** `./repo`
**Status:** Integrated & Downloaded

## Overview
CellTypeAgent is an LLM-driven multi-agent framework specifically designed for the automated annotation of cell types in single-cell RNA-seq (scRNA-seq) data. It addresses the "annotation bottleneck" by automating the interpretation of marker genes.

## Key Features
- **Automated Annotation:** Uses LLMs to assign cell types based on marker gene lists.
- **Trustworthiness:** Designed to minimize hallucinations common in generic LLM queries.
- **Benchmarks:** Evaluated on multiple standard scRNA-seq datasets.

## Quick Start
1.  **Installation:**
    ```bash
    cd repo
    pip install -r requirements.txt
    ```
2.  **Usage:**
    Examine the `repo` directory for the main execution scripts (likely `main.py` or similar in `repo/src` or root).
    ```bash
    python repo/main.py --data your_data.h5ad
    ```

## Note on "CellAgent" Naming
This repository is `CellTypeAgent`. The broader "CellAgent" framework discussed in some literature may refer to a larger system, but `CellTypeAgent` provides the core cell type annotation capability which is the most critical agentic task in this domain.