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
name: 'clinical-llm-evaluation-benchmarking'
description: 'Design and run clinical LLM evaluation benchmarks grounded in systematic review evidence on AI-generated clinical note evaluation methods.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Clinical LLM Evaluation Benchmarking

## Overview

Use this skill to design, run, and interpret evaluations for clinical LLM outputs, especially AI-generated clinical notes and related clinical text. It turns a broad evaluation request into a structured benchmark plan with explicit metrics, safety labels, clinician adjudication, provenance controls, and deployment regression gates.

The workflow is grounded in the finding that evaluation methods for AI-generated clinical notes need systematic selection and benchmarking rather than relying on a single similarity, preference, or fluency score.

## When to Use This Skill

- Evaluating AI-generated clinical notes, summaries, handoffs, discharge instructions, referrals, or chart messages.
- Comparing clinical LLM outputs across prompts, model versions, vendors, retrieval settings, or fine-tunes.
- Designing benchmarks for clinical Q&A, guideline support, imaging-report text, patient education, or documentation assistance.
- Creating clinician review rubrics for omissions, hallucinations, contradictions, inappropriate certainty, bias, or unsafe recommendations.
- Establishing regression gates before deploying a clinical LLM workflow into pilot or production use.
- Auditing dataset provenance, de-identification, consent, license constraints, and train-test leakage risk.

## Core Capabilities

1. **Evaluation scope definition**  
   Identify the clinical task, intended users, care setting, input source, output format, decision impact, and unacceptable failure modes before choosing metrics.

2. **Dataset provenance and split design**  
   Document source systems, inclusion criteria, time ranges, de-identification process, annotation history, license or use restrictions, and leakage controls. Prefer held-out temporal or site-level splits when assessing deployment readiness.

3. **Metric selection matrix**  
   Match metrics to the output type: factual consistency, information completeness, omission severity, contradiction detection, clinical usefulness, readability, guideline concordance, calibration, citation support, and patient-safety risk.

4. **Safety and harm labeling**  
   Label outputs for hallucinated facts, missing critical findings, wrong medications or doses, contraindicated advice, delayed-care risk, inappropriate reassurance, privacy exposure, and misleading uncertainty.

5. **Omission and commission scoring**  
   Separate missing necessary information from added incorrect information. Score omissions by clinical severity, recoverability, and whether the missing item changes triage, diagnosis, treatment, follow-up, or patient behavior.

6. **Clinician adjudication workflow**  
   Use at least two qualified reviewers for high-impact tasks when feasible. Define reviewer specialty, blinding, disagreement resolution, escalation criteria, and inter-rater agreement reporting without treating agreement as proof of clinical safety.

7. **Automated evaluator use with controls**  
   Use automated metrics or LLM-as-judge methods only as screening or regression aids unless validated against clinician adjudication for the specific task. Calibrate prompts, anchors, and score thresholds against labeled examples.

8. **Error taxonomy and root-cause analysis**  
   Categorize errors by source: input ambiguity, retrieval failure, prompt instruction conflict, model medical reasoning failure, formatting failure, unsupported extrapolation, or evaluation artifact.

9. **Regression gates for deployment**  
   Define minimum pass criteria before clinical release, including no critical safety failures in the reviewed sample, bounded severe-error rate, stable performance across key subgroups, and documented rollback criteria.

10. **Reporting and interpretation**  
   Produce a benchmark report that distinguishes statistical performance, clinical acceptability, residual risk, subgroup behavior, and operational readiness. Avoid claiming safety or superiority from narrow or nonclinical metrics alone.

## Inputs / Outputs

### Inputs

- Clinical task description and target setting.
- Representative input cases, source documents, prompts, model outputs, and expected use constraints.
- Reference standards when available, such as clinician-authored notes, guideline passages, structured chart facts, or adjudicated answer keys.
- Candidate metrics, reviewer rubrics, acceptable-risk thresholds, and deployment criteria.
- Dataset provenance details, de-identification status, license constraints, and protected health information handling plan.

### Outputs

- Benchmark protocol with task scope, dataset design, evaluation axes, reviewer workflow, and analysis plan.
- Metric matrix mapping each clinical risk to human, automated, or hybrid evaluation methods.
- Safety rubric covering omissions, hallucinations, contradictions, bias, privacy exposure, and patient-harm severity.
- Adjudication template for clinician reviewers, including score anchors and disagreement handling.
- Regression gate checklist for prompt, model, retrieval, and workflow changes before pilot or deployment.
- Final evaluation summary with limitations, residual risks, and recommended next actions.

## References

- PubMed: Dahlberg A, Käenniemi T, Winther-Jensen T, Tapiola O, Luisto R. "Measuring the quality of AI-generated clinical notes: A systematic review and experimental benchmark of evaluation methods." Artif Intell Med. 2026 Jul. https://pubmed.ncbi.nlm.nih.gov/41955894/
