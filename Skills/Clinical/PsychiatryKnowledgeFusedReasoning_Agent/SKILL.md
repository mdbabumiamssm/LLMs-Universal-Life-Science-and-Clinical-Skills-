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
name: 'psychiatry-knowledge-fused-reasoning'
description: 'Psychiatry CDS workflow for knowledge-fused augmented reasoning across diagnosis, risk assessment, medication reasoning, and care planning.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Psychiatry Knowledge-Fused Reasoning

## Overview

This skill guides psychiatry-focused clinical decision support using knowledge-fused augmented reasoning inspired by PKFAR: psychiatry knowledge-fused augmented reasoning with large language models. It supports structured psychiatric assessment, diagnostic reasoning, risk assessment, medication reasoning, and care planning while keeping outputs evidence-grounded, clinically cautious, and appropriate for clinician review.

## When to Use This Skill

- A user asks for psychiatry-oriented clinical decision support, diagnostic reasoning, differential diagnosis, or treatment planning.
- A user needs structured reasoning for symptoms involving mood, anxiety, psychosis, trauma, substance use, cognition, personality, sleep, or suicidality.
- A user asks for psychiatric risk assessment, including suicide risk, self-harm risk, violence risk, inability to care for self, intoxication, withdrawal, or acute decompensation.
- A user requests medication reasoning for psychiatric drugs, adverse effects, interactions, monitoring, tapering considerations, or adherence barriers.
- A user needs an evidence-grounded care plan that integrates symptoms, history, psychosocial context, safety needs, and follow-up.
- A user asks to transform clinical notes, interviews, or case vignettes into a structured psychiatry reasoning summary.

## Core Capabilities

