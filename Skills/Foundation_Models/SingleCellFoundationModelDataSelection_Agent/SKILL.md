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
name: 'single-cell-foundation-model-data-selection'
description: 'Audit and reproduce single-cell foundation-model data-selection experiments, documenting pretraining size, diversity, splits, and zero-shot or fine-tuned performance under controlled budgets.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Single-Cell Foundation Model Data Selection

## Overview

Use the scFM-dataselection workflow to investigate how pretraining dataset size and composition affect single-cell model performance. Audit data provenance, sampling, evaluation splits, and training budgets so comparisons separate selection effects from confounding changes. The 15-minute outcome is a reproducibility audit and experiment specification, optionally accompanied by a small validation run when dependencies and data are already available; full downloads and model training require a separate resource budget.

## When to Use This Skill

- Reproduce or inspect scFM-dataselection experiments on pretraining size and diversity.
- Compare uniform random sampling, cell type reweighting, and geometric sketching.
- Document which cells, donors, tissues, studies, and cell types enter each subset.
- Compare zero-shot and fine-tuned cell type classification or batch integration results.
- Investigate whether apparent improvements reflect data selection, leakage, preprocessing, or unequal training effort.

## Core Capabilities

1. **Verify the implementation and choose a bounded workflow.** Record the repository commit, selected model family, task, and available local artifacts. The repository describes scVI, SSL, and Geneformer, with separate `pretraining`, `finetuning`, and `eval` directories. Inspect the selected implementation before constructing commands; a directory name or saved notebook output is not evidence of a completed experiment.

2. **Inventory notebooks and dependencies.** Confirm notebook paths at the selected revision. Verified examples in `plotting` include `pretraining_dataset_sizes.ipynb`, `lineplots.ipynb`, and `heatmaps.ipynb`; these are analysis artifacts, not a substitute for model execution. Inspect notebook input paths, kernel requirements, and result schemas before running cells. Read `requirements.txt` and the model-specific setup instructions; preserve required fork revisions and the documented SSL branch when reproducing the original environment.

3. **Establish data access and composition.** Inspect `data/preprocess/README.md`, `download_sctab.py`, and `features.parquet` for scTab acquisition and feature definitions. Check evaluation downloads separately: the documentation identifies a manual download route for the COVID dataset. Record source release, access status, license constraints, cell and gene counts, raw versus transformed layers, gene identifiers and ordering, and metadata availability. Verify actual file access before calling inputs ready; do not initiate a full corpus or checkpoint download merely to complete the audit.

4. **Trace split construction and leakage risks.** Inspect sampling callers and `downsampling/train_val_test_split.py`. Its helper shuffles supplied cell indices and returns `(train, test, val)`; its command-line driver is commented out, so running that file alone does not generate splits. Do not interpret random cell partitions as donor- or study-held-out evaluation. Check unique cell IDs, pairwise split intersections, donor/study overlap, label coverage, and overlap between pretraining and downstream test data. Record unknown overlap explicitly. Preserve original splits for reproduction; label any donor-disjoint redesign as a new experiment.

5. **Specify size and diversity contrasts.** Use the implementations referenced by `downsampling/README.md` for random sampling, cell type reweighting, and geometric sketching. Record requested and realized subset sizes, seeds, sampling weights, replacement policy, and selected cell IDs. Compare methods at matched realized sizes and report cell type, tissue, donor, and study distributions where available. Inspect the HVG and PCA fitting population used by geometric sketching; disclose evaluation-data exposure. For a new controlled experiment, freeze evaluation splits and fit selection transforms on eligible training data only. Do not claim independently sampled subsets are nested.

6. **Control preprocessing and training effort.** Verify each model's input contract, including count normalization, log transformation, feature alignment, missing-gene handling, and tokenization where applicable. Keep preprocessing fixed within each model comparison. Specify either reproduction of upstream schedules or a new budget-matched design; record optimizer steps, effective batch size, examples processed, early stopping, and hardware time. Equal epochs across differently sized datasets do not imply equal compute. Match fine-tuning splits, label access, and tuning budgets across compared checkpoints.

7. **Execute only verified entry points.** Inspect script argument parsing and local paths before using README commands: examples contain inconsistent variable names such as `OUTPUTPATH` versus `OUTPUPATH` and `METHOD` versus `method`. Resolve these against source code rather than guessing an interface. With prepared inputs, run one small selection or evaluation check, retain logs, and verify finite outputs and expected dimensions. Keep a smoke test clearly labeled; it does not reproduce the full study. If prerequisites are missing or the time budget is insufficient, return the audit with exact blockers and the next verified action.

8. **Compare and report downstream evidence.** Keep zero-shot and fine-tuned results separate and document any trained classifier or probe used with frozen embeddings. Use metric definitions from the selected evaluation code, including direction, aggregation, and evaluated cell counts. Report individual seeds and variability when replicates exist, include available matched baselines, and distinguish batch mixing from biological signal preservation. Link each score to its checkpoint, subset, split, and log; leave missing measurements empty with a reason. Do not infer a universal optimal dataset size or diversity strategy from a single task or model.

## Inputs / Outputs

**Inputs**

- Repository revision or checkout, model family, downstream task, and reproduction or new-experiment intent.
- Accessible scTab or user-supplied single-cell data, feature definitions, stable cell IDs, and available donor/study/tissue/cell-type metadata.
- Sampling methods, target sizes, seeds, split definitions, and permitted compute/time budget.
- Optional compatible checkpoints and evaluation outputs for analysis without retraining.

**Outputs**

- A reproducibility report listing verified files, dependency requirements, data access, split behavior, uncertainties, and blocking prerequisites.
- A dataset manifest with source/version, method, seed, requested and realized cell counts, feature schema, composition summaries, split identifiers, and overlap checks.
- An experiment matrix mapping each subset to model, preprocessing, training budget, evaluation regime, checkpoint, and metric definition.
- When execution is feasible, validation logs and a comparison table with measured scores, replicate counts, and provenance; otherwise an explicit unexecuted plan without invented results.

**Completion criteria:** Within 15 minutes, produce the audit and experiment matrix with every prerequisite marked verified, missing, or unknown. A valid audit may report blocked execution, but must not claim successful training or reproduction. Any reported numerical result must trace to an inspected artifact or completed run; any split advertised as disjoint must have a recorded overlap check.

## References

- [scFM-dataselection source repository](https://github.com/microsoft/scFM-dataselection) — primary implementation and experiment overview.
- [Data acquisition and preprocessing](https://github.com/microsoft/scFM-dataselection/blob/main/data/preprocess/README.md) — scTab and evaluation data requirements.
- [Downsampling workflow](https://github.com/microsoft/scFM-dataselection/blob/main/downsampling/README.md) — sampling methods and data preparation.
- [Split helper implementation](https://github.com/microsoft/scFM-dataselection/blob/main/downsampling/train_val_test_split.py) — cell-index partitioning and return order.
- [Plotting notebooks](https://github.com/microsoft/scFM-dataselection/tree/main/plotting) — result visualization artifacts to inspect before execution.
