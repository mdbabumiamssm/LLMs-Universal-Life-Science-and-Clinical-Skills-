---
name: transcriptformer-cell-embeddings
description: Operate CZI TranscriptFormer cross-species generative single-cell models to produce cell embeddings, contextual gene embeddings, likelihoods, zero-shot classifiers, disease-state representations, and regulatory analyses from raw-count AnnData files. Use when selecting TF-Sapiens, TF-Exemplar, or TF-Metazoa, processing in- or out-of-distribution species, or scaling embedding extraction across GPUs.
---

# TranscriptFormer Cell Embeddings

Use TranscriptFormer for model-derived representations of single-cell transcriptomes. Embeddings and attention-derived relationships are not direct evidence of cell identity, disease mechanism, or gene regulation.

## Model Selection

- Use TF-Sapiens for human-only analyses when the human vocabulary and training distribution fit the study.
- Use TF-Exemplar for human plus common model-organism comparisons.
- Use TF-Metazoa for the broadest cross-species analysis across vertebrates, invertebrates, fungus, and protist data.
- Supply the official protein embeddings for species outside a checkpoint's training set and label the analysis out-of-distribution.

## Workflow

1. Preserve raw counts in `adata.raw.X` or `adata.X`; do not replace them with scaled or log-transformed values without an explicit configuration change.
2. Store Ensembl gene identifiers in `adata.var['ensembl_id']` or set the corresponding configuration key.
3. Audit species, tissue, assay, cell count, gene coverage, sparsity, batch, disease, and donor metadata.
4. Download and pin the checkpoint and protein-embedding files.
5. Run a small batch to quantify vocabulary filtering, memory use, likelihood behavior, and output shape.
6. Select cell embeddings for cell-level tasks or contextual gene embeddings for within-cell gene representation analyses.
7. Use the OOM-safe loader and multi-GPU execution for large H5AD files; preserve output order and source-cell identifiers.
8. Evaluate embeddings with donor- and dataset-held-out tasks, nearest-neighbor inspection, batch sensitivity, and simpler baselines.
9. Treat zero-shot labels, disease scores, and inferred regulatory relationships as hypotheses requiring external validation.

## Guardrails

- Do not mix species or gene identifier systems without explicit mapping and provenance.
- Do not allow cells from the same donor or study to leak across evaluation splits.
- Report the fraction of genes filtered from the vocabulary.
- Distinguish in-distribution from out-of-distribution species and tissues.
- Pin PyTorch to a compatible version and record precision, layer index, clipping, and normalization overrides.
- Do not interpret contextual embeddings as causal regulatory interactions.

## Output Contract

Return the checkpoint, species status, H5AD schema, raw-count source, gene retention, inference configuration, embedding location, likelihoods, QC, downstream benchmark, and limitations.

Read `references/operations.md` for installation, CLI patterns, input requirements, and canonical sources.
