---
name: 'test-time-knowledge-clinical-llm'
description: 'Guide clinical LLM workflows that acquire and inject relevant medical knowledge at inference time to support safer decision-making without full fine-tuning.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

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
11. Test-time acquisition procedure: Generate patient- and decision-specific queries, select only relevant evidence after source quality checks, identify and disclose contradictions rather than silently resolving them, bind each material clinical claim to its supporting citation, and abstain when evidence is insufficient or unreliable; evaluate the procedure against both zero-shot and static-RAG baselines.
12. Knowledge-gap acquisition loop: Detect knowledge gaps before answering, formulate targeted retrieval queries, rank and validate returned evidence, inject concise decision-relevant context, and require answers grounded in that evidence; compare performance with a no-retrieval baseline and measure accuracy gains alongside citation failures and unsafe uptake of retrieved knowledge.
13. Acquisition controls and ablation: Constrain query generation to the patient, decision, and identified knowledge gap; rank sources by clinical authority and evidence freshness; preserve and explicitly resolve or report contradictions; allocate the context budget to decision-relevant evidence and dissenting evidence; verify that each citation entails the claim it supports; and ablate acquired knowledge to identify unsupported reasoning that comes only from model parameters.
14. Uncertainty-triggered acquire-and-revise procedure: Detect clinically material uncertainty before finalizing an answer; generate patient- and decision-specific retrieval queries; filter evidence for relevance, source quality, and applicability; identify, reconcile when justified, or explicitly report contradictions; capture source provenance for each material claim; revise the answer using the accepted evidence; abstain when evidence remains insufficient, unreliable, or irreconcilable; and compare the procedure against static-RAG and no-retrieval baselines.
15. Unsupported recommendation rejection: During inference, retrieve current evidence, vet source authority, inject concise cited context, compare the evidence-grounded answer with base-answer behavior, and reject clinical recommendations that lack adequate source support.
16. Test-time knowledge acquisition audit: Retrieve current evidence at inference time, vet source authority, inject compact citations, record the retrieved context and provenance used for the answer, and compare answer quality against no-retrieval and fine-tuned baselines.
17. Evidence-freshness tracked acquisition workflow: Retrieve current clinical evidence at inference time, vet source authority and relevance, inject concise evidence context, require source-linked rationales for material clinical claims, track evidence freshness, and compare medical decision-support outputs against fine-tuning or static prompting baselines.
18. Test-time medical decision-support pattern: Formulate patient- and decision-specific queries, retrieve and vet evidence for authority, recency, relevance, and applicability, inject concise source-linked context, enforce citations for every material clinical claim, mitigate stale model knowledge by preferring current retrieved evidence over parameter memory, and run post-answer verification for claim support, date freshness, and safety without model fine-tuning.
19. Medical decision-support acquisition steps: Formulate patient- and decision-specific queries, retrieve evidence from authoritative medical sources, vet relevance, quality, recency, and applicability, inject only uncertainty-labeled vetted evidence into prompts, capture citation and provenance metadata for each material claim, and qualify or block recommendations when sources are stale, low-quality, conflicting, or insufficient.
20. Test-time acquisition workflow for clinical decision support: Generate targeted queries from patient facts and the decision need, retrieve evidence, vet source authority, relevance, recency, and applicability, inject concise vetted context, bind each material claim to citations, abstain when evidence is insufficient, unreliable, stale, conflicting, or inapplicable, and run post-answer verification for claim support, citation integrity, safety, and consistency with retrieved evidence without fine-tuning.
21. Test-time knowledge acquisition pattern: For LLM-based medical decision-making, retrieve current evidence during inference, vet source quality before use, inject concise grounded context with provenance, cite the sources supporting material claims, and compare outputs against fine-tuning or static-RAG baselines.
22. Medical decision-support acquisition workflow: Formulate retrieval queries from the clinical question, retrieve trusted evidence, check recency and guideline status, inject source-linked evidence into the answer context, cite sources for clinical claims, and abstain when evidence is weak or insufficient.
23. Test-time evidence delta gate: Retrieve current evidence for the clinical decision, assess source quality before context injection, inject concise provenance-linked context, cite provenance for material claims, compare the pre-retrieval answer against the evidence-grounded answer to document clinically material deltas, and fail closed by abstaining when retrieval is weak, low-quality, conflicting, or cannot support the recommendation.
24. Retrieval-and-verification workflow: Plan patient- and decision-specific queries, vet source authority and freshness before use, inject only relevant evidence into the clinical context, capture citations for material claims, and apply safeguards that block ungrounded reasoning without requiring fine-tuning.
25. Freshness-centered test-time knowledge acquisition: When clinical correctness depends on current knowledge, retrieve evidence during inference, vet source authority before use, inject concise provenance-linked context, cite supporting sources, reject stale or conflicting evidence instead of smoothing over it, and avoid fine-tuning as the primary remedy for knowledge freshness.
26. Medical decision-support TKA workflow: Formulate retrieval queries from patient facts, the decision target, knowledge gaps, and jurisdiction; retrieve trusted medical evidence; check publication date, guideline status, source authority, and applicability before use; inject only concise vetted knowledge with preserved citation metadata; carry citations through prompt construction, answer generation, and post-answer verification; explicitly disclose or abstain on contradictions; and document no-fine-tuning deployment tradeoffs such as retrieval quality, source access, latency, context limits, and validation burden.
27. Test-time knowledge acquisition stop rule: Formulate queries from patient facts, clinical decision target, PICO-style concepts, synonyms, jurisdiction, and recency needs; rank databases and sources by clinical authority, guideline or label status, peer-review level, freshness, and patient applicability; preserve retrieval-to-answer provenance from query, database, record ID, date, snippet, and citation through every material claim; compare contradictions by authority, recency, population fit, and outcome relevance; and stop rather than answer when retrieved evidence is stale, low-authority, sparse, inapplicable, irreconcilably conflicting, or too weak to support a clinical recommendation.
28. Medical decision-support test-time acquisition pattern: Retrieve current evidence during inference, vet source authority before context use, inject concise evidence context, cite provenance for material claims, detect and disclose conflicts, and compare the evidence-grounded workflow against zero-shot and fine-tuned baselines.
29. Evidence-quality gated inference loop: During inference, retrieve current clinical evidence for the specific decision, vet source authority, publication or update date, relevance, applicability, and evidence quality, inject only concise citation-preserving context, require citations for material claims, check the draft answer against retrieved evidence, and fail closed when support is stale, low-quality, conflicting, absent, or unsuitable instead of fine-tuning to compensate for freshness gaps.
30. Test-time knowledge acquisition for medical decision support: Retrieve and vet evidence at inference time, inject compact grounded context, cite provenance for material claims, handle conflicting sources explicitly, and avoid treating retrieved evidence as an autonomous diagnosis or substitute for clinician judgment.
31. Citation-aware acquisition pattern: Generate patient- and decision-specific queries, vet retrieved sources before use, inject concise evidence with provenance, produce citation-aware answers, check for stale evidence, and fall back to abstention, escalation, or explicit conflict disclosure when retrieved evidence conflicts.
32. Inference-time evidence gate for decision support: Retrieve current evidence at inference time, vet source authority before use, inject concise evidence context, cite provenance for material claims, compare results against no-retrieval baselines, and avoid treating retrieval as a substitute for clinician judgment.
33. Test-time knowledge acquisition refresh boundary: For medical decision support, retrieve current evidence at inference time, rank and reconcile sources before use, inject compact citations for material claims, and keep knowledge refresh as an inference-time retrieval step separate from model fine-tuning.
34. Medical decision-making acquisition workflow: Retrieve current evidence during inference, vet source authority before context use, inject concise decision-relevant context, cite provenance for material claims, compare the evidence-grounded response against a baseline response, and document residual uncertainty without fine-tuning.
35. Clinical authorization boundary: Retrieve current evidence, assess source quality, inject concise provenance-preserving context, cite supporting sources, handle conflicts explicitly, and state that retrieval supports decision-making but does not authorize diagnosis, treatment, prescribing, or escalation without qualified clinical review.
36. Retrieve-vet-inject clinical evidence workflow: Prefer test-time retrieval over fine-tuning when the clinical question depends on current, jurisdiction-specific, or frequently updated knowledge; select authoritative sources, check publication or update dates before use, inject only concise relevant evidence with preserved citation metadata, report uncertainty or abstain when evidence is stale, conflicting, or insufficient, and keep citations attached to every material clinical claim.
37. Uncertainty- and guideline-triggered acquisition: Trigger retrieval only when clinical uncertainty is high, the answer depends on current guidelines or evidence, or the baseline response lacks adequate support; vet retrieved sources before use, inject concise provenance-linked evidence, cite supporting sources, compare pre- and post-retrieval answers for material changes, and require clinician review before final clinical decisions.
38. Test-time knowledge acquisition operating pattern: For LLM-based medical decision-making, retrieve current evidence during inference, validate source authority before use, inject concise provenance-preserving context, cite supporting sources, and compare outputs against fine-tuning or static-RAG baselines.
39. Base-answer comparison and uncertainty log: For clinical decision-support workflows, retrieve fresh evidence at inference time, verify source authority, inject concise context with provenance, cite supporting sources, compare the evidence-grounded answer against the base-model answer, and log residual uncertainty.
40. Test-time knowledge acquisition decision gate: Trigger retrieval for high-uncertainty, guideline-sensitive, current-evidence-dependent, population-specific, jurisdiction-specific, or unsupported baseline responses; vet evidence for source authority, relevance, applicability, publication or update date, and conflicts before use; inject only concise citation-preserving evidence snippets; run freshness and citation-support checks after drafting; report residual uncertainty or abstain when evidence is insufficient; and compare this inference-time acquisition workflow against fine-tuning, static-RAG, and no-retrieval baselines as distinct options.
41. No-fine-tuning test-time acquisition workflow: Trigger retrieval at answer time for current, guideline-sensitive, or unsupported clinical claims; vet evidence for source authority, publication or update date, relevance, applicability, and conflicts before prompt injection; inject compact citation-carrying snippets tied to each material claim; disclose conflicting sources; and block, revise, or abstain on stale, weak, uncited, or hallucinated claims instead of relying on model parameters or fine-tuning to fill gaps.
42. Retrieval-and-verification pattern for medical decision support: Acquire evidence at test time when a decision is high-risk, guideline-sensitive, current-evidence-dependent, patient- or jurisdiction-specific, uncertain, or unsupported by the baseline answer; vet sources for authority, publication or update date, relevance, applicability, and conflicts; inject only concise citation-preserving snippets tied to the clinical question; cite provenance for each material claim; and report residual uncertainty, conflict, or abstention explicitly without using fine-tuning to fill evidence gaps.
43. Retrieved-evidence versus model-prior boundary: During inference, retrieve current evidence for the clinical decision, vet source quality before use, distinguish retrieved facts from model-prior inferences in the answer, cite accepted evidence for material claims, and reject unsupported recommendations when evidence quality is low, absent, conflicting, or inapplicable.
44. Clinician-judgment-preserving acquisition workflow: Retrieve current evidence at inference time, vet source authority before use, inject concise decision-relevant context, cite provenance for material claims, run contradiction checks against retrieved and baseline information, and avoid treating retrieval as a substitute for clinician judgment.
45. Clinician-reviewed evidence delta workflow: Retrieve current clinical evidence at inference time, vet source authority before prompt use, inject concise evidence snippets with provenance, cite accepted sources for material claims, compare evidence-grounded recommendations against model priors, and require clinician review before acting on changed recommendations.
46. Test-time knowledge acquisition clinical LLM pattern: Retrieve current evidence during inference, vet source quality, inject concise grounded context, cite provenance for material claims, compare against fine-tuning and static RAG baselines, and flag retrieved evidence that is stale or conflicting.
47. Retrieved evidence impact audit: For medical decision support, retrieve current evidence at inference time, rank and vet sources before prompt use, inject concise grounded context, require citations for material clinical claims, separate retrieved facts from model reasoning, and audit whether retrieval changed the clinical answer.
48. Test-time knowledge acquisition guardrail: Trigger retrieval for current, uncertain, guideline-sensitive, patient-specific, jurisdiction-specific, or unsupported clinical decisions; vet evidence for authority, relevance, applicability, freshness, and conflicts; inject concise citation-linked context; disclose disagreement; and block, revise, or abstain from unsupported clinical recommendations without fine-tuning.
49. Test-time knowledge-acquisition method: Generate explicit patient- and decision-specific queries; rank retrieved evidence by source authority, relevance, recency, and applicability; preserve and disclose conflicts, resolving them only when the evidence justifies it; enforce a context budget that prioritizes decision-relevant and dissenting evidence; verify that every material citation supports its associated claim; abstain when evidence is insufficient, unreliable, inapplicable, or irreconcilably conflicting; and run ablations comparing the retrieved-knowledge workflow with parametric-only reasoning to isolate the effect of acquired evidence.

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

- Li S, Bao L, Li S, Wan B. Enhancing LLM-based medical decision-making by test-time knowledge acquisition. Health Inf Sci Syst, 2026 Dec. PubMed PMID 41953846: https://pubmed.ncbi.nlm.nih.gov/41953846/
- Lewis P, Perez E, Piktus A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. arXiv: https://arxiv.org/abs/2005.11401
- Gao Y, Xiong Y, Gao X, et al. Retrieval-Augmented Generation for Large Language Models: A Survey. arXiv: https://arxiv.org/abs/2312.10997
- Singhal K, Azizi S, Tu T, et al. Large language models encode clinical knowledge. Nature / PubMed: https://pubmed.ncbi.nlm.nih.gov/37438534/
- U.S. Food and Drug Administration. Medication Guides and drug labeling search resources: https://www.accessdata.fda.gov/scripts/cder/daf/
