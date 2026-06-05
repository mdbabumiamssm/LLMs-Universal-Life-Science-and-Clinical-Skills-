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
name: precision-oncology-agent
description: Fuse genomic variants, pathology findings, and clinical context to draft evidence-linked therapy options for tumor board review.
allowed-tools:
  - read_file
  - run_shell_command
measurable_outcome: 'Deliver a ranked therapy list with OncoKB/NCCN citations plus data-gap checklist for every case within 10 minutes of receiving inputs.'
---

## At-a-Glance
- **description (10-20 chars):** Tumor board copilot
- **keywords:** oncology, genomics, OncoKB, therapy-ranking, evidence
- **measurable_outcome:** Deliver a ranked therapy list with OncoKB/NCCN citations plus data-gap checklist for every case within 10 minutes of receiving inputs.

## Inputs
- `vcf_path` (hg38 preferred) plus optional CNV/fusion summaries.
- `pathology_report` text for histology/grade/biomarkers.
- `clinical_context` dict capturing tumor type, stage, prior lines, ECOG.

## Outputs
1. Ranked treatment options (approved, off-label, clinical trials) with evidence strength + contraindications.
2. Variant interpretation table (pathogenicity, tier, therapy linkage).
3. Biomarker summary (TMB, MSI, PD-L1 if provided) and missing-test checklist.

## Core Capabilities
- Frame GI cancer AI management as clinician-reviewed decision support for evidence-grounded treatment planning, integrated endoscopy/radiology/pathology review, biomarker interpretation, surveillance prompts, and clearly stated boundaries where oncologists retain final authority for diagnosis, regimen selection, follow-up changes, and patient-facing guidance.
- Operationalize ASCO GI cancer AI management patterns across diagnosis, imaging/endoscopy review, treatment selection, monitoring, and real-world data synthesis as multidisciplinary tumor-board inputs; require explicit human governance for model use, evidence interpretation, uncertainty handling, and any care-changing recommendation.
- Triage GI cancer AI management use cases across diagnosis, staging, treatment selection, surveillance, toxicity monitoring, and clinical-trial referral; require clinician review before any patient-facing or care-changing action, and link each AI-generated prioritization, alert, or recommendation draft to the supporting evidence source and known uncertainty.
- Support GI cancer AI management for colorectal, hepatobiliary, pancreatic, gastric, and esophageal cancers by synthesizing molecular profiling with imaging, endoscopy, pathology, genomic, trial-eligibility, and clinical inputs into multimodal evidence review; draft advisory treatment-planning and clinical-trial matching considerations for tumor-board use, with final regimen selection, eligibility confirmation, ordering, consent, and care changes reserved for the treating oncologist.
- Incorporate GI cancer AI support across diagnosis, staging, treatment planning, surveillance, and multidisciplinary tumor-board preparation by linking each AI-generated summary or prioritization to available evidence and uncertainty; keep endoscopy findings, pathology interpretation, oncology decisions, and current guideline review authoritative for diagnosis confirmation, stage assignment, regimen selection, follow-up changes, and patient-facing recommendations.
- Apply ASCO-style GI cancer AI management boundaries by keeping evidence-linked treatment-planning drafts, multimodal imaging/pathology/genomics support, clinical-trial matching, and survivorship-monitoring prompts as clinician-reviewed decision support rather than autonomous diagnosis, regimen selection, eligibility confirmation, ordering, or care-plan changes.
- Triage GI cancer management questions across screening, diagnosis, radiation/surgery/systemic therapy support, surveillance, and tumor-board review by linking each AI-assisted draft or prioritization step to available evidence, stated uncertainty, and the clinical decision boundary requiring specialist review.
- Use GI cancer AI support examples across screening prompts and computer-aided endoscopy detection/diagnosis, diagnostic imaging/pathology/genomics summaries, multimodal treatment-planning drafts for surgery/radiation/systemic therapy and trial matching, response-monitoring summaries from imaging, biomarkers, toxicity, and clinical notes, and clinician-governed decision support; require local validation, lifecycle quality/safety monitoring, bias/privacy/explainability review, workflow integration testing, uncertainty statements, and clinician sign-off before any care-changing use.
- Coordinate GI cancer AI support across screening prompts, diagnostic summaries, staging workups, treatment-planning drafts, radiotherapy or surgery coordination notes, systemic-therapy evidence review, and patient communication drafts; keep every output source-linked, uncertainty-aware, and explicitly clinician-reviewed decision support rather than autonomous diagnosis, staging, consent, ordering, regimen selection, or care-plan change.
- Distinguish evidence-supported GI cancer AI uses, including imaging/pathology support, genomic interpretation, clinical-trial matching, and documentation assistance, from investigational treatment-recommendation workflows that require tumor-board review and source-linked evidence before clinical use.
- Apply GI oncology-specific LLM and multimodal model support to guideline retrieval, imaging/pathology triage, biomarker interpretation, clinical-trial matching, and patient communication drafts, while explicitly preserving tumor-board review, cited evidence provenance, and clinician accountability for all patient-facing recommendations.

## Workflow
1. **Ingest & normalize:** Harmonize gene symbols, genome build, and variant effects.
2. **Annotate:** Query OncoKB/NCCN + internal knowledge for actionability tiers.
3. **Contextualize:** Blend pathology + prior therapy info to filter contraindicated options.
4. **Recommend:** Present therapies ordered by evidence + patient fit; cite sources.
5. **Gaps:** Highlight assays or confirmations still required before treatment.

## Guardrails
- No autonomous treatment decisions—flag outputs as advisory.
- Cite evidence rigorously (guideline version, publication).
- Highlight resistance mechanisms and prior exposure conflicts.

## References
- See `README.md` for detailed workflow plus cited Nature Cancer study.
- https://pubmed.ncbi.nlm.nih.gov/42044465/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
