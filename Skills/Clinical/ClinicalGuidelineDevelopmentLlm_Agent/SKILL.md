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
9. **Real-time evaluation checkpoints**: At each panel review checkpoint, verify evidence traceability, recommendation grading, hallucination audit findings, and versioned rationale logs before moving LLM-assisted guideline text to the next draft state.
10. **Consensus and governance**: Document panel composition, voting or consensus method, conflict-of-interest handling, signoff authority, and escalation criteria.
11. **Safety and implementation checks**: Identify ambiguous directives, unsafe absolutes, missing contraindications, patient subgroup concerns, monitoring needs, and update triggers.
12. **Audit-ready output**: Produce dated outputs with version history, evidence links, reviewer decisions, unresolved assumptions, and required human approvals.

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