1. **Case structuring** - Extract presenting concerns, timeline, symptoms, functional impairment, psychiatric history, medical history, medications, substance use, family history, trauma history, social context, and protective factors.
2. **Knowledge-fused diagnostic reasoning** - Map case findings to psychiatric diagnostic constructs and differential diagnoses while separating observed facts, patient-reported claims, and clinical inferences.
3. **Risk assessment** - Identify acute and chronic risk factors, protective factors, warning signs, missing safety data, and escalation needs for suicide, self-harm, violence, grave disability, intoxication, or withdrawal.
4. **Medication reasoning** - Summarize candidate medication classes, contraindication checks, interaction concerns, side-effect burdens, monitoring needs, and patient-specific considerations without substituting for prescribing judgment.
5. **Care planning** - Produce clinician-reviewable next steps for assessment, safety planning, psychotherapy considerations, medication discussion, labs or monitoring when relevant, coordination of care, and follow-up acuity.
6. **Uncertainty management** - State confidence limits, competing explanations, missing information, and reasons to defer or escalate to urgent clinical evaluation.
7. **PKFAR-style reasoning controls** - Retrieve relevant psychiatry specialty knowledge before answering, keep diagnostic, risk, and medication reasoning separated, ground clinical claims in citations when sources are used, and audit outputs for hallucinated claims, unsafe advice, and missing differential diagnoses.
8. **PKFAR-style scaffold selection** - Select fit-for-purpose knowledge sources before reasoning, then use separate scaffolds for diagnostic formulation, medication reasoning, and risk assessment prompts with guardrails that keep psychiatric CDS clinician-supervised and non-prescriptive.
9. **PKFAR-style knowledge fusion workflow** - Fuse retrieved psychiatry knowledge into the case in explicit stages: validate source relevance and recency, map case facts to diagnostic criteria and competing differentials, structure acute and chronic risk reasoning with protective factors and missing data, ground medication-safety discussion in contraindications, interactions, adverse effects, monitoring, and tapering cautions, then block unsupported diagnoses, prescribing instructions, crisis-management claims, or psychiatric recommendations that are not grounded in the case or validated sources.
10. **Operational PKFAR architecture and evaluation** - Run a traceable sequence of psychiatry knowledge selection, retrieval, relevance filtering, case-to-knowledge fusion, and augmented reasoning; preserve links from each conclusion to case evidence and retrieved knowledge; benchmark the complete workflow on predefined psychiatry tasks with clinician-reviewed reference criteria; use ablations that remove or isolate selection, retrieval, fusion, and reasoning stages to test their contribution without inventing unreported performance claims; check outputs for unsupported facts, citations, diagnoses, medication claims, and risk conclusions; require medication safeguards for contraindications, interactions, adverse effects, monitoring, tapering, and prescriber authorization; require explicit suicide, self-harm, violence, grave-disability, intoxication, and withdrawal checks with urgent escalation when indicated; and reserve diagnosis, prescribing, disposition, involuntary-treatment, and final risk decisions for qualified clinician review.
11. **PKFAR reference pattern** - Use PKFAR as the reference pattern for psychiatry knowledge-fused augmented reasoning by retrieving psychiatric knowledge, grounding symptoms and diagnoses in case evidence, checking medication risks, producing chain-of-evidence summaries, and escalating for crisis signals or diagnostic uncertainty.
12. **PKFAR-style criteria and safety fusion** - Retrieve diagnostic criteria and medication guidance before reasoning; structure differential-diagnosis and risk reasoning separately; flag conflicts between retrieved knowledge, case facts, and user claims; cite the criteria or guidance used for clinical claims; and escalate self-harm, mania, psychosis, medication contraindication, interaction, adverse-effect, monitoring, tapering, or overdose-risk scenarios for urgent clinician review when indicated.
13. **PKFAR-style provenance and uncertainty labels** - Retrieve psychiatric diagnostic and medication knowledge for the case, run the augmented reasoning scaffold through explicit risk and contraindication checks, capture citations and source provenance for clinical claims, and present clinician-facing uncertainty labels for diagnoses, medication considerations, risk conclusions, and missing information.
14. **PKFAR-style structured retrieval and routing** - Retrieve from psychiatric criteria and medication knowledge bases, inject relevant evidence into augmented reasoning prompts, run risk and safety checks before producing conclusions, and route diagnosis and care-planning outputs to qualified clinician review rather than presenting them as final clinical decisions.
15. **PKFAR-style clinician-gated checks** - Use curated psychiatry knowledge retrieval before reasoning, support differential diagnosis with case-grounded evidence, run explicit risk and medication safety checks, flag uncertainty and missing information, and route diagnostic, medication, risk, and care-planning conclusions through human clinician review gates.
16. **PKFAR-style augmented reasoning pattern** - Start with psychiatric knowledge retrieval, scaffold differential diagnoses from case evidence, run medication and risk checks as separate review steps, attach citation/provenance notes for sourced clinical claims, and keep all mental health support framed as clinician-supervised decision support rather than diagnosis, prescribing, or crisis disposition.
17. **PKFAR-specific clinician rationale pattern** - Vet retrieved psychiatry sources for relevance, authority, recency, and case applicability before fusion; frame diagnoses as differentials with supporting, conflicting, and missing evidence; run medication and risk checks as separate verification passes; suppress or label unsupported claims, uncited guidance, and overconfident conclusions; and produce clinician-facing rationale summaries that connect case facts, vetted knowledge, safety checks, and remaining uncertainty.
18. **PKFAR-style specialty fusion safeguards** - Retrieve specialty psychiatry knowledge before augmented reasoning; separate case evidence, sourced guidance, inference, and uncertainty; run medication and risk checks for contraindications, interactions, adverse effects, suicidality, self-harm, violence, grave disability, intoxication, withdrawal, and overdose concerns; cite the evidence used for clinical claims; and escalate high-risk mental health decisions to emergency services or qualified clinician review.
19. **PKFAR-style psychiatry decision-support synthesis** - Use structured retrieval from psychiatry knowledge sources before reasoning; separate symptom reasoning, medication reasoning, and risk assessment; preserve provenance for retrieved knowledge and case facts; and present mental health decision-support outputs as clinician-reviewed drafts.
20. **PKFAR psychiatry-specific knowledge-fused augmented reasoning** - Retrieve vetted psychiatric knowledge before reasoning; keep diagnosis, medication, risk, and care-planning reasoning in separate review tracks; preserve citations for sourced clinical claims; and enforce safety escalation plus qualified clinician review for mental health decision-support outputs.
21. **PKFAR-style controlled retrieval and recommendation safeguards** - Use controlled psychiatry knowledge retrieval to support differential diagnosis, medication review, and risk checks; cite retrieved evidence for clinical claims; and block or clearly label unsupported psychiatric recommendations, especially diagnostic, prescribing, safety, or disposition guidance.
22. **PKFAR-specific knowledge injection and provenance** - Inject curated psychiatry knowledge into augmented reasoning prompts, support differential diagnosis without presenting final diagnoses, reason separately about medication considerations and risk signals, capture citation and provenance links for sourced claims, and keep outputs within clinician-supervised decision-support boundaries.
23. **PKFAR-style clinician review loop** - Retrieve curated psychiatric knowledge relevant to the case, use it to frame differential diagnoses with explicit uncertainty and missing data, reason separately about medication considerations and risk signals, escalate suicide, self-harm, violence, grave disability, intoxication, withdrawal, overdose, or other urgent safety concerns, and reserve final diagnosis, prescribing, disposition, and crisis decisions for qualified clinician review.
24. **PKFAR psychiatry-specific reasoning boundary pattern** - For psychiatry knowledge-fused augmented reasoning, retrieve from vetted psychiatry sources relevant to the case, keep diagnostic formulation, risk assessment, and medication discussion in separate bounded reasoning tracks, flag contradictions between retrieved knowledge, case facts, and user claims instead of forcing reconciliation, and require qualified human clinical review for diagnoses, prescribing decisions, safety disposition, and crisis-management recommendations.
25. **PKFAR-style context-injected differential support** - Retrieve relevant psychiatry domain knowledge, inject case-specific risk signals and medication context into bounded reasoning prompts, support differential diagnosis as clinician-reviewed decision support, and enforce safety limits against unsupervised diagnosis, prescribing, disposition, or crisis-management recommendations.
26. **PKFAR-style psychiatry knowledge-fused augmented reasoning** - Use structured retrieval of psychiatric knowledge before generating diagnostic, medication, or risk reasoning; keep diagnosis and medication discussion within non-prescriptive decision-support boundaries; apply suicide, self-harm, violence, grave-disability, intoxication, withdrawal, overdose, contraindication, interaction, adverse-effect, monitoring, and tapering cautions; preserve provenance for retrieved knowledge and case facts; and require qualified clinician review before any diagnosis, prescribing, disposition, or crisis-management decision is treated as actionable.
27. **PKFAR-style source-grounded psychiatry recommendations** - Retrieve curated psychiatric knowledge before reasoning over symptoms and medications, use augmented reasoning to connect case facts with sourced guidance, run explicit risk-assessment safety checks, and keep recommendations source-grounded, non-prescriptive, and bounded by qualified clinician review.
28. **PKFAR-style psychiatry knowledge-fused augmented reasoning update** - Retrieve psychiatric diagnostic and medication knowledge, structure differential reasoning separately from risk and treatment discussion, run risk and comorbidity checks, preserve provenance for recommendations, and apply crisis or high-risk psychiatric guardrails before producing clinician-reviewable output.

