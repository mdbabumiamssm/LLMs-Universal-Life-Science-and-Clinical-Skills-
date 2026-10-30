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
name: 'lineage-context-cell-dynamics'
description: 'Prepare lineage-traced transcriptomes for lineage inpainting, model cell-state dynamics with tree context, and evaluate the predictive contribution of relatives using lineage-aware splits and missing-context checks.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Lineage-Context Cell Dynamics

## Overview

Use lineage inpainting to infer unobserved transcriptional states from measured cells and their relatives across developmental trees. The source finding reports transcriptional convergence and perturbation hypotheses in mouse embryogenesis; this skill adds practical data validation and evaluation safeguards for applying that approach.

## When to Use This Skill

- Prepare expression measurements linked to reconstructed lineage trees for developmental modeling.
- Infer ancestral or descendant cell states conditional on an observed lineage snapshot.
- Test whether sister, cousin, or broader lineage context improves predictions beyond expression alone.
- Evaluate sensitivity to incomplete relatives, uncertain trees, or developmental sampling gaps.
- Generate explicitly exploratory perturbation hypotheses from an unperturbed-development model.

## Core Capabilities

The method facts below follow the linked paper. Data checks, split policies, ablations, and acceptance criteria are recommended workflow safeguards, not claims about its published evaluation.

1. **Establish a reproducible execution scope.** Read the paper's methods and the repository README and configuration before selecting commands. Record the paper version, repository commit, environment, dataset provenance, random seeds, and available compute. Public code availability is confirmed; checkpoint availability and local compatibility must be checked separately. Do not invent package APIs or download names.

2. **Validate expression-to-tree alignment.** Require unique cell and node identifiers, a cell-to-node mapping, rooted parent-child edges, developmental node times, capture times, and embryo or biological-replicate identifiers. Check for cycles, multiple parents, disconnected components, duplicate mappings, nonfinite states, and parent times later than child times. Report excluded cells and trees with reasons. Preserve unobserved internal states as missing values with explicit masks; never encode missingness as measured zero expression. If only clone labels are available, report the missing topology and timing requirements instead of inventing ancestors.

3. **Prepare compatible cell-state representations.** The paper uses timed reconstructed trees, observed leaf transcriptomes, and a shared 50-dimensional scVI representation. Keep raw counts and preprocessing provenance separate from derived states. For a new application, document quality filters, gene identifiers, batch covariates, feature order, and latent representation. Fit learned preprocessing on training data for an inductive evaluation; label any jointly fitted atlas representation as transductive. Verify checkpoint feature and latent-space compatibility before inference.

4. **Construct lineage-aware splits before sampling subtrees.** Prefer holding out whole embryos or biological replicates, retaining their complete trees together. When necessary, hold out independent lineage roots and disclose shared-embryo dependence. Keep overlapping subtrees and shared ancestors in one partition. Check identifier overlap and group counts across train, validation, and test sets. Use a separate held-out-time analysis for temporal extrapolation. Distinguish test-time conditioning on allowed relatives from using hidden target states during fitting or preprocessing.

5. **Configure tree-structured inpainting.** The published method jointly trains an imputer with cross-tree distributional consistency and a stochastic-interpolant sampler using tree-distance-biased attention. Sampling conditions on a snapshot while retaining observed states. Follow the verified implementation for objectives, masks, noise schedules, and optimization. Distinguish developmental time from interpolant time. Descendant inference needs a supplied future topology; this model does not establish a division-tree generator. Bound subtree size and monitor memory before scaling.

6. **Measure the contribution of relatives.** Evaluate the full-context model against an expression-only baseline and a model without tree-distance information under identical target masks, splits, and computational budgets where feasible. Add a context-permutation control that preserves capture time and relevant batch structure. Test sister-only, broader-relative, and no-relative context where the implementation supports those masks. Treat unsupported masks as out-of-distribution stress tests. Report performance by embryo, stage, cell type, and available-context size, with uncertainty resampled at the independent biological-unit level.

