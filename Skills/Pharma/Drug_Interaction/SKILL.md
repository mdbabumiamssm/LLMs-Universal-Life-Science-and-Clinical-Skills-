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
name: 'drug-interaction-checker'
description: 'Checks for potential drug-drug interactions (DDIs) between a list of medications.'
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
  - read_file
  - run_shell_command
---


# Drug-Drug Interaction (DDI) Checker

This skill analyzes a list of medications to identify known interactions, focusing on safety and contraindications.

## When to Use This Skill

*   Reviewing patient medication lists.
*   Prescribing new medications.
*   Pharmacovigilance monitoring.

## Core Capabilities

1.  **Interaction Detection**: Identifies pairs of drugs with known interactions.
2.  **Severity Grading**: Classifies interactions as Minor, Moderate, or Major.
3.  **Clinical Recommendations**: Provides actionable advice (e.g., "Monitor K+ levels").
4.  **Antiseizure Medication DDI Review**: For antiseizure medication DDIs, validate any LLM-generated interaction assessment against trusted references such as Lexicomp and Drugs.com; treat iterative prompting as a source of potential variability rather than proof of correctness, normalize interaction severity labels across references before reporting, and require pharmacist review for clinically relevant findings or discrepancies.
5.  **LLM DDI Evidence Hierarchy and Validation Checklist**: Treat curated DDI references such as Lexicomp or Drugs.com as higher-priority evidence than LLM output; use antiseizure medication DDIs as a stress case by checking each LLM-generated answer against reference entries, documenting prompt iterations and answer changes in an audit log, recording severity-label normalization, and flagging discrepancies before reporting.
6.  **Antiseizure DDI Source Hierarchy**: For antiseizure medication interaction checks, compare LLM output against authoritative DDI references such as Lexicomp and Drugs.com; prompt iteration may refine the query but must not replace database verification, and uncertain or conflicting interactions should be escalated for pharmacist or clinical review.
7.  **Cautionary LLM-DDI Comparison Workflow**: For antiseizure medication DDIs, benchmark LLM outputs against authoritative references such as Lexicomp, track how iterative prompting changes interaction detection or severity, explicitly flag hallucinated or omitted interactions, and require source-backed pharmacist review before clinical use.
8.  **Antiseizure DDI Ground-Truth Verification**: For antiseizure medication DDI evaluation, use Lexicomp or equivalent curated drug-interaction databases as the ground truth for interaction presence and severity; treat iterative prompting as a risk for inconsistent or overconfident answers, explicitly check for hallucinated interactions and severity mismatches, and defer to curated database results whenever LLM output conflicts with, lacks support from, or cannot be reconciled with those references.

## Workflow

1.  **Input**: List of drug names (e.g., "Warfarin, Aspirin").
2.  **Analysis**: Queries internal interaction database.
3.  **Output**: Interaction report with severity and mechanisms.

## Example Usage

**User**: "Check interactions for Warfarin and Aspirin."

**Agent Action**:
```bash
python3 Skills/Pharma/Drug_Interaction/impl.py --drugs "Warfarin, Aspirin"
```

## References

*   https://pubmed.ncbi.nlm.nih.gov/41994367/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
