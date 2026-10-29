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
name: 'clinical-ehr-derivation-agent-evaluation'
description: 'Specify clinical EHR derivations and evaluate coding agents against reviewed references using M4Bench-style controls for item codes, time windows, missingness, and output grain.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Clinical EHR Derivation Agent Evaluation

## Overview

Turn clinical derived-variable definitions into executable specifications and evaluate agent-generated SQL or code against reviewed references. M4Bench studies 28 tasks across 15 families on MIMIC-IV and eICU and motivates separating specification completeness from delivery format and schema familiarity. Treat agreement with a reference as a reproducibility result, not proof of clinical validity or readiness for patient care. See the [source finding](http://arxiv.org/abs/2610.37459v1).

## When to Use This Skill

- A clinical derivation depends on definitions absent from the database schema.
- An agent returns plausible values but incorrect patients, admissions, stays, or time bins.
- Compare no-skill, operational-specification, and targeted-skill conditions fairly.
- Audit benchmark evidence, reference validity, or portability across EHR schemas.

## Core Capabilities

1. **Verify prerequisites and choose a bounded mode.** Inspect the task manifest, repository documentation, evaluator, and dataset versions before execution. Use an authorized local dataset and prepared container for a derivation run; otherwise audit public evidence or return a blocked execution report. PhysioNet requires credentialing, required training, and a signed data-use agreement for both [MIMIC-IV](https://physionet.org/content/mimiciv/) and [eICU](https://physionet.org/content/eicu-crd/). Public benchmark code does not grant access to these data.

2. **Resolve release provenance.** Start from the paper-linked M4 repository and tag `m4bench-neurips2026-camera-ready`; record the resolved commit, task IDs, skill version, and evaluator version. Verify available manifests and checksums before using evidence. The [public evidence card](https://huggingface.co/datasets/hannesill/m4bench-evidence) identifies the release and explains that source data, task databases, reference outputs, and row-level agent outputs are withheld. The repository URL was discoverable during skill authoring, but its contents could not be fetched; inspect its actual commands and file layout before running anything, and do not invent a CLI.

3. **Build an operational derivation contract.** Populate the fields below from the task and reviewed definition. Mark unresolved rules explicitly; never infer clinical item codes or missingness semantics from column names alone. Separate confirmed requirements from proposed assumptions and obtain clarification for ambiguities that change the cohort or result.

   | Contract field | Required detail |
   | --- | --- |
   | Population and keys | Inclusion/exclusion criteria, patient/admission/stay linkage, join cardinality |
   | Output grain | One row per specified entity or entity-time bin; composite key and uniqueness rule |
   | Source mapping | Dataset version, tables, columns, exact item codes and provenance |
   | Temporal logic | Index event, timestamp or offset units, window endpoints and inclusivity |
   | Value handling | Units, conversions, validity thresholds, duplicate and tie handling |
   | Missingness | Distinguish absent observations, SQL NULL, zero, unknown, and inapplicable |
   | Aggregation | Selection order, grouping, formulas, rounding, and denominator rules |
   | Output schema | Column names, types, nullability, and ordering if semantically required |
   | Reference status | Reference version, review evidence, known limitations, unresolved disagreements |

4. **Execute a controlled agent run.** Keep reference outputs and evaluator internals outside the agent workspace. Use the release's isolation harness with read-only source data, a separate output location, resource limits, and recorded network policy. Record model identifier, prompt, condition, trial, resource budget, exit status, and elapsed time. Expose reference SQL only in an explicitly labeled reference-SQL control. Keep restricted rows and query results inside the approved environment; sanitize any exported report or trace under the dataset agreement.

5. **Evaluate rows and values separately.** Run the pinned evaluator without changing its checks or thresholds after inspecting results. Check schema, composite-key uniqueness, row coverage, null patterns, values, units, and temporal boundary behavior. Report key precision, recall, and F1 where supported, alongside value agreement and the fraction passing every strict check. Preserve official reward definitions; label any additional diagnostics separately. Record timeouts, execution errors, invalid outputs, and empty outputs explicitly, including the evaluator's empty-set convention. Never equate partial reward with task completion.

6. **Attribute improvements with matched controls.** Hold task data, model configuration, budgets, and trial protocol constant across conditions. Compare no skill with targeted skill first; add operational specification alone to investigate completeness. Use decoy skills, reference SQL, or schema transformations only when relevant and supported by the release. Preserve derivation semantics under transformed schemas. Report paired task-level changes and uncertainty when repeated trials support it; identify subset sizes and avoid pooling unlike campaigns. Interpret schema robustness as descriptive evidence, not a bound on memorization.

7. **Audit references and deliver an actionable result.** Inspect reference assumptions at the task-family level and record whether clinician review is documented, pending, or disputed. Diagnose mismatches as key/cohort, timing, source mapping, missingness, aggregation, or implementation errors. Do not silently alter a reference to improve scores; version corrections and rerun affected comparisons. A computational match alone cannot certify that a reference expresses the intended clinical definition.

### Fifteen-minute workflow

- **Minutes 0–3:** Select one task or a small evidence slice; verify access, release provenance, and execution readiness.
- **Minutes 3–6:** Complete the derivation contract and identify missing or disputed rules.
- **Minutes 6–12:** Run a bounded evaluation in the prepared environment, or inspect existing sanitized evidence. Choose a timeout that leaves time to report results.
- **Minutes 12–15:** Produce a report with status, provenance, checks, failure categories, and next actions.

Successful execution requires an actual completed run with parseable evaluation output and recorded provenance. A valid audit report can satisfy evidence-review mode, but must state that no new derivation was executed. If access, setup, runtime, or specification prevents execution, return `blocked` or `incomplete` with the exact missing prerequisite; do not claim the fifteen-minute target was achieved. Dataset provisioning and a full benchmark campaign are outside this bounded workflow.

## Inputs / Outputs

**Inputs**

- Task selection, clinical definition, intended cohort, and requested comparison conditions.
- Authorized dataset location, version, schema dictionary, and code mappings.
- Reviewed reference implementation or outputs, review status, and evaluator configuration.
- Agent configuration, isolated execution environment, resource budget, and release checkout; alternatively, sanitized public evidence for audit mode.

**Outputs**

- An explicit derivation contract with provenance, assumptions, and unresolved questions.
- Generated SQL or code and run metadata when execution is possible.
- An evaluation report containing mode, completion status, task/run identifiers, versions, condition, runtime, row/key checks, value checks, strict-pass result, and failures.
- A comparison table when multiple matched conditions were run, with denominators and unsupported metrics marked unavailable.
- A reference-validity assessment and concrete remediation steps; share only permitted aggregate or sanitized evidence.

## References

- [M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents, arXiv:2610.37459v1](http://arxiv.org/abs/2610.37459v1) — source finding and experimental interpretation.
- [M4 benchmark repository, paper-linked release](https://github.com/hannesill/m4/tree/m4bench-neurips2026-camera-ready/benchmark) — task, skill, isolation, and evaluation artifacts; verify availability and commands at use time.
- [M4Bench public per-run evidence](https://huggingface.co/datasets/hannesill/m4bench-evidence) — sanitized artifacts, manifests, checksums, and disclosure limits.
- [MIMIC-IV on PhysioNet](https://physionet.org/content/mimiciv/) — dataset documentation and credentialed-access requirements; use the version required by the selected task.
- [eICU Collaborative Research Database on PhysioNet](https://physionet.org/content/eicu-crd/) — dataset documentation and credentialed-access requirements.
