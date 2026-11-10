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
name: 'heimdall-single-cell-tokenization-evaluation'
description: 'Evaluate how tokenization affects single-cell foundation models with Heimdall, reproducing documented comparisons under controlled preprocessing, partitions, model settings, and evaluation tasks.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Heimdall Single-Cell Tokenization Evaluation

## Overview

Use Heimdall to investigate how tokenization influences single-cell foundation-model performance and generalization. This skill turns documented experiments into reproducible comparisons and distinguishes tokenizer effects from differences in data preparation, training, and evaluation. Its 15-minute scope is a bounded smoke evaluation or a validated reproduction plan, not a promise to complete full training.

## When to Use This Skill

- Reproduce a tokenization comparison documented in Heimdall.
- Compare supported tokenization configurations while holding the rest of an experiment fixed.
- Audit whether preprocessing, data leakage, or unequal training budgets explain an apparent tokenizer advantage.
- Assess whether an observed result transfers to held-out donors, studies, tissues, or platforms when suitable metadata and tasks are available.
- Prepare a traceable evaluation plan when data, dependencies, checkpoints, or compute are unavailable.

## Core Capabilities

1. **Resolve the documented experiment.** Read the repository README, relevant configuration files, and task implementation at a recorded commit. Identify the exact tokenizer variants, dataset, task, metrics, dependencies, and execution entry point. Use repository files if hosted documentation is unavailable. Do not infer supported variants, configuration keys, or checkpoint availability from other single-cell models; record missing documentation as a blocker.

2. **Create a controlled comparison specification.** Select at least two documented tokenizer configurations and state the hypothesis before inspecting test results. Record each configuration's vocabulary, gene ordering or selection, expression encoding, sequence limits, padding, masking, and special-token behavior where applicable. Change only the intended tokenization factor; label comparisons with multiple changed factors as compound interventions.

3. **Validate data and preprocessing.** Confirm matrix orientation, gene identifiers, cell identifiers, expression scale, metadata, missing values, and duplicate features. Record filtering, normalization, transformation, feature selection, and identifier mapping in execution order. Preserve a common input dataset across variants; fit learned preprocessing on training data only. Record unavoidable tokenizer-specific transformations and the number of cells or genes they exclude.

4. **Lock partitions and prevent leakage.** Reuse explicit train, validation, and test cell IDs for every variant. Keep donors or studies disjoint when the claimed evaluation concerns transfer across those groups. Tune thresholds, vocabulary fitting, expression bins, feature selection, and model choices without test data. Record known pretraining overlap; if unavailable, mark it unknown and qualify claims about unseen data.

5. **Match model and training conditions.** Hold architecture, initialization policy, objective, optimizer, learning-rate schedule, batch policy, training budget, stopping rule, and seed set constant where compatible. Record parameter-count or compute differences caused by tokenization, including sequence-length effects. Evaluate incompatible tokenizer/checkpoint combinations only with a documented adaptation or retraining procedure; otherwise stop that comparison. A swap into an incompatible pretrained embedding table is not a valid tokenizer ablation.

6. **Execute a bounded reproduction.** Inspect the pinned environment requirements and resolved configuration before running. The repository README provides this cell-type-classification development entry point:

   ```bash
   WANDB_MODE=disabled python train.py +experiments=cta_pancreas
   ```

   Run it only from a compatible checkout after verifying local data paths, resources, and configuration; it is an entry point, not a complete comparison. Derive variant overrides from actual configuration files rather than inventing flags. Use the same bounded cell subset and budget for smoke runs. Separate caches by data, preprocessing, split, and tokenizer configuration, or disable caching through a verified repository option. Preserve commands, exit status, resolved settings, and logs for each variant.

7. **Evaluate matched tasks and generalization.** Use the same task implementation, label mapping, metric definitions, and aggregation rule for all variants. Separate frozen-representation evaluation, fine-tuning, and training from scratch. Report each seed and paired differences where repeated runs exist; do not manufacture uncertainty from one run. For classification, inspect class support and imbalance alongside the documented metrics. Report within-distribution and held-out-domain results separately; a random cell split alone does not establish cross-donor or cross-study generalization.

8. **Produce an auditable conclusion.** Distinguish reproduced results, smoke-test observations, proposed extensions, and failed runs. Explain residual confounding, domain coverage, small subgroup sizes, unknown pretraining overlap, and training-budget limitations. Do not declare a universally best tokenizer or extrapolate to untested species, tissues, assays, or tasks.

### Workflow and completion checks

- **Minutes 0–3:** Resolve the repository revision, documented comparison, input availability, and execution prerequisites.
- **Minutes 3–6:** Produce the comparison specification and check preprocessing, partition integrity, vocabulary compatibility, and shared task settings.
- **Minutes 6–12:** Run a small documented evaluation if feasible, or validate the planned commands and configurations against the checkout. Do not initiate full training merely to meet the time target.
- **Minutes 12–15:** Summarize observed results or blockers and provide a concrete continuation plan. Mark unfinished runs incomplete; never substitute planned values for measured metrics.

A valid output contains a provenance manifest, explicit controls and deviations, and either traceable measured results or a reproduction plan identifying unmet prerequisites. Use `completed`, `smoke_only`, `blocked`, or `incomplete` as the run status. Only `completed` supports a claim that the selected full comparison was reproduced; a plan alone does not establish scientific performance.

## Inputs / Outputs

**Inputs**

- Heimdall repository URL or local checkout and a commit, tag, or revision to resolve.
- A documented experiment and at least two supported tokenization configurations.
- Single-cell expression data in the format required by that experiment, with gene and cell identifiers, labels, and available donor, batch, study, tissue, or platform metadata.
- Explicit data partitions or a justified partition rule, plus preprocessing and model configurations.
- Compatible checkpoints when required, seed set, evaluation mode, compute budget, and output location.

If essential inputs are absent, produce the bounded plan and name the missing inputs. Do not silently download substitutes or describe an alternative dataset as an exact reproduction.

**Outputs**

- **Provenance manifest:** repository revision, environment versions, dataset identifiers or checksums, split identifiers, preprocessing settings, tokenizer settings, model/checkpoint identity, seeds, and execution commands.
- **Comparison specification:** intended variable, fixed controls, task and metric definitions, training budget, and any departures from the documented experiment.
- **Results table:** one row per variant, seed, task, and evaluation domain, with sample counts, metric name, value, direction, elapsed time, status, and log reference. Leave unavailable measurements empty and explain why.
- **Evaluation report:** paired comparisons when available, leakage checks, observed generalization limits, unresolved confounders, and a clear distinction between smoke evidence and full reproduction.
- **Continuation plan when needed:** missing dependencies or artifacts, verified commands, estimated resource needs if known, and the remaining evaluation steps.

## References

- [Heimdall source repository and documented experiment entry points](https://github.com/ma-compbio-lab/Heimdall).
- [Heimdall documentation linked by the repository](https://heimdall-doc.readthedocs.io/en/latest/) — consult when accessible and verify compatibility with the selected revision.
