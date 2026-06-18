---
name: consensus-interpret
description: "LLM-grounded biological interpretation of a verified typed consensus run. Reads the typed run dir + the original adata, runs inline per-cluster DE, looks up markers in a bundled tissue-keyed marker DB, and asks the chair LLM to (γ) name each cluster's likely cell type with mandatory marker citations and (β) recommend top-3 next-step skills with mandatory evidence_refs. Output banner [A+I: Interpreted on verified consensus]. Failure-mode contract per ADR 0012."
version: 0.1.0
author: OmicsClaw
license: Apache-2.0
tags:
- spatial
- consensus
- interpreted-layer
- biology-annotation
- marker-grounded
- backward-proof-driven-recommendation
requires:
- anndata
- scanpy
- numpy
- pandas
- scikit-learn
---

# consensus-interpret

## When to use

The user has just finished a verified typed consensus run
(`consensus-domains` or `sc-consensus-clustering`) and wants the next
manual step (read `cross_method_nmi.csv` → run `spatial-de` →
cross-reference markers → name cell types → decide downstream skill) done
automatically with **falsifiable evidence** binding every LLM claim.

This skill does NOT replace the typed run. It is a strictly downstream
consumer: it reads `<typed_run_dir>/{plan.json, consensus_labels.tsv,
member_scores.csv, cross_method_nmi.csv}` plus the original adata, and
writes its output to a *different* directory under
`analysis://interpreted/<typed_run_id>`. The verified-vs-exploratory
boundary established by ADR 0010 is preserved.

Skip when:

- The typed run did not produce `consensus_labels.tsv` (i.e.
  `consensus-domains` exited non-zero — fix the typed run first).
- You are looking for a generic `query → skill` dispatcher; use
  `orchestrator` for that (forward direction).
- You want to refine the consensus itself based on LLM judgment; that is
  explicitly forbidden by §11.4 "LLM never participates in statistical
  merging" and would be rejected by this skill's T3 invariants.

## Inputs & Outputs

| Input | Format | Required |
|---|---|---|
| Typed run directory | `--input <typed_run_dir>` (must contain `plan.json` written by `consensus-domains` / `sc-consensus-clustering`) | yes |
| Output directory | `--output <interpreted_dir>` | yes |
| Tissue hint | `--tissue {brain, immune, kidney, liver}` (selects bundled marker DB) | yes (unless `--markers` provided) |
| Original AnnData path | `--adata <preprocessed.h5ad>` | no — defaults to `plan.json` `input_path` |
| User-provided marker DB | `--markers <file.tsv>` (overrides bundled DB; same schema) | no |
| Disable LLM (structural-only) | `--no-llm` | no — default fails-fast on LLM unavailability |
| LLM seed (for self-consistency runs) | `--seed 0` | no |
| Top-K markers reported per cluster | `--top-k-markers 20` | no |
| Top-K next-step recommendations | `--top-k-next-steps 3` | no (capped at 3 by ADR 0012) |
| Coverage floor for T2 escalation | `--coverage-floor 0.5` | no |

| Output | Path | Notes |
|---|---|---|
| Interpreted report | `interpreted_report.md` | **First line: `[A+I: Interpreted on verified consensus]`** (or `[I-noLLM: ...]` if `--no-llm`). Non-configurable per ADR 0012. |
| Structured cell-type assignments | `interpreted_assignments.json` | machine-readable; schema below |
| Per-cluster DE table | `de_per_cluster.csv` | inline `scanpy.tl.rank_genes_groups` output; consensus-interpret computes this |
| Contradiction regions | `contradiction_regions.csv` | rows where cross_method_nmi indicates disagreement; LLM-narrated in markdown |
| Audit | `audit.json` | `typed_run_id`, adata checksum, marker DB used, LLM model/seed, `interpreted_namespace`, `evidence_base_namespace` |

### `interpreted_assignments.json` schema

```json
{
  "schema_version": "0.1",
  "typed_run_id": "<plan.json:run_id>",
  "evidence_base_namespace": "analysis://typed/<run_id>",
  "interpreted_namespace": "analysis://interpreted/<run_id>",
  "banner": "[A+I: Interpreted on verified consensus]",
  "operator": "<from typed plan.json>",
  "clusters": [
    {
      "id": 5,
      "n_cells": 778,
      "interpretation_status": "interpreted | low_confidence | failed",
      "cell_type": "CA1 pyramidal",
      "confidence": 0.84,
      "evidence": {
        "markers": [
          {"gene": "Pvrl3", "de_rank": 1, "db_source": "panglaodb_brain", "db_celltype": "CA1 pyramidal neuron", "weight": 0.9},
          {"gene": "Wfs1",  "de_rank": 3, "db_source": "panglaodb_brain", "db_celltype": "CA1 pyramidal neuron", "weight": 0.85}
        ],
        "mean_local_purity": 0.617,
        "member_agreement": [
          {"member": "leiden_resolution-0.5", "label_overlap": 0.92},
          {"member": "leiden_resolution-1.0", "label_overlap": 0.78}
        ]
      },
      "narrative_md_anchor": "#cluster-5"
    }
  ],
  "next_steps": [
    {
      "skill": "spatial-de",
      "args_hint": "--groupby consensus_kmode --comparisons cluster_3_vs_5",
      "priority": 1,
      "evidence_refs": [
        "cross_method_nmi.csv:row=leiden_resolution-0.5,col=leiden_resolution-1.5,value=0.597"
      ],
      "reason": "Lowest pair-wise NMI in matrix; marker disambiguation between clusters 3 and 5 will resolve whether these are sub-types of CA1 or a transition zone."
    }
  ]
}
```

