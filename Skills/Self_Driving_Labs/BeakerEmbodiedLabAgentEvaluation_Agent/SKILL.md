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
name: 'beaker-embodied-lab-agent-evaluation'
description: 'Evaluate multimodal laboratory agents with BEAKER through verified benchmark acquisition, experimental-state interpretation, procedural constraint assessment, and reproducible offline failure reporting.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# BEAKER Embodied Laboratory Agent Evaluation

## Overview

This skill supports research evaluation of multimodal agents using BEAKER, which reports 1,000 expert-curated image and video questions across 11 task types in an offline, single-turn setting. It diagnoses experimental-state interpretation and execution-relevant reasoning, contingent on verified access to benchmark materials and their protocol. Benchmark results do not authorize physical equipment control or establish readiness for autonomous laboratory operation.

## When to Use This Skill

- Check whether BEAKER materials support a reproducible evaluation.
- Compare laboratory perception and reasoning across model versions under matched conditions.
- Diagnose errors in apparatus recognition, action grounding, experimental states, or procedure ordering.
- Audit reported benchmark scores for missing assets, protocol deviations, or unsupported deployment claims.

## Core Capabilities

1. **Verify and acquire benchmark materials.** Open the versioned source in References and follow only attributable project or dataset links. Confirm that a candidate release is BEAKER rather than an unrelated project with the same name. Record retrieval date, release or commit, asset checksums, license, access requirements, annotation availability, and evaluator provenance. Acquire media and annotations only through permitted access routes; public paper access does not establish redistribution rights for underlying media.

   Verification baseline on 2026-11-05: the abstract and full-text paper were accessible, including Section 4.1 and Appendices E and F. An official downloadable benchmark package and evaluation repository were not confirmed from the inspected pages. Recheck availability at execution time; do not invent repository URLs, download commands, or release status.

   Proceed to scoring only when required media, questions, reference answers, and scoring rules are accessible and attributable. If any are missing, return `blocked_materials` with the missing components and evidence checked. A paper-only review may produce a readiness report, but must not substitute generated questions or guessed annotations for BEAKER.

2. **Freeze the evaluation contract.** Read Section 4.1 for inference and aggregation, Appendix E for metrics, and Appendix F for task prompts and output formats. Record the exact task mapping, media preprocessing, video sampling, coordinate convention, decoding settings, answer parsing, invalid-output handling, and aggregation rules before inference. Resolve omissions against official release documentation; unresolved scoring choices block an official-comparable score.

   Use the verified evaluator when available, after inspecting its execution requirements. If implementing published equations locally, label the implementation as a reproduction and verify it against official examples where available. Do not silently replace spatial, trajectory, or phrase scoring with a generic correctness judge. Preserve official task names instead of inferring an eleven-category taxonomy from the abstract.

3. **Run a bounded, reproducible offline evaluation.** Select a full run or a deterministic diagnostic subset based on available time, model access, and compute. Record sample IDs, model identifier and revision, prompt version, inference configuration, timestamps, and errors. Keep reference answers out of model inputs. Preserve single-turn conditions; retries for transport errors must be logged, and answer-conditioned retries must not count as ordinary benchmark inference.

   Target a valid report within 15 minutes: use approximately the first four minutes for readiness and protocol checks, the next eight for an eligible evaluation or audit, and the remaining three for reporting. This is a reporting budget, not a guarantee that full benchmark inference completes. At the deadline, report `partial` with completed and pending counts; never extrapolate a subset score into a full benchmark result.

4. **Interpret experimental states from evidence.** For each reviewed error, identify the relevant image region or video timestamp and separate visible observations from model inferences. Compare apparatus identity, connections, material state, and apparent procedure stage with the supplied reference and task context. Mark obscured or unavailable evidence explicitly; do not infer chemical identity, temperature, pressure, or operability solely from appearance when the sample does not establish them.

5. **Assess procedural constraints without actuation.** Diagnose whether the answer respects the sample's stated prerequisites, apparatus configuration, operation order, and spatial or temporal constraints. Distinguish an observed violation from an uncertainty that prevents judgment. Keep supplementary expert interpretation separate from official scoring, and flag disputed references for review without rewriting them to match predictions. Do not send trajectories, commands, or proposed procedures to robots or laboratory devices; physical execution requires a separate authorized workflow and appropriate operational validation.

6. **Score and report failures transparently.** Apply the verified task metrics and aggregation exactly, retaining unrounded intermediate values. Report evaluated counts, missing assets, malformed responses, inference failures, and exclusions alongside each score; follow documented denominator rules rather than silently dropping failures. Compare models only on matched samples and protocol settings, and disclose deviations prominently.

   Use a local diagnostic taxonomy such as perception, state inference, spatial grounding, temporal ordering, constraint assessment, output formatting, and infrastructure failure. Label this taxonomy as analyst-defined, not an official BEAKER annotation. Each failure record should include sample ID, official task, evidence locator, raw prediction, parsed answer, reference, score or unscorable reason, diagnosis, uncertainty, and review action. Explanations are evidence-based hypotheses, not proof of a model's internal reasoning.

## Inputs / Outputs

**Inputs**

- Versioned BEAKER paper and, when accessible, attributable media, questions, annotations, prompts, and evaluation code or complete metric specifications.
- Model endpoint or local inference interface, model revision, supported modalities, and permitted compute and time budget; alternatively, saved predictions for audit.
- Evaluation scope, sample selection rule, intended comparison, and authorized output location.

**Outputs**

- A readiness and provenance record with status `ready`, `blocked_materials`, or `blocked_protocol`, including checked sources and unresolved requirements.
- A run manifest and prediction records for executed samples, with completion status `complete`, `partial`, or `not_run`.
- Per-task results and capability or overall scores only where the verified protocol and coverage justify them; label subset results as diagnostic.
- A failure report linking diagnoses to observable evidence, listing protocol deviations and distinguishing benchmark performance from equipment-control authorization.

**Completion criteria:** Within the reporting budget, produce either an evidence-backed readiness/blocker report or a reproducible evaluation report with explicit coverage, status, and limitations. A blocker report completes the readiness workflow, not benchmark evaluation. Never claim inference, verification, or scoring that was not performed.

## References

- [BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories — arXiv:2611.06911v1](http://arxiv.org/abs/2611.06911v1). Source finding; submitted November 4, 2026.
- [BEAKER full text, version 1](https://arxiv.org/html/2611.06911v1). Consult Section 4.1 and Appendices E–F for the evaluation contract, and the asset usage and dataset documentation appendices before acquisition.
