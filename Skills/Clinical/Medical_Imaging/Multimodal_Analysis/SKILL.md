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
name: 'multimodal-medical-imaging'
description: 'Analyzes medical images (X-ray, MRI, CT) using multimodal LLMs to identify anomalies and generate reports.'
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
  - read_file
  - run_shell_command
---


# Multimodal Medical Imaging Analysis

The **Multimodal Medical Imaging Analysis Skill** leverages state-of-the-art Vision-Language Models (VLMs) like Gemini 1.5 Pro and GPT-4o to interpret medical imagery alongside clinical text.

## When to Use This Skill

*   When you need a preliminary screening of medical images.
*   When correlating visual findings with textual clinical notes.
*   To generate structured reports (DICOM-SR-like) from raw images.

## Core Capabilities

1.  **Anomaly Detection**: Identify potential pathologies in X-rays, CTs, etc.
2.  **Report Generation**: Draft radiology reports in standard formats.
3.  **VQA (Visual Question Answering)**: Answer specific questions about an image (e.g., "Is there a fracture in the left femur?").
4.  **Dermatology/Dermoscopy BCC Evaluation**: For suspected basal cell carcinoma and common mimickers, standardize clinical and dermoscopic image acquisition (focus, lighting and color, lesion framing, scale, and dermoscopic artifact control), keep paired images linked at the lesion level, and apply image-quality gates before analysis. Evaluate image-only and image-plus-clinical-context conditions separately with matched prompts, and return ranked common-mimicker differentials with explicit scores and calibrated confidence rather than a single label. Report sensitivity and specificity when ground-truth labels support them, stratify results by image quality and condition, and perform lesion-level error analysis by diagnosis, modality, and clinically relevant context without unsupported performance claims. Use a structured abstention when image quality is inadequate, required context is missing, or confidence is below a predefined threshold; report uncertainty, quality limitations, and model disagreements explicitly. Require dermatologist review for every suspected malignancy and before any clinical decision, patient-facing guidance, or benchmark interpretation.

## Workflow

1.  **Input**: Provide an image file path (JPG, PNG) and a specific clinical question or "generate report" instruction.
2.  **Analyze**: The agent sends the image and prompt to the VLM.
3.  **Output**: Returns a JSON object with findings, confidence scores, and reasoning.

## Example Usage

**User**: "Analyze this chest X-ray for pneumonia."

**Agent Action**:
```bash
python3 Skills/Clinical/Medical_Imaging/Multimodal_Analysis/multimodal_agent.py \
    --image "/path/to/cxr.jpg" \
    --prompt "Check for signs of pneumonia and consolidation."
```


## References

*   https://pubmed.ncbi.nlm.nih.gov/41952838/

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
