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
11. **Deployment-scale evaluation:** Define prospective workflow metrics before use; measure criterion resolution, unresolved conflicts, review burden, turnaround, and clinician overrides without presuming benchmark values; analyze override reasons against knowledge-graph construction, agent responsibilities, symbolic rule results, and criterion-level evidence; and retain reproducible patient, protocol, rule, agent, conflict, override, and reviewer audit records for deployment-scale trial matching.
12. **Prospective-evaluation controls:** Record source and version provenance for every knowledge-graph assertion used in a match; execute symbolic eligibility checks separately from language-model interpretation; resolve agent and rule disagreements through documented multi-agent conflict resolution and clinician adjudication; provide criterion-level explanations; audit recall against a defined review set; capture clinician overrides and their reasons; and report operational throughput metrics without assuming unreported benchmark values.
13. **3,804-patient prospective validation pattern:** Structure validation after the reported prospective oncology evaluation by preserving criterion-level traceability and knowledge-graph provenance, documenting agent-conflict resolution, measuring turnaround time, recording clinician overrides and reasons, and reporting predefined prospective matching metrics without inventing unreported benchmark values.
14. **Reference architecture and validation pattern:** Use the prospective 3,804-patient evaluation as a reference pattern for oncology knowledge-graph grounding, specialized agents, symbolic eligibility checks, criterion-level explanations, documented conflict resolution, and clinician review; evaluate recall and clinician workload using predefined metrics without inferring unreported benchmark values.
15. **Prospective 3,804-patient reference pattern:** Use oncology-specific knowledge-graph retrieval to ground trial candidates and protocol concepts; run symbolic criterion checks; resolve agent conflicts with documented rationale; emit clinician-auditable evidence with per-criterion `MET`, `NOT`, or `UNKNOWN` outputs; and track prospective performance over time without adding unreported benchmark claims.
16. **Benchmark scenario:** Use PubMed 42004487's prospective 3,804-patient oncology trial matching evaluation as a benchmark scenario for neuro-symbolic eligibility reasoning, oncology knowledge-graph grounding, multi-agent role separation, conflict resolution, and clinician-auditable evidence outputs without importing unreported performance thresholds.
17. **Prospective multi-agent reference pattern:** Treat PubMed 42004487 as a reference pattern for oncology-specific knowledge-graph retrieval, criterion-level symbolic reasoning, documented conflict resolution, auditable evidence packages, predefined prospective metrics, and clinician-in-the-loop review without inventing unreported benchmarks or claims.
18. **Prospective evaluation operating loop:** For workflows modeled on the 3,804-patient prospective report, ground candidate trials and eligibility criteria in an oncology-specific knowledge graph, run criterion-level symbolic checks, route agent and rule conflicts through documented resolution, maintain audit trails, and keep clinician review loops before final recommendations.
19. **Prospective cohort reporting pattern:** For neuro-symbolic multi-agent trial matching modeled on PubMed 42004487, parse criteria against oncology knowledge-graph entities, keep agent roles separated, route conflicts through documented resolution, preserve patient-level audit traces, and report cohort-scale performance without adding unreported benchmark values.
20. **Prospective benchmark example:** Use the 3,804-patient prospective oncology trial-matching evaluation as a benchmark example for neuro-symbolic matching workflows that combine knowledge-graph eligibility reasoning, multi-agent conflict handling, source-linked evidence trails, and clinician auditability without adding unreported performance claims.
21. **Prospective throughput and explanation capture:** For the reported prospective neuro-symbolic multi-agent evaluation, document oncology knowledge-graph grounding, criterion-level reasoning, conflict-resolution decisions, throughput metrics across the 3,804-patient cohort, and clinician-auditable explanations without adding unreported benchmark values.
22. **Patient-scale prospective reporting:** When adapting the 3,804-patient prospective evaluation, report patient-scale performance without inventing absent benchmarks; connect oncology knowledge-graph eligibility reasoning, conflict-resolution outcomes, criterion-level evidence, and clinician-auditable outputs to patient, protocol, rule, agent, and reviewer provenance.
23. **Audit-ready prospective handoff workflow:** Use the prospective 3,804-patient oncology trial-matching evaluation as a reference workflow for oncology knowledge-graph retrieval, neuro-symbolic eligibility reasoning, multi-agent review, criterion-level evidence capture, documented conflict resolution, and audit-ready clinician handoff without adding unreported benchmark claims.
24. **Prospective 3,804-patient evidence integration:** For workflows informed by PubMed 42004487, ground patient and protocol concepts in the oncology knowledge graph, apply criterion-level neuro-symbolic reasoning, document multi-agent conflict resolution, capture prospective performance metrics and clinician-review outcomes, and preserve audit artifacts for every recommendation without adding unreported benchmark values.
25. **Prospective validation anchor:** Anchor neuro-symbolic multi-agent oncology trial matching to the reported 3,804-patient prospective evaluation by requiring criterion-level evidence, oncology knowledge-graph grounding, documented conflict resolution, clinician review, and measurable matching outcomes without inventing unreported performance values.
26. **Prospective monitoring pattern:** When adapting the 3,804-patient neuro-symbolic multi-agent evaluation, represent eligibility in an oncology knowledge graph, evaluate each criterion explicitly, resolve patient-rule-agent conflicts with documented rationale, capture throughput metrics prospectively, expose clinician-auditable evidence, and monitor match changes over time without adding unreported benchmark values.
27. **Prospective design evidence:** Treat the 3,804-patient oncology evaluation reported in PubMed 42004487 as evidence supporting neuro-symbolic multi-agent trial matching designs that combine oncology knowledge-graph grounding, eligibility rule parsing, documented conflict resolution, patient-level audit trails, predefined prospective performance metrics, and clinician review checkpoints without adding unreported benchmark values.
28. **KG-backed eligibility benchmark:** Treat PubMed 42004487's prospective 3,804-patient neuro-symbolic multi-agent oncology trial-matching evaluation as a benchmark for knowledge-graph-backed eligibility reasoning, documented conflict resolution, criterion-level evidence, and clinician-auditable matching outputs without adding unreported performance thresholds.
29. **Prospective reference-pattern adoption:** Apply PubMed 42004487's prospective 3,804-patient oncology trial-matching evaluation as a reference pattern for explicit multi-agent role splitting, oncology knowledge-graph grounding, symbolic eligibility checks, criterion-level evidence, disagreement handling, predefined metrics, and clinician-auditable outputs without adding unreported benchmark values.
30. **Prospective deployment benchmark pattern:** Use the reported 3,804-patient prospective evaluation as a benchmark pattern for neuro-symbolic, multi-agent oncology trial matching with oncology knowledge-graph grounding, criterion-level reasoning, documented conflict handling, clinician auditability, and measured deployment outcomes, while avoiding unreported performance claims.
31. **Key prospective validation reference:** Cite the 3,804-patient prospective oncology trial-matching evaluation as validation context for neuro-symbolic eligibility reasoning, oncology knowledge-graph grounding, multi-agent coordination, documented conflict resolution, auditable evidence packages, and clinician review without adding claims beyond the source finding.
32. **Prospective evidence source:** Incorporate PubMed 42004487 as a key evidence source for prospective 3,804-patient neuro-symbolic multi-agent oncology trial matching, including oncology knowledge-graph grounding, specialized agents, criterion-level reasoning, conflict handling, and clinician-auditable output.
33. **Prospective validation evidence:** Cite the prospective 3,804-patient evaluation in PubMed 42004487 as validation evidence for neuro-symbolic multi-agent oncology trial matching that combines oncology-specific knowledge-graph grounding, criterion-level symbolic eligibility checks, documented conflict resolution, and clinician-auditable output without adding unreported benchmark claims.
34. **Prospective match-quality evaluation:** Use the 3,804-patient prospective neuro-symbolic multi-agent evaluation as a pattern for oncology-specific knowledge-graph grounding, criterion-level symbolic eligibility checks, documented conflict resolution, audit trails, and prospectively captured match-quality metrics without inventing unreported values.
35. **Clinician-auditable neuro-symbolic rationale:** Strengthen match rationales with the prospective 3,804-patient oncology trial-matching evaluation by decomposing eligibility work across specialized agents, grounding patient and protocol concepts in an oncology knowledge graph, separating symbolic criterion checks from language-model interpretation, recording criterion-level evidence and conflict-resolution decisions, and presenting clinician-auditable `MET`, `NOT`, or `UNKNOWN` reasoning without adding unreported benchmark claims.
36. **Prospective benchmark case:** Treat the 3,804-patient prospective evaluation in PubMed 42004487 as a benchmark case for neuro-symbolic multi-agent oncology trial matching that combines oncology-specific knowledge-graph grounding, criterion-level reasoning, documented conflict resolution, clinician-auditable evidence, and prospective workflow metrics without inventing unreported benchmark values.
37. **KG-grounded benchmark pattern:** Use PubMed 42004487's prospective 3,804-patient neuro-symbolic multi-agent oncology trial-matching evaluation as a benchmark pattern for KG-grounded eligibility parsing, criterion-level evidence capture, documented conflict resolution, recall and precision reporting, and clinician override audit trails without inventing unreported performance values.
38. **Prospective 3,804-patient support:** Use the 2026 prospective evaluation in 3,804 oncology patients as support for neuro-symbolic multi-agent trial matching that combines an oncology-specific knowledge graph, criterion-level reasoning, documented conflict resolution, auditability, and clinician review without adding unreported benchmark claims.
39. **Clinician-auditable prospective outputs:** For workflows informed by PubMed 42004487, ground patient and protocol concepts in the oncology-specific knowledge graph, run neuro-symbolic eligibility checks, route multi-agent disagreements through documented conflict resolution, preserve patient-level evidence trails, and emit clinician-auditable `MET`, `NOT`, or `UNKNOWN` outputs without adding claims absent from the source finding.
40. **Prospective implementation pattern:** Model neuro-symbolic, multi-agent oncology trial matching on PubMed 42004487's prospective 3,804-patient evaluation by combining oncology knowledge-graph grounding, criterion-level eligibility reasoning, documented conflict resolution, predefined metrics, and clinician-auditable evidence without importing unreported benchmark values.
41. **Prospective validation pattern:** Use the reported 3,804-patient neuro-symbolic multi-agent evaluation as a validation pattern for criterion-level eligibility extraction, oncology knowledge-graph grounding, separated agent roles, documented conflict resolution, confidence scoring, and clinician-auditable evidence trails without adding claims absent from the source finding.
42. **High-priority 2026 evidence update:** Treat PubMed 42004487, a prospective evaluation in 3,804 oncology patients, as high-priority evidence for neuro-symbolic, multi-agent trial matching; require oncology-specific knowledge-graph grounding, criterion-level symbolic eligibility reasoning, documented conflict resolution, clinician-in-the-loop review, and audit-ready provenance while avoiding unreported benchmark or performance claims.
43. **Prospective validation pattern with evidence summaries:** Apply the 3,804-patient prospective evaluation as a validation pattern for oncology-specific knowledge graph retrieval, neuro-symbolic eligibility checks, multi-agent review roles, criterion-level audit trails, conflict handling, and clinician-facing evidence summaries for trial matching without adding unreported benchmark claims.
44. **Prospective study implementation details:** When applying the 3,804-patient prospective neuro-symbolic multi-agent study pattern, include oncology-specific knowledge graph construction with provenance, criterion-level symbolic reasoning, separated agent roles, documented conflict resolution, clinician-facing evidence display, and prospective performance monitoring without adding unreported benchmark values.
45. **Prospective KG-backed eligibility evidence:** Use PubMed 42004487's prospective 3,804-patient neuro-symbolic multi-agent oncology trial-matching evaluation as evidence for knowledge-graph-backed eligibility reasoning, criterion-level auditability, documented conflict resolution, clinician review, and prospective performance monitoring without adding claims absent from the source finding.
46. **Prospective 3,804-patient operating evidence:** Incorporate PubMed 42004487 by grounding patient and protocol concepts in an oncology-specific knowledge graph for eligibility reasoning, separating agent roles, documenting conflict resolution, preserving criterion-level evidence, capturing prospective metrics, and enforcing human review checkpoints without adding claims absent from the source finding.
47. **Prospective 3,804-patient trial-matching evidence:** Incorporate the 2026 prospective evaluation in 3,804 oncology patients by constructing oncology-specific knowledge graphs with source and version provenance, separating criterion-level symbolic eligibility reasoning from language-model interpretation, documenting conflict-resolution and confidence-scoring decisions, and producing clinician-auditable evidence trails without adding claims absent from PubMed 42004487.
48. **Prospective neuro-symbolic multi-agent evaluation:** Incorporate PubMed 42004487's prospective 3,804-patient oncology trial-matching evaluation as source evidence for oncology-specific knowledge-graph grounding, criterion-level eligibility reasoning, multi-agent conflict resolution, evidence-linked criteria, and clinician-auditable review without adding unreported benchmark or performance claims.
49. **Prospective 3,804-patient design pattern:** Use the June 2026 prospective evaluation in 3,804 oncology patients as a reference pattern for oncology-specific knowledge-graph grounding, criterion-level symbolic reasoning, separated extraction and eligibility-review agents, auditable evidence trails, documented disagreement handling, and prospective performance monitoring without adding claims absent from PubMed 42004487.
50. **Confidence-reported prospective evidence:** Use the 2026 prospective 3,804-patient evaluation as evidence for neuro-symbolic multi-agent oncology trial matching that combines oncology knowledge graphs, criterion-level reasoning, documented conflict resolution, confidence reporting, and clinician-auditable explanations without adding unreported benchmark claims.
51. **Prospective benchmark workflow pattern:** Treat PubMed 42004487's June 2026 prospective evaluation in 3,804 oncology patients as a benchmark pattern for neuro-symbolic multi-agent trial matching workflows that retrieve evidence through an oncology-specific knowledge graph, evaluate eligibility at criterion level with symbolic reasoning, document conflict resolution, preserve audit trails, and require clinician review gates before action.
52. **Clinician-review metric integration:** When using PubMed 42004487 as prospective 3,804-patient evidence, require oncology-specific knowledge-graph grounding, criterion-level symbolic eligibility checks, documented multi-agent conflict resolution, evidence-linked audit trails, and deployment-defined clinician-review metrics without adding unreported performance values.
53. **Prospective adjudication and throughput checkpoints:** Incorporate the prospective 3,804-patient neuro-symbolic multi-agent trial matching evaluation by scoring eligibility at the criteria level, preserving oncology knowledge-graph provenance, documenting conflict-resolution decisions, capturing throughput metrics, maintaining audit logs, and routing clinician adjudication checkpoints before final recommendations without adding unreported benchmark values.
54. **Prospective KG-backed eligibility reference:** Use PubMed 42004487's prospective 3,804-patient neuro-symbolic multi-agent oncology trial matching evaluation as a reference pattern for knowledge-graph-backed eligibility reasoning, criterion-level evidence, conflict resolution, prospective performance measurement, and clinician-auditable outputs without adding claims absent from the source finding.
55. **Prospective adjudication pattern:** Apply the reported prospective 3,804-patient oncology trial-matching pattern by grounding patient and trial concepts in oncology knowledge graphs, translating eligibility into symbolic criterion logic, routing specialized multi-agent review with criterion-level evidence, resolving conflicts explicitly, and requiring human-in-the-loop final adjudication before actionable recommendations.
56. **Prospective 3,804-patient evaluation details:** Incorporate the June 2026 prospective neuro-symbolic multi-agent oncology trial-matching evaluation by grounding patient and protocol concepts in an oncology-specific knowledge graph, evaluating eligibility at criterion level, documenting agent and rule conflict resolution, flagging coverage gaps in patient facts, criteria, and knowledge-graph mappings, producing clinician audit trails, and capturing operational metrics without inventing unreported benchmark values.
57. **Prospective evaluation matching guidance:** Apply the June 2026 prospective evaluation in 3,804 patients as guidance for neuro-symbolic multi-agent oncology trial matching by grounding candidate trials in an oncology-specific knowledge graph, extracting criterion-level evidence, executing symbolic eligibility checks, documenting conflict resolution among agents, evaluating operation across thousands-patient cohorts, and emitting clinician-auditable match rationales without adding performance claims absent from PubMed 42004487.
58. **Key 3804-patient validation pattern:** Use the prospective evaluation in 3804 patients as the primary validation pattern for assigning neuro-symbolic agent roles, grounding patient and protocol concepts in an oncology-specific knowledge graph, reasoning over eligibility at criterion level, resolving agent-rule-data conflicts, preserving audit trails, running clinician review loops, and reporting prospective performance without adding claims absent from PubMed 42004487.
59. **Prospective trial-matching reference pattern:** Incorporate the 3,804-patient neuro-symbolic multi-agent evaluation as a reference pattern for oncology knowledge-graph retrieval, symbolic criterion reasoning, separated agent roles, documented conflict resolution, evidence-linked outputs, and clinician-auditable matching decisions without adding claims absent from the source finding.
60. **Core 3804-patient evidence update:** Incorporate the June 2026 prospective evaluation in 3804 patients as core evidence for neuro-symbolic, multi-agent oncology trial matching that uses oncology-specific knowledge-graph grounding, criterion-level eligibility reasoning, documented conflict resolution, auditable evidence, workflow metrics, and clinician-in-the-loop review without adding claims absent from PubMed 42004487.
61. **Prospective false-negative and override auditing:** Apply the 3,804-patient prospective evaluation pattern by constructing the oncology-specific knowledge graph with source provenance, executing criterion-level symbolic reasoning, routing agent disagreements through documented multi-agent conflict resolution, capturing prospective workflow metrics, auditing false negatives, recording clinician overrides and their rationales, and producing evidence-linked explanations for each match without inventing unreported performance values.

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
- Source finding: https://pubmed.ncbi.nlm.nih.gov/42004487/
- PubMed 42004487: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Key validation reference: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Source URL: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Source finding URL: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Prospective evaluation source: https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- 2026 prospective 3,804-patient evaluation: https://pubmed.ncbi.nlm.nih.gov/42004487/
- PubMed 42004487 source URL: https://pubmed.ncbi.nlm.nih.gov/42004487/
- PubMed source finding: https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- High-priority 2026 prospective evaluation source: https://pubmed.ncbi.nlm.nih.gov/42004487/
- PubMed 42004487 prospective validation source: https://pubmed.ncbi.nlm.nih.gov/42004487/
- PubMed 42004487: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Prospective 3,804-patient neuro-symbolic multi-agent trial matching evaluation: https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- Prospective 3,804-patient neuro-symbolic multi-agent oncology trial-matching evaluation: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Prospective 3,804-patient design pattern source: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Source finding: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Source URL: https://pubmed.ncbi.nlm.nih.gov/42004487/
- Prospective 3,804-patient neuro-symbolic oncology trial matching source: https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- PubMed 42004487 prospective 3,804-patient trial-matching pattern: https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- Source finding update: https://pubmed.ncbi.nlm.nih.gov/42004487/
- https://pubmed.ncbi.nlm.nih.gov/42004487/
- Prospective 3,804-patient evaluation (PubMed 42004487): https://pubmed.ncbi.nlm.nih.gov/42004487/
