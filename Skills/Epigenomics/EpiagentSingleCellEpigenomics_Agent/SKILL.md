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
name: 'epiagent-single-cell-epigenomics'
description: 'Prepare human scATAC-seq data for EpiAgent and run documented embedding, annotation, imputation, integration, or adaptation workflows with reproducibility checks.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# EpiAgent Single-Cell Epigenomics

## Overview

Use EpiAgent to represent human single-cell chromatin accessibility as ordered cCRE token sequences and derive cell embeddings or task-specific predictions. This skill connects the repository's preprocessing and inference examples with checks that prevent mismatched genome coordinates, feature vocabularies, and model resources from silently corrupting results.

## When to Use This Skill

- Convert human scATAC-seq fragments into EpiAgent-compatible AnnData and cell sentences.
- Extract pretrained cell embeddings or adapt EpiAgent to a specified dataset.
- Annotate cells using the supplied annotation models or supervised fine-tuning.
- Follow the documented imputation, reference integration, query mapping, perturbation prediction, or in-silico cCRE knockout examples.
- Check whether an existing EpiAgent analysis uses compatible inputs and reproducible resources.

## Core Capabilities

1. **Validate assay and resource compatibility.** Establish genome build, fragment layout, cell identifiers, cCRE order, checkpoint, and intended task before computation. The documented workflow targets human scATAC-seq; do not assume direct support for methylation, histone-mark assays, RNA expression, or nonhuman data.
2. **Prepare model inputs.** Convert hg19 fragments to hg38 when necessary, intersect fragments with the supplied cCRE BED, construct a sparse cell-by-cCRE AnnData object, and apply repository global TF-IDF and tokenization.
3. **Run pretrained inference.** Use the base checkpoint for cell embeddings. Select EpiAgent-B for brain annotation or EpiAgent-NT for other tissues, retaining the corresponding model's label mapping and preprocessing.
4. **Adapt models for documented tasks.** Route to the matching notebook for feature extraction, supervised annotation, imputation, reference integration/query mapping, perturbation prediction, or cCRE knockout. Obtain the labels, reference data, condition information, and external embeddings required by that notebook rather than treating every task as zero-shot inference.
5. **Verify outputs and provenance.** Check cell alignment, numerical validity, checkpoint compatibility, and repeatability; record data and resource hashes alongside execution settings. Treat biological predictions as task-dependent research outputs rather than validated causal or clinical conclusions.

### Workflow

**1. Establish scope and execution readiness.**

