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
name: 'bioscore-pathology-foundation-model-evaluation'
description: 'Evaluate biological representations in pathology image encoders using BioScore, sparse features, and spatial transcriptomic cell-identity references alongside downstream task metrics.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# BioScore Pathology Foundation Model Evaluation

## Overview

Assess which marker-defined cell identities pathology encoders represent using same-tissue spatial transcriptomics and unsupervised sparse autoencoders. BioScore complements classification and retrieval evaluation with biological alignment and specificity, including a breakdown across 52 identities in the supplied finding.

## When to Use This Skill

- Compare biological representations across pathology foundation models.
- Audit identity-specific strengths and weaknesses behind aggregate rankings.
- Prepare paired histology and spatial transcriptomics for biological evaluation.
- Review a proposed BioScore reproduction or adaptation before expensive computation.

## Core Capabilities

1. **Verify implementation readiness.** Read the pinned paper and inspect any available benchmark release before executing. Version 1 promises code and panel upon publication; the cited `dictionary_learning` repository supplies SAE components, not the complete benchmark. Verify its `BatchTopKSAETrainer` and checkpoint interfaces against the installed revision. Never invent a BioScore package, executable, or release URL.

2. **Audit inputs and spatial alignment.** Check specimen identifiers, coordinate units, registration transforms, tissue masks, patch boundaries, gene symbols, and measured-gene coverage. Confirm embedding rows and transcript-count rows reference identical patches. Reject mismatched coordinates or duplicate identifiers; distinguish unmeasured genes from measured zeros. Record encoder checkpoint, embedding extraction, normalization, and spatial resolution so comparisons use equivalent tissue fields.

3. **Recover the exact benchmark configuration.** The paper uses 224-pixel patches at 20×, frozen encoders, and BatchTopK SAEs with 8× expansion and k=64. Features become 3,000 groups through weighted spherical k-means of normalized decoder atoms; group maps are activation shares. Its reference uses depth-adjusted marker signatures and per-patch maxima across eligible signatures. Matching uses Pearson correlation, impurity U, and Q=ρ−3U; maximize Q per identity and average within five lineage classes, then across classes. Five seeds (40–44) provide mean and standard deviation; seed-averaged identity qualities support paired Wilcoxon tests with Holm correction. Follow Sections 3–5 and appendices for equations, masks, training, and panel curation. [Methods](https://arxiv.org/html/2611.34930v1)

4. **Execute a bounded evaluation.** Within 15 minutes, validate readiness and, when cached compatible artifacts permit, score a declared subset. Otherwise return an actionable readiness report with missing artifacts, estimated compute needs, and the next executable step. A full reproduction is not promised within this budget. Keep transcript references out of encoder/SAE optimization. Record any overlap between SAE training sections and scoring sections; do not describe such a run as held-out generalization.

5. **Compare models reproducibly.** Freeze the cohort, eligible identities, extraction rules, and analysis configuration before comparing encoders. Preserve per-identity support counts and paired differences. Explicitly flag deviations from the published recipe and keep exploratory subsets separate from reproduction results. Specify the multiple-comparison family; do not infer that a nonsignificant comparison proves equivalence. If adding a supervised probe, fit preprocessing only on training folds and split by specimen rather than neighboring patches.

6. **Validate and interpret results.** Check finite embeddings, reconstruction diagnostics, active-feature counts, group coverage, and reproducible seed handling. Flag zero activation denominators and constant maps instead of silently replacing undefined correlations with zero. Verify score aggregation independently on a small worked example. Inspect matched spatial maps for registration artifacts and broad tissue-composition effects. Treat spatial association as evidence about representations, not causal biology or clinical accuracy; missing marker coverage cannot establish an encoder's failure to represent an identity.

## Inputs / Outputs

**Inputs**

- Registered H&E images and spatial transcript counts, or cached patch embeddings with matching coordinates and count matrices.
- Specimen/section manifest, tissue masks, spatial calibration, gene-panel metadata, and marker-signature definitions with provenance.
- Encoder identifiers and checkpoints, SAE configuration/checkpoints, grouping artifacts, seeds, software revisions, and available compute budget.
- Verified scoring implementation and panel for exact reproduction; document missing dependencies when only a readiness assessment is possible.

**Outputs**

- A run manifest identifying inputs, versions, configuration, exclusions, and deviations.
- A status of `completed`, `subset_only`, or `blocked`, with concrete reasons and next steps. Never report an unexecuted score as measured.
- When computed, an identity-level table containing encoder, seed, identity, matched group, correlation, impurity, quality, and contributing sections/patches.
- Aggregate and lineage summaries, seed variability, and paired comparison results with correction scope.
- Matched-group/reference-map visualizations when available, plus limitations concerning registration, marker specificity, tissue coverage, spatial dependence, and cohort transfer.

Success means a traceable evaluation or explicit readiness report within the time budget. Label reduced-cohort results as adaptations, and do not present their scores as directly interchangeable with the published benchmark.

## References

- [A gene informed benchmark for BioScoring of pathology foundation models, arXiv:2611.34930v1](http://arxiv.org/abs/2611.34930v1) — supplied source finding.
- [Full methods and appendices](https://arxiv.org/html/2611.34930v1) — scoring equations, panel construction, comparison protocol, and release statement.
- [dictionary_learning](https://github.com/saprmarks/dictionary_learning) — SAE implementation cited by the paper; inspect the pinned revision before use.
