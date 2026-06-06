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
19. **Antiseizure DDI Patient Summary Benchmarking**: When benchmarking antiseizure medication DDI responses, compare LLM output and Drugs.com results against Lexicomp, keep authoritative-source grounding explicit, treat iterative prompting as a limited sensitivity check, reconcile severity labels before reporting, and state uncertainty clearly in patient-facing summaries when sources conflict, are incomplete, or require pharmacist confirmation.
20. **Comparative LLM-DDI Benchmarking Against Lexicomp and Drugs.com**: For antiseizure medication DDI answers generated by LLMs, benchmark the response against Lexicomp and Drugs.com, cite the evidence source for each interaction conclusion, use iterative prompting only to probe answer stability and limitations, and state that LLMs may explain DDI database findings but must not replace authoritative drug-interaction databases.
21. **2026 Comparative LLM-DDI Benchmark Note**: Validate LLM drug-drug interaction answers against authoritative references such as Lexicomp, especially for antiseizure medications; include iterative prompting only as an evaluation condition for answer stability and limitations, not as a substitute for safety validation.
22. **Antiseizure Medication DDI Benchmark Workflow**: For antiseizure-medication DDI benchmarks, compare LLM outputs with authoritative references such as Lexicomp and Drugs.com, document iterative prompting effects on interaction presence and severity, harmonize severity labels before judging agreement, apply source precedence when references or LLM outputs conflict, and require pharmacist review for clinically relevant, discrepant, unsupported, or omitted findings.
23. **Antiseizure Medication Lexicomp-Comparator Rule**: When benchmarking antiseizure-medication DDIs, compare LLM outputs and Drugs.com results against Lexicomp, use iterative prompting only to test response stability and limitations, normalize contraindication and severity categories before judging agreement, check asserted or omitted interactions for hallucination or unsupported content, and escalate contraindications, clinically relevant interactions, source conflicts, omissions, or prompt-dependent management changes to a pharmacist before clinical use.
24. **Antiseizure Medication Comparative Performance Check**: For antiseizure medication DDI evaluations, benchmark LLM outputs and Drugs.com findings against Lexicomp as the comparator source, document iterative prompting as a limited stability check rather than evidence of correctness, require source-grounded verification for each high-risk DDI call, and escalate high-risk, unsupported, omitted, discrepant, or prompt-dependent conclusions for pharmacist or clinical review.
25. **Antiseizure Medication DDI Benchmarking Protocol**: When benchmarking antiseizure-medication DDIs, compare each LLM output and Drugs.com result with Lexicomp as the stated comparator, record prompt versions without treating iterative prompting as proof of correctness, harmonize severity labels before judging agreement, cite the consulted source for each interaction, severity, and management statement, and allow pharmacist override when sources conflict, citations are missing, or clinical risk is uncertain.
26. **Antiseizure Medication Comparative DDI Evaluation**: For antiseizure medication DDI evaluations, compare LLM outputs with curated references such as Lexicomp and Drugs.com, treat iterative prompting as a limited stability check rather than validation, normalize severity categories before judging agreement, require citations for each interaction, severity, mechanism, and management statement, and route clinically relevant, discrepant, uncited, or uncertain conclusions to pharmacist oversight.
27. **Antiseizure Medication DDI Validation Metrics**: For antiseizure-medication DDI validation, compare LLM outputs with authoritative references such as Lexicomp and Drugs.com, use iterative prompting only as a documented stability and limitation check, report interaction-presence and severity-agreement metrics after harmonizing labels, review missed interactions and unsupported additions, and require pharmacist oversight for clinically relevant, discrepant, or uncertain cases.
28. **2026 Antiseizure Medication DDI Comparator Finding**: Based on the PubMed-indexed 2026 cross-sectional comparison of general LLMs and Drugs.com versus Lexicomp for antiseizure medication DDIs, use Lexicomp or equivalent curated DDI references as the higher-priority comparator, normalize severity labels before judging agreement, document iterative-prompt changes as caveated variability rather than validation, and explicitly warn that general LLMs must not be relied on for final DDI decisions.
29. **Antiseizure Medication DDI Validation Pattern**: Compare each LLM-generated antiseizure medication DDI conclusion against authoritative references such as Lexicomp and Drugs.com, cite the consulted source for interaction presence, severity grade, and management guidance, treat iterative prompting as a limitation and stability check rather than proof of correctness, and require pharmacist review for high-risk combinations, discrepancies, or uncited claims.
30. **LLM DDI Confidence Thresholds and Pharmacist Review**: For LLM-based DDI checking, benchmark answers against trusted references such as Lexicomp and Drugs.com, treat antiseizure medication combinations as edge cases requiring heightened scrutiny, set explicit confidence thresholds before accepting any LLM-assisted conclusion, document iterative-prompt changes as a risk signal, and require pharmacist review before clinical use.
31. **PubMed 41994367 Antiseizure DDI Benchmark Rule**: For antiseizure-medication DDI benchmarking, compare LLM answers and Drugs.com findings against Lexicomp or equivalent curated drug references, use iterative prompting only to identify variability and uncertainty, prioritize curated references when LLM answers conflict with them, state unresolved uncertainty explicitly, and escalate discrepant or clinically relevant conclusions to pharmacist or clinical review before clinical use.
32. **Antiseizure Medication Severity-Agreement Benchmarking**: When benchmarking antiseizure medication DDI outputs, compare LLM responses and Drugs.com-style references against Lexicomp or equivalent curated references, report interaction-presence and severity-label agreement after harmonizing categories, require citations for each interaction, severity, mechanism, and management statement, preserve iterative-prompt changes as variability-risk evidence, and route clinically relevant, discrepant, uncited, or uncertain conclusions through pharmacist review gates.
33. **Antiseizure Medication LLM-DDI Benchmarking Workflow**: For antiseizure medication DDI benchmarking, compare LLM outputs and Drugs.com findings against Lexicomp, run iterative prompt sensitivity analysis, assess severity and management concordance after harmonizing labels, preserve source provenance for every interaction conclusion, and require pharmacist verification before clinical use.
34. **PubMed 41994367 Antiseizure Medication DDI Benchmark Pattern**: For cross-sectional antiseizure-medication DDI comparisons, benchmark LLM outputs and Drugs.com findings against Lexicomp, require citations for each interaction presence, severity, mechanism, and management statement, reconcile severity labels before judging agreement, preserve iterative-prompt changes as safeguards for variability and unsupported shifts, and send clinically relevant, discrepant, uncited, or uncertain conclusions to pharmacist review before use.
35. **Antiseizure Medication DDI Evaluation Source Hierarchy**: When evaluating antiseizure medication DDI outputs, compare LLM conclusions with Lexicomp and Drugs.com while treating Lexicomp or an equivalent curated database as the primary comparator, normalize severity labels before assessing agreement, document iterative-prompt changes as caveated variability rather than validation, and require pharmacist review before any clinical conclusion or patient-facing recommendation.
36. **Antiseizure Medication Benchmark Safeguards**: Use an authoritative compendium such as Lexicomp as the reference for antiseizure medication interaction checks; test prompt sensitivity, assess interaction severity separately from management advice, cite the supporting evidence for each conclusion, and never use reassurance produced only through iterative prompting when authoritative support is absent.

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