Choose one task and read its notebook from the [repository demo directory](https://github.com/xy-chen16/EpiAgent/tree/main/demo). Record the repository commit and installed package version; do not assume a PyPI installation exactly matches the current GitHub branch.

The documented environment uses Python 3.11, PyTorch 2.0.1, CUDA 11.7, and FlashAttention 2.5.8; installation is via `pip install epiagent`. Check the actual GPU, CUDA, compiler, and FlashAttention compatibility before following those historical version pins. A notebook's CPU device fallback alone does not establish that its FlashAttention configuration works on CPU.

For the 15-minute outcome, use a small fixed subset of already prepared cells with dependencies and checkpoints available locally. Time a single inference pass and save a validated output. Installation, large downloads, full fragment processing, fine-tuning, and paper reproduction are separate workloads with no documented 15-minute guarantee; report incomplete prerequisites instead of claiming successful execution.

**2. Acquire matching models and resources.**

The README links [model weights and example data on Google Drive](https://drive.google.com/drive/folders/1WlNykSCNtZGsUp2oG0dw3cDdVKYDR-iX?usp=sharing). The embedding demo expects `model/pretrained_EpiAgent.pth`; annotation requires the corresponding EpiAgent-B or EpiAgent-NT model and its label mapping. Obtain `data/cCRE.bed` and `data/cCRE_document_frequency.npy` from the compatible repository resources. Record download URLs and SHA-256 hashes; if access fails, report the unavailable resource without substituting unrelated weights.

The repository software has an [MIT license](https://github.com/xy-chen16/EpiAgent/blob/main/LICENSE). Preserve its required notice when redistributing upstream software. The reviewed README does not establish separate licensing terms for every externally hosted checkpoint or dataset; inspect their accompanying terms before redistribution. The copyright header of this skill does not change upstream ownership or licensing.

**3. Construct and check inputs.**

Follow [Data Preprocessing.ipynb](https://github.com/xy-chen16/EpiAgent/blob/main/demo/Data%20Preprocessing.ipynb):

- Confirm hg38 coordinates and chromosome naming. For hg19, use the appropriate liftOver chain and record unmapped fragments and retained barcodes.
- Compute overlaps with `bedtools intersect -a fragments.bed -b cCRE.bed -wa -wb`. The constructor expects fragment chromosome/start/end/barcode, optionally a count, followed by cCRE coordinates; inspect the actual layout before parsing.
- Call `construct_cell_by_ccre_matrix(intersect_file, ccre_bed_path)` from `epiagent.preprocessing`. Join metadata by unique sample-qualified barcodes, not row position. Report cells absent from overlap output and missing metadata.
- Preserve raw counts separately. Existing `.h5ad` inputs are acceptable only after confirming their columns match the supplied cCRE vocabulary exactly in both identity and order; arbitrary peak matrices are not interchangeable.
- Check nonnegative finite counts, nonempty cells, and a positive finite document-frequency vector of matching length before TF-IDF. Keep matrices sparse.
- Call `global_TFIDF(adata, cCRE_document_frequency)`, then `epiagent.tokenization.tokenization(adata)`. Verify `adata.obs['cell_sentences']` exists and use the repository tokenizer/dataset logic for token IDs, special tokens, and sequence limits.

**4. Execute the selected analysis.**

For the minimal embedding workflow, follow [Zero-shot Feature Extraction using EpiAgent.ipynb](https://github.com/xy-chen16/EpiAgent/blob/main/demo/Zero-shot%20Feature%20Extraction%20using%20EpiAgent.ipynb):

- Build `CellDataset` from the cell sentences and a `DataLoader` using `collate_fn` from `epiagent.dataset`. Keep `shuffle=False` so output rows remain aligned with cells; reduce batch size if GPU memory is insufficient.
- Instantiate `epiagent.model.EpiAgent` with the checkpoint's architecture. The supplied demo uses vocabulary size 1,355,449, 18 layers, embedding dimension 512, 8 attention heads, and 8,192 rank embeddings. Do not silently discard incompatible state-dictionary keys.
- Load the trusted checkpoint and call `epiagent.inference.infer_cell_embeddings(model, device, dataloader)`. Ensure evaluation mode and disabled gradients for inference.
- Store returned embeddings in `adata.obsm['cell_embeddings_zero_shot']` and save the resulting `.h5ad`. Optional neighbors/UMAP visualization is exploratory and is not an accuracy test.

For other tasks, use the corresponding demo's architecture, loss, data split, and inference routine. EpiAgent-B and EpiAgent-NT are supervised annotation models applied directly to new data; their zero-shot application does not imply recognition of arbitrary unseen label categories. Perturbation and knockout workflows require their task-specific setup, and predicted changes are hypotheses rather than experimental validation.

For imputation, use the corrected `cCRE_frequency.npy` resource: the README's 2026-05-28 update reports a scale correction affecting imputation. Record its hash and version, and do not confuse this file with `cCRE_document_frequency.npy` used for global TF-IDF.

**5. Validate and report.**

- Require one finite embedding row per retained cell; for the supplied base model, confirm 512 embedding columns. For annotation, verify prediction count and label-map coverage. For imputation, verify both cell and cCRE axes and the output scale defined by the selected notebook.
- Save the ordered cell IDs, feature-resource hashes, checkpoint hash, repository commit, dependency versions, device, random seeds, batch size, and any sequence truncation or filtering settings.
- Repeat a small fixed inference batch in evaluation mode and compare with a stated numerical tolerance; disclose nondeterminism rather than promising bitwise equivalence across hardware.
- For adaptation, keep evaluation donors/datasets or perturbation conditions separate from training as appropriate. Check overlap with pretraining/reference data where provenance permits, and disclose uncertainty when it cannot be excluded.
- Assess annotation on held-out labels and imputation on held-out measurements when available. Without independent targets, report structural validation only; do not infer accuracy from a visually separated UMAP.
- For paper reproduction, consult the repository's [reproducibility directory](https://github.com/xy-chen16/EpiAgent/tree/main/reproducibility) and match its datasets, labels, splits, and resource versions. Report measured results only; do not transfer published performance to new assays or cohorts.

## Inputs / Outputs

**Inputs:** Human scATAC-seq fragment BED files with cell barcodes and optional counts, or a validated cell-by-cCRE `.h5ad`; genome-build information; cell/sample metadata; the ordered cCRE BED and frequency resources; a compatible checkpoint; and task-dependent labels, references, perturbation metadata, or external embeddings.

**Outputs:** A processed AnnData file containing tokenized cell sentences and, for embedding inference, `obsm['cell_embeddings_zero_shot']`; task-specific predictions or adapted weights when requested; and a run manifest with input/resource hashes, parameters, elapsed time, validation results, and limitations. Preserve cell IDs and feature order in every exported matrix. A blocked setup report is useful diagnostic output but does not satisfy the successful-execution outcome.

## References

- [EpiAgent source repository and README](https://github.com/xy-chen16/EpiAgent).
- [Preprocessing implementation](https://github.com/xy-chen16/EpiAgent/blob/main/epiagent/preprocessing.py) and [workflow notebooks](https://github.com/xy-chen16/EpiAgent/tree/main/demo).
- [Repository MIT license](https://github.com/xy-chen16/EpiAgent/blob/main/LICENSE).
- [Reproducibility code](https://github.com/xy-chen16/EpiAgent/tree/main/reproducibility) and [reproducibility discussion](https://github.com/xy-chen16/EpiAgent/issues/12).
- Chen et al. (2025), [EpiAgent: foundation model for single-cell epigenomics](https://doi.org/10.1038/s41592-025-02822-z), Nature Methods; linked by the repository.
