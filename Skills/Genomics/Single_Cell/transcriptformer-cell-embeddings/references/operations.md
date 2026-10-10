# TranscriptFormer Operations

## Installation

TranscriptFormer requires Python 3.11 or newer. The official repository currently constrains PyTorch to 2.5.1 or earlier because later versions may cause checkpoint-loading errors.

```bash
uv venv --python=3.11
source .venv/bin/activate
uv pip install transcriptformer
```

## Download Models

```bash
transcriptformer download tf-sapiens
transcriptformer download tf-exemplar
transcriptformer download tf-metazoa
transcriptformer download all-embeddings
```

## Inference

```bash
transcriptformer inference --checkpoint-path ./checkpoints/tf_sapiens --data-file input.h5ad --output-path ./results --batch-size 8
```

For contextual gene embeddings:

```bash
transcriptformer inference --checkpoint-path ./checkpoints/tf_sapiens --data-file input.h5ad --emb-type cge --batch-size 8
```

For large data, add `--oom-dataloader`, set workers, and use `--num-gpus` with matched GPUs.

## Input Contract

- H5AD/AnnData input;
- raw integer-like counts in `adata.raw.X` or `adata.X`;
- Ensembl IDs in `adata.var['ensembl_id']` by default;
- preserved donor, study, tissue, disease, and species metadata;
- official species embedding file for out-of-distribution species.

Cell embeddings are written to `obsm['embeddings']`. Contextual gene embeddings and their cell and gene indices are written under `uns`.

## Provenance

Verified 2026-06-18:

- Official repository: https://github.com/czi-ai/transcriptformer
- Latest release observed: `v0.6.1`, published 2025-11-06
- License: MIT
- Package: https://pypi.org/project/transcriptformer/
- Paper: https://www.biorxiv.org/content/10.1101/2025.04.25.650731v2
- Training data source: https://cellxgene.cziscience.com/
