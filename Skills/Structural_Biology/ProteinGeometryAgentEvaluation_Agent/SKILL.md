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
name: 'protein-geometry-agent-evaluation'
description: 'Evaluate protein-structure agents by separating metadata lookup from coordinate geometry, fixing structure selections and tool conditions, and comparing repeated runs with uncertainty.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Protein Geometry Agent Evaluation

## Overview

Evaluate structural-biology agents with reproducible coordinate calculations, explicit atom selections, and controlled execution conditions. ProteinGeoBench reports that metadata retrieval and numeric geometry can differ substantially, while task composition, repeated runs, access conditions, and harness choices complicate model comparisons ([source finding](http://arxiv.org/abs/2610.26829v1)). Use these findings as research evidence motivating the workflow, not as guaranteed performance for a new model or dataset.

## When to Use This Skill

- Compare agents answering questions about protein structures.
- Diagnose correct metadata answers paired with incorrect distances, angles, contacts, or structural alignments.
- Audit whether structure selection, residue numbering, or alternate conformations explain a failure.
- Compare network access or agent harness configurations under matched task and grading conditions.
- Reproduce a published evaluation or prepare a small, auditable pilot before a larger study.

## Core Capabilities

1. **Verify assets and define the evaluation scope.**
   Read task instructions, coordinate files, answer specifications, and verifier logic before running an evaluation. For ProteinGeoBench, begin with the repository linked from the paper, pin a commit, and verify the selected task assets and their dependencies; a repository listing alone does not establish that a task runs. Record task IDs, source URLs, retrieval dates, file hashes, and verifier version. Do not invent repository paths, commands, task IDs, ground truth, or expected outputs. Document executable examples only after inspecting their actual inputs and verifying the invocation. If assets are unavailable, return an asset-validation report and blocked execution status.

2. **Separate task families before observing scores.**
   Label each task as metadata lookup, coordinate calculation, or mixed, with a short rationale. For mixed tasks, score independently defined components when possible and retain the original benchmark score separately. Fix the task subset, family weights, numeric tolerances, repeat count, timeout, and failure policy in advance. Preserve published labels when reproducing the benchmark; identify any local relabeling as a separate analysis.

3. **Resolve structures and atom identities explicitly.**
   Record the accession or local filename, coordinate format and hash, experimental or predicted origin, model identifier, and biological assembly versus asymmetric unit. Select chains using a declared identifier namespace; for mmCIF, retain the mapping between author and label chain/residue identifiers. Identify residues by chain, residue number, insertion code, and residue name, then identify each atom by name and alternate-location identifier.

   Declare treatment of alternate conformations, occupancies, missing residues or atoms, hydrogens, waters, ligands, and symmetry-generated copies. Select a consistent conformer rather than mixing incompatible alternate atoms. For multiple models, select one explicitly or calculate per-model values and report the aggregation rule. Never silently substitute another chain, residue, atom, assembly, or structure revision. Report ambiguous or absent selections as such.

4. **Compute reference geometry reproducibly.**
   Parse the selected coordinates with a recorded library and version. Retain the selected atom identifiers and coordinate values alongside the calculation, units, and precision. Do not replace a requested coordinate measurement with an annotated or literature value.

   | Quantity | Calculation contract |
   | --- | --- |
   | Distance | Euclidean norm of the difference between two specified coordinates; report in angstroms. |
   | Angle | Angle between vectors from the middle atom; clamp numerical cosine values to the valid range and reject zero-length vectors; report degrees. |
   | Dihedral | Signed torsion from four ordered atoms using a documented convention; reject degenerate geometry and compare with circular angular error. |
   | Contacts | State atom sets, cutoff, strict or inclusive boundary, excluded covalent or sequence neighbors, and whether counts represent atom pairs or unique residue pairs. |
   | RMSD | Specify atom correspondence, weighting, alignment selection, and evaluation selection; state whether rigid-body superposition was performed and disallow reflections. |

   Check coordinate units and finite values before calculating. Cross-check at least one representative result with an independent implementation or a direct calculation from the retained coordinates. Use simple geometric invariants where applicable, such as distance symmetry and invariance to a common rigid transformation. Treat disagreements between reference methods as unresolved ground truth, not agent failures.

5. **Control the agent environment and preserve traces.**
   Record the model endpoint/version and date, prompt, sampling and reasoning settings when supported, harness version, installed tools, runtime image or dependency versions, and time/token/tool-call budgets. Start repeated attempts with clean contexts and declared cache behavior. Keep reference answers and evaluator-only files inaccessible to the agent.

   Define access conditions concretely: unrestricted network, a specified domain blocklist, or disabled network with a declared local asset set. Verify enforcement at runtime, including alternate tools, proxies, and preexisting caches; prompt instructions alone do not enforce access restrictions. Provide identical starting assets where required by the comparison. Save prompts, tool calls, outputs, timestamps, costs when available, exit states, and access-check results.

   Change one factor at a time for a direct contrast. Use the same tasks, budgets, reference assets, and grading pass across conditions; randomize or interleave execution order when feasible. If several factors change, describe the result as a joint configuration comparison.

6. **Grade results with explicit error handling.**
   Retain the raw answer and extracted value, extraction status, reference value, unit conversion, error, tolerance, and final score. For scalar measurements, predeclare a rule such as `absolute_error <= absolute_tolerance + relative_tolerance * abs(reference)`. Use circular differences for torsions and exact integer agreement for counts unless the task defines another rule. Do not adjust tolerances after seeing model answers.

   Distinguish answer errors, atom-selection errors, computation errors, output-format failures, timeouts, access failures, invalid assets, and verifier failures. Count agent failures according to the fixed scoring policy; report infrastructure failures and unresolved references separately with their denominators. Keep benchmark-native grades separate from diagnostic regrading. Apply verifier corrections to every affected condition and retain both versions.

7. **Compare models with task-aware uncertainty.**
   Average repeated attempts within each task, then aggregate task means using the declared weights so that heavily repeated tasks do not dominate. Report overall and family-specific scores with eligible task counts, completed and planned run counts, exclusions, and failure counts.

   Compare models on shared tasks using paired task-level differences. For confidence intervals, resample shared task IDs together across models and conditions; stratify by family if family weights are fixed. If estimating run variability as well, resample attempts within each sampled task while preserving genuinely paired attempts. Do not treat repeated attempts as independent tasks. State the bootstrap seed, replicate count, confidence level, weighting, and target of inference.

   Report pairwise effect sizes and intervals; an interval spanning zero is an unresolved difference, not proof of equivalence. Treat rank frequencies as descriptive stability measures. A single run cannot estimate within-task run variability; tiny pilots support diagnostics rather than firm rankings. Account for multiple comparisons when making broad superiority claims.

   The source finding used different subsets for different experiments and different grading passes for its access contrasts. Do not use those contrasts to decompose network effects or rank the contributions of model, harness, access, and task composition. A small harness comparison also does not establish the absence of a harness effect.

8. **Deliver a bounded pilot and an auditable result.**
   For the 15-minute workflow, use already available assets and a predeclared small subset containing both lookup and geometry tasks. Allocate time to asset and selection validation, a representative reference calculation, bounded agent execution, and reporting. Set a deadline and per-run timeout before execution; record incomplete trials without silently reducing the planned denominator.

   A valid pilot output includes verified asset provenance, explicit selections, a checked numeric reference, a configuration manifest, trial records, family summaries, and limitations. If prerequisites or execution cannot be completed within the window, return a clearly labeled partial or blocked report with the missing prerequisites. Do not label an incomplete pilot a successful full benchmark reproduction or imply that a full evaluation fits the pilot time budget.

## Inputs / Outputs

**Inputs**

- Task prompts and IDs, family labels, coordinate files, and any required metadata sources.
- Structure/model/assembly/chain/residue/atom selections, or enough information to resolve them unambiguously.
- Reference answers or verifier assets with provenance, units, and tolerance definitions.
- Agent endpoints, harnesses, access conditions, execution budgets, repeat counts, and the intended comparison.

**Outputs**

- A manifest recording task and coordinate hashes, source versions, resolved selections, calculation conventions, and execution conditions.
- A reference-calculation record containing atom identities, coordinates, formulas or code used, numeric results, units, and cross-check status.
- A trial table with task family, model, condition, attempt, raw answer, extracted result, reference, error, score, runtime, and failure category.
- A comparison report with family and overall denominators, task-weighted scores, paired differences and uncertainty where supported, exclusions, and limits on interpretation.
- A completion status: completed pilot, partial pilot, or blocked; identify which larger evaluation steps remain.

Keep outputs within the user's authorized destination and format. A pilot report may embed the manifest and tables in one document; separate artifacts are optional.

## References

- [ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry, arXiv:2610.26829v1](http://arxiv.org/abs/2610.26829v1) — source finding and research limitations.
- [ProteinGeoBench repository](https://github.com/Protege-AI/ProteinGeoBench) — repository linked from the paper; inspect and pin task assets and verifiers before executable use.
