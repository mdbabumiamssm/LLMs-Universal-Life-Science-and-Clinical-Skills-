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
name: 'venusfactory-protein-engineering-workflows'
description: 'Use VenusFactory2 to translate protein-engineering requests into supported data retrieval, prediction, design, and fine-tuning workflows with validated results and reproducible input and model records.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# VenusFactory Protein Engineering Workflows

## Overview

Use VenusFactory2 to turn a biological question into a supported computational workflow involving protein data, models, and agent tools. This skill guides task selection, input preparation, execution, and validation while preserving enough provenance to repeat the analysis. Treat predictions as computational evidence for experimental prioritization, not demonstrated biological improvement.

## When to Use This Skill

- Retrieve protein sequences, annotations, or existing structures before an engineering analysis.
- Score variants, predict protein properties, or design sequences using an enabled VenusFactory2 model.
- Train and evaluate a custom predictor from labeled protein sequences.
- Convert an exploratory Agent analysis into a repeatable workflow with compatible input and output connections.
- Audit a completed run for missing samples, incompatible checkpoints, or incomplete provenance.

## Core Capabilities

1. **Select the task and execution mode.** Capture the protein accession or sequence, organism, desired property, assay context, constraints, and expected output. Use Agent for exploratory tool selection, Model Plaza for a known predictor, and Workflow for established repeated steps. Route method-development requests to Scientist and literature-integrated reports to Researcher; do not initiate those broader activities unless requested. Consult the deployed manual rather than assuming an older interface. See the [Agent guide](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Agent.md).

2. **Verify model support before execution.** Search the current catalog by function and inspect the selected tool's input contract, parameters, enabled state, dependencies, and available weights. Documented model examples include ProSST, ProtSSN, ESM-1v, ProteinMPNN, LigandMPNN, and dataset-specific predictors such as DeepSol with an ESM2-650M backbone; inclusion in documentation does not establish deployment availability. Distinguish the chat LLM and harness from the protein model and checkpoint. See [Model Plaza](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Models.md).

3. **Retrieve and prepare traceable data.** Resolve ambiguous names using organism and accession before downloading records. Use enabled database tools such as UniProt, RCSB, or AlphaFold DB, preserving accessions, source links, retrieval dates, and releases where available. AlphaFold DB retrieval supplies existing structures; it does not run new AlphaFold inference. Within the VenusFactory Agent sandbox, retrieve through registered tools before local analysis because the sandbox itself has no network access. See [data retrieval and capability boundaries](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Data.md).

   Prepare inputs according to the selected adapter:

   - Sequences: follow its plain-sequence or FASTA contract, retain stable sample IDs, and check length and accepted residue alphabet. Flag unsupported symbols rather than silently changing biological sequences.
   - Tables: identify sequence, feature, target, and ID columns explicitly; retain a mapping from each original row to its processed input.
   - Structures: supply the supported format and confirm chain selection, residue numbering, missing residues, and any required ligand context. Verify each mutation's reference residue against the selected sequence and structure mapping.
   - Labels: record class encoding or regression units. Separate training, validation, and final test data; prevent duplicate leakage and group related proteins when testing generalization across families.

4. **Configure inference or fine-tuning.** For prediction, pair a custom checkpoint with its original backbone, training method, pooling, and label mapping. For training, select the supported method and explicitly resolve epochs, batch size, learning rate, and method-specific settings. The documented online training form supports ESM2-8M with a 10 MB per-file upload limit; verify current deployment limits before submission. Larger or other locally configured models require installed dependencies, weights, and adequate hardware. See [prediction](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Prediction.md) and [training](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Training.md).

