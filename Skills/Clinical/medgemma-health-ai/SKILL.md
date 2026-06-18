---
name: medgemma-health-ai
description: Build and evaluate medical text and vision applications with Google MedGemma, including MedGemma 1.5 workflows for CT, MRI, whole-slide pathology, longitudinal chest X-rays, lab reports, and EHR text. Use when prototyping, fine-tuning, deploying, or validating MedGemma-based health AI under clinical data and safety controls.
---

# MedGemma Health AI

Use MedGemma as a development foundation. It requires use-case-specific validation and human oversight before any clinical deployment.

## Model Selection

- Use MedGemma 1.5 4B for multimodal medical text generation, 3D CT or MRI, multi-patch whole-slide pathology, longitudinal chest X-rays, bounding-box localization, lab-document extraction, and EHR understanding.
- Consider MedGemma 1 variants when a 27B text-only model is required and the use case matches its model card.
- Use MedSigLIP instead when the task is image embedding, retrieval, or classification without text generation.

## Workflow

1. Define the intended user, clinical setting, decision supported, failure cost, and whether the system is research-only.
2. Create a data-governance plan before model access:
   - de-identify protected health information;
   - document data rights and retention;
   - keep inference local when policy requires it;
   - review Health AI Developer Foundations terms.
3. Choose local Hugging Face inference for experiments, Vertex AI endpoints for scalable online service, or Vertex AI batch prediction for large offline workloads.
4. Use the official preprocessing notebooks for CT, MRI, and whole-slide images. Do not send raw high-dimensional studies through a generic 2D image path.
5. Establish a baseline before fine-tuning. Split evaluation by site, device, demographic group, disease prevalence, and time when applicable.
6. Evaluate task accuracy plus calibration, abstention, hallucination, subgroup performance, robustness, latency, and clinician workflow impact.
7. Add retrieval, structured output validation, and deterministic post-processing only when they are separately tested.
8. Require human review, audit logs, rollback criteria, and post-deployment monitoring for any real clinical workflow.

## Guardrails

- Do not present model output as a diagnosis or treatment order without qualified clinician review.
- Do not rely on benchmark performance as evidence of local clinical validity.
- Do not expose PHI to an unapproved service.
- Detect and report missing modalities, truncated context, unsupported file types, and preprocessing failures.
- Preserve model identifier, prompt, image preprocessing, decoding settings, and all fine-tuning data lineage.

## Output Contract

Return a model card supplement for the local use case: intended use, excluded use, dataset and subgroup coverage, metrics, failure analysis, human-oversight design, privacy controls, and deployment recommendation.

Read `references/operations.md` for current model details, a local inference pattern, deployment paths, and authoritative sources.
