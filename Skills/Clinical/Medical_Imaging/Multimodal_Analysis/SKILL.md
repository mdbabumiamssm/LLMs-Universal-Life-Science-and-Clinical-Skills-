---
name: 'multimodal-medical-imaging'
description: 'Analyzes medical images (X-ray, MRI, CT) using multimodal LLMs to identify anomalies and generate reports.'
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
  - read_file
  - run_shell_command
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
4.  **Dermatology/Dermoscopy BCC Evaluation**: For suspected basal cell carcinoma and common mimickers, standardize clinical and dermoscopic image acquisition (focus, lighting and color, lesion framing, scale, and dermoscopic artifact control), keep paired images and supporting visual evidence linked at the lesion level, and apply image-quality gates before analysis. Evaluate image-only and image-plus-clinical-context conditions separately with matched prompts, and return ranked common-mimicker differentials with explicit scores and calibrated confidence rather than a single label. Report sensitivity and specificity when ground-truth labels support them, stratify results by image quality and condition, and perform lesion-level error analysis by diagnosis, modality, and clinically relevant context without unsupported performance claims. Use a structured abstention when image quality is inadequate, required context is missing, or confidence is below a predefined threshold; report uncertainty, quality limitations, and model disagreements explicitly. Require dermatologist review for every suspected malignancy and before any clinical decision, patient-facing guidance, or benchmark interpretation.
5.  **Dermatology Evaluation Integrity**: Evaluate basal cell carcinoma against common mimickers using matched image-only and image-plus-context comparisons, ranked differential diagnoses, and confidence calibration. Check for lesion overlap across evaluation splits and metadata leakage, and require dermatologist adjudication of clinically consequential errors.
6.  **Paired Clinical–Dermoscopic BCC Mimicker Evaluation**: Test basal cell carcinoma and common mimickers at the lesion level using clinical-image-only, dermoscopic-image-only, and paired clinical-plus-dermoscopic inputs. Apply the same predefined image-quality controls across conditions; report lesion-level sensitivity and specificity when ground-truth labels permit; compare models using identical lesions, prompts, clinical context, and output criteria; and require dermatologist review of predictions, model disagreements, errors, and any clinical interpretation.
7.  **Cross-Model BCC Safety Review**: Stratify clinical and dermoscopic evaluations by predefined image-quality categories, produce a lesion-level differential diagnosis for basal cell carcinoma and common mimickers, and abstain when image quality or diagnostic confidence is inadequate. Compare models on the same lesions and input conditions, and require expert dermatologist review of clinically dangerous false negatives before results inform clinical use.
8.  **Dermoscopic BCC Comparative Evaluation**: Gate basal cell carcinoma and common-mimicker dermoscopic images for focus, illumination and color, framing, scale, and artifacts before scoring a ranked differential diagnosis. Compare multimodal models on identical lesion-level inputs and criteria; define abstention for failed quality gates, missing required context, low confidence, or material model disagreement; analyze errors per lesion by diagnosis and input modality; and require dermatologist review of predictions, abstentions, disagreements, and clinically consequential errors.
9.  **Paired Clinical–Dermoscopic Skin-Lesion Evaluation**: Evaluate paired clinical and dermoscopic images for skin lesions, including basal cell carcinoma and its common mimickers. Reject images that fail predefined quality criteria, run matched modality ablations using clinical-only, dermoscopic-only, and paired inputs, report sensitivity and specificity when ground-truth labels permit, calibrate diagnostic confidence, and require dermatologist review of predictions, abstentions, disagreements, errors, and clinical interpretations.
10. **Clinical–Dermoscopy BCC Evaluation Pattern**: For basal cell carcinoma and common mimickers, apply predefined image-quality checks and matched modality ablations using clinical-image-only, dermoscopic-image-only, and paired inputs; return a predefined top-k differential diagnosis with explicit uncertainty; and abstain when image quality, required context, or confidence is inadequate. Prevent lesion-level leakage by keeping all images and metadata for each lesion in one evaluation split and auditing duplicate or near-duplicate inputs. Require dermatologist adjudication of predictions, errors, disagreements, and abstentions before any clinical use.
11. **Closed-System Radiography Response Evaluation**: Evaluate closed-system LLM radiography responses by separating image-interpretation accuracy from generated-explanation quality, and score factuality, omissions, unsupported recommendations, uncertainty, and potential patient harm.
12. **Closed-System X-ray Education QA Review**: For X-ray or radiography education questions, use fixed prompts such as "Answer this radiography education question using only the provided closed-system case, image description, and teaching materials; state when the supplied material does not support an answer" and "Evaluate this generated response against the reference answer and closed-system materials; score correctness and clinically important omissions separately using the predefined rubric, then flag unsupported claims, missing uncertainty, and clinician-review needs." Keep evaluation inside the closed environment without outside lookup during scoring, document the prompt and permitted materials, and include escalation language such as "This output is educational and requires review by a qualified clinician or radiography educator before clinical use" when responses are uncertain, incomplete, or clinically consequential.
13. **Closed-System LLM Radiography Response Assessment**: Assess closed-system LLM radiography responses for accurate radiographic terminology, quality of patient-facing explanations, missing safety caveats, and clear deferral rules requiring licensed radiology review before any clinical interpretation, diagnosis, or patient guidance.
14. **BCC and Mimicker Benchmarking**: Benchmark basal cell carcinoma and common mimickers with paired clinical-image and dermoscopic-image evaluation, scored differential diagnoses, lesion-level dataset splits, confidence calibration, and dermatologist adjudication of predictions and errors.
15. **Clinical-History Dermoscopy BCC Prompt Comparison**: For basal cell carcinoma and common mimickers, compare clinical-only image prompts against image-plus-history prompts using identical lesions and output criteria. Track each mimicker class separately, require dermatologist review of predictions and clinically consequential errors, and report dermoscopy and skin-lesion failure modes separately from general radiology use cases.
16. **LLM-Assisted BCC Skin Cancer Assessment**: For clinical and dermoscopic image analysis of suspected basal cell carcinoma and common mimickers, frame outputs as lesion-level differentials rather than stand-alone diagnoses; apply image-quality gates before interpretation; keep clinical-only, dermoscopic-only, and paired multimodal inputs explicit; report uncertainty, missing context, model limitations, and potential false-negative or false-positive harms; and require dermatologist review before any clinical decision, patient guidance, or safety conclusion.
17. **BCC Mimicker Dermoscopy Prompt Guardrails**: When using multimodal models such as ChatGPT, Gemini, or Claude for clinical or dermoscopic images of suspected basal cell carcinoma and common mimickers, use matched prompt templates that state the input modality, available clinical context, required image-quality checks, and output schema. Return a ranked differential diagnosis with explicit uncertainty, competing mimicker diagnoses, missing-context notes, and abstention triggers for inadequate images or low confidence. Require clinician or dermatologist confirmation before diagnosis, treatment advice, patient-facing guidance, or safety conclusions.
18. **BCC Multimodal LLM Dermatology Cautions**: For basal cell carcinoma and common mimickers, separate clinical-image and dermoscopic-image inputs in prompts, outputs, and review notes before interpreting any paired multimodal result. Frame responses as differential diagnoses rather than definitive labels; report uncertainty, missing context, and model disagreement explicitly; and require dermatologist review of ChatGPT, Gemini, Claude, or other multimodal LLM outputs before clinical interpretation or patient-facing guidance.
19. **Closed-System Radiography LLM Evaluation Controls**: For closed-system radiography LLM evaluation, standardize prompts and permitted context before scoring; assess answer correctness against the closed-system reference materials; track harmful omissions separately from incorrect statements; document image, report, and case-context limits that constrain interpretation; and require radiographer or clinician review before any generated response is used in patient-facing communication.
20. **Radiography Closed-System Educational Response Review**: For radiography-specific closed-system LLM responses, document the modality and permitted case context, state when image or context limits prevent an answer, score response correctness against the closed-system reference materials, and review hallucinated claims and clinically important omissions separately. Use escalation language for uncertain, incomplete, or clinically consequential outputs, and constrain results to non-diagnostic educational use unless a qualified clinician or radiography educator reviews them.
21. **Closed-System Radiography Technique and Safety Wording Review**: When evaluating closed-system LLM radiography responses, score radiographic technique accuracy separately from explanatory quality; check positioning, exposure and technique terminology, anatomy and view labeling, and whether each answer is supported by the supplied closed-system case, image description, and teaching materials. Review patient-safety wording, radiation-risk communication, unsupported reassurance or alarm, and explicit scope boundaries for non-diagnostic educational use. Escalate technique corrections, radiation-safety questions, clinical interpretation, diagnosis, or patient-specific advice to a licensed radiologic technologist or radiographer, radiologist, or other qualified imaging professional before use.

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
*   https://pubmed.ncbi.nlm.nih.gov/42024724/

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
