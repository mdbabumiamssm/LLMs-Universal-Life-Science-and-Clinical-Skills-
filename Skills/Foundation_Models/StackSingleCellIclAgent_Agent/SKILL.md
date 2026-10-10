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
8. **Stack-vs-embedding workflow selection** — Prefer Stack when the task can be expressed as labeled support cells plus unlabeled query cells and the user needs inference-time adaptation without task fine-tuning; keep scGPT/Geneformer-style embedding workflows when the goal is reusable latent representations, clustering, or a downstream model trained outside the ICL prompt. For benchmark checks, evaluate only against user-provided held-out labels or explicitly named project baselines, and record the query/support split, label column, and model revision with the reported outputs.
9. **Stack-specific ICL inference design** — Use Stack as an inference-time in-context learner when a representative labeled reference can guide unlabeled query-cell prediction, avoiding per-task fine-tuning unless the task cannot be expressed through support/query examples. Format inputs as AnnData support and query cells with genes aligned to Stack's expected vocabulary, labels present only for support/reference cells, and stable cell IDs retained for auditing. Build reference-query contexts that cover expected cell types, states, batches, and perturbation conditions without leaking query labels, then validate predictions against conventional annotation workflows such as marker-gene review, clustering, and user-provided reference label transfer before treating outputs as final annotations.
10. **Repository-guided Stack workflow** — Follow the ArcInstitute/stack repository's current examples for data formatting and task-prompt construction, using labeled support examples and unlabeled queries for inference-time ICL without task-specific fine-tuning. Treat cell annotation, label transfer, and perturbation-response prediction as candidate no-fine-tuning use cases only when they can be represented by the repository-supported prompt format. Do not assume benchmark gains or fixed metrics: report results on held-out data using task-appropriate metrics and compare them with conventional annotation or perturbation baselines supplied by the project, while recording the Stack revision, prompt composition, data split, and preprocessing needed to reproduce the comparison.
11. **Repository-grounded no-fine-tuning Stack notes** — Ground Stack use in the ArcInstitute/stack README and notebooks: install `arc-stack`, extract reusable single-cell embeddings with `stack-embedding`, and run in-context generation with `stack-generation` over base/reference AnnData, test/query AnnData, a gene list, and a split column. Construct contexts from reference/base cells that represent the biological conditions the query cells should be predicted in, keep query labels out of the prompt, and use no-fine-tuning ICL only for workflows the repository examples support, including embedding extraction and zero-shot prediction or generation of unseen perturbation/observation profiles. Validate Stack outputs against conventional annotation, label-transfer, perturbation, or embedding baselines that the project explicitly supplies, and report those comparisons without inventing benchmark claims.
12. **GitHub source finding integration** — Treat Stack as a single-cell foundation model for inference-time ICL: format each task as labeled reference/support cells plus unlabeled query cells, keep query labels out of the context, and use this no-fine-tuning workflow when the desired prediction can be expressed through reference-query examples. Prefer Stack over task-specific single-cell models when inference-time adaptation from a compact labeled reference is the main requirement; prefer task-specific models when the project requires retraining, a fixed supervised task head, or an evaluation not representable as a reference/query prompt. For benchmarks, make no claims from repository metadata alone; require held-out labels, explicit comparison baselines, and recorded Stack revision, split, prompt composition, and preprocessing details.
13. **Atlas-transfer ICL validation** — Select representative context cells that span the expected cell types, tissues, batches, and states before running Stack inference without per-task fine-tuning. Validate atlas-transfer behavior on held-out query labels or trusted reference annotations, benchmark only against explicitly configured fine-tuned single-cell foundation-model baselines, and document observed failure modes for batch effects, tissue shift, or unsupported context composition.
14. **Prediction-time Stack repository workflow** — Use ArcInstitute/stack for in-context single-cell inference when the task can be expressed with repository-style AnnData inputs: a base/reference `.h5ad`, a test/query `.h5ad`, a gene list, and a split or label column that separates support context from held-out prediction targets. For embedding workflows, run Stack embeddings as reusable cell representations and evaluate them with the project's clustering, label-transfer, or annotation baselines; for annotation workflows, write predictions back to query `obs` and compare only against held-out labels or explicitly supplied conventional baselines. Avoid fine-tuning when prediction-time adaptation from labeled context cells is sufficient, and reserve training or frozen-teacher fine-tuning for cases where the repository-supported ICL or embedding commands cannot represent the requested prediction.
15. **Current Stack repository ICL usage** — Set up Stack from the current ArcInstitute/stack repository or PyPI package (`arc-stack`), pin the checkpoint and code revision, and follow the repository notebooks or CLI patterns before adapting them. Format inputs as AnnData base/reference and test/query files plus the required gene list and split or label column; construct the task prompt by placing only labeled support/context cells in the reference side and withholding query labels during inference-time ICL. Prefer this repository-supported no-fine-tuning path for annotation, label-transfer, embedding, or perturbation-profile tasks that fit the support/query prompt format, and use frozen-teacher fine-tuning or other supervised workflows only when the task cannot be represented that way. Validate outputs against held-out annotation labels or project-provided perturbation benchmarks and report only observed metrics, baselines, preprocessing, prompt composition, and revision details.
16. **Arc Institute Stack implementation reference** — Use the ArcInstitute/stack GitHub repository as the implementation reference for single-cell ICL at inference time: take setup commands, checkpoints, and example notebook or CLI patterns from the repository; construct prompt/reference contexts from labeled support cells and held-out query cells without leaking query labels; run repository-supported embedding and annotation workflows; compare the no-fine-tuning Stack path only against explicitly configured fine-tuned or conventional approaches; and validate on held-out cell states with recorded Stack revision, preprocessing, gene alignment, context composition, split, baseline, and observed metrics.
17. **Inference-time Stack usage pattern** — Frame Stack tasks as no-fine-tuning single-cell ICL runs: package labeled reference/support cells and unlabeled query cells in AnnData-compatible inputs, align genes and metadata needed to rebuild the support/query split, and run inference without treating repository metadata as benchmark evidence. Validate predicted annotations or states against held-out labels and conventional annotation baselines such as project-provided marker review, clustering, or label-transfer workflows before accepting Stack outputs.
18. **ArcInstitute/stack repository handling** — Install and run Stack from the ArcInstitute/stack repository instructions or pinned package artifacts, record the commit, checkpoint, device, and runtime settings, and keep inference workflows free of task fine-tuning when the task can be expressed as in-context labeled support cells plus unlabeled query cells. Require repository-compatible single-cell input formatting, including aligned gene features, retained cell IDs, support labels only in the reference context, and query labels withheld until evaluation. For benchmark prompts, store the exact support/query examples, split column, label column, preprocessing, and comparison baseline supplied by the project without inventing metrics. Export Stack embeddings when the workflow calls for reusable cell representations, and flag out-of-distribution or weakly represented cell states as potential failure modes that need additional support coverage or separate validation before interpretation.
19. **Inference-time ICL task adaptation** — Adapt Stack to new annotation or perturbation-response tasks by formatting repository-compatible AnnData inputs with aligned genes, retained cell IDs, labeled exemplar/support cells, unlabeled query cells, and metadata needed to recreate the split. Select exemplars that represent the expected cell types, states, batches, and perturbation conditions while keeping query labels out of the context. Use this no-finetune path when reference-query examples express the task, evaluate outputs only against held-out annotation labels or project-supplied perturbation baselines, and state limits versus fine-tuned single-cell models when the task needs retraining, a fixed supervised head, or support coverage beyond the available exemplars.
20. **Arc Institute Stack ICL case** — Treat Arc Institute Stack as the single-cell foundation model case for in-context learning at inference time: format inputs as Stack-compatible single-cell data with labeled exemplars/support cells, unlabeled query cells, aligned gene features, retained cell IDs, and metadata needed to rebuild the split. Choose exemplars that cover the expected annotations, perturbation conditions, batches, and cell states without exposing query labels, then frame annotation or perturbation-response tasks as reference-query prompts instead of fine-tuning. Evaluate outputs only against held-out annotation labels, conventional annotation baselines, or project-supplied perturbation baselines, and explicitly flag out-of-distribution or poorly represented cell states as failure modes requiring separate validation.

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
- ArcInstitute/stack GitHub repository: https://github.com/ArcInstitute/stack
- Arc Institute: https://arcinstitute.org
- Related single-cell foundation models for comparison:
  - scGPT — https://github.com/bowang-lab/scGPT
  - Geneformer — https://huggingface.co/ctheodoris/Geneformer
  - scFoundation — https://github.com/biomap-research/scFoundation
- AnnData / scanpy ecosystem — https://github.com/scverse/anndata , https://github.com/scverse/scanpy
- Source finding: https://github.com/ArcInstitute/stack
- GitHub source finding (2026-04-28): https://github.com/ArcInstitute/stack
- ArcInstitute/stack repository source finding: https://github.com/ArcInstitute/stack
- Stack repository usage source: https://github.com/ArcInstitute/stack
- Source finding (GitHub, ArcInstitute/stack, published 2026-04-28): https://github.com/ArcInstitute/stack
- Source finding title `stack` (GitHub, published 2026-04-28): https://github.com/ArcInstitute/stack
- ArcInstitute/stack source finding: https://github.com/ArcInstitute/stack
- GitHub source finding id `ArcInstitute/stack`: https://github.com/ArcInstitute/stack
- Source finding (GitHub, ArcInstitute/stack, 126 stars, published 2026-04-28): https://github.com/ArcInstitute/stack
