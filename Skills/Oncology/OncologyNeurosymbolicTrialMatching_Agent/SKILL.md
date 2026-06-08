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
name: 'oncology-neurosymbolic-trial-matching'
description: 'Match oncology patients to clinical trials using knowledge-graph context, symbolic eligibility reasoning, specialized agents, conflict resolution, and clinician review.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Oncology Neuro-Symbolic Trial Matching

## Overview

This skill produces auditable oncology clinical trial candidate matches by combining structured patient facts, an oncology-specific knowledge graph, symbolic eligibility rules, and specialized reasoning agents. It is grounded in a prospective evaluation involving 3,804 patients and keeps clinician review central to resolving uncertainty and approving final recommendations.

## When to Use This Skill

- Match a patient with cancer to recruiting or otherwise specified clinical trials.
- Evaluate complex inclusion and exclusion criteria across diagnosis, stage, biomarkers, treatment history, laboratory results, performance status, age, and geography.
- Reconcile inconsistent patient records, trial text, terminology, or agent conclusions.
- Produce criterion-level evidence, uncertainty labels, and reasons for inclusion or exclusion.
- Design or assess an auditable multi-agent workflow for oncology trial matching.
- Re-evaluate matches after patient data, trial status, protocol amendments, or recruiting sites change.

## Core Capabilities

1. **Patient fact normalization:** Convert clinical notes and structured records into dated, source-linked facts while preserving absent, unknown, and conflicting values.
2. **Trial retrieval and versioning:** Retrieve plausible trials using disease, molecular, treatment, phase, age, geography, and recruitment constraints; record the registry identifier, protocol version, status, sites, and retrieval time.
3. **Oncology knowledge-graph grounding:** Map cancers, variants, biomarkers, therapies, prior regimens, resistance concepts, and trial concepts to canonical entities and explicit relationships without treating inferred links as documented patient facts.
4. **Symbolic criterion compilation:** Decompose eligibility text into atomic, testable rules with operators, thresholds, temporal windows, units, dependencies, and negation.
5. **Specialized agent assessment:** Assign focused agents to disease context, molecular eligibility, treatment history, safety and laboratory criteria, and logistics while requiring each conclusion to cite supporting patient and protocol evidence.
6. **Neuro-symbolic synthesis:** Use language-model reasoning for extraction and interpretation, then enforce deterministic rule evaluation for criteria that can be represented symbolically.
7. **Conflict resolution:** Detect disagreements among records, rules, knowledge-graph inferences, and agent outputs; prefer authoritative and current evidence, retain unresolved conflicts, and prohibit unsupported tie-breaking.
8. **Clinician review:** Escalate ambiguous, safety-critical, temporally unstable, or potentially disqualifying findings for human adjudication before presenting a match as actionable.
9. **Audit and monitoring:** Preserve criterion-level decisions, evidence provenance, rule versions, agent outputs, overrides, timestamps, and reasons for match changes.
10. **Prospective-evaluation workflow:** Apply the integrated pattern evaluated prospectively in 3,804 oncology patients: ontology-backed knowledge-graph grounding, multi-agent division of labor, neuro-symbolic eligibility checks, criterion-level audit trails, and clinician review loops.

## Inputs / Outputs

### Inputs

- Patient data: cancer diagnosis, histology, stage, disease state, biomarkers, genomic findings, age, sex where protocol-relevant, performance status, comorbidities, organ function, laboratory values with dates and units, prior and current treatments, outcomes, and relevant procedures.
- Trial data: registry record, protocol or eligibility text, recruitment status, phase, intervention, cohort definitions, sites, contacts, amendment or version date, and retrieval timestamp.
- Operational constraints: travel radius, preferred geography, referral requirements, consent limitations, language needs, and the matching cutoff date.
- Terminology resources: oncology ontologies, drug and disease vocabularies, variant annotations, and knowledge-graph relations with source and version metadata.

### Outputs

- Ranked candidate trials labeled `potentially eligible`, `potentially ineligible`, or `insufficient information`; do not report definitive eligibility without authorized trial-site confirmation.
- A criterion-by-criterion matrix containing the normalized rule, patient evidence, evidence source and date, evaluation result, confidence, and rationale.
- A missing-information list that distinguishes retrievable data from tests, examinations, or clinician judgments still required.
- A conflict report describing contradictory facts or agent conclusions and how each was resolved or escalated.
- A clinician-review queue prioritizing safety-critical, exclusionary, ambiguous, and time-sensitive issues.
- An audit record containing trial and rule versions, provenance, timestamps, agent roles, overrides, and final reviewer disposition.

### Workflow

1. Validate that patient and trial inputs have identifiers, dates, units, provenance, and an explicit matching cutoff date.
2. Normalize patient facts and trial concepts to canonical oncology entities while retaining original text and source links.
3. Retrieve candidate trials broadly enough to avoid premature exclusion, then apply explicit operational filters.
4. Compile each trial's eligibility criteria into atomic rules; mark criteria that cannot be represented deterministically.
5. Run specialized assessments independently and require evidence for every eligibility claim.
6. Execute symbolic rules using normalized facts, including unit conversion and temporal-window checks where valid.
7. Compare agent conclusions with symbolic results and knowledge-graph context; log every disagreement.
8. Resolve conflicts using source authority, recency, protocol wording, and clinician adjudication. Never convert missing data into a favorable eligibility result.
9. Rank candidates using transparent factors such as eligibility coverage, unresolved exclusions, missing data burden, recruitment status, and logistics.
10. Generate the criterion matrix, review queue, conflict report, and audit record for clinician approval.
11. Re-run affected criteria when patient facts, trial status, recruiting sites, or protocol versions change.

## References

- Loaiza-Bonilla A, Yost C, Kurnaz S, Tuysuz E, Thaker NG. “Transforming oncology clinical trial matching through neuro-symbolic, multi-agent AI and an oncology-specific knowledge graph: a prospective evaluation in 3804 patients.” *ESMO Real World Data and Digital Oncology*. 2026 Jun. PubMed: https://pubmed.ncbi.nlm.nih.gov/42004487/
