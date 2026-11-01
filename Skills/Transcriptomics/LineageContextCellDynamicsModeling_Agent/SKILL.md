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
name: 'lineage-context-cell-dynamics-modeling'
description: 'Prepare lineage-linked transcriptomes, model developmental cell states with lineage inpainting, and evaluate held-out predictions against models that omit lineage context.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Lineage-Context Cell Dynamics Modeling

## Overview

Use lineage trees alongside transcriptional states to investigate developmental dynamics and distinguish predictions supported by relatives from those supported by expression alone. The source finding reports lineage inpainting, transcriptional convergence, and exploratory perturbation predictions in mouse development; this workflow adds explicit input validation and leakage-aware evaluation. Treat inferred trajectories as model-dependent reconstructions and counterfactual responses as hypotheses requiring independent validation.

## When to Use This Skill

- Matched single-cell transcriptomes and reconstructed lineage trees are available across developmental snapshots.
- Predicting ancestral or descendant states may benefit from sister-cell or cousin-cell context.
- Assessing whether apparent transcriptional convergence persists across distinct lineages.
- Comparing lineage-aware predictions with expression-only models under matched evaluation conditions.
- Exploring perturbation hypotheses using a fitted developmental model with an explicit intervention representation.

## Core Capabilities

1. **Define the prediction task and execution budget.** Specify ancestral reconstruction, masked-state prediction, or forecasting, along with conditioning snapshots and target times. Within 15 minutes, aim for validated inputs, an auditable split, and a small inference/evaluation run using compatible existing weights; full training is a separate compute task. If data or weights are unavailable, return a readiness report with missing prerequisites rather than claiming successful prediction.

2. **Prepare lineage-aware inputs.** Join expression rows to observed tree nodes by stable, sample-qualified cell identifiers. Require node and parent identifiers, embryo or biological-replicate identity, clone/tree identity, capture times, node times or branch lengths with units, and observed-state masks. Check duplicate mappings, orphan nodes, cycles, multiple parents, negative branch lengths, and parent times later than child times. Preserve inferred topology and timing confidence; flag unsupported timing instead of silently substituting pseudotime. Keep unobserved ancestral states explicitly missing rather than encoding them as measured zeros.

3. **Prevent leakage before preprocessing.** Partition biological replicates first and retain every clone, shared ancestor, overlapping subtree, and technical duplicate within its assigned partition. Prefer held-out embryos for generalization; random cell splits cannot establish independence among relatives. Fit variable-gene selection, scaling, latent embeddings, integration, annotation references, and nearest-neighbor target banks on training data only, then freeze them. Record any pretrained representation's exposure to evaluation embryos. Audit cross-partition cell, clone, embryo, and subtree overlap, and report relatedness where clone labels are incomplete.

