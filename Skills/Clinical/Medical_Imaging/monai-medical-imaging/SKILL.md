---
name: monai-medical-imaging
description: Build reproducible healthcare imaging pipelines with Project MONAI for DICOM, NIfTI, pathology, and multidimensional imaging tasks including preprocessing, augmentation, training, sliding-window inference, evaluation, model bundles, labeling, and deployment. Use when implementing medical image classification, segmentation, registration, detection, generative, or foundation-model workflows in PyTorch.
---

# MONAI Medical Imaging

Use MONAI as the domain framework around a clearly defined clinical imaging task, not as a substitute for data governance, study design, or external validation.

## Workflow

1. Define the clinical question, modality, target, unit of analysis, annotation source, and intended deployment setting.
2. Build patient-level train, validation, and test splits before preprocessing. Separate sites, scanners, or time periods when testing generalization.
3. Preserve physical metadata: orientation, spacing, affine, DICOM identifiers, acquisition parameters, and label geometry.
4. Compose deterministic transforms before stochastic augmentation. Cache only transformations that are safe to reuse.
5. Choose the architecture, loss, sampling strategy, patch size, and class balancing from the target and memory constraints.
6. Train with fixed seeds, versioned configs, mixed-precision controls, checkpoint selection rules, and monitored failure states.
7. Use sliding-window or patch inference with explicit overlap and blending settings for large volumes.
8. Evaluate voxel or image metrics plus calibration, lesion-wise performance, surface metrics, subgroup behavior, and clinically meaningful errors.
9. Package the finalized pipeline as a versioned MONAI Bundle with preprocessing, network, post-processing, metadata, and tests.
10. Use MONAI Label for annotation workflows and MONAI Deploy components only after validating security, DICOM integration, and operational monitoring.

## Guardrails

- Prevent patient, study, patch, and temporal leakage.
- Do not resample images and masks with incompatible interpolation.
- Do not discard physical-space metadata after array conversion.
- Report per-case failures and empty-mask behavior, not only aggregate Dice.
- Pin MONAI, PyTorch, CUDA, bundle, and model-zoo versions.
- Require local clinical, privacy, cybersecurity, and regulatory review before deployment.

## Output Contract

Return the task definition, cohort and splits, transform graph, model and loss, training configuration, inference settings, metrics with uncertainty, failure analysis, bundle contents, and deployment readiness.

Read `references/operations.md` for installation, core patterns, bundle guidance, and canonical sources.
