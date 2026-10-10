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
name: 'clinical-guideline-development-llm'
description: 'Guide LLM-assisted clinical practice guideline drafting with real-time review, evidence traceability, recommendation grading, and clinician governance.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Clinical Guideline Development LLM

## Overview

This skill guides LLM-assisted clinical practice guideline development from question framing through evidence-linked recommendations, review, and governance. It emphasizes transparent evidence handling, recommendation grading, consensus documentation, auditability, and human clinical oversight because guideline development affects care standards and must not be treated as ordinary drafting.

## When to Use This Skill

- Drafting, updating, or revising a clinical practice guideline, protocol, pathway, or consensus statement.
- Converting evidence summaries into guideline recommendations with explicit strength, certainty, and rationale.
- Building evidence-to-decision tables, recommendation matrices, implementation notes, or audit trails.
- Running real-time clinician or panel review of LLM-generated guideline text.
- Checking guideline drafts for evidence traceability, conflicts, scope drift, unsafe wording, or missing governance steps.
- Preparing clinician-facing review packets that separate evidence, judgment, consensus, and implementation considerations.

## Core Capabilities

1. **Scope and question framing**: Define population, intervention, comparator, outcomes, care setting, exclusions, and intended users before drafting recommendations.
2. **Evidence traceability**: Link every material claim and recommendation to cited evidence, evidence tables, or an explicit expert-consensus rationale.
3. **Recommendation grading**: Record certainty of evidence, balance of benefits and harms, values and preferences, resource considerations, equity, feasibility, and recommendation strength.
4. **LLM-assisted drafting controls**: Use the model for synthesis, wording, consistency checks, and gap detection while preserving source-grounded claims and clinician review.
5. **Real-time review workflow**: Track reviewer comments, disagreement, edits, unresolved issues, and rationale changes during live or iterative guideline development.
6. **Real-time LLM evaluation during drafting**: Maintain live evidence traceability, recommendation grades, clinician adjudication of model-suggested changes, bias and omission checks against source evidence, and audit logs from draft through final guideline approval.
7. **Draft-to-final evaluation workflow**: For real-time LLM guideline development, preserve change-level evidence traceability, recommendation-grade updates, conflict logs, clinician review checkpoints, and audit artifacts explaining accepted, rejected, or revised model contributions.
8. **Real-time guideline-panel safeguards**: During live LLM-assisted development, run evidence traceability and recommendation grading checks, keep human guideline-panel oversight over accepted wording, log hallucinations or errors with corrections, and escalate unsupported, unsafe, overconfident, or grading-inconsistent generated language for clinician rewrite.
9. **Clinician-in-the-loop drafting evaluation**: During recommendation drafting, require clinician review of model-generated language, live evidence traceability, recommendation grading, conflict-of-interest checks, and explicit limits that LLM text remains draft support until human approval.
10. **Real-time evaluation checkpoints**: At each panel review checkpoint, verify evidence traceability, recommendation grading, hallucination audit findings, and versioned rationale logs before moving LLM-assisted guideline text to the next draft state.
11. **Guideline text acceptance gates**: Before accepting LLM-assisted guideline text, confirm evidence traceability, recommendation grading, iterative clinician review disposition, conflict logging, and governance checkpoint signoff.
12. **Expert adjudication advance criteria**: Before LLM-generated draft text advances to clinician review, require source-linked evidence traceability, recommendation-grade consistency, hallucination and unsupported-claim checks, expert adjudication of disputed wording, and documented governance criteria for promotion or revision.
13. **Real-time LLM evaluation handoffs**: Before panel handoff, check evidence traceability, recommendation grading, conflicts, and omissions; label LLM output as drafting assistance only, with guideline authority reserved for documented panel review and approval.
14. **Reject-or-escalate governance criteria**: During real-time LLM evaluation for guideline development, reject or escalate generated text when evidence traceability is missing, recommendation grading is inconsistent, reviewer checkpoint disposition is unresolved, contradictions are logged against source evidence or prior recommendations, or required governance approval is absent.
15. **Real-time LLM-assisted guideline development pattern**: Maintain evidence traceability and recommendation grading through iterative expert review, require conflict-of-interest disposition, retain audit logs of model suggestions and panel decisions, and reject unsupported recommendations lacking source or consensus justification.
16. **Real-time recommendation drafting audits**: Audit recommendation drafts for source-linked evidence traceability, recommendation-grade consistency, panel review checkpoint disposition, and unsupported or overconfident language; do not allow unsupervised LLM-generated guideline language to advance without documented panel review and approval.
17. **Real-time LLM-assisted guideline governance**: In live drafting, require evidence traceability, recommendation grading, clinician editorial control, audit logs, conflict handling, and explicit reject-or-revise gates for generated guideline text that is unsupported, grading-inconsistent, unsafe, unresolved after review, or lacking required approval.
18. **Draft adoption evaluation checkpoints**: Before any draft guideline is adopted, confirm evidence traceability, recommendation grading, live expert review disposition, disagreement logging, and governance gate approval.
19. **Consensus and governance**: Document panel composition, voting or consensus method, conflict-of-interest handling, signoff authority, and escalation criteria.
20. **Safety and implementation checks**: Identify ambiguous directives, unsafe absolutes, missing contraindications, patient subgroup concerns, monitoring needs, and update triggers.
21. **Audit-ready output**: Produce dated outputs with version history, evidence links, reviewer decisions, unresolved assumptions, and required human approvals.
22. **Real-time LLM evaluation record**: Across draft iterations, verify evidence traceability and recommendation grading, require expert adjudication of model-suggested recommendations or disputed edits, perform risk-of-harm review for unsafe or overconfident wording, and retain audit logs of prompts, outputs, edits, reviewer decisions, and rationale changes.
23. **Prospective guideline review checkpoints**: During real-time LLM-assisted guideline development, use prospective panel review checkpoints to confirm evidence traceability, adjudicate generated text, verify recommendation grading, and log failure modes such as unsupported claims, omissions, unsafe wording, or grading conflicts before accepting draft language.
24. **Live expert review acceptance criteria**: Use live expert review loops to compare LLM-suggested guideline language against source evidence, recommendation grades, and panel judgment; log discrepancies and treat LLM assistance as acceptable only when evidence traceability, grading consistency, reviewer disposition, and governance signoff are complete, escalating unsafe or unsupported output.
25. **Documented acceptance checkpoints**: Before guideline text is accepted, verify evidence traceability, recommendation grading, expert adjudication, bias and omission review, and documented human sign-off.
26. **Limits on autonomous guideline drafting**: At defined expert adjudication checkpoints, verify evidence traceability and recommendation grading, review generated content for bias, hallucinations, and unsupported claims, and prohibit the LLM from autonomously drafting, approving, or issuing guideline recommendations without documented expert review and sign-off.
27. **Concurrent expert evaluation protocol**: Review LLM-generated text concurrently with guideline drafting, trace claims to evidence, classify identified errors, verify recommendation grading, and adjudicate disagreements; prevent any unreviewed LLM text from entering the guideline or advancing toward approval.
28. **Worked real-time evaluation protocol**: Prospectively log prompts, outputs, edits, elapsed drafting and review time, evidence-verification results, recommendation grades, reviewer disagreements and adjudications, and errors by defined taxonomy; compare recorded time with the selected non-LLM workflow without presuming savings, escalate unsupported evidence, grading conflicts, unresolved disagreement, unsafe language, or high-impact errors, and keep LLM drafting assistance separate from final recommendation and approval decisions reserved for the guideline panel.
29. **Prospective real-time evaluation design**: During live guideline development, retrieve evidence as questions arise, preserve recommendation-to-source traceability, require expert adjudication of generated drafts, log reviewer disagreements and their disposition, measure retrieval, drafting, and review latency, and stop the workflow when a draft is unsafe, unsupported by retrieved evidence, or cannot be resolved through expert review.
30. **Operational case study for real-time guideline-development evaluation**: Apply task-level measurement to evidence retrieval, synthesis, recommendation drafting, grading, and revision; preserve claim-to-source evidence traceability; require expert adjudication and recommendation-grade review; log errors and their disposition; and stop unsupported synthesis when source support cannot be verified or expert review cannot resolve it.
31. **Worked example from real-time LLM guideline evaluation**: Use the 2026 real-time evaluation of an LLM for clinical practice guideline development as a worked authoring example: trace each draft recommendation to evidence or consensus rationale, capture expert review and conflicts as they arise, record recommendation drafting changes, and require human governance checkpoint signoff before draft language advances.
32. **Real-time evaluation authority checkpoints**: At each live guideline-development checkpoint, verify evidence traceability, recommendation grading, conflict tracking, and expert adjudication status, and state that LLM output is drafting assistance only while final guideline authority remains with the designated human guideline process.
33. **Prospective model-suggestion evaluation**: Prospectively capture model suggestions during guideline drafting, preserve evidence traceability and recommendation grading for each generated text segment, require expert adjudication, log reviewer disagreements and disposition, and apply predefined governance thresholds for accepting, revising, or rejecting model-generated guideline text.
34. **Real-time guideline-development evaluation pattern**: Evaluate LLM outputs during live guideline drafting for evidence traceability, recommendation grading support, hallucinations or unsupported claims, expert panel review disposition, and explicit human governance approval before any guideline language is adopted.
35. **Real-time evaluation loop**: For each LLM-suggested claim or recommendation, run evidence traceability checks, verify recommendation-level grading, route disputed or high-impact language through expert adjudication checkpoints, retain audit logs of prompts, outputs, edits, decisions, and rationale, and state that LLM output may inform drafting but must not determine clinical practice guidance.
36. **Criterion-level real-time adjudication record**: During live guideline drafting, document criterion-level evidence traceability, recommendation grading, expert adjudication decisions, unresolved uncertainty, and audit artifacts that distinguish LLM drafting support from autonomous clinical guideline authorship.
37. **Case study: real-time guideline-development evaluation**: Use the 2026 real-time LLM guideline-development evaluation as a case study for LLM-assisted evidence synthesis, recommendation drafting, provenance tracking, expert adjudication, and governance checkpoints; do not infer benchmark performance or clinical effectiveness claims beyond the source finding.
38. **Nuance and certainty failure-mode checks**: At real-time guideline-development checkpoints, verify evidence traceability and recommendation grading, route disputed or high-impact draft language to expert adjudication, retain audit logs, and flag LLM drafts that omit clinical nuance or overstate certainty before they can advance.
39. **Real-time guideline-development adjudication controls**: For live LLM-assisted guideline drafting, require evidence traceability, recommendation grading, expert adjudication, conflict-of-interest and disagreement handling, audit logs of prompts, outputs, edits, and decisions, and an explicit rule that LLM outputs are drafting aids only and never autonomous guideline authors or approvers.
40. **Governed real-time drafting boundary**: During live clinical practice guideline drafting, allow LLM assistance only within documented support tasks and require evidence traceability, expert adjudication, recommendation grading, bias checks, and human approval before any generated wording or recommendation advances.
41. **Real-time evaluation acceptance record**: Before accepting any LLM-assisted guideline text, document evidence traceability, recommendation grading, expert adjudication, failure logging, and explicit human governance approval.
42. **Live drafting stop/go governance**: During real-time LLM-assisted guideline drafting, route model suggestions through expert adjudication, verify evidence traceability and recommendation-grade consistency, log reviewer conflicts and dispositions, and apply documented stop/go decisions before wording or recommendations advance.
43. **Real-time panel workflow evaluation**: During clinical practice guideline development, evaluate LLM contributions in real time with evidence traceability, recommendation grading checks, hallucination review, expert adjudication, and documented governance requirements for guideline-panel workflows.
44. **Case study: governed live model review**: Treat the 2026 real-time clinical practice guideline development evaluation as a case study for evidence traceability, recommendation grading, expert adjudication, conflict logging, live model review, and human governance checkpoints during guideline drafting; do not add performance benchmarks or clinical-effectiveness claims beyond the cited finding.
45. **Staged real-time governance pattern**: During live guideline development, stage evidence retrieval before recommendation drafting, route generated wording through expert adjudication, run traceability checks and hallucination screening before acceptance, and keep LLM assistance limited to guideline wording support while evidence grading remains a documented human guideline-panel responsibility.
46. **Real-time checkpoint failure boundaries**: At live guideline-development checkpoints, verify evidence traceability, recommendation grading, human expert adjudication, and conflict logging before accepting model-suggested language; do not let the model draft recommendations independently when source support is missing, grading is unresolved or inconsistent, conflicts remain unadjudicated, or human guideline authority has not approved the draft.
47. **Real-time practice-guideline evaluation controls**: Use the 2026 real-time clinical practice guideline development evaluation as source support for evidence traceability, expert-review checkpoints, recommendation grading review, prompt and audit logging, and explicit limits that prevent autonomous LLM drafting or approval of guideline recommendations.
48. **Recommendation drafting checkpoint discipline**: During real-time LLM-assisted guideline development, pause each draft recommendation for evidence traceability, expert adjudication, recommendation-grade consistency review, and guardrail checks that reject unsupported or grading-inconsistent guideline language before it advances.
49. **Operational real-time guideline evaluation pattern**: Apply real-time clinical practice guideline development evaluation as an operational pattern by preserving evidence traceability, routing drafts through iterative expert panel review, verifying recommendation grading, logging conflicts and dispositions, and prohibiting unsupervised LLM-generated guideline text from being accepted, approved, or issued.
50. **Workflow evidence source for live CPG evaluation**: Use the 2026 real-time clinical practice guideline development evaluation as workflow evidence for separating LLM-assisted drafting, literature summarization, recommendation wording, grading review, conflict checking, and expert panel review; maintain traceable citations and audit logs for each assisted step.
51. **Real-time provenance and stop-condition protocol**: During clinical practice guideline development, keep provenance tables that map each LLM-generated claim or recommendation to source evidence, recommendation grade, expert adjudication decision, conflict status, and disposition; stop or reject the workflow when model output diverges from source evidence, lacks traceability, conflicts with grading, or cannot be resolved by expert adjudication.
52. **Constrained real-time guideline governance pattern**: For real-time clinical practice guideline development evaluation, constrain LLM use to evidence retrieval, draft comparison, traceability checks, recommendation grading support, and expert panel adjudication; do not treat model output as independent recommendation authorship, approval, or issuance.
53. **Audit-ready real-time evaluation pattern**: During LLM-assisted clinical practice guideline development, run evidence traceability checks, AGREE/GRADE-aligned recommendation review, recommendation discrepancy logging, expert adjudication, and audit-ready versioning of prompts, outputs, source links, edits, decisions, and rationale changes.
54. **Real-time evaluation boundaries for guideline drafting**: Evaluate LLM contributions during live clinical practice guideline development by preserving evidence traceability, requiring expert adjudication and recommendation grading review, retaining audit logs of prompts, outputs, edits, and decisions, and explicitly prohibiting autonomous LLM drafting, approval, or issuance of guideline recommendations.
55. **Real-time CPG authority checkpoints**: During clinical practice guideline development, evaluate LLM-supported drafts in real time with evidence traceability, recommendation grading review, expert panel checkpoints, conflict logging, and explicit separation of drafting support from final clinical authority.
56. **Criterion-level guideline-writing assistance controls**: For each LLM-assisted claim, evidence criterion, and draft recommendation, define source-linked evidence traceability, expert adjudication checkpoints, recommendation grading boundaries, hallucination and unsupported-claim review, and governance logs before text advances.
57. **Source-grounded real-time CPG evaluation**: Use the 2026 real-time clinical practice guideline development evaluation as source support for LLM-assisted guideline workflows that require evidence traceability, recommendation grading review, expert adjudication, audit logs, and explicit limits on autonomous drafting or approval.
58. **Role-defined real-time CPG evaluation**: Before live guideline drafting, define the LLM role as support rather than authority, preserve evidence traceability for generated claims and recommendations, require expert adjudication and recommendation grading review, run hallucination and unsupported-claim checks, and obtain documented governance approval before guideline text is accepted.
59. **Panel-bounded real-time LLM evaluation**: During clinical practice guideline development, map each LLM contribution to evidence traceability, recommendation grading support, expert adjudication status, reviewer disagreement or conflict disposition, and an explicit boundary that LLMs may assist with retrieval, synthesis, wording, and checks while guideline panels decide recommendation strength, adoption, approval, and issuance.
60. **Real-time CPG evaluation checklist**: For each LLM-assisted guideline-panel work item, confirm source-linked evidence traceability, expert adjudication of generated or disputed text, recommendation grading review, hallucination or unsupported-claim checks, and documented governance disposition before wording advances.
61. **Real-time LLM contribution disposition pattern**: For clinical practice guideline development, require explicit evidence provenance, recommendation grading, live expert review, uncertainty capture, and audit logs that classify each model contribution as accepted, revised, or rejected.
62. **Real-time LLM evaluation loop**: During clinical practice guideline development, extract evidence tables, check recommendation grading consistency, review conflict-of-interest declarations and citation provenance, stage living-guideline update triggers, route disputed model-assisted edits to expert panel adjudication, and retain audit logs for prompts, outputs, edits, decisions, and rationale.
63. **Governance example: real-time CPG evaluation**: Use the 2026 real-time clinical practice guideline development evaluation as a governance example requiring source-linked evidence traceability, recommendation grading checkpoints, live expert review, disagreement logging with disposition, and explicit limits that LLM-generated guideline text remains draft support until documented consensus approval.
64. **Real-time model-impact evaluation**: During clinical practice guideline development, use LLMs for recommendation drafting support and checks while preserving evidence traceability, expert-review checkpoints, grading/rationale separation, hallucination and unsupported-claim checks, and documentation of where model output changed or failed to change panel output.
65. **Real-time guideline text adjudication**: Evaluate LLM-generated guideline text during development by preserving evidence traceability, verifying recommendation grading, logging conflicts and dispositions, requiring expert-panel review, and rejecting or revising text that lacks source support, conflicts with grading or panel decisions, contains unsupported or unsafe claims, or has unresolved review status.
66. **Evidence case study: prospective task-level safeguards**: Use the 2026 real-time guideline-development evaluation as a case study for prospectively logging each LLM-assisted task and its source traceability, recording expert corrections so correction rates can be calculated without presuming a benchmark, documenting recommendation grading, and predefining risk-based criteria that prohibit LLM assistance or require dual expert review before high-impact or unresolved content advances.

## Inputs / Outputs

**Inputs**

- Guideline topic, scope, target population, setting, intended users, and clinical questions.
- Source evidence, citations, systematic reviews, trial summaries, existing guideline text, or evidence tables.
- Preferred grading framework, consensus method, review timeline, and required institutional governance steps.
- Reviewer identities or roles, conflict-of-interest declarations, comments, decisions, and approval requirements.

**Outputs**

- Structured guideline draft with scope, definitions, recommendations, rationale, implementation notes, and review status.
- Evidence-to-recommendation table linking each recommendation to evidence, certainty, strength, and rationale.
- Traceability matrix mapping claims to sources or consensus justification.
- Reviewer decision log with comments, changes, unresolved issues, and escalation items.
- Final human-review checklist covering evidence support, grading, conflicts, safety language, governance, and update plan.

## References

- Erstad BL. Real-Time Evaluation of a Large Language Model for Clinical Practice Guideline Development. *Crit Care Explor*. 2026 May 1. https://pubmed.ncbi.nlm.nih.gov/42042855/
- PubMed record: https://pubmed.ncbi.nlm.nih.gov/42042855/