7. **Check missing context and inference validity.** Remove increasing fractions of relatives, then remove entire sister or cousin groups to test structured missingness. Keep targets fixed across conditions and record the removal seed and actual remaining relatives. Test plausible topology or node-time uncertainty separately from missing expression. Confirm that conditioned states stay fixed, generated values remain finite, and results are reproducible with fixed seeds while multiple draws retain variability. If removing leaves changes tree representation, preserve branch lengths and record the pruning rule.

8. **Evaluate dynamics without invented ground truth.** On masked measured cells, report prediction error in the declared state space and sample uncertainty. On independently observed snapshots, compare state distributions and cell-type composition. Do not treat imputed ancestors as experimental truth or latent-space accuracy as gene-expression accuracy. Interpret convergence using distinct lineage histories and sensitivity analyses, rather than proximity in a two-dimensional embedding alone. Separate conditional reconstruction, temporal extrapolation, and synthetic ground-truth tests in the report.

9. **Generate bounded counterfactual hypotheses.** State the exact intervention operator, altered states or conditioning, fixed topology assumptions, comparison window, and unsupported biological mechanisms. Keep perturbation measurements out of fitting when assessing generalization from unperturbed development. Compare distributions and lineage-specific responses with independent perturbation observations when available. Label outputs as hypotheses: observational inpainting does not identify causal knockout effects, and setting a gene count to zero is not automatically a valid knockout simulation in latent space.

10. **Deliver a fifteen-minute validation result.** Use the time budget for input validation, split and mask checks, and a small inference run with an available compatible model. Full atlas preprocessing or model training is outside this timing promise. If dependencies, data, or weights are missing, return a readiness report with explicit blocked checks and the next executable step; do not label an unrun model as successful. A successful inference result requires disjoint split groups, finite samples of expected shape, unchanged conditioning states, and recorded configuration and provenance.

## Inputs / Outputs

**Required inputs**

- A cell-by-gene count matrix with cell and gene identifiers, or a documented compatible state embedding.
- Rooted lineage topology, node times and units, leaf-to-cell mapping, and observed-state masks.
- Capture-stage, embryo or replicate, and batch metadata; multiple developmental snapshots for training dynamics.
- A declared prediction task, allowed conditioning context, output location, and compute or time budget.
- For inference: a compatible model checkpoint and its preprocessing specification. For training: the verified code, configuration, and sufficient data and compute.

**Optional inputs**

- Cell-type annotations, tree-confidence estimates, alternative reconstructions, or independent perturbation measurements.
- A supplied future topology for descendant simulation, with its origin and assumptions recorded.

**Outputs**

- A readiness and quality-control report listing input dimensions, mapping coverage, invalid trees, unresolved dependencies, and execution status.
- A split manifest and conditioning/target-mask specification with biological-unit overlap checks.
- A reproducibility record containing source versions, preprocessing, feature order, model configuration, seeds, and runtime.
- When inference runs: sampled states indexed by tree, node, developmental time, and draw; observed versus generated flags; and uncertainty summaries in the correct state space.
- When evaluation runs: matched baseline and ablation results, missing-context sensitivity, and limitations on convergence or counterfactual interpretation.

Return artifacts only for steps actually executed. Distinguish `validated`, `inference-complete`, and `blocked` outcomes, and explicitly identify checks omitted because of the time budget.

## References

- [Learning developmental dynamics from lineage context, arXiv:2610.40447v1](http://arxiv.org/abs/2610.40447v1) — source finding; [full methods](https://arxiv.org/html/2610.40447v1), particularly Sections 4.1 and 4.3.
- [Lineage inpainting implementation](https://github.com/g-kl/lineage-inpainting) — public code linked by the paper; inspect the selected commit before execution.
- [Associated data, Zenodo DOI 10.5281/zenodo.23750040](https://doi.org/10.5281/zenodo.23750040) — availability location reported by the paper, including Tbx5 mutant measurements; verify access and file contents before use.