4. **Use verified modeling details.** Methods Sections 4.1.2–4.1.5 describe separate imputer and sampler weights trained jointly. Node tokens encode state, developmental time, and observed status; attention receives learned per-head/layer patristic-distance biases. Outputs add residuals to recursively averaged child states or copied observed ancestors. Imputation aligns marginal, path, and common-ancestor feature distributions. The sampler conditions on one snapshot, corrupts remaining states, and predicts clean states using a stochastic interpolant; interpolation time is distinct from developmental time. The paper evaluates CFM and VP-SDE, using VP-SDE in main analyses. Training mixes imputed and nearest-observed-cell targets. These details were checked against the [full Methods](https://arxiv.org/html/2610.40447v1); the [repository](https://github.com/g-kl/lineage-inpainting) calls the imputer a `pooler` and sampler a `splitter`.

   Before execution, inspect the chosen repository revision, configuration, input loader, and checkpoint metadata. Record state-space dimensions, gene order, masks, distance units, interpolant schedule, solver, and preprocessing compatibility. Do not invent executable flags or silently substitute a generic transformer. Label any simplified implementation as an approximation. Constrain nearest-observed training targets to the training partition.

5. **Run held-out prediction with explicit information boundaries.** Keep model weights fixed on evaluation embryos. Supply only the designated context states; remove targets from every feature, displacement calculation, retrieval index, and annotation input. Check that masked target values cannot affect predictions and that observed anchors stay fixed. Distinguish interpolation within a known tree from forecasting: later relatives and future topology constitute extra information. Descendant sampling in the reported method uses supplied topology, not generated division histories; label known-future-topology evaluations accordingly. For prospective claims, use only information available at the forecast origin.

6. **Compare lineage context fairly.** Use identical partitions, expression representation, target masks, evaluation samples, and tuning budgets for the lineage model and an expression-only predictor. Add a matched model without related-cell states and, separately, an ablation of tree-distance information to separate context from architecture effects. A context-shuffling control should preserve time and batch structure while breaking the biological relationships of interest. Treat these as recommended controls, not reported benchmark results. Report compute and parameter differences rather than assuming they are equivalent.

7. **Evaluate observed targets and uncertainty.** For masked measured cells, report error in a fixed state space and cell-type composition differences where labels are independently available. For distributions, preselect a distance metric and compare repeated conditional samples rather than only their mean. Summarize results by time, cell type, context size, and lineage confidence; estimate uncertainty across embryos or clones rather than treating every cell as independent. Evaluate ancestor trajectories against known truth only in suitable synthetic data: imputed ancestors are not ground truth. Include sensitivity to topology uncertainty, missing relatives, and alternative random seeds. Do not infer convergence solely from overlap in a two-dimensional visualization.

8. **Bound counterfactual interpretation and deliver evidence.** Define the perturbed variable, intervention time, state-space mapping, retained context, and fixed-topology assumptions. Gene knockouts cannot generally be represented by zeroing an arbitrary latent coordinate. Pair perturbed and control simulations under matched sampling settings, report effect distributions, and compare with independent perturbation data when available. Distinguish interpolation within training support from extrapolation, and flag omitted effects on proliferation, survival, or topology. A model trained on observational development does not by itself identify a causal perturbation response.

## Inputs / Outputs

**Required inputs**

- Expression matrix or documented latent representation with cell and gene identifiers, preprocessing provenance, and sample metadata.
- Rooted lineage trees or a forest, observed-node mappings, developmental timing, and biological replicate identifiers.
- A defined prediction target, permitted conditioning information, evaluation split policy, and compute budget.
- For inference: a compatible implementation revision and checkpoint. For training: sufficient independent snapshots and a separate training budget.

**Optional inputs**

- Tree uncertainty estimates, alternative reconstructed trees, independent cell annotations, synthetic trajectories with known truth, and perturbation measurements.

**Required outputs**

- Input-validation report with mapping coverage, exclusions, timing assumptions, and topology checks.
- Split manifest and leakage audit covering related cells, preprocessing, retrieval targets, and checkpoint provenance.
- Run manifest with implementation revision, model configuration, random seeds, checkpoint, conditioning mask, and supplied topology.
- Predicted state samples keyed by embryo, tree, node, target time, and draw; preserve observed, predicted, and unavailable status separately.
- Evaluation table comparing lineage-aware and lineage-omitting models, with metric definitions, replicate counts, uncertainty, and failure cases.
- Brief interpretation distinguishing measured evidence, inferred trajectories, and optional counterfactual hypotheses.

**Completion criteria:** A successful bounded run has valid mappings, no prohibited partition overlap, finite predictions of the expected shape, unchanged observed anchors, and metrics on genuinely withheld measured targets. Mark a preparation-only result or failed inference as incomplete; the 15-minute target is not a claim about full model training or biological accuracy.

## References

- [Learning developmental dynamics from lineage context, arXiv:2610.40447v1](http://arxiv.org/abs/2610.40447v1), submitted October 29, 2026. Source finding for lineage inpainting and its developmental applications.
- [Full text and implementation Methods](https://arxiv.org/html/2610.40447v1), especially Sections 4.1.2–4.1.5 and Supplement S8. Source for the architecture and stochastic-interpolant description.
- [Lineage inpainting implementation](https://github.com/g-kl/lineage-inpainting). Inspect and pin the revision before running; repository availability alone does not establish a local reproduction.
