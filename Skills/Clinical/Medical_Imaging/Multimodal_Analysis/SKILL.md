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
4.  **Dermatology/Dermoscopy BCC Benchmarking**: For clinical or dermoscopic images involving suspected basal cell carcinoma and common mimickers, frame outputs as educational triage or differential considerations only, not a diagnosis. Use modality-specific prompts that distinguish clinical close-up photography from dermoscopy, require image-quality checks before interpretation (focus, lighting, lesion framing, scale/context, and dermoscopic artifact visibility), explicitly list the mimic classes supplied in the clinical prompt or dataset, ask for a differential diagnosis rather than a single label, report uncertainty and image-quality limitations explicitly, and require dermatologist confirmation before any clinical decision or patient-facing guidance. Escalate uncertain, discordant, high-risk, or management-changing cases for dermatopathology correlation or biopsy-directed review through appropriate clinical channels. When comparing multimodal LLMs such as ChatGPT, Gemini, and Claude for this task, use the same images, clinical context, prompts, and review rubric across models, compare outputs against expert labels or dermatologist reference annotations, and keep educational triage benchmarking separate from diagnostic claims; the finding does not establish standalone diagnostic use.

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
