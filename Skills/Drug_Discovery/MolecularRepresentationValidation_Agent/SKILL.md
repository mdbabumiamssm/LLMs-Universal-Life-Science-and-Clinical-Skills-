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
name: 'molecular-representation-validation'
description: 'Audit molecular fingerprints and learned embeddings for structural, shape, and ADMET similarity, degeneracy, and implications for clustering, dataset splitting, and screening.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Molecular Representation Validation

## Overview

Evaluate molecular representations beyond downstream prediction scores using reproducible comparisons. The cited study motivates separate checks of similarity and representation degeneracy; its findings apply to the tested settings, not every future model.

## When to Use This Skill

- Selecting a representation for a molecular dataset.
- Reviewing clustering or train/test partition quality.
- Investigating indistinguishable screening candidates or surprising similarity rankings.
- Auditing whether a proposed embedding improves on available baselines.

## Core Capabilities

1. **Establish reproducible baselines.** Compare embeddings with ECFP4, FCFP4, atom-pair and topological-torsion fingerprints; include physicochemical descriptors for ADMET comparisons.
2. **Detect degeneracy.** Group distinct molecular identities sharing identical representations. Report affected molecules and group sizes; distinguish duplicates from collisions. Identical inputs constrain a deterministic screening predictor to identical outputs.
3. **Check graph fidelity.** Correlate representation similarity with normalized weighted MCES distance using Spearman correlation. Keep exact distances separate from censored lower bounds.
4. **Inspect clustering and splitting.** Measure close graph neighbours assigned to different clusters or partitions, alongside singleton fractions and cluster sizes. Representation similarity alone cannot independently establish structural separation.
5. **Check 3D fidelity.** Compare similarity with conformer-based shape and pharmacophoric overlap. Examine broad similarity ranges and narrow bins separately; report conformer failures.
6. **Check endpoint fidelity.** Compare median endpoint differences among increasingly similar pairs. Restrict comparisons to compatible assays and flag overlap with embedding training data.

### Execution workflow

- Establish the requested application, available inputs and runtime budget before computing. Use cached embeddings and reference measurements where available; select a seeded, bounded pilot that can finish within 15 minutes. This budget is an operational target, not a full-paper replication claim.
- Record dataset version, molecule identifiers, preprocessing, stereochemistry policy, exclusions, software versions, model checkpoint, fingerprint settings, descriptor scaling and similarity definitions. Use the same eligible molecules for comparisons and disclose coverage lost through filtering.
- Select applicable capabilities above. Read the paper Methods and linked implementation before reproducing a metric; record departures explicitly. Do not silently substitute another graph or shape metric and label it a reproduction.
- Set pair counts, sampling rules and computation limits in advance. Preserve sampled identifiers. Treat unavailable labels, conformers, checkpoints or reference distances as explicit limitations rather than fabricated values. Stop expensive calculations at the budget and report completed coverage.
- Produce task-specific recommendations supported by the measured comparisons. Separate observations on the supplied data from published conclusions. Do not infer universal superiority or extrapolate sample collision counts to an entire library.

## Inputs / Outputs

**Inputs:** Molecular structures with stable identifiers; candidate representation settings or cached vectors; intended application; optional assay values, conformers, graph distances, cluster labels and split assignments; runtime and sampling constraints.

**Outputs:** A concise audit report containing the run configuration, eligibility counts, per-representation results, representative failure pairs or collision groups, and application-specific limitations. Include metric definitions, denominators, sample identifiers and completion status for each requested check.

**Valid completion:** Every reported result is traceable to inputs and settings; missing checks are marked with reasons. If inputs prevent evaluation, return an explicitly incomplete audit with the required next inputs, not a successful validation claim.

## References

- Acer Blake, Fergus Imrie and Charlotte M. Deane. *On the limitations of molecular representations*, arXiv:2611.08420v1: http://arxiv.org/abs/2611.08420v1. Full text and Methods: https://arxiv.org/html/2611.08420v1.
- Paper-linked code and data: https://github.com/oxpig/On-the-limitations-of-molecular-representations.