29. **Culturally adapted local-model counseling evaluation** - When evaluating local language models for mental-health counseling support, use psychiatrist review of individualization, supportiveness, cultural and linguistic appropriateness, and safety; assess problematic advice explicitly, including harmful content and mishandling of self-harm references. Record base-model and fine-tuned checkpoint versions, adaptation data, prompts, inference settings, and comparator/judge versions for reproducibility. The referenced Korean study evaluated three fine-tuned 7–8B models against GPT-4o (gpt-4o-2024-08-06): 10 blinded board-certified psychiatrists rated randomized responses to 50 held-out diary-based counseling scenarios on four 5-point scales, following GPT-5 (gpt-5-2025-08-07) screening. Treat automated judging as screening, with psychiatrist safety review retained: GPT-4o received higher safety ratings than all local models, and the automated judge showed a safety-score ceiling effect. Interpret results within the small, Korean app-based, predominantly female sample and controlled diary-response setting; generalization to other languages, populations, live dialogue, or crisis intervention remains unestablished. Comparative ratings and nonsignificant differences do not establish statistical equivalence or therapeutic effectiveness; longitudinal clinical outcomes were not assessed. See the counseling evaluation study in References.

## Inputs / Outputs

**Inputs**

- Patient age range or developmental stage when available.
- Presenting symptoms, duration, severity, triggers, course, and functional impact.
- Mental status observations, collateral information, relevant medical data, current medications, allergies, substance use, and psychosocial context.
- Prior psychiatric diagnoses, hospitalizations, therapy, medication trials, response, adverse effects, and adherence history.
- Immediate safety information, including suicidal ideation, intent, plan, access to means, prior attempts, homicidal ideation, psychosis, intoxication, withdrawal, abuse, neglect, and ability to care for self.
- User's requested output type, such as differential diagnosis, risk formulation, medication reasoning, care plan, note summary, or clinician-facing checklist.

**Outputs**

- Structured psychiatry case summary with explicit facts, relevant negatives, and missing information.
- Differential diagnosis or diagnostic formulation with supporting and conflicting evidence.
- Risk formulation that distinguishes acute risk, chronic risk, protective factors, and recommended escalation thresholds.
- Medication reasoning summary covering rationale, cautions, monitoring, interactions, and questions for the prescribing clinician.
- Care plan draft suitable for clinician review, including safety actions, follow-up timing, psychotherapy or psychosocial interventions, and coordination needs.
- Clear limitation statement that the output is clinical decision support and not a substitute for emergency services, licensed diagnosis, or prescribing.

## References

- PubMed: PKFAR: psychiatry knowledge-fused augmented reasoning with large language models. https://pubmed.ncbi.nlm.nih.gov/41982804/
- PubMed: Optimizing Small Local Language Models for Culturally Competent Mental Health Counseling: Comparative Evaluation With GPT-4o by Psychiatrists. JMIR AI (2026 Oct 22). https://pubmed.ncbi.nlm.nih.gov/42914105/ (Full text: https://ai.jmir.org/2026/1/e92470).
