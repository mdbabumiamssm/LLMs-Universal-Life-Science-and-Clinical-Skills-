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
