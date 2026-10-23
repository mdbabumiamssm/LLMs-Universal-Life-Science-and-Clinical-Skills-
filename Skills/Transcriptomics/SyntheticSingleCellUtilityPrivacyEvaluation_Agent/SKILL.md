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
name: 'synthetic-single-cell-utility-privacy-evaluation'
description: 'Compare synthetic single-cell RNA-seq methods using donor-separated utility and membership-inference evaluation, with explicit HVG scope, non-HVG reconstruction, and computational limits.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Synthetic Single-Cell Utility and Privacy Evaluation

## Overview

Evaluate donor-linked synthetic single-cell RNA-seq datasets across statistical fidelity, biological preservation, and membership-inference vulnerability. Use the OneK1K benchmark as a methodological reference while explicitly tracking gene coverage, reconstruction choices, and compute budgets. Synthetic generation and weak performance by a tested attacker do not establish a privacy guarantee.

## When to Use This Skill

- Compare scGFT, scLDM, Cell2Sentence, or other generators against a simple independent Poisson baseline.
- Audit whether highly variable gene (HVG) restriction hides losses or leakage elsewhere in the transcriptome.
- Compare non-HVG reconstruction strategies under consistent utility and attack settings.
- Review synthetic-data sharing candidates for donor leakage and preservation of biological structure.
- Produce a bounded evaluation of existing synthetic outputs when full training is too expensive.

## Core Capabilities

1. **Verify evidence before reproducing a benchmark.** Read the complete versioned paper, methods, tables, and available evaluation code before adopting metric definitions or conclusions. Record version, access date, and unresolved implementation details; if full text is unavailable, label the supplied summary as unverified and produce a provisional protocol rather than a reproduction claim.

   The verified v1 report uses GAN-leaks and reports fidelity, clustering, and attack metrics. Its scLDM experiment uses 1,000 HVGs; scGFT uses 1,118. Cell2Sentence covers only 1% of cells with 200 genes per cell and has no entry in the privacy table. Copied non-HVGs leak strongly in the reported scGFT setting; Poisson replacement reduces measured leakage. These are configuration-specific observations, not universal rankings. See the benchmark in References.

2. **Establish donor-separated evaluation.** Require donor identifiers and assert disjoint donor sets for generator training, validation, and final testing. Split donors before fitting HVG selection, population normalization parameters, embeddings, reconstruction rates, or model selection. Keep final test data out of tuning. If donor identifiers are missing, report that donor separation cannot be verified rather than substituting a random cell split.

   Validate unique cell and gene identifiers, matrix dimensions, count versus transformed layers, finite values, and label availability. Record donor and cell counts by split and cell type. Keep sensitive identifiers in the controlled evaluation environment; report aggregate diagnostics.

3. **Compare explicit method configurations.** Treat each generator, seed, hyperparameter setting, and non-HVG strategy as a distinct configuration. Record generated cell counts, conditioning labels, checkpoint provenance, pretrained-data overlap uncertainty, gene masks, normalization, clipping, and rounding. Check that conditional outputs match their labels and that any unconditional samples are handled explicitly.

   Build an independent Poisson baseline with rates estimated from training data only. Specify whether rates are global per gene or conditional on cell type; disclose fallback rules for sparse or unseen types. Distinguish full-matrix baseline generation from Poisson completion of a generator's non-HVGs. Audit existing copied-value outputs as leakage controls; do not recommend them for release.

4. **Evaluate comparable gene spaces.** Align real and synthetic matrices by gene identifiers and order, never by shape alone. Evaluate HVG-only, non-HVG-only, and reconstructed full-gene outputs separately when available. Use a common gene intersection and matched cell sampling for direct comparisons, alongside each method's native-space results. Missing genes are unmeasured, not automatically biological zeros. Record gene counts, detected-gene coverage, and excluded cell types; do not label an HVG-only score as full-transcriptome performance.

