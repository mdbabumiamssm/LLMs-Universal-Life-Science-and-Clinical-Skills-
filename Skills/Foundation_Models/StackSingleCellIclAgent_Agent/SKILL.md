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
name: 'stack-single-cell-icl-agent'
description: 'Apply Arc Institute Stack, a single-cell foundation model that performs in-context learning at inference time without per-task fine-tuning.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Stack In-Context Single-Cell Foundation Model Agent

## Overview
This skill operationalizes Arc Institute's Stack, a single-cell foundation model designed for in-context learning (ICL) at inference time. Instead of fine-tuning on each downstream task, the user supplies a small support set of labeled cells and Stack predicts on query cells in a single forward pass. The agent wraps model loading, support/query construction from AnnData, and ICL inference for tasks such as cell-type annotation and perturbation response.

## When to Use This Skill
- The user wants cell-type or state predictions on a new dataset without fine-tuning a foundation model.
- A small labeled reference (support set) is available and should generalize to a larger query set.
- Comparing in-context single-cell modeling against fine-tuned baselines (scGPT, Geneformer, scFoundation).
- Rapid prototyping of label transfer, batch-aware annotation, or zero/few-shot prediction over scRNA-seq data.
- Studying how prompt composition (which cells are placed in context) shapes single-cell predictions.

## Core Capabilities
1. **Pretrained model loading** — Fetch Stack weights and tokenizer/gene vocabulary from the Arc Institute release and instantiate the model in eval mode for inference-only workflows.
2. **AnnData ingestion** — Validate `.h5ad` inputs, align genes to Stack's vocabulary, normalize counts as expected by the model, and split cells into support and query subsets.
3. **In-context prompt construction** — Assemble a context window of labeled support cells together with unlabeled query cells, respecting the model's maximum sequence/cell budget.
4. **ICL inference** — Run a single forward pass per query batch to obtain cell-level predictions or embeddings without gradient updates.
5. **Few-shot annotation** — Map predicted labels back to AnnData `obs`, including confidence scores when produced by the model head.
6. **Embedding export** — Optionally extract per-cell representations for downstream clustering, visualization, or transfer learning.
7. **Reproducibility scaffolding** — Pin model revision, random seeds, and the exact support-set composition used for each run so results can be regenerated.

## Inputs / Outputs

### Inputs
- `query.h5ad` — AnnData of cells to be predicted on (raw or normalized counts as required by Stack).
- `support.h5ad` (or `support_indices` within `query.h5ad`) — Labeled reference cells used as in-context examples; must include a label column in `obs`.
- `label_column` — Name of the `obs` column holding ground-truth labels for the support set.
- `model_revision` — Stack checkpoint identifier (tag or commit) from the Arc Institute repository.
- `n_shots_per_class` — Number of support cells to sample per class for the in-context prompt.
- Optional: `gene_panel` override, `device` (cpu/cuda), `batch_size`, `seed`.

### Outputs
- Annotated `query_predictions.h5ad` with predicted labels (and confidences, if available) written to `obs`.
- `predictions.csv` — Tabular per-cell predictions including the support-set composition used.
- Optional `embeddings.npy` of per-cell Stack representations.
- `run_manifest.json` — Records model revision, seed, support-cell IDs, gene-overlap stats, and runtime, enabling reproduction.

## References
- Source repository: https://github.com/ArcInstitute/stack
- Arc Institute: https://arcinstitute.org
- Related single-cell foundation models for comparison:
  - scGPT — https://github.com/bowang-lab/scGPT
  - Geneformer — https://huggingface.co/ctheodoris/Geneformer
  - scFoundation — https://github.com/biomap-research/scFoundation
- AnnData / scanpy ecosystem — https://github.com/scverse/anndata , https://github.com/scverse/scanpy
