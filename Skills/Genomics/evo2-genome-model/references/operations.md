# Evo 2 Operations

## Deployment Selection

| Need | Recommended path |
|---|---|
| Local prototyping without FP8 | `evo2_7b`, `evo2_7b_262k`, or `evo2_7b_base` |
| Maximum local long-context capacity | `evo2_20b` or `evo2_40b` on Hopper-class NVIDIA GPUs |
| No local installation | NVIDIA hosted API |
| Controlled service deployment | NVIDIA NIM |
| Training or fine-tuning | Savanna or NVIDIA BioNeMo |

The 7B models can run in bfloat16. The official repository states that the 1B base, 20B, and 40B checkpoints require Transformer Engine FP8 support for numerical accuracy.

## Setup

```bash
pip install flash-attn==2.8.0.post2 --no-build-isolation
pip install evo2
python -m evo2.test.test_evo2_generation --model_name evo2_7b
```

Officially supported local environments are Linux or limited WSL2 with Python 3.11 or 3.12, CUDA 12.1+, cuDNN 9.3+, and a C++17 compiler.

## Core Patterns

### Sequence scoring

Tokenize a DNA sequence, run a forward pass, and compare reference and alternate log likelihoods in identical context. Normalize alleles first and retain the genomic window used for every score.

### Embeddings

Request named intermediate layers and benchmark them on the downstream task. The upstream project reports that intermediate embeddings may outperform final embeddings.

### Generation

```python
from evo2 import Evo2

model = Evo2("evo2_7b")
result = model.generate(
    prompt_seqs=["ACGT"],
    n_tokens=400,
    temperature=1.0,
    top_k=4,
)
```

Treat generated sequences as candidates requiring computational and experimental screening.

## Provenance

Verified 2026-06-18:

- Official repository: https://github.com/ArcInstitute/evo2
- Latest GitHub release observed: `v0.5.0`, published 2026-02-28
- Package license: Apache-2.0
- Paper: https://www.nature.com/articles/s41586-026-10176-5
- OpenGenome2 dataset: https://huggingface.co/datasets/arcinstitute/opengenome2
- NVIDIA NIM documentation: https://docs.nvidia.com/nim/bionemo/evo2/latest/overview.html