5. **Execute a bounded, inspectable run.** Use an existing functioning deployment when possible. For local setup, read installation instructions from the checked-out revision and verify that referenced scripts exist; do not combine commands from conflicting documentation revisions or invent CLI flags or API routes. Select the smallest representative input that can establish the requested operation before a larger batch.

   For repeatable workflows, connect actual compatible ports and set required parameters on every step; card placement alone creates no dependency. Save the definition, submit once, retain the job ID, and follow status and per-step logs. Saving a workflow is not evidence of execution. Inspect a failed step before retrying, since retries create new jobs and can consume online allowance. See [workflow execution](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Workflows.md).

   The 15-minute outcome is a target for a small supported workflow on a prepared environment, not a benchmark or a guarantee for installation, downloads, queue waits, or training. If it cannot finish in that window, report the actual pending or failed state, job identifier, and remaining work; do not report success from submission alone.

6. **Validate outputs against the task.** Require a completed job and readable, nonempty artifacts. Reconcile output identifiers and valid prediction counts with inputs, list failures explicitly, and inspect missing or nonfinite scores, units, score direction, and task-specific constraints. For designed sequences, check requested lengths and fixed positions; for variant rankings, verify mutation mapping before interpreting scores. Never infer that a higher score means improvement without the model's definition.

   Evaluate trained predictors on an independent labeled test set with matching preprocessing and label definitions. Choose metrics appropriate to the endpoint: classification metrics may include MCC, precision/recall, F1, or AUROC when applicable; regression needs error and correlation or ranking measures appropriate to the assay. Compare baselines on the same split and report failed cases and variability where supported. Without independent labels, report artifact validation rather than predictive accuracy. See the [evaluation guide](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Evaluation.md).

7. **Deliver a reproducible record.** Alongside the results, record the following as a run manifest; this is a skill-level reporting convention, not an asserted VenusFactory export schema:

   - Biological objective, endpoint, organism, accession, and constraints.
   - Input file paths, SHA-256 hashes, sample IDs, preprocessing, exclusions, and sequence-to-structure mappings.
   - Database links, retrieval timestamps, and available record or release versions.
   - Repository commit or deployment version; exact protein model identifier, checkpoint revision or hash, and resolved configuration.
   - Chat model and harness separately when used; relevant dependency versions, hardware/device, random seeds where supported, and train/validation/test membership.
   - Actual command or request parameters, saved workflow definition when available, job IDs, timestamps, status, logs, output paths, and output hashes.
   - Validation findings, evaluation metrics actually calculated, limitations, and any next experimental checks.

   Mark unavailable versions or nondeterministic behavior explicitly. Exclude credentials from records. Preserve models and results in the requested workspace; publication is a separate action from completing training or evaluation.

## Inputs / Outputs

**Inputs:** A protein-engineering objective; sequence/accession, FASTA, supported structure, or sample table; optional labeled datasets and split definitions; deployment access; an enabled model or permission to select one; task constraints and resource limits. Training additionally requires a defined target and enough suitable data to support evaluation.

**Outputs:** A task-to-tool selection with resolved parameters; retrieved data and provenance where requested; prediction tables, variant rankings, designed sequences, or training checkpoints as applicable; completed-job evidence and logs; a validation summary; and a reproducibility manifest. Include a saved workflow definition when the task requires reuse. Report blocked, queued, or failed execution explicitly instead of fabricating results.

**Completion criterion:** The selected small workflow finishes, artifacts open successfully, identifiers and constraints reconcile with inputs, and the validation summary and manifest identify the exact data and model used. A prepared configuration or queued job alone does not meet this criterion.

## References

- [VenusFactory2 source repository and README](https://github.com/ai4protein/VenusFactory2).
- [Documentation index](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Home.md).
- [Model catalog and availability](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Models.md).
- [Agent usage](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Agent.md) and [data retrieval](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Data.md).
- [Training](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Training.md), [prediction](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Prediction.md), and [evaluation](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Evaluation.md).
- [Reusable workflows](https://github.com/ai4protein/VenusFactory2/blob/main/docs/wiki/Workflows.md).
- [Self-evolving AI agents for protein discovery and directed evolution](https://arxiv.org/abs/2603.27303), 2026; paper linked by the repository citation.
