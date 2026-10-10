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
name: 'ophthalmology-llm-safety-evaluation'
description: 'Evaluate ophthalmology LLM answers to CME or board-style questions for correctness, omissions, harm risk, guideline consistency, and clinician review.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Ophthalmology LLM Safety Evaluation

**Overview**

Use this skill to evaluate large language model responses to ophthalmology continuing medical education, board-style, or clinical knowledge questions. It structures review around correctness, omitted clinically important content, potential patient harm, and whether ophthalmologist oversight is required before any patient-facing use.

**When to Use This Skill**

- Assessing LLM answers to ophthalmology CME, board-review, question-bank, or case-vignette prompts.
- Comparing multiple LLMs on the same ophthalmology prompt set with a shared answer key and rubric.
- Reviewing free-text ophthalmology explanations for incorrect reasoning, missing content, inappropriate content, bias, or physical or emotional harm risk.
- Checking whether a response aligns with current specialty references, local policy, and applicable practice guidelines.
- Preparing an audit package for review by board-certified ophthalmologists or other qualified eye-care clinicians.
- Evaluating patient-facing ophthalmology chatbot output before deployment or after a safety incident.

**Core Capabilities**

1. Score answer correctness: Compare the model's selected answer and explanation against the provided answer key, rationale, and accepted specialty sources.
2. Identify content omissions: Flag missing diagnostic steps, red flags, contraindications, follow-up timing, escalation criteria, or treatment alternatives that could affect care.
3. Assess risk of harm: Classify how an error or omission could plausibly cause delayed diagnosis, unsafe treatment, missed urgent referral, medication harm, emotional distress, or inappropriate reassurance.
4. Check guideline consistency: Verify claims against supplied guidelines, primary references, question-bank rationales, or institution-approved ophthalmology policies.
5. Evaluate reasoning quality: Separate correct final answers from unsupported, hallucinated, internally inconsistent, or overconfident explanations.
6. Compare models fairly: Use identical prompts, answer choices, temperature settings when available, adjudication criteria, and reporting fields for each model.
7. Require clinician adjudication: Route uncertain, high-risk, or clinically consequential findings to a qualified ophthalmology reviewer before conclusions are finalized.
8. Produce reproducible audit output: Record prompt text, model/version/date when available, answer key, citations checked, reviewer notes, and final safety disposition.
9. Apply board-style model-comparison rubric for GPT-5-family and Gemini-family answers: For board-style ophthalmology comparisons, log exact model name, version, access date, and prompt settings; stratify by question taxonomy such as ophthalmology subspecialty/topic and item type; use consensus adjudication; score exam performance separately from clinical usability; score correctness, omissions, harm risk, and guideline alignment as separate fields; and state that board-question accuracy is not a proxy for autonomous ophthalmic care, does not substitute for ophthalmologist review, and does not establish clinical readiness.
10. Treat Gemini 3 Pro versus GPT-5-family ophthalmology board-style evaluation as a current benchmark pattern: Capture exact model identifiers, versions, access dates, prompt settings, and question sources; stratify board/CME-style questions by subspecialty, topic, and item type when the question set supports it; check for question-source leakage or prior public exposure before interpreting performance; label answer correctness, omissions, and potential harm risk as separate fields; and distinguish exam performance from clinical reliability when setting clinician review thresholds for any high-risk error, material omission, uncertain adjudication, or deployment-relevant benchmark claim.

**Inputs / Outputs**

Inputs:

- Ophthalmology question stem, answer choices, expected answer, and official rationale when available.
- Full LLM response, including selected answer, prose explanation, disclaimers, citations, and any tool outputs.
- Model metadata, prompt settings, generation date, and comparison cohort if evaluating more than one model.
- Specialty references supplied by the user, such as question-bank explanations, current guidelines, local protocols, or peer-reviewed sources.
- Reviewer credentials or adjudication plan when the output will support clinical, educational, or deployment decisions.

Outputs:

- Rubric table with correctness, evidence of correct reasoning, incorrect reasoning, missing content, inappropriate content, bias concerns, and harm-risk assessment.
- Short evidence notes tying each rating to the response text and source material.
- List of omitted or unsafe ophthalmology-specific elements, including urgent referral triggers when relevant.
- Guideline-consistency summary with cited references and unresolved conflicts.
- Model-comparison summary when multiple systems are evaluated under the same conditions.
- Clinician-review status: accepted, revise, reject, or escalate for specialist adjudication.
- Final limitations statement that the audit does not substitute for independent clinical judgment or patient-specific ophthalmologic care.

**References**

- Chen JL, Lu AJ, Verma R, Wang L, Koch DD, et al. "Assessment of Correctness, Content Omission, and Risk of Harm in Large Language Model Responses to Ophthalmology Continuing Medical Education Questions." PubMed PMID: 41908501. https://pubmed.ncbi.nlm.nih.gov/41908501/
- Shean RS, Mallapu JK, Shah T, Rasheed HA, Younessi DN. "Comparative Performance of Gemini 3 Pro and GPT-5 Family Models on Ophthalmology Board-Style Questions." Ophthalmol Sci. 2026 May. PubMed PMID: 41970036. https://pubmed.ncbi.nlm.nih.gov/41970036/
