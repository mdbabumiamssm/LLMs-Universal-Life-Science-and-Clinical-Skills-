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
name: 'molecular-representation-auditing'
description: 'Audit fingerprints and learned molecular embeddings for collisions and preservation of graph, shape, and endpoint similarity before clustering, dataset splitting, or virtual screening.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Molecular Representation Auditing

## Overview

Audit molecular representations against their intended use by comparing fingerprints, physicochemical descriptors, and available learned embeddings on the same molecules. The source finding motivates examining graph structure, three-dimensional shape, and endpoint similarity alongside downstream performance, because both learned representations and classical fingerprints have limitations. Produce a reproducible, bounded audit with explicit coverage gaps and use-specific recommendations.

## When to Use This Skill

- Selecting representations or similarity measures for molecular clustering or diversity selection.
- Designing dataset splits and checking structural overlap across partitions.
- Preparing ligand-based virtual screening or nearest-neighbor retrieval.
- Investigating identical encodings, unstable neighbors, or unexpectedly similar scores for distinct molecules.
- Comparing a learned embedding with classical baselines beyond a narrow prediction benchmark.

## Core Capabilities

1. **Establish evidence and scope.** Retrieve the versioned full paper in References before attributing exact metrics, protocols, or conclusions to it. Verify the title and version; if full text is unavailable, label the evidence as abstract-only and avoid detailed paper-specific claims. The checks below are an operational audit design, not a claim to reproduce the paper. Record the intended application, dataset population, available compute, and acceptance criteria before examining results.

2. **Prepare consistent molecular identities.** Validate molecular inputs and retain stable source identifiers. Document salt handling, charge normalization, aromaticity, tautomer policy, and stereochemistry; retain a mapping from original records to standardized structures. Separate duplicate records and standardization-induced merges from distinct structures with identical representations. Report parsing failures and exclusions rather than silently dropping them.

3. **Construct reproducible comparisons.** Use a common molecule set for available fingerprints, physicochemical descriptors, and candidate embeddings, while reporting coverage for each representation. Record fingerprint family, radius or path settings, bit length, counts versus bits, and chirality settings; descriptor names and scaling; and embedding checkpoint, pooling, preprocessing, precision, and normalization. Record software versions, input checksums, seeds, sample identifiers, distance functions, and commands sufficient to rerun the audit. Fit preprocessing only on training data when evaluating a split.

4. **Detect representation collisions.** Group distinct standardized structures by exactly equal representation vectors; confirm vector equality after hash-based grouping. For N distinct structures and G unique vectors, report N, G, the number of groups with size greater than one, the number of structures in those groups, and their fraction of N. Keep N minus G separate from the number of affected structures. For embeddings, distinguish exact collisions from near-collisions under a declared tolerance and distance; reject nonfinite vectors and handle zero vectors explicitly. Inspect representative colliding pairs, including stereoisomers where available. Do not infer full-library collision rates from a convenience sample or equate zero observed collisions with uniqueness.

5. **Assess graph and neighborhood fidelity.** Define an independent structural reference, such as a bounded maximum-common-substructure comparison with explicit atom, bond, and stereochemistry rules. Record timeouts as missing measurements. Compare representation neighbors against that reference using declared top-k overlap and rank agreement on a fixed pair sample. Use binary Tanimoto for compatible fingerprints and documented cosine or Euclidean distances for embeddings or scaled descriptors; specify conventions for zero vectors and empty fingerprints. Include close analogs and diverse molecules, inspect discordant pairs, and avoid treating one fingerprint as universal structural ground truth.

6. **Assess shape and endpoint fidelity.** When conformers exist, document their source or generation seed, protonation state, alignment method, conformer budget, and ensemble aggregation before comparing representation similarity with aligned shape overlap. Treat generated conformers as a modeling assumption, not experimental truth. For ADMET endpoints, compare neighbors within a single compatible assay and unit system: use absolute differences for continuous measurements or label agreement for categorical measurements, with endpoint-specific denominators and missingness. Keep censored values and assay context explicit; do not pool incompatible endpoints into a universal similarity score. Mark unavailable shape or endpoint checks as not assessed.

7. **Translate findings into application decisions.** Evaluate the intended use directly, retaining molecule identifiers for failure examples.

   - For clustering, report sensitivity to representation, seed, and clustering settings, together with structural coherence assessed independently of the clustering distance. Separate algorithm instability from representation effects.
   - For dataset splitting, check duplicate identities, collision groups, and close structural neighbors across partitions. Report cross-partition overlap without equating all similarity with leakage; judge it against the intended generalization task. Keep model tuning and threshold selection separate from held-out evaluation.
   - For virtual screening, inspect tied rankings, collision groups, retrieval diversity, and relevant shape or endpoint disagreement. Use enrichment or ranking performance only when suitable labels and an explicit evaluation population exist; unlabeled molecules are not confirmed negatives. Preserve distinct molecular identities in tied groups.

8. **Deliver a bounded, reviewable audit.** Target a completed pilot report within 15 minutes using installed tools, cached embeddings, and a deterministic subset sized to available resources. Allocate approximately two minutes to scope and evidence, three to preparation, seven to checks, and three to reporting; these are workflow budgets, not performance claims. Bound pair counts, conformer generation, and graph comparisons instead of launching exhaustive all-pairs computations or training new models. If a required resource is missing or a computation exceeds its budget, return partial results with the blocker and a concrete continuation procedure. Never label an incomplete audit as a passed scientific assessment.

## Inputs / Outputs

**Inputs**

- Molecule table or structure file containing stable IDs and SMILES or molecular graphs; optional conformers and assay measurements with units and provenance.
- Intended application, candidate representations or precomputed vectors, available checkpoints, and current clustering, splitting, or retrieval settings.
- Resource budget, sampling constraints, and application-specific acceptance criteria. If criteria are absent, report comparative findings without inventing pass thresholds.

**Outputs**

- Audit report identifying scope, evidence status, examined population, sample selection, exclusions, and elapsed time.
- Reproduction manifest containing dataset and checkpoint identifiers, representation settings, preprocessing, software versions, seeds, distance definitions, sample IDs, and execution commands.
- Comparison table with one row per representation: valid coverage, exact-collision counts and denominators, near-collision definition, graph fidelity, shape fidelity, endpoint fidelity, and runtime. Label every check as completed, not assessed, or failed with a reason.
- Inspectable examples of collisions, discordant neighbors, and relevant cross-partition overlap, linked to original molecule IDs.
- Separate recommendations for each requested application: supported within the audited scope, limited, or insufficient evidence. State mitigations such as retaining original structures, using a complementary representation, or conducting additional shape checks; do not claim that increasing fingerprint length necessarily eliminates all collisions.

**Completion criteria:** A valid workflow output contains the manifest, comparison table, failure examples where observed, and scoped recommendations. Identify descriptive pilot results as such; any uncertainty estimate must state its sampling unit and method, accounting for dependence among pairs sharing molecules. Missing labels, conformers, or embeddings must remain visible limitations rather than successful checks.

## References

- [On the limitations of molecular representations — source finding, arXiv:2611.08420v1](http://arxiv.org/abs/2611.08420v1).
- [Versioned full text](https://arxiv.org/html/2611.08420v1): consult methods and supplementary material before reproducing or attributing exact experimental choices.
