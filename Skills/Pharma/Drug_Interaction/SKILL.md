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
9.  **LLM DDI Benchmarking Controls**: When benchmarking LLM drug-drug interaction answers against authoritative references such as Lexicomp, normalize medication names before comparison, report severity and evidence labels, run iterative-prompt sensitivity checks, and require pharmacist review for antiseizure medications and other high-risk medication classes.
10. **Antiseizure Medication Chatbot Benchmarking**: For antiseizure-medication DDI benchmarking, compare LLM or chatbot answers against curated drug references such as Lexicomp, track how iterative prompting affects outputs, and flag high-risk hallucination or omission modes before using chatbot answers in medication review.
11. **Antiseizure Medication LLM-DDI Caution**: For antiseizure medication DDI checks, compare LLM outputs and Drugs.com entries against Lexicomp or another curated DDI database, document any changes from iterative prompting, flag hallucinated or unsupported interactions, preserve curated database source hierarchy, and state that LLMs must not replace curated DDI databases for clinical decision-making.
12. **Antiseizure Medication LLM Evaluation Guardrails**: When evaluating LLM answers for antiseizure medication DDIs, compare each answer with Lexicomp or an equivalent curated reference, require citations to the reference used for interaction presence, severity, mechanism, and management guidance, normalize severity categories before reporting, treat iterative prompting as sensitivity testing rather than validation, and trigger pharmacist review for clinically relevant interactions, unsupported or omitted interactions, LLM-reference discrepancies, or prompt-dependent severity or management changes.
13. **Antiseizure Medication Reference Benchmarking**: For antiseizure medication DDI checks, benchmark LLM output and consumer drug-reference results such as Drugs.com against authoritative references such as Lexicomp, explicitly assess interaction-presence and severity agreement, audit missing interactions as well as unsupported additions, document output changes from iterative prompting, and require pharmacist review for clinically relevant discrepancies or omissions.
14. **Antiseizure Medication Contraindication Benchmarking**: When benchmarking antiseizure-medication DDI outputs, compare LLM answers and Drugs.com results against Lexicomp, normalize severity labels before deciding agreement, explicitly check for missed or unsupported contraindications, treat iterative prompting as a variability check rather than validation, and trigger pharmacist review for contraindications, omitted interactions, unsupported additions, reference disagreements, or prompt-dependent severity or management changes.
15. **Antiseizure Medication DDI Benchmark Audit**: For antiseizure-medication DDI benchmarking against Lexicomp and Drugs.com, report interaction severity with source ranking, preserve iterative prompting audit trails, explicitly handle contraindications and escalation triggers, and warn that LLM outputs must not replace validated drug-interaction databases.
16. **Antiseizure Medication Comparative Benchmarking**: When comparing LLM outputs and Drugs.com against Lexicomp for antiseizure medication DDIs, evaluate interaction presence and severity classification against the curated source, treat iterative prompting results as caveated sensitivity checks, and require source-grounded verification before using findings in clinical recommendations.
17. **LLM-Based DDI Benchmark Caution**: Use antiseizure medication interactions as an example when checking LLM-based DDI outputs; require source grounding against authoritative references such as Lexicomp, approved prescribing labeling, or equivalent curated databases, verify iterative-prompt reproducibility, report severity classification explicitly, and require pharmacist review for clinically relevant or discrepant findings.
18. **Published LLM-DDI Benchmarking Guidance**: For LLM-based drug-drug interaction assessment, benchmark LLM responses and consumer drug-reference outputs such as Drugs.com against authoritative references such as Lexicomp; use antiseizure medication DDIs as representative examples, treat iterative prompting as a variability check rather than independent validation, and require source-backed pharmacist review before clinical conclusions.

## Benchmark Caution: LLM-Based DDI Checks

For LLM-assisted DDI checks, use antiseizure medication interactions as a benchmark caution example. Do not accept an LLM or consumer-facing checker output without source grounding against authoritative references such as Lexicomp, approved prescribing labeling, or equivalent curated DDI databases. Preserve iterative prompt attempts for reproducibility review, compare whether interaction presence or severity classification changes across prompts, and route clinically relevant interactions, unsupported findings, omissions, or discrepant severity labels to pharmacist review.

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
