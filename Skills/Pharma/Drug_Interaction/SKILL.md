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
4.  **Antiseizure Medication DDI Review**: For antiseizure medication DDIs, compare any LLM-generated interaction assessment against Lexicomp or an equivalent authoritative reference source; treat iterative prompting as a verification aid rather than a substitute for source-grounded checking, and explicitly screen for false negatives that could miss clinically harmful interactions.

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
