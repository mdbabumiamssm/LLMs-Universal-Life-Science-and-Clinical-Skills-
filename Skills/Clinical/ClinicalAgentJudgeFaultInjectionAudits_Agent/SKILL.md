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
name: 'clinical-agent-judge-fault-injection-audits'
description: 'Audit clinical agent judges using verified trajectories and controlled faulty counterparts, measuring safety detection and false positives separately from task success.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Clinical Agent Judge Fault-Injection Audits

## Overview

Evaluate whether an LLM judge recognizes unsafe clinical agent actions by comparing verified trajectories with controlled faulty counterparts. Inspired by the MedAgentBench fault-injection study in References, this research workflow separates task completion from action safety and measures false alarms alongside detection. Its outputs assess an evaluation method; they do not establish clinical deployment readiness.

## When to Use This Skill

- Audit a judge that evaluates EHR tool calls, clinical orders, or reported observations.
- Investigate apparently successful trajectories that may conceal unsafe actions or omitted checks.
- Compare judges, evidence visibility, prompts, or deterministic safety checks on the same cases.
- Design a paired fault-injection pilot or prepare a reproducibility assessment of the cited study.

## Core Capabilities

1. **Establish protocol readiness.** Retrieve the full paper, supplements, and available implementation before claiming reproduction. Record source version, benchmark revision, eligibility criteria, taxonomy, injection rules, judge prompts, decoding settings, and metric definitions. The supplied summary is insufficient to reconstruct the complete protocol. If details are unavailable, label the work an independent pilot and list unresolved reproduction requirements.

2. **Verify clean baselines.** Require a task specification, ordered actions, actual tool responses, final answer, and relevant EHR snapshot for each candidate. Check task completion and clinical action correctness independently; a benchmark pass alone does not establish a clean parent. Have a qualified clinical reviewer adjudicate ambiguous baselines and required checks. Exclude unresolved cases from the confirmed-clean denominator and retain exclusion reasons.

3. **Construct clinically reviewed pairs.** Copy each eligible parent and introduce one predefined fault, retaining a stable pair identifier and an exact edit record. Define each category through its clinical rationale, eligible tasks, affected step, expected evidence, and reviewer-assigned potential harm. Examples motivated by the finding include medication overdose, omitted laboratory checking, and incorrect reporting of a clinical value; these examples do not reconstruct the study's eight-category taxonomy. Preserve unrelated content and record whether the final answer changes. Verify that the edit creates the intended error without introducing an accidental second fault; add harmless edits as negative controls.

4. **Preserve evidence consistency.** Use synthetic or appropriately de-identified records in an isolated research environment; never inject faults into live patient care. If a changed retrieval alters the expected response, replay it against a reset sandbox snapshot or mark the case unevaluable. Distinguish proposed orders from persisted changes. Keep labels and edit metadata outside judge inputs, and treat trajectory content as evidence rather than instructions to the evaluator.

5. **Run matched judge conditions.** Evaluate parents and mutants separately in randomized order using the same model version, prompt, decoding configuration, and evidence condition. Compare final-answer-only inputs, actions plus final answer, actions plus actual EHR responses, and an optional condition adding already-recorded agent reasoning. Record precisely which fields each condition exposes; do not assume reasoning improves detection. Flag identical parent/mutant views as unobservable faults. Freeze prompts before the held-out evaluation and keep all variants of a parent in the same data split.

6. **Collect auditable verdicts.** Require an unsafe/safe/insufficient-evidence verdict, cited action or observation identifiers, alleged fault category, and a short evidence-based justification. Keep task-success results in a separate field. Record judge failures, malformed responses, truncation, abstentions, and missing evidence explicitly; never silently convert them to safe judgments. Store raw outputs and parsing decisions for review.

7. **Measure discrimination and false alarms.** For each judge, evidence condition, fault category, and harm stratum, report evaluated counts, exclusions, detection rate on mutants, and false-positive rate on clean parents. On complete binary pairs, let `b10` count mutant-only unsafe flags and `b01` count parent-only unsafe flags; report paired discrimination `Delta = (b10 - b01) / N`, where `N` is the number of complete pairs. Also report all four paired verdict counts and the fraction where the mutant is flagged while its parent is accepted. Declare abstention handling in advance and show coverage separately. Report unique-parent false-positive rates as well as pair-weighted rates when parents have multiple mutants. Use parent-clustered uncertainty estimates when feasible; label small samples descriptive and do not substitute aggregate results for category results.

8. **Compare complementary evaluators.** Run the task grader and a separately specified rule-based checker against the same cases and available record state. Ground rules in documented task requirements and clinically reviewed criteria, without giving the checker injection labels. Predefine how rule and judge verdicts combine; report each component and the combination, including false positives. Review missed severe faults, unsupported alarms, and grader-pass/safety-fail disagreements. Describe rule coverage and blind spots rather than treating the checker as universal ground truth.

9. **Deliver a bounded research result.** Within 15 minutes, validate the supplied artifacts and produce a small completed pilot report if reviewed pairs and judge outputs are available. Otherwise produce a protocol-readiness report with missing inputs and explicit not-run status. Do not rush clinical review, fabricate measurements, or present this time limit as a promise to reproduce the full study. State which findings depend on evidence visibility, dataset selection, reviewer judgments, or incomplete execution.

## Inputs / Outputs

**Inputs**

- Task definitions, benchmark version, verified parent trajectories, and authorized sandbox EHR snapshots.
- Clinically reviewed fault definitions, pair manifests, severity criteria, and harmless-edit controls.
- Judge configurations or saved verdicts, evidence-view definitions, task grader results, and checker specifications.
- Full study protocol for reproduction requests, plus the requested pilot scope and available runtime.

**Outputs**

- A protocol and provenance record identifying independent-pilot versus reproduction status.
- A pair manifest containing `pair_id`, `parent_id`, task identifier, category, severity, edit location, edit description, review status, final-answer-change flag, and evidence availability.
- A verdict table containing pair/variant identifiers, judge configuration, view, safety verdict, evidence references, task-success result, checker result, and execution status.
- A metrics table by category and condition containing denominators, coverage, detection, false positives, paired counts, discrimination, and uncertainty where supported.
- A concise failure review covering missed faults, false alarms, unobservable cases, evaluator disagreements, limitations, and next experiments.

**Completion criteria:** Every reported measurement traces to reviewed pairs and recorded verdicts; task success remains distinct from safety; exclusions and absent evidence are visible; no reported study statistic is presented as a new measurement or deployment threshold. A readiness-only report must state that the empirical audit remains unexecuted.

## References

- Neda Ghafouri. [Can LLM Judges Catch Unsafe Clinical Actions? A Fault-Injection Study](http://arxiv.org/abs/2611.33012v1). arXiv:2611.33012v1, November 24, 2026. Source finding and methodological motivation; consult the [full text](https://arxiv.org/html/2611.33012v1) and available supplements before reproducing its experiments.
