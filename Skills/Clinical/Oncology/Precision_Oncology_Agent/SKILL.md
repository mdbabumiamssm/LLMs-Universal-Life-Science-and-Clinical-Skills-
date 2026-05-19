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
- Support GI cancer AI management for colorectal, hepatobiliary, pancreatic, gastric, and esophageal cancers by synthesizing molecular profiling with imaging, endoscopy, pathology, genomic, trial-eligibility, and clinical inputs into multimodal evidence review; draft advisory treatment-planning and clinical-trial matching considerations for tumor-board use, with final regimen selection, eligibility confirmation, ordering, consent, and care changes reserved for the treating oncologist.
- Triage GI cancer management questions across screening, diagnosis, radiation/surgery/systemic therapy support, surveillance, and tumor-board review by linking each AI-assisted draft or prioritization step to available evidence, stated uncertainty, and the clinical decision boundary requiring specialist review.
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
