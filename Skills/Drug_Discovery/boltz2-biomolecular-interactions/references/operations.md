# Boltz-2 Operations

## Installation

```bash
pip install "boltz[cuda]" -U
```

Use a fresh environment. CPU inference is supported but substantially slower.

## Prediction

```bash
boltz predict input.yaml --use_msa_server
```

`input.yaml` can be replaced with a directory of YAML files for batch processing. Review the official prediction schema before constructing complexes with ligands, modified residues, templates, constraints, or affinity requests.

## Affinity Fields

| Field | Use |
|---|---|
| `affinity_probability_binary` | Binder-versus-decoy prioritization during hit discovery |
| `affinity_pred_value` | Affinity comparison among binders during hit-to-lead and lead optimization |

The official documentation describes `affinity_pred_value` as `log10(IC50)` for IC50 measured in micromolar. Preserve this definition in every table and visualization.

## Reproducibility Checklist

- pin the package or container digest;
- retain the exact input YAML;
- retain ligand identifiers and prepared structures;
- retain MSA source and authentication mode;
- record model outputs before post-processing;
- run multiple seeds or replicates for close decisions;
- validate top candidates with an assay matched to the intended affinity endpoint.

## Provenance

Verified 2026-06-18:

- Official repository: https://github.com/jwohlwend/boltz
- Latest GitHub release observed: `v2.2.1`, published 2025-09-08
- Repository pushed: 2026-05-29
- License for code and weights: MIT
- Prediction instructions: https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md
- Boltz-2 report: https://doi.org/10.1101/2025.06.14.659707
