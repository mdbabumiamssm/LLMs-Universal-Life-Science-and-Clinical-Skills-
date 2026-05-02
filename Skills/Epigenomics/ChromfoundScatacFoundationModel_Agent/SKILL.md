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
name: 'chromfound-scatac-foundation-model'
description: 'Apply ChromFound, a genome-wide foundation model for single-cell chromatin accessibility (scATAC-seq), to enable cell-type annotation, regulatory element discovery, and cross-tissue transfer.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# ChromFound scATAC Foundation Model Agent

## Overview

This skill operationalizes **ChromFound**, a genome-wide foundation model purpose-built for single-cell chromatin accessibility (scATAC-seq) data. It guides agents through environment setup, loading pretrained ChromFound weights, embedding scATAC cells, and applying the embeddings to downstream epigenomics tasks such as cell-type annotation, regulatory element discovery, and cross-tissue transfer. Use this skill when an analysis demands a chromatin-native foundation model rather than RNA-centric models (e.g., scFoundation, scGPT) or methylation-specific models (e.g., MethylGPT).

## When to Use This Skill

- The user has scATAC-seq data (10x Multiome, sci-ATAC, snATAC, etc.) and wants foundation-model embeddings rather than peak-calling-only pipelines.
- Tasks involve **cell-type annotation** on chromatin accessibility profiles, especially in rare or transitional populations where peak-based clustering is noisy.
- The user wants to perform **cross-tissue or cross-dataset transfer** of chromatin states using a pretrained genome-wide model.
- Discovering or prioritizing **cis-regulatory elements** (CREs), enhancers, or accessibility-defined regulatory programs from learned representations.
- Integrating scATAC with paired modalities (e.g., scRNA-seq from Multiome) where chromatin embeddings are needed as one side of the integration.
- Benchmarking ChromFound against ATAC-only baselines (cisTopic, SCALE, ArchR's LSI, PeakVI) or other foundation models.

## Core Capabilities

1. **Environment & Repository Setup** — Clone the SAIS-LifeScience/ChromFound GitHub repository, install Python dependencies (PyTorch, AnnData, scanpy/snapatac2), and verify pretrained checkpoints are downloaded.
2. **Data Ingestion for scATAC** — Convert fragment files, peak-by-cell matrices, or AnnData (`.h5ad`) objects into the genome-wide tokenization scheme expected by ChromFound; perform QC (TSS enrichment, fragment size distributions, doublet filtering) before embedding.
3. **Cell Embedding Generation** — Run inference with the pretrained ChromFound model to produce per-cell latent embeddings suitable for clustering, UMAP, and downstream classifiers.
4. **Cell-Type Annotation** — Train lightweight heads (k-NN, logistic regression, MLP) on ChromFound embeddings against reference labels, or transfer labels from an annotated reference dataset using embedding similarity.
5. **Regulatory Element Discovery** — Use attention/attribution signals or embedding-space neighborhoods to nominate cell-type-specific cis-regulatory regions and accessibility programs.
6. **Cross-Tissue / Cross-Dataset Transfer** — Apply embeddings learned on one tissue to query datasets from a different tissue, donor, or technology, enabling label transfer and batch integration without per-dataset retraining.
7. **Fine-Tuning Hooks** — Where supported by the upstream repo, fine-tune ChromFound on a user-provided cohort with a task head (classification, regression on accessibility scores, or contrastive integration with paired scRNA).
8. **Comparison & Reporting** — Generate side-by-side metrics versus ATAC-only baselines and emit a concise report with figures (UMAP, confusion matrices, top CREs per cluster).

## Inputs / Outputs

**Inputs**
- scATAC-seq data in one of: 10x fragments (`fragments.tsv.gz` + index), peak-by-cell matrix (`.mtx`/`.h5`), or `AnnData` `.h5ad` with a peaks/bins layer.
- Optional reference annotations (cell-type labels, donor metadata) for supervised heads or transfer.
- Optional paired scRNA-seq from Multiome experiments for joint analysis.
- Genome build identifier (e.g., `hg38`, `mm10`) consistent with ChromFound's pretraining.
- Pretrained ChromFound checkpoint (downloaded from the upstream repo / releases).

**Outputs**
- Per-cell embedding matrix (`cells × d`) saved as `.npy` or in `adata.obsm['X_chromfound']`.
- Cluster assignments and UMAP coordinates derived from ChromFound embeddings.
- Predicted cell-type labels with confidence scores (when annotation head is used).
- Ranked lists of candidate regulatory elements per cluster/cell type.
- Diagnostic figures (UMAPs, label-transfer confusion matrices, accessibility tracks at top CREs).
- A markdown summary report capturing dataset stats, model version, runtime, and key findings.

## References

- ChromFound GitHub repository (source finding): https://github.com/SAIS-LifeScience/ChromFound
- Related foundation models for single-cell omics:
  - scFoundation: https://github.com/biomap-research/scFoundation
  - scGPT: https://github.com/bowang-lab/scGPT
  - Geneformer: https://huggingface.co/ctheodoris/Geneformer
- Standard scATAC tooling that interoperates with ChromFound outputs:
  - ArchR: https://www.archrproject.com/
  - SnapATAC2: https://github.com/kaizhang/SnapATAC2
  - signac: https://stuartlab.org/signac/
- Background on scATAC-seq foundation modeling and CRE discovery (PubMed search): https://pubmed.ncbi.nlm.nih.gov/?term=single-cell+ATAC+foundation+model
