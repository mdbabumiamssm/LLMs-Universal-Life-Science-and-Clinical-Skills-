<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'scprint2-foundation-model-agent'
description: 'Agentic skill for using scPRINT-2, the next-generation single-cell foundation model from the Cantini Lab, for cell-type annotation, embedding, and downstream single-cell analysis.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# scPRINT-2 Single-Cell Foundation Model Agent

## Overview

This skill operationalizes scPRINT-2, a next-generation single-cell foundation model developed by the Cantini Lab, as an agentic workflow for single-cell RNA-seq analysis. It guides loading pretrained scPRINT-2 weights, preparing AnnData inputs, and producing cell embeddings, annotations, and gene network outputs for downstream interpretation. The skill is intended for researchers who want to apply a modern transformer-based single-cell foundation model to their own datasets without writing the orchestration boilerplate from scratch.

## When to Use This Skill

- The user wants to embed, annotate, or denoise a single-cell RNA-seq dataset using a foundation model.
- The user explicitly mentions scPRINT, scPRINT-2, or the Cantini Lab single-cell model.
- The user is comparing single-cell foundation models (e.g., scGPT, Geneformer, scFoundation) and needs an scPRINT-2 baseline.
- The user wants gene-gene network inference or cell-type annotation transferred from a pretrained model.
- The user needs to fine-tune or run inference on an AnnData / `.h5ad` object with a transformer-based scRNA-seq model.

## Core Capabilities

1. **Environment setup** — Install the `scprint` package and PyTorch dependencies, verify CUDA availability, and download the appropriate pretrained checkpoint from the official release.
2. **Data preparation** — Load an `.h5ad` AnnData object, validate gene symbols against the model's gene vocabulary, and harmonize raw counts to the format scPRINT-2 expects.
3. **Cell embedding** — Run inference to produce per-cell latent embeddings suitable for clustering, integration, and visualization (UMAP/t-SNE).
4. **Cell-type annotation** — Use the model's classification head to assign cell-type labels and confidence scores, with optional reference-based label transfer.
5. **Gene network inference** — Extract attention-derived gene-gene interaction scores for biological interpretation and pathway analysis.
6. **Fine-tuning** — Optionally fine-tune the model on a user-provided labeled dataset for task-specific adaptation.
7. **Benchmarking and comparison** — Produce side-by-side metrics versus other foundation models when a comparison is requested.

## Inputs / Outputs

**Inputs**
- An AnnData `.h5ad` file containing raw scRNA-seq counts with gene symbols in `adata.var_names`.
- Optional: a reference dataset for label transfer or a labeled subset for fine-tuning.
- Optional: configuration parameters (batch size, precision, target task, checkpoint name).

**Outputs**
- AnnData object enriched with `obsm["X_scprint2"]` cell embeddings.
- `obs` columns containing predicted cell-type labels and per-cell confidence scores.
- Optional gene-gene interaction matrix (when network inference is requested).
- Run summary (model version, checkpoint, runtime, GPU usage, key QC metrics).

## References

- Source repository: https://github.com/cantinilab/scPRINT-2
- Original scPRINT method (Cantini Lab): https://github.com/cantinilab/scPRINT
- AnnData / scanpy ecosystem: https://github.com/scverse/scanpy
- PyTorch: https://github.com/pytorch/pytorch