## Flow

```
1. Preflight (T1 — fail-fast if any fail)
   ├─ Load plan.json from --input; assert schema_version + typed run integrity
   ├─ Locate adata at plan.json.input_path (or --adata override); check exists
   ├─ Load consensus_labels.tsv; assert observation column ⊆ adata.obs.index
   ├─ Resolve marker DB:
   │    --markers <path> if given;
   │    else bundled `data/markers/panglaodb_<tissue>.tsv` for --tissue;
   │    else exit 5 (MarkerDBUnavailable)
   └─ If LLM required and unreachable AND --no-llm not set → exit 6 (LLMUnavailable)

2. Per-cluster differential expression (deterministic, scanpy)
   └─ scanpy.tl.rank_genes_groups(adata, groupby=consensus_<operator>, method='wilcoxon')
       → de_per_cluster.csv with top-K markers per cluster (K=20 default)

3. Marker → cell-type lookup (deterministic, pre-LLM)
   └─ For each cluster, compute candidate cell types by ranking DB entries
       whose gene appears in the cluster's top-K markers (weighted by db.weight × 1/de_rank).

4. LLM grounded interpretation (γ + β; one call per cluster + one synthesis call)
   ├─ Prompt template embeds (per cluster):
   │    cluster_id, n_cells, top-K DE markers,
   │    DB candidate cell types (ranked),
   │    member_agreement summary, cross_method_nmi neighbors
   ├─ LLM must return JSON conforming to interpreted_assignments.json
   │   schema; mandatory evidence.markers[] with non-empty
   │   {gene, db_source, db_celltype}
   └─ After all clusters: one synthesis call to produce next_steps[]
       with mandatory evidence_refs[] (capped at top-3 by priority)

5. Invariant enforcement (T3 — fail-fast if violated)
   ├─ Every cluster.evidence.markers != []      → else exit 7
   ├─ Every next_steps[*].evidence_refs != []   → else exit 7
   └─ Banner present and matches one of two allowed values → else exit 7

6. Coverage check (T2 — escalate to T1 if floor breached)
   └─ interpretable_cluster_frac < --coverage-floor → exit 8

7. Artifact writes
   ├─ interpreted_report.md (banner enforced in format_interpreted_report)
   ├─ interpreted_assignments.json
   ├─ de_per_cluster.csv
   ├─ contradiction_regions.csv
   └─ audit.json
```

## Failure modes (per ADR 0012)

| Exit | Name | Meaning |
|---|---|---|
| 0 | success | All clusters interpreted (or `low_confidence`), invariants intact, no degradation triggered |
| 2 | argparse | CLI error |
| 3 | TypedRunInvalid | `plan.json` missing / malformed / not from a typed run |
| 4 | AdataMismatch | adata `obs` index disjoint from `consensus_labels.tsv` `observation` |
| 5 | MarkerDBUnavailable | `--tissue` not in bundled DBs and `--markers` not provided |
| 6 | LLMUnavailable | LLM endpoint unreachable and `--no-llm` not given |
| 7 | InvariantViolation | LLM violated marker-grounding or evidence-ref contract (T3) |
| 8 | CoverageBelowThreshold | < 50% of clusters interpretable (after T2 degradation) |

## Examples

### Default usage (after a typed run completes)

```bash
oc run consensus-domains --input preprocessed.h5ad --output run1/ \
  --members banksy,graphst,leiden:resolution=0.5,leiden:resolution=1.0 \
  --non-interactive --operator kmode --seed 0

oc run consensus-interpret --input run1/ --output run1_interpreted/ \
  --tissue brain
# → run1_interpreted/interpreted_report.md begins with [A+I: ...]
```

### CI / offline (structural-only)

```bash
oc run consensus-interpret --input run1/ --output run1_struct/ \
  --tissue brain --no-llm
# → run1_struct/interpreted_report.md begins with [I-noLLM: ...]
# → no cell-type claims, only cluster sizes / NMI summary / contradiction regions
```

### User-provided marker DB (non-bundled tissue)

```bash
oc run consensus-interpret --input run1/ --output run1_interp/ \
  --markers ~/markers/mouse_intestine.tsv
# → bypasses --tissue requirement; uses user's custom DB
```

## Related skills

| Direction | Skill | Relationship |
|---|---|---|
| upstream (required) | `consensus-domains` / `sc-consensus-clustering` | produces the typed run this skill interprets |
| upstream (auto-chained, internal) | none — DE is computed inline with `scanpy.tl.rank_genes_groups`; we do not invoke `spatial-de` as a subprocess (see ADR 0012 rejected alternatives §4) | |
| sibling (semantically distinct) | `orchestrator` | forward `query → skill`; this skill does backward `result → (skill, evidence)` |
| downstream (β suggests these) | `spatial-de`, `spatial-deconv`, `spatial-communication`, `spatial-trajectory`, etc. | next-step skills the LLM may recommend; each recommendation MUST cite specific typed-run evidence |

## References

- ADR 0010 — typed-vs-narrative consensus runtime (boundary integrity)
- ADR 0011 — typed consensus evaluation protocol (composite member score; DLPFC hero)
- ADR 0012 — this skill's evaluation protocol (4-axis panel + T3 invariants)
- `docs/CONTEXT.md` "Cross-reference: Consensus runtime" — canonical vocabulary
