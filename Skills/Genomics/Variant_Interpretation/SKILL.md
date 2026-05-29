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
name: 'variant-interpretation-acmg'
description: 'Classifies genetic variants according to ACMG (American College of Medical Genetics) guidelines.'
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
  - read_file
  - run_shell_command
---


# Variant Interpretation (ACMG)

The **Variant Interpretation Skill** automates the classification of genetic variants (Pathogenic, Benign, VUS) using a rules-based engine derived from ACMG guidelines.

## When to Use This Skill

*   When analyzing a VCF file for clinical reporting.
*   To determine the clinical significance of a specific mutation (e.g., BRCA1 c.123A>G).
*   To aggregate evidence (population freq, computational predictions) into a final verdict.

## Core Capabilities

1.  **Rule Scoring**: Applies codes like PVS1 (Null variant), PM2 (Rare), PP3 (In silico).
2.  **Classification**: Combines scores to reach a verdict (Pathogenic, Likely Pathogenic, VUS, etc.).
3.  **Explanation**: Provides the logic/evidence used for the classification.
4.  **Precision-Grounded Summarization**: Retrieves variant evidence from ClinVar, gnomAD, ACMG-linked sources, or equivalent evidence-based databases; cites database evidence; separates evidence from interpretation; reports source freshness and review status when available; tracks uncertainty and conflicting evidence; and rejects unsupported pathogenicity claims.
5.  **Evidence Database Augmentation**: Uses Precision Grounding-style database augmentation for variant summaries by grounding claims in ClinVar, gnomAD, OMIM-style, or equivalent evidence sources; preserving provenance links; checking for stale evidence; and adding ACMG-aware uncertainty statements when evidence is limited, conflicting, or outdated.
6.  **Evidence-Grounded Variant Summaries**: Retrieves supporting data from trusted databases and literature; separates asserted classifications from model-generated synthesis; cites evidence levels where available; flags conflicts across ClinVar, gnomAD, and literature; and requires ACMG-style traceability from each summary statement back to its evidence source.
7.  **Identifier-Normalized Evidence Summaries**: Normalizes variant, gene, and transcript identifiers before evidence lookup; retrieves evidence from trusted databases; cites database provenance; reconciles conflicting assertions; keeps evidence separate from interpretation; and flags unresolved gaps before clinical use.
8.  **Precision-Grounded Variant Summarization**: Before generating a variant summary, retrieves evidence from ClinVar, gnomAD, ACMG/AMP criteria, disease databases, and literature; includes explicit citations for each evidence source; and identifies, reports, and reconciles conflicting evidence without inventing unsupported claims.
9.  **Precision-Grounded Cross-Checks**: Retrieves authoritative variant database evidence before generation; preserves citations and provenance; separates known pathogenicity assertions from model inference; and requires ClinVar, gnomAD, COSMIC-style, or equivalent cross-checks before presenting a variant summary.
10. **Evidence-Grounded LLM Variant Summarization**: For LLM-generated variant summaries, first retrieve ClinVar, gnomAD, OMIM, and literature evidence; cite database or publication provenance; keep pathogenicity claims distinct from uncertainty, conflicts, and evidence gaps; and validate the summary against ACMG-style criteria before clinical use.
11. **Citation-Backed Trustworthy Reports**: For precision-grounded genetic variant summaries, anchor each assertion to evidence-based databases or cited literature; cross-check ClinVar classifications against ACMG/AMP criteria before reporting; explicitly surface conflicts, missing evidence, database review status when available, and uncertainty instead of presenting unsupported or unresolved claims as definitive.
12. **Clinically Separated Precision Grounding**: For genetic variant summarization, require evidence-backed retrieval from ClinVar, gnomAD, and ACMG/AMP sources; preserve provenance for each summary claim; flag conflicting evidence; and keep automated summaries separate from final clinical interpretation.
13. **Precision-Grounded Pathogenicity Review**: Ground variant summaries in ClinVar, gnomAD, COSMIC, or equivalent evidence databases; cite provenance for pathogenicity statements; explicitly handle conflicting or missing evidence; check for unsupported disease, frequency, or classification claims before output; and require an ACMG-aligned final review.
14. **Precision-Grounded Evidence Mapping**: For variant summarization, retrieve evidence from ClinVar, gnomAD, dbSNP, COSMIC, ACMG/AMP criteria, and literature; require every factual claim to link back to its source; keep pathogenicity classification separate from the explanatory summary; and flag conflicting findings or low-review-status evidence before reporting.
15. **Precision Grounding for LLM Summaries**: For genetic variant summarization, retrieve ClinVar, gnomAD, ACMG/AMP, disease, and literature evidence before synthesis; present retrieved evidence facts separately from LLM-generated synthesis; and cite sources for uncertainty statements, evidence gaps, and conflict handling.
16. **Source-Linked Variant Summarization**: For precision-grounded summaries, require retrieval from ClinVar, gnomAD, ACMG/AMP evidence codes, disease databases, and literature; link each summary claim to its source; report evidence strength, conflicts, database review status, and explicit uncertainty; and avoid free-form LLM interpretation unsupported by retrieved evidence.
17. **Auditable Precision Grounding**: Constrain LLM-generated genetic variant summaries to evidence-based databases; cite ClinVar, gnomAD, COSMIC, or equivalent sources for variant claims; separate pathogenicity evidence from interpretation; and audit outputs for hallucinated disease, frequency, or classification claims.
18. **Pre-Interpretation Precision Grounding**: Before ACMG-style interpretation, require evidence-backed database retrieval, citation-linked variant summaries, ClinVar or relevant domain database cross-checks, and hallucination controls that block unsupported variant, disease, frequency, or classification claims.
19. **Precision-Grounded Source Separation**: For variant summarization, retrieve evidence from ClinVar, gnomAD, dbSNP, disease databases, and literature before synthesis; present retrieved source facts separately from model-generated synthesis; and flag any pathogenicity claim unsupported by retrieved evidence.
20. **Precision Grounding-Style Variant Summarization**: Ground every genetic variant summary in evidence databases such as ClinVar, gnomAD, OMIM, HGMD/COSMIC where licensed, and ACMG criteria; emit provenance, evidence strength, uncertainty, and warnings for unsupported claims.
21. **Evidence-Grounded LLM Summary Checks**: For LLM-generated variant summaries, ground claims in trusted databases such as ClinVar, gnomAD, dbSNP, COSMIC, and ACMG evidence categories; link each summary statement to cited provenance; and check for hallucinated or unsupported variant, disease, frequency, or classification claims before output.
22. **Clinician-Facing Precision Grounding**: For concise clinician-facing genetic variant summaries, retrieve ClinVar, gnomAD, OMIM, and relevant literature evidence before synthesis; preserve database provenance for each claim; map findings to ACMG-compatible evidence tags where applicable; explicitly resolve or surface conflicting classifications, frequencies, disease links, and evidence gaps; and run hallucination checks for unsupported variant, disease, frequency, inheritance, or pathogenicity statements.
23. **Precision-Grounded Genetic Variant Summarization**: Retrieve evidence from ClinVar, gnomAD, dbSNP, and disease resources before synthesis; present retrieved evidence separately from generated summary text; and expose citations, confidence, conflicts, and ACMG-relevant fields for review.
24. **Evidence-Grounded Genetic Variant Summarization**: Retrieve ClinVar, gnomAD, ACMG/AMP, literature, and disease database evidence before summarization; separate asserted source facts from model synthesis; cite every claim; flag conflicts and database review status; and block unsupported pathogenicity conclusions.
25. **Audit-Ready Precision-Grounded Summaries**: For trustworthy genetic variant summaries, retrieve evidence-based database records before synthesis; preserve ClinVar, gnomAD, COSMIC-style, or equivalent provenance; map retrieved facts to ACMG evidence categories where applicable; use explicit uncertainty wording for limited, conflicting, or missing evidence; and maintain citation trails for audit review.
26. **Evidence-Grounded Genetic Variant Summarization**: Ground variant summaries in trusted sources such as ClinVar, gnomAD, OMIM, dbSNP, and cited literature; cite each source used; handle conflicting classifications, frequencies, disease links, and evidence gaps explicitly; use ACMG-compatible language; and label conclusions with clear uncertainty terms such as supported, limited, conflicting, or insufficient evidence.

## Workflow

1.  **Input**: Variant details (Gene, HGVS, Consequence) or Evidence codes directly.
2.  **Process**: Sums weights of applied ACMG criteria.
3.  **Output**: Final classification and score breakdown.

## Example Usage

**User**: "Classify a variant with evidence PVS1 and PM2."

**Agent Action**:
```bash
python3 Skills/Genomics/Variant_Interpretation/acmg_classifier.py \
    --evidence "PVS1,PM2"
```

## References

*   https://pubmed.ncbi.nlm.nih.gov/41950627/



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
