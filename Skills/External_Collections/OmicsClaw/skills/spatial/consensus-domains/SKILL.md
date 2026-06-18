---
name: consensus-domains
description: 'Multi-method consensus over spatial-domains. Fans out 5 methods in parallel, computes a SACCELERATOR-style base-clustering ranking, runs typed consensus (kmode / weighted / LCA), and emits a verified consensus report with the mandatory A-path banner per ADR 0010.'
version: 0.1.0
author: OmicsClaw
license: Apache-2.0
tags:
- spatial
- consensus
- typed-consensus
- expert-in-the-loop
- saccelerator
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

# consensus-domains

## When to use

The user has a preprocessed spatial AnnData (typically already QC'd via
`spatial-preprocess`) and wants a **more trustworthy** tissue-domain
assignment than any single method can produce — because the user knows
single-method results disagree on cancer / non-standard tissues, or
because the analysis is going to drive a downstream decision (cell-type
deconvolution, region-specific DE, paper figure).

This skill fans out `spatial-domains` over N method choices, computes a
typed statistical consensus, and surfaces the **cross-method
disagreement** explicitly. It does NOT replace `spatial-domains`; it
wraps it.

## Inputs & Outputs

| Input | Format | Required |
|---|---|---|
| Preprocessed AnnData | `--input <preprocessed.h5ad>` (PCA + spatial graph) | yes |
| Output directory | `--output <dir>` | yes |
| Member list | `--members banksy,graphst,sedr,leiden,spagcn` | no (defaults to LLM-curated 5) |
| Run ALL eligible methods | `--all` | no (slower; SACCELERATOR-style benchmark mode) |
| Target cluster count | `--n-clusters 7` | no (defaults to median across members) |
| Pre-run plan confirmation | `--confirm-plan` | no (default off) |
| Non-interactive BC picker | `--non-interactive` | no (forces top-K by score) |
| Score weights | `--alpha 0.6 --beta 0.4` | no (ADR 0011 defaults) |
| Class-imbalance cap | `--max-class-frac 0.8` | no |
| LLM judge veto/reweight | `--llm-judge` | no (default deterministic) |
| Operator | `--operator {kmode,weighted,lca}` | no (default `kmode`) |
| Seed | `--seed 0` | no |
| Per-member timeout (s) | `--timeout 600` | no |
| Concurrency cap | `--max-parallel 4` | no |

| Output | Path | Notes |
|---|---|---|
| Verified consensus labels | `consensus_labels.tsv` | columns `observation,consensus_<operator>` |
| Per-member labels (raw) | `member_<name>/figure_data/spatial_*.csv` | passed through from spatial-domains |
| Cross-method NMI matrix | `cross_method_nmi.csv` | square matrix per member |
| Composite member scores | `member_scores.csv` | ADR 0011 schema |
| Markdown report | `report.md` | **starts with `[A: Verified consensus]`** (non-configurable) |
| Plan + audit trail | `plan.json` | LLM rationale + chosen operator + filtered members |

## Flow

1. **Plan** — `runtime/consensus/plan.propose_members` reads
   `skills/spatial/spatial-domains/parameters.yaml` `param_hints`,
   queries the evaluation-chair LLM (or falls back deterministically),
   produces N PlannedMember entries.
2. **Fan out** — `runtime/consensus/team.run_team` invokes
   `omicsclaw.skill.runner.run_skill("spatial-domains", ...)` per
   member with `max_parallel = min(N, cpu_count//2, 4)` and a 600 s
   per-member timeout. `cancel_event` is propagated through.
3. **Score** — `runtime/consensus/scoring.score_all_members` ranks
   survivors by composite `alpha * cross_NMI + beta * mean_local_purity`
   with the `max_class_frac > 0.8` hard filter.
4. **BC pick** — on the CLI surface in interactive mode, prompt the
   user with the top-K-by-score default; on Desktop/Channel surfaces
   (or `--non-interactive`), accept the default.
5. **Consensus** — invoke the chosen operator
   (`kmode` / `weighted` / `lca`) on the selected base clusterings.
6. **Report** — write `report.md` starting with the mandatory ADR 0010
   banner; persist `plan.json` for audit; ready for graph-memory
   storage under `analysis://typed/<run_id>`.

## Gotchas

- **A path is allowed to fail loudly.** If fewer than 2 members survive
  the fan-out, this skill raises `InsufficientSurvivorsError` and does
  NOT silently downgrade to narrative consensus. Re-run with
  `--members` adjusted or fall back to the dedicated narrative skill
  (when shipped).
- **Banner is non-configurable.** The `[A: Verified consensus]` header
  is enforced by `runtime/consensus/dispatch.output_banner`. Do not
  edit `report.md` to strip it before distribution.
- **`--n-clusters` defaults to the median across members**, not 7.
  Override only when you have prior k from histology / known anatomy.
- **LCA requires R + diceR.** When unavailable, the skill prints an
  installation hint and exits non-zero rather than silently switching
  operators. Pass `--operator kmode` to bypass.
- **`requires_preprocessed: true`** — the underlying spatial-domains
  members expect `obsm["X_pca"]` and `obsm["spatial"]` populated. Run
  `spatial-preprocess` first.

## Key CLI

```bash
# Minimal interactive run (CLI surface) — LLM picks 5, you confirm BCs
oc run consensus-domains --input preprocessed.h5ad --output out/

# Non-interactive (server / scripted)
oc run consensus-domains --input preprocessed.h5ad --output out/ \
  --non-interactive

# Explicit members + weighted operator
oc run consensus-domains --input preprocessed.h5ad --output out/ \
  --members banksy,graphst,sedr,leiden,spagcn \
  --operator weighted --n-clusters 7

# SACCELERATOR-style benchmark (run ALL eligible methods)
oc run consensus-domains --input preprocessed.h5ad --output out/ --all
```

## Pointers

- ADR 0010 — runtime layer architecture
- ADR 0011 — scoring + evaluation protocol
- `omicsclaw/runtime/consensus/` — runtime module
- `examples/consensus_benchmark/` — DLPFC 151673 hero benchmark
