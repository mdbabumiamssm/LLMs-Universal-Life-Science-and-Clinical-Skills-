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
name: 'test-time-knowledge-clinical-llm'
description: 'Guide clinical LLM workflows that acquire and inject relevant medical knowledge at inference time to support safer decision-making without full fine-tuning.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Test-Time Knowledge Clinical LLM

## Overview

This skill guides clinical LLM workflows that improve medical decision support by acquiring relevant knowledge during inference rather than relying only on model parameters. It focuses on source selection, evidence injection, conflict handling, safety review, and evaluation so outputs remain traceable, current, and clinically cautious.

## When to Use This Skill

- A clinical LLM task requires current or guideline-sensitive medical knowledge.
- The workflow should retrieve evidence at inference time instead of fine-tuning a model.
- A user asks to design, audit, or improve retrieval-augmented medical decision support.
- The answer must distinguish evidence-backed statements from model inference.
- Retrieved sources conflict, are outdated, or vary by population, setting, or jurisdiction.
- The workflow needs a safety layer for diagnosis, treatment, triage, medication, or escalation advice.
- Evaluation should test source grounding, citation quality, clinical appropriateness, and failure handling.

## Core Capabilities

1. Evidence need framing: Identify the clinical question, patient context, decision point, required recency, and source type before retrieval.
2. Source selection: Prefer authoritative clinical references such as guidelines, drug labels, systematic reviews, PubMed-indexed literature, institutional protocols, and regulatory sources when appropriate.
3. Retrieval planning: Convert the clinical question into search concepts, synonyms, eligibility constraints, and exclusion criteria that can be checked against returned evidence.
4. Evidence injection: Add concise, source-linked evidence snippets to the model context with publication date, population, intervention, comparator, outcome, and key limitations when available.
5. Conflict handling: Compare recommendations across sources, prioritize higher-quality and more current evidence, and surface unresolved disagreement instead of forcing a single conclusion.
6. Clinical reasoning scaffold: Separate patient facts, retrieved evidence, applicability assessment, reasoning, recommendation options, uncertainty, and escalation triggers.
7. Safety review: Check for high-risk omissions, contraindications, dosing concerns, emergency symptoms, vulnerable populations, and cases requiring clinician or specialist involvement.
8. Output traceability: Link each clinically important claim to evidence or label it as inference, background knowledge, or an unresolved uncertainty.
9. Evaluation design: Assess retrieval relevance, evidence faithfulness, citation accuracy, harmful recommendation risk, abstention behavior, and robustness to missing or conflicting sources.
10. Test-time knowledge acquisition: At inference time, retrieve current evidence, vet source authority, inject only concise relevant context, cite provenance, and compare results with a no-retrieval baseline without implying that retrieval confers fine-tuned clinical competence.

## Inputs / Outputs

Inputs consumed by this skill:

- Clinical task or decision question.
- Patient context, including age group, sex, pregnancy status, comorbidities, medications, allergies, setting, and acuity when available.
- Retrieval constraints such as preferred sources, date range, jurisdiction, language, specialty, and evidence hierarchy.
- Available local documents, protocols, notes, or reference corpora.
- Output requirements such as clinician-facing note, patient-facing explanation, differential diagnosis support, medication safety check, or evaluation plan.

Outputs produced by this skill:

- A retrieval plan with prioritized source types and search terms.
- An evidence packet with citations, dates, source quality notes, and applicability comments.
- A clinically structured LLM prompt or workflow for test-time knowledge acquisition.
- A grounded answer template that separates evidence, reasoning, uncertainty, and recommended next steps.
- A conflict and safety review identifying gaps, disagreements, high-risk issues, and escalation conditions.
- An evaluation checklist or test set outline for validating retrieval-grounded clinical behavior.

## References

- Li S, Bao L, Li S, Wan B. Enhancing LLM-based medical decision-making by test-time knowledge acquisition. PubMed: https://pubmed.ncbi.nlm.nih.gov/41953846/
- Lewis P, Perez E, Piktus A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. arXiv: https://arxiv.org/abs/2005.11401
- Gao Y, Xiong Y, Gao X, et al. Retrieval-Augmented Generation for Large Language Models: A Survey. arXiv: https://arxiv.org/abs/2312.10997
- Singhal K, Azizi S, Tu T, et al. Large language models encode clinical knowledge. Nature / PubMed: https://pubmed.ncbi.nlm.nih.gov/37438534/
- U.S. Food and Drug Administration. Medication Guides and drug labeling search resources: https://www.accessdata.fda.gov/scripts/cder/daf/
