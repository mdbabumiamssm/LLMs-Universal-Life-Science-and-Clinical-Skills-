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
name: ai-safety-auditor
description: Validates clinical AI outputs for safety, bias, and hallucination risks before delivery to end-users or clinicians.
keywords:
  - ai-safety
  - compliance
  - bias-detection
  - hallucination-check
  - clinical-validation
measurable_outcome: Identifies 100% of critical safety violations and potential PHI leakage in generated clinical notes.
license: MIT
metadata:
  author: Biomedical AI Team
  version: "1.0.0"
compatibility:
  - system: Python 3.10+
allowed-tools:
  - run_shell_command
  - read_file
---

# AI Safety Auditor

The **AI Safety Auditor** is a critical "human-in-the-loop" simulator and automated guardrail system. It intercepts outputs from other clinical agents to ensure they meet medical safety standards, do not contain Protected Health Information (PHI) where inappropriate, and are free from harmful hallucinations.

## When to Use This Skill

*   As a final check before any clinical agent output is shown to a user.
*   To audit historical logs of agent interactions for compliance.
*   When detecting potential bias in diagnosis or treatment recommendations.
*   To verify that citations in a generated report actually exist (hallucination check).

## Core Capabilities

1.  **PHI Scrubbing Verification**: Ensures no identifiers leaked into non-secure outputs.
2.  **Hallucination Detection**: Cross-references generated claims against trusted knowledge bases.
3.  **Bias Scanning**: Checks for demographic or socioeconomic bias in clinical reasoning.
4.  **Contraindication Check**: Verifies treatment recommendations against patient allergies/conditions.
5.  **On-Premises Open-Source Clinical LLM Deployment Risk Review**: Evaluates distilled reasoning models proposed for local clinical diagnosis by requiring diagnostic performance validation, local infrastructure constraint review, privacy-control verification, and mandatory clinician oversight before clinical use.
6.  **On-Premises Reasoning Model Deployment Audit**: Evaluates distilled open-source reasoning models proposed for clinical diagnosis by checking model provenance, calibration drift risk, local privacy controls, benchmark representativeness, and required human oversight before clinical use.
7.  **Clinical Practice Guideline LLM Assistance Audit**: Evaluates LLM-supported guideline development for evidence traceability, conflict-of-interest awareness, consensus workflow support, versioned citations, and red-team checks for omitted harms or overconfident recommendations.
8.  **Real-Time Guideline Development Evaluation Workflow**: Audits LLM assistance during clinical practice guideline development with real-time evidence checking, conflict-of-interest and citation verification, consensus-panel handoff, and documented human oversight gates before recommendations enter practice guidance.
9.  **Guarded Test-Time Knowledge Acquisition Audit**: Checks medical decision support outputs for retrieve-before-answer evidence acquisition when current clinical knowledge is needed, verifies source authority and freshness before use, records acquired evidence and provenance in audit logs, handles contradictions with explicit uncertainty or escalation, compares pre/post retrieval decisions, and refuses or escalates when retrieved evidence is insufficient.
10. **LLM-Assisted Guideline Drafting Evaluation**: Checks clinical practice guideline drafts for evidence traceability, conflict handling, recommendation grading, human panel review, and real-time discrepancy logging during guideline development.
11. **Fine-Grained Medical Q&A Dataset Evaluation**: Audits domain-specific medical Q&A evaluation sets with domain stratification, omission and harm taxonomies, calibration checks, uncertainty labeling, and trustworthy-answer scoring beyond simple accuracy.
12. **Clinical Guideline Contribution Review**: Evaluates LLM contributions to clinical practice guideline development by requiring recommendation-level evidence traceability, real-time expert reviewer workflows, omission and harm checks, explicit source grading, consensus handling for disagreements, and mandatory human expert oversight before adoption.
13. **Real-Time Guideline Recommendation Evaluation**: Reviews LLM-supported guideline development for real-time evidence traceability, conflict-of-interest review, recommendation grading checks, citation audit, and panel-level human signoff before recommendations are finalized.
14. **Domain-Specific Medical QA Stratified Error Analysis**: Classifies answer correctness, omissions, unsafe reasoning, evidence support, and dataset leakage in medical QA datasets, requiring stratified error analysis before trusting medical LLM answers.
15. **Clinical Practice Guideline Development Audit Pattern**: Limits LLM use to draft synthesis and checking, tracks source provenance, compares draft recommendations against guideline-panel decisions, and flags unverifiable evidence, omitted harms, conflicts, and strength-of-recommendation mismatches.
16. **Fine-Grained Trustworthy Medical QA Dataset Audit**: Evaluates domain-specific Q&A datasets with item-level error labels, omission and risk-of-harm scoring, dataset provenance checks, specialty stratification, and regression benchmarks for trustworthy medical language model evaluation.
17. **Medical Decision Support Test-Time Knowledge Acquisition Check**: Requires retrieval provenance for acquired clinical facts, separates retrieved facts from model priors, evaluates answer changes after retrieval, and flags unsupported or outdated clinical claims.
18. **On-Premises Open-Source Clinical LLM Deployment Checklist**: Requires local diagnostic benchmark design, calibration and harm review, PHI containment, model provenance documentation, regression gates, and clinician override requirements before production use.
19. **LLM-Assisted Clinical Practice Guideline Acceptance Checklist**: Evaluates guideline-development use of LLMs by checking evidence synthesis traceability, recommendation drafting provenance, conflict detection, audit trails, and documented human panel sign-off before guideline text is accepted.
20. **Diagnosis-Focused On-Premises Open-Source LLM Deployment Checklist**: Compares distilled reasoning models against closed baselines before diagnosis use, requires local specialty validation, documents governance and latency tradeoffs, and classifies autonomous diagnostic use as high-risk with mandatory clinician oversight.
21. **Clinical Guideline-Development LLM Evaluation Mode**: Requires source traceability, conflict-of-interest awareness, recommendation grading checks, omission review, and human panel adjudication before any LLM-assisted guideline language is accepted.
22. **Fine-Grained Domain-Specific Medical Q&A Benchmark Review**: Evaluates trustworthy medical language model benchmarks with item-level correctness checks, omission labeling, harm-potential assessment, domain stratification, rubric reliability review, and dataset documentation before using Q&A results as evidence of model safety.
23. **Test-Time Knowledge Acquisition Clinical Safety Pattern**: Requires retrieval of current vetted references before medical reasoning, logs source provenance, compares pre/post-retrieval answer changes, and escalates uncertainty when retrieved evidence conflicts.

## Workflow

1.  **Intercept**: Receive candidate response from a Clinical Agent.
2.  **Scan**: Run parallel safety checks (PHI, Bias, Factuality).
3.  **Verdict**: Pass, Flag for Review, or Reject.
4.  **Feedback**: Provide specific reasons for rejection to the generating agent.

## Example Usage

**User**: "Audit this generated discharge summary for safety."

**Agent Action**:
```bash
python3 Skills/Clinical/Safety/AI_Safety_Auditor/audit_output.py --input discharge_summary.txt --checks "all"
```

## References

- https://pubmed.ncbi.nlm.nih.gov/42062641/
- https://pubmed.ncbi.nlm.nih.gov/42042855/
- https://pubmed.ncbi.nlm.nih.gov/41953846/
- https://pubmed.ncbi.nlm.nih.gov/42039929/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