5. **Measure statistical and biological utility.** The benchmark lists Spearman/Pearson correlation, MMD, EMD, gene-correlation preservation, LISI, and clustering ARI. Recover their exact definitions from the evaluation implementation before claiming replication. Freeze transformations, aggregation rules, distance scales, MMD kernels, embeddings, and clustering parameters across comparable configurations; otherwise label metrics as local alternatives.

   As additional local diagnostics, compare library sizes, zero fractions, gene means and variances, cell-type proportions, and marker patterns. Evaluate within cell type as well as globally to expose composition effects. Use biological labels for joint real/synthetic clustering assessment when available. Pairwise real-versus-synthetic ARI requires genuine cell correspondence: the paper flags ordering sensitivity for scLDM. Do not invent pairings for independently generated cells. UMAP appearance or marginal correlation alone is insufficient evidence of biological preservation.

6. **Test a stated membership threat model.** Declare whether the attacker predicts cell membership or donor membership, what data and model access it has, and which attack scores it computes. Training members and held-out nonmembers must have known provenance and comparable cell-type, batch, and sampling distributions. Calibrate thresholds and any score-direction choices on separate attack-validation data, never on final attack labels.

   Report ROC-AUC, average precision, PR-AUC, and accuracy only with their definitions, membership prevalence, score direction, and threshold-selection rule. Do not conflate average precision with integrated PR-AUC. Chance ROC-AUC is 0.5; precision-based baselines depend on member prevalence. Test sensitivity to gene subset and transformation, and report donor-stratified behavior. Cell-level results do not establish donor-level protection; define and validate donor score aggregation separately if needed. Use donor-resampling uncertainty estimates when feasible because cells from one donor are correlated.

   Interpret near-chance results as limited evidence for the specified attack and configuration. Poisson rates can retain information about their training population, and a weak attack can miss leakage. Claim differential privacy only when an actual mechanism and its privacy accounting, adjacency definition, and parameters are documented.

7. **Deliver a bounded, reproducible comparison.** Use existing outputs or checkpoints for the 15-minute workflow. Allocate approximately three minutes to provenance and split checks, eight to feasible metrics and attacks, and four to interpretation and reporting. Use sparse or chunked operations and a fixed donor-aware subsample if needed; avoid unbounded dense pairwise matrices. Record hardware, versions, seeds, runtime, peak memory when measurable, and sampling fractions.

   Reserve time to return completed results and explicit omissions. Full generator training or cohort-wide attacks may require a separate run; a timed-out or skipped test is not a passing result. Report utility and privacy side by side without an unexplained composite score. Mark configurations as comparable, scope-limited, or not assessed, and state which uncertainty prevents a stronger conclusion.

## Inputs / Outputs

**Inputs**

- Real expression matrices, preferably AnnData with an identified raw-count layer, gene identifiers, donor identifiers, cell-type labels, and split manifests.
- Synthetic outputs for each method, configuration, and seed, including HVG masks and non-HVG reconstruction provenance.
- Generation logs or checkpoint metadata, preprocessing settings, reference benchmark version, and available evaluation implementation.
- Compute/time budget, intended biological use, and attacker access assumptions. Missing artifacts must be recorded before evaluation begins.

**Outputs**

- A provenance and validation record covering donor disjointness, gene alignment, transformations, model provenance, and unresolved evidence gaps.
- A comparison table with one row per configuration, evaluation space, and sampling scope: method, seed, cell/donor/gene counts, reconstruction strategy, utility metrics, attack metrics, uncertainty, runtime, and status.
- A metric specification stating formulas or implementation references, aggregation, score direction, calibration, membership prevalence, and missing-label limitations.
- A concise interpretation identifying utility/privacy trade-offs, suspected copying or leakage, unsupported comparisons, and remaining experiments. Separate measured observations from benchmark findings and proposed follow-up work.

**Completion criteria:** deliver these outputs within the bounded run, with every reported metric tied to its data space and protocol. Use `not assessed` with a reason for missing results. If inputs or runtime prevent evaluation, return a clearly marked incomplete assessment and executable next-step protocol; do not claim successful empirical validation or authorize data release.

## References

- [Benchmarking Recent Single-Cell Synthetic Data Generation Methods on the OneK1K Dataset, arXiv:2610.31454v1](http://arxiv.org/abs/2610.31454v1), Buse Giledereli, Basar Temiz, and Amirreza Sattarzadeh Khanehbargh (2026). [Complete versioned text](https://arxiv.org/html/2610.31454v1), inspected 2026-10-23; Sections 2–4 and Tables 1–3 inform the benchmark-specific observations above. Additional evaluation safeguards are workflow recommendations, not claims that the paper implemented them.
