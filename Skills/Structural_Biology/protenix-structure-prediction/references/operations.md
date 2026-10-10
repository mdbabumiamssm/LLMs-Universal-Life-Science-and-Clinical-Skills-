# Protenix Operations

## Installation

```bash
pip install --upgrade protenix --index-url https://pypi.org/simple
```

The repository releases code and model parameters under Apache-2.0 for academic and commercial use.

## Prediction

```bash
protenix pred -i examples/input.json -o ./output -n protenix-v2
```

Review the official JSON schema before using templates, RNA MSAs, ligands, atom-level contacts, pocket constraints, or modified residues.

## Model Selection

| Model | Cutoff | Use |
|---|---|---|
| `protenix-v2` | Document with the exact release | Current enhanced-capacity model |
| `protenix_base_default_v1.0.0` | 2021-09-30 | AlphaFold3-aligned benchmark comparisons |
| `protenix_base_20250630_v1.0.0` | 2025-06-30 | Practical applied predictions with later training data |
| `protenix_base_default_v0.5.0` | 2021-09-30 | Backward compatibility |

Protenix-v2 emphasizes improved antibody-antigen prediction and ligand plausibility. Inference-time scaling can improve challenging targets, but benchmark every additional sampling budget against cost and selection bias.

## Reproducibility Checklist

- save the input JSON and exact model identifier;
- save MSA, template, constraint, and seed provenance;
- inspect every generated candidate for chemical and geometric validity;
- record the selection rule before viewing outcomes;
- distinguish current applied models from cutoff-controlled benchmark models.

## Provenance

Verified 2026-06-18:

- Official repository: https://github.com/bytedance/Protenix
- Official web server: https://protenix-server.com
- Latest release observed: `v2.0.0`, published 2026-04-07
- Code and model license: Apache-2.0
- Input schema: https://github.com/bytedance/Protenix/blob/main/docs/infer_json_format.md
- Training and inference guide: https://github.com/bytedance/Protenix/blob/main/docs/training_inference_instructions.md
- Protenix-v2 technical report: https://github.com/bytedance/Protenix/blob/main/docs/PX2.pdf
- Protenix-v2 DOI: https://doi.org/10.64898/2026.04.10.717613
