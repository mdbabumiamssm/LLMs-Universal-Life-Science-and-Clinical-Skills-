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
name: radgpt-radiology-reporter
description: Radiology Reporter
keywords:
  - radiology
  - report-generation
  - patient-friendly
  - summarization
  - explanation
measurable_outcome: Generate a patient-friendly explanation of a radiology report with <1% hallucination rate within 30 seconds.
license: MIT
metadata:
  author: MD BABU MIA
  version: "1.0.0"
compatibility:
  - system: Python 3.9+
allowed-tools:
  - run_shell_command
  - read_file
---

# RadGPT (Radiology Report Assistant)

An LLM-based agent designed to summarize and explain complex radiology reports for patients and clinicians.

## When to Use

*   **Patient Communication**: Converting technical findings into plain language.
*   **Clinician Review**: Highlighting critical findings (e.g., "Pneumothorax detected").
*   **Follow-up**: Suggesting appropriate next steps based on findings.

## Core Capabilities

1.  **Simplification**: Translates "bilateral opacity" to "cloudiness in both lungs".
2.  **Entity Extraction**: Identifies key anatomical structures and pathologies.
3.  **Q&A**: Answers follow-up questions about the report.
4.  **MRI Patient Education**: Translates MRI reports into personalized plain language at an audience-appropriate readability target while preserving uncertainty, clearly distinguishing reported findings from diagnoses, and retaining laterality, severity, follow-up recommendations, and red flags; checks factual fidelity and omissions against the source report, compares the explanation with an expert-reviewed interpretation when available, and escalates urgent or ambiguous results to clinicians before delivery.

## Workflow

1.  **Input**: Raw text of the radiology report.
2.  **Process**: LLM summarizes and identifies key findings.
3.  **Output**: Structured summary or conversational explanation.

## Example Usage

**User**: "Explain this chest X-ray report to the patient."

**Agent Action**:
```bash
python -m radgpt.explain --report ./report.txt --target_audience patient
```

## References

- https://pubmed.ncbi.nlm.nih.gov/41865475/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
