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
name: 'spadag-spatial-regulatory-graph-inference'
description: 'Prepare spatial transcriptomics data and use SpaDAG to infer regional directed regulatory graphs, quantify posterior uncertainty, and investigate changes in edge direction.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# SpaDAG Spatial Regulatory Graph Inference

## Overview

SpaDAG infers spatially varying Bayesian directed acyclic graphs from expression profiles and tissue coordinates, allowing regional changes in edge presence and direction. This skill guides preparation, fitting, uncertainty assessment, and regional comparison to generate experimentally testable regulatory hypotheses.

## When to Use This Skill

- Investigating regulatory differences across a tumor boundary or other tissue contexts.
- Testing whether a gene pair has different inferred orientations in different regions.
- Preparing spatial expression data for Bayesian graph inference.
- Reviewing uncertainty, reproducibility, or assumptions of a SpaDAG analysis.

## Core Capabilities

1. **Verify the implementation and scientific scope.** The linked repository was accessible during authoring on 2026-11-25; execution was not tested. Record its commit and inspect current documentation before installation. Python 3.10+, NumPy, SciPy, Rscript, and BayesLogit are required; custom preparation additionally needs the `prepare` extra and BayesGPfit. The sampler uses a Gaussian spike (`--v0`, default `1e-3`) in place of the theoretical point mass: report this working-posterior approximation explicitly. Do not transfer the population identifiability guarantee directly to numerical output. See the repository reference.

2. **Check assumptions before fitting.** The paper specifies a linear spatial SEM, independent Gaussian errors, location-wise causal Markov and causal sufficiency assumptions, and gene-specific error variances constant across space. Identifiability requires, on at least one triangle, nonconstant sums of squared outgoing coefficients divided by child error variances for every nonempty child subset. This holds almost surely under the specified prior; it does not ensure finite-sample recovery. Review Sections 2–3 and the supplement before interpreting directions. Record possible violations from omitted regulators, cell mixtures, batch effects, nonlinear responses, feedback, and spatially varying noise. See the paper reference.

3. **Prepare aligned expression and coordinates.** Require unique observation and gene identifiers; join expression and coordinates by identifier rather than row position. Reject nonfinite values and unresolved duplicate coordinates, and document exclusions. Preserve raw counts, library sizes, coordinate units, transformations, and gene-selection rationale. Choose a biologically motivated gene panel and assess how omitted genes could confound it. Select an expression transformation appropriate to the Gaussian model; do not silently feed raw counts or impute zeros. Keep tissue labels available for interpretation without allowing outcome-driven region selection.

4. **Construct and inspect the tissue mesh.** SpaDAG fixes a coordinate-derived triangulation before sampling; its graphs use vertex-indicator OR rules and enforce acyclicity per triangle. Inspect coverage, degenerate triangles, tissue holes, disconnected sections, and observation density. Record coordinate scaling and mesh resolution. Use the verified preparation interface and data-format documentation; do not invent bundle keys or command flags. Report regions with inadequate support and plan mesh-resolution sensitivity checks.

5. **Run a bounded smoke test, then plan inference.** With dependencies installed, use the repository-root example below. These commands are documented upstream; the smoke test checks execution only and cannot establish convergence.

   ```bash
   spadag --data artifacts/data/example_reversal_p50_n500 \
     --trace-dir runs/smoke/trace --iters 20 --burn 10 --seed 1
   ```

   Inspect `runs/smoke/trace/summary.npz` without pickle loading. `edge_prob[t,j,k]` represents `k -> j`; verify finite probabilities, dimensions, and positive retained-draw count. For custom data, consult `spadag-prepare --help` and the upstream usage/data-format documents first. Stop with a precise blocker if those interfaces cannot be verified. Save seeds, configuration, dependency versions, and logs. For substantive inference, budget separately for multiple chains, warmup, retained draws, and diagnostic review; do not reduce sampling merely to meet the smoke-test deadline.

6. **Assess uncertainty and compare regions.** Inspect chain agreement, traces, effective sample sizes, and Monte Carlo error for available continuous and graph summaries; report unavailable diagnostics. Check zero diagonal and opposing-direction probability sums no greater than one, allowing numerical tolerance. Compare both orientations and absence support, not only selected edges. Define regional weighting explicitly, such as tissue area or observation count, and calculate contrasts within posterior draws when available. Marginal probabilities alone cannot recover joint reversal probabilities. Report selection thresholds, uncertainty, sparse coverage, and sensitivity to preprocessing, priors, mesh, and gene panel. Check any thresholded graph for cycles rather than assuming marginal selection preserves acyclicity; regional unions also need not be DAGs. Distinguish reversal of arrow direction from a coefficient sign change. Describe results as model-inferred hypotheses requiring perturbation or other independent validation, never as established therapeutic mechanisms.

## Inputs / Outputs

**Inputs**

- Expression matrix with observation and gene identifiers; raw counts and preprocessing metadata where available.
- Matching two-dimensional coordinates, units, tissue mask, and optional histology or regional annotations.
- Verified SpaDAG checkout, dependency environment, selected genes, mesh configuration, sampling budget, and random seeds.

**Outputs**

- Alignment and quality-control report, preprocessing record, mesh visualization, and observation-to-triangle mapping.
- Run manifest with implementation revision, assumptions, configuration, runtime, and diagnostic status.
- Triangle-level directed-edge probabilities with explicit source/target convention; coefficient summaries and posterior draws when supported.
- Regional comparison table with weighting, direction support, uncertainty, selection rule, and validation hypotheses.
- A status of `smoke_test_passed`, `inference_completed`, or `blocked`, with evidence and outstanding limitations. A successful smoke test must not be labeled completed scientific inference.

**15-minute acceptance scope:** On a prepared environment, target a validated example smoke-test artifact and run report. Installation and full posterior convergence are not guaranteed within this time. If dependencies, documentation, or runtime prevent completion, report the blocker and elapsed time honestly; do not fabricate results or count a blocked run as success.

## References

- Kyungwook Back and Junsouk Choi. [Bayesian Learning of Spatially Heterogeneous Causal Structure in Spatial Transcriptomics](http://arxiv.org/abs/2611.33094v1), arXiv:2611.33094v1. [Full text](https://arxiv.org/html/2611.33094v1); consult Sections 2–3 for assumptions and posterior inference, and the supplementary material for implementation details.
- [SpaDAG implementation](https://github.com/KyungWookBack/SpaDAG). README inspected during authoring; linked [usage guide](https://github.com/KyungWookBack/SpaDAG/blob/main/docs/usage.md) and [data format](https://github.com/KyungWookBack/SpaDAG/blob/main/docs/data-format.md) could not be fetched during authoring and must be inspected before preparing custom input. Repository availability does not establish successful local installation or execution.
