# BioMaster: Automated Bioinformatics Workflows

**Source:** [ai4nucleome/BioMaster](https://github.com/ai4nucleome/BioMaster)
**Local Repository:** `./repo`
**Status:** Integrated & Downloaded

## Overview
BioMaster is a multi-agent system designed to handle complex, multi-step bioinformatics workflows. Unlike single-task agents, BioMaster specializes in end-to-end pipeline management for various omics data types.

## Supported Workflows
1.  **RNA-seq:** QC -> Alignment -> Quantification -> DEG -> Enrichment.
2.  **ChIP-seq:** Peak calling -> Motif analysis.
3.  **Single-Cell:** Standard Scanpy workflow.
4.  **Hi-C:** Chromatin interaction map generation.

## Key Components
- **Domain Knowledge RAG:** Retrieves tool manuals and best practices to ensure correct parameter usage.
- **Task Decomposition:** Breaks down "Analyze this FASTQ file" into shell commands and scripts.
- **Error Recovery:** Autonomously parses stderr logs to fix common bioinformatics errors.

## Quick Start
1.  **Installation:**
    ```bash
    cd repo
    pip install -r requirements.txt
    ```
2.  **Execution:**
    The main entry point is `run.py`.
    ```bash
    python repo/run.py --config repo/config.yaml
    ```
3.  **Configuration:**
    Check `repo/config.yaml` to define your tool paths (samtools, star, etc.) and API keys.

## Configuration Details
BioMaster requires a `tools_registry.json` defining the available CLI tools in the environment. The `repo/data` folder may contain example datasets for testing.