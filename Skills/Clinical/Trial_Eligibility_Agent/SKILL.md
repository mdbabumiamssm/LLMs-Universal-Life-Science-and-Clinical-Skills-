<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

---
name: trial-eligibility-agent
description: Parse trial protocols and patient data to produce criterion-level MET/NOT/UNKNOWN determinations with evidence and gaps for clinical trial screening tasks.
allowed-tools:
  - read_file
  - run_shell_command
measurable_outcome: 'Produce a MET/NOT/UNKNOWN matrix with supporting citations for ≥90% of inclusion/exclusion criteria within 5 minutes per trial request.'
---

## At-a-Glance
- **description (10-20 chars):** Trial triage hub
- **keywords:** eligibility, ClinicalTrials, FHIR, evidence, gaps
- **measurable_outcome:** Produce a MET/NOT/UNKNOWN matrix with supporting citations for ≥90% of inclusion/exclusion criteria within 5 minutes per trial request.

## Inputs
- `trial_id` (NCT or sponsor ID) plus protocol text if not public.
- `patient_summary` narrative and optional `patient_structured` FHIR bundle.
- Declare data sources used (notes, labs, imaging, meds) to show provenance.

## Outputs
1. Structured table (JSON recommended) listing each criterion id/text with status, evidence snippet, and confidence.
2. Overall recommendation (`potentially_eligible`, `not_eligible`, `needs_more_information`).
3. Data gap checklist covering missing labs/imaging/biomarkers.

## Core Capabilities
- Support neuro-symbolic multi-agent oncology trial matching by combining an oncology-specific knowledge graph with agentic criterion parsing, prospective patient-level evaluation, confidence scoring, and human review for inclusion/exclusion decisions.
- For oncology trial matching, encode each eligibility criterion as symbolic rules grounded in oncology-specific knowledge graph concepts, keep evidence-extraction agents separate from eligibility-reasoning agents, report prospective evaluation metrics without inventing benchmark thresholds, and route borderline eligibility calls to human review.
- For neuro-symbolic multi-agent oncology workflows, perform criterion-level extraction, ground oncology terms and biomarkers in the knowledge graph, separate retrieval/extraction/reasoning agent roles, track patient-level audit trails for evidence and decisions, report prospective evaluation metrics from the run, and require human review for eligibility conflicts or uncertain criteria.
- For treatment-trial matching in oncology, use neuro-symbolic multi-agent reasoning over an oncology knowledge graph to connect treatment context, biomarkers, and criterion-level evidence; include confidence scoring, audit trails, prospective evaluation metrics, and clinician review before any matching recommendation is acted on.

## Workflow
1. **Acquire protocol:** Pull eligibility text from ClinicalTrials.gov or sponsor PDF.
2. **Normalize criteria:** Break into atomic checks with AND/OR logic and thresholds.
3. **Extract patient facts:** Map narrative + FHIR data into canonical features (age, labs, ECOG, biomarkers).
4. **Evaluate:** Assign MET/NOT/UNKNOWN with cited evidence for each criterion, flag missing context explicitly.
5. **Summarize:** Present recommendation and highlight gating unknowns plus next-best actions.

## Guardrails
- Never claim enrollment decisions; mark outputs as advisory.
- Cite direct patient evidence for every MET/NOT call; default to UNKNOWN rather than guessing.
- Respect PHI handling expectations—avoid storing raw notes outside secure paths.

## Tooling & References
- Use `README.md` for API snippets (FHIR parsing, JSON schema) and dependency versions.
- Pair with `Clinical/Trial_Matching/TrialGPT` when retrieval/ranking is also needed.

## References
- https://pubmed.ncbi.nlm.nih.gov/42004487/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
