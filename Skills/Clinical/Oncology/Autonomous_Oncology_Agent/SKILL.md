---
name: autonomous-oncology-agent
description: "Multimodal precision oncology agent that combines vision transformer analysis of H&E pathology slides with LLM-based clinical reasoning to predict biomarker status (MSI, KRAS, BRAF) and generate NCCN/ASCO-aligned treatment recommendations."
compatibility: "Python 3.9+"
allowed-tools: "run_shell_command, web_fetch"
metadata:
  author: Nature Cancer 2025
  version: "1.0.0"
  keywords: "oncology, multimodal, H&E, biomarkers, NCCN"
  measurable_outcome: "Generate a prioritized treatment plan with evidence levels and predicted biomarker status (MSI/KRAS) within 5 minutes of data ingest."
  license: MIT
---

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

# Autonomous Clinical AI Agent (Oncology)

Implements the "Autonomous Clinical AI Agent" architecture from Nature Cancer (2025), combining LLM reasoning with specialized vision models for pathology image analysis to support precision oncology decision-making.

Use when interpreting complex cancer cases that involve pathology slides, genomic panels, and clinical history — especially when biomarker prediction or guideline-aligned treatment planning is needed.

## When to Use This Skill

- **Precision oncology case review** — interpreting cancer cases involving pathology, genomics, and clinical history.
- **Biomarker detection from H&E** — predicting MSI, KRAS, or BRAF status directly from histology slides.
- **Guideline adherence checks** — validating treatment plans against NCCN or ASCO guidelines via OncoKB/PubMed.
- **Multimodal synthesis** — combining pathology image data with text-based clinical reports.

## Workflow

1. **Ingest inputs** — accept clinical notes, pathology reports, genomic panels, and H&E histology slides.
2. **Run vision analysis** — vision transformer predicts molecular features (MSI, KRAS, BRAF) from slides.
3. **Extract clinical entities** — LLM parses stage, histology, and mutation data from text inputs.
4. **Retrieve evidence** — query OncoKB for actionable mutations and match against standard-of-care guidelines.
5. **Generate report** — produce a "Tumor Board" style report with ranked treatment options and evidence levels.

## Example

**Prompt**: "Review this case of metastatic colorectal cancer. The H&E slide is attached. What is the predicted MSI status and recommended first-line therapy?"

**Agent steps**:
1. Runs vision model on H&E image → "MSI-High (Predicted)".
2. Reads clinical notes → "Patient is fit, ECOG 0."
3. Consults OncoKB → "MSI-High CRC responds to Pembrolizumab."
4. Recommends: "Based on predicted MSI-High status, immunotherapy (Pembrolizumab) is recommended over standard chemotherapy."

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->