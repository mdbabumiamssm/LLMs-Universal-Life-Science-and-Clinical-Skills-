---
name: sc-consensus-clustering
description: 'Multi-resolution typed consensus over sc-clustering. Fans out leiden / louvain at several resolutions in parallel, scores members by silhouette + cross-method NMI, runs kmode / weighted / LCA consensus on the surviving base clusterings, and emits a verified report carrying the mandatory A-path banner per ADR 0010.'
version: 0.1.0
author: OmicsClaw
license: Apache-2.0
tags:
- singlecell
- consensus
- typed-consensus
- multi-resolution
- silhouette
- bc-ranking
- kmode
- lca
- weighted
requires:
- anndata
- scanpy
- numpy
- pandas
- scipy
- scikit-learn
- pyyaml
---

# sc-consensus-clustering

## When to use

The user has a preprocessed scRNA AnnData (PCA + neighborhood graph
already computed via `sc-preprocessing`) and wants robust cell-cluster
assignments insensitive to the chosen `resolution`. Single-resolution
Leiden/Louvain results are notoriously resolution-sensitive — at
`r=0.4` you get 6 broad types, at `r=1.5` you get 22 sub-states. This
skill runs a SACCELERATOR-style consensus across a resolution sweep
(and optionally across `leiden` vs `louvain`) and reports the **stable
core** of the labels.

It does NOT replace `sc-clustering`; it wraps it.

## Inputs & Outputs

| Input | Format | Required |
|---|---|---|
| Preprocessed AnnData | `--input <preprocessed.h5ad>` (with `obsm["X_pca"]`) | yes |
| Output directory | `--output <dir>` | yes |
| Resolutions to sweep | `--resolutions 0.4,0.8,1.0,1.4,2.0` | no (default 0.5,0.8,1.0,1.4,2.0) |
| Cluster methods to use | `--cluster-methods leiden,louvain` | no (default `leiden`) |
| Explicit member list | `--members leiden:resolution=0.5,louvain:resolution=1.0` | no (overrides the sweep) |
| Fan-out everything | `--all` | no (sweeps both methods × all default resolutions) |
| Operator | `--operator {kmode,weighted,lca}` | no (default kmode) |
| Score weights | `--alpha 0.6 --beta 0.4` | no (ADR 0011 defaults) |
| Class-imbalance cap | `--max-class-frac 0.8` | no |
| Pre-run plan confirm | `--confirm-plan` | no |
| Non-interactive | `--non-interactive` | no |
| Seed | `--seed 0` | no |

| Output | Path | Notes |
|---|---|---|
| Verified consensus labels | `consensus_labels.tsv` | columns `cell_id,consensus_<operator>` |
| Per-member labels | `member_<name>/figure_data/embedding_points.csv` | from sc-clustering |
| Cross-method NMI matrix | `cross_method_nmi.csv` | square per member |
| Composite scores | `member_scores.csv` | ADR 0011 schema |
| Markdown report | `report.md` | starts with `[A: Verified consensus]` (non-configurable) |
| Audit | `plan.json` | resolution sweep + chosen operator + filtered members |

## Flow

1. **Plan members** — either user-supplied (`--members` / `--all`) or
   derived from the resolution sweep × cluster-methods combinations.
2. **Fan out** — runtime invokes `sc-clustering` once per member.
3. **Score** — `silhouette_score` from each member's
   `clustering_summary.csv` is the intrinsic-quality signal; cross-method
   NMI is computed across members.
4. **BC pick** — top-K-by-composite-score default; CLI interactive
   override allowed.
5. **Consensus** — kmode / weighted / LCA on the selected base
   clusterings.
6. **Report** — banner + score table + NMI matrix.

## Gotchas

- **`--cluster-methods` defaults to `leiden` ONLY**, not both, because
  `louvain` and `leiden` agree to within 1–2% on most datasets and the
  consensus signal comes mostly from the resolution sweep.
- **Resolutions must span at least one factor of 2** for the consensus
  to be informative; default sweep covers 0.5–2.0.
- The mandatory banner is enforced by
  `runtime/consensus/dispatch.output_banner`. Do NOT strip it.
- `requires_preprocessed: true` — run `sc-preprocessing` first.

## Key CLI

```bash
# Default sweep (leiden at 5 resolutions)
oc run sc-consensus-clustering --input preprocessed.h5ad --output out/

# Both methods × 5 resolutions = 10 members; SACCELERATOR-style benchmark
oc run sc-consensus-clustering --input preprocessed.h5ad --output out/ \
  --cluster-methods leiden,louvain --resolutions 0.5,0.8,1.0,1.4,2.0

# Explicit
oc run sc-consensus-clustering --input preprocessed.h5ad --output out/ \
  --members leiden:resolution=0.5,leiden:resolution=1.0,louvain:resolution=1.0
```

## Pointers

- ADR 0010 — runtime architecture
- ADR 0011 — scoring + evaluation
- `skills/spatial/consensus-domains/` — sibling spatial-side skill
