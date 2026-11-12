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
name: 'pyrite-protein-ligand-pose-ranking'
description: 'Prepare protein-ligand pose pairs, compare Pyrite-style reasoning and feature-based ranking, and evaluate structural selection with target-aware splits and traceable evidence.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Pyrite Protein-Ligand Pose Ranking

## Overview

Prepare candidate pose pairs and evaluate agents that select the more plausible binding configuration for the same protein and ligand. Pyrite introduces 1,500 pose pairs, PyriteRep structural representations, direct comparison through PyriteReasoner, and executable feature discovery followed by logistic regression through PyriteFeaturizer. This skill supports structural pose ranking; its outputs are not affinity predictions or evidence of biological efficacy.

## When to Use This Skill

- Select between docking or cofolding poses for an identical protein-ligand query.
- Compare direct LLM reasoning against learned combinations of structural features.
- Evaluate ranking with held-out targets and inspect the evidence behind individual decisions.
- Reproduce a documented Pyrite evaluation after verifying released data and executable support.

## Core Capabilities

1. **Verify access and scoring before execution.** Open the versioned paper, linked repository, and dataset in References. Record access date, repository commit, dataset revision, licenses, available structures, representation schema, label meaning, and documented entry points. The linked repository and dataset pages were accessible during authoring; this does not establish that every agent implementation or dependency is released. Inspect actual files before constructing commands; never invent a package, CLI, download path, or PyriteRep field. If essential artifacts are missing, report exactly what is unavailable and stop the dependent step.

2. **Prepare comparable pairs.** Assign stable pair, target, ligand, and pose identifiers. Check ligand connectivity, stereochemistry, atom mapping, coordinate units, receptor chains, protonation, missing atoms, and pose-specific receptor coordinates. Compare only candidates for the same query. Preserve original structures and document preparation changes; reject ambiguous mappings rather than silently aligning or repairing them. Use documented reference alignment and symmetry handling when calculating evaluation metrics.

3. **Build traceable structural evidence.** Prefer released PyriteRep records. For custom inputs, record geometry, contacts, clashes, torsional strain, and available physicochemical scores with tool versions, parameters, units, and missing-value indicators. Label independently constructed representations as custom until compatibility is checked. Anchor each decisive observation to pose IDs, ligand atom IDs, receptor chain/residue IDs, and measured values. Distinguish measured contacts from hypothesized interactions; missing scores are not zero. Do not assume an energy score alone identifies the correct pose.

4. **Establish evaluation boundaries.** For reproduction, preserve the paper's pre-AF3 training and post-AF3 evaluation protocol; do not interpret a dataset hosting split named `train` as the scientific split. Inspect split metadata and keep evaluation labels, reference structures, reference-derived metrics, and published predictions out of model inputs. In the released table, fields such as `correct`, `grpo_pred`, and `grpo_correct` must be excluded from predictive features. For an additional target-aware experiment, group all pairs sharing a target, complex, or pose before partitioning; define target identity or sequence-clustering criteria explicitly. Audit homolog and ligand-series overlap. Report this custom protocol separately from the published split.

5. **Run the selected ranking route.** For a Reasoner-style run, supply the two representations and require an A/B decision or explicit abstention with a concise evidence summary. For a Featurizer-style run, generate numerical feature code and fit logistic regression using training data only. Review generated code and execute it with restricted filesystem access, no credentials, bounded runtime, and no network unless explicitly needed for configured LLM subcalls. Fit imputation, scaling, feature selection, and hyperparameters within training folds; freeze them before evaluation. Cache optional subcalls with model and prompt versions. If official implementations are unavailable, identify the result as an independent adaptation rather than a reproduction.

6. **Score ranking and inspect failure modes.** The paper evaluates binary accuracy and counts abstentions as incorrect. Use released labels for benchmark scoring; label derivation involves reference RMSD, lDDT-PLI, interaction recall, and filtering, so verify the full rules before rebuilding labels. Calculate accuracy as correct choices divided by all designated evaluation pairs; report execution failures, abstentions, and exclusions explicitly without silently shrinking the denominator. For unlabeled prospective pairs, provide rankings without accuracy claims. Supplement with target-level accuracy and target-cluster bootstrap intervals, recording the grouping and seed. Compare against a fixed simple baseline on the same pairs. Swap A/B on a diagnostic subset to check order sensitivity, mapping predictions back to original IDs. Explain whether errors concentrate by target, missing evidence, or conflicting scores. Pairwise success does not establish a consistent global ranking; report cycles if aggregating comparisons.

7. **Deliver a bounded, reproducible run.** Aim for a validated smoke run within 15 minutes using available representations and a small, declared subset. Reserve time for schema checks and output validation; stop new model calls before the budget expires. A smoke run is successful only when selected pairs have valid records and scoring is reproducible when labels exist. Report subset size and incomplete work plainly. Full benchmark evaluation, structure regeneration, and GRPO training are separate workloads and must not be claimed complete from a smoke run.

## Inputs / Outputs

**Inputs**

- Released pose-pair records and representations, or candidate protein structures and ligand poses in documented structural formats with stable identifiers.
- Optional reference structures and labels, reserved for evaluation; split metadata and target grouping definitions.
- Ranking route, accessible model or checkpoint, runtime and call budget, and installed chemistry dependencies where feature extraction is needed.
- For training: labeled training pairs, a validation protocol, random seed, and feature-generation configuration.

**Outputs**

- A run manifest containing source revisions, input hashes, preparation choices, schema mapping, split assignments, software/model versions, prompts, seeds, and timing.
- A prediction table with one row per requested pair: pair/target/pose IDs, selected original pose or abstention, execution status, evidence references, and optional probability with calibration status.
- Feature code, feature definitions, preprocessing parameters, and fitted model metadata when the feature-based route is used.
- An evaluation report with numerator and denominator, failure and abstention counts, split-specific metrics, baseline comparisons, overlap audit, order-sensitivity results, and limitations. Mark accuracy unavailable when labels are absent.

Before delivery, check unique pair IDs, complete requested-pair coverage, valid A/B mapping, finite computed features or explicit missing values, and separation of prediction artifacts from evaluation-only data. These are recommended workflow artifacts, not claims about official Pyrite file formats.

## References

- [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents, arXiv:2611.14511v1](http://arxiv.org/abs/2611.14511v1) — source finding and versioned paper.
- [Full paper](https://arxiv.org/html/2611.14511v1) — scoring and splits in Section 3; agent methods in Section 5; pair-filtering details in Appendix A.
- [Paper-linked Pyrite repository](https://github.com/genesistherapeutics/pyrite) — verify current implementation coverage and documented interfaces before execution.
- [Paper-linked Pyrite dataset](https://huggingface.co/datasets/genesisml/pyrite) — verify revision, schema, labels, and access to associated pose artifacts.
