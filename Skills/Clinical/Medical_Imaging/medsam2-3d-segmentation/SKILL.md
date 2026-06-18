---
name: medsam2-3d-segmentation
description: Operate MedSAM2 for promptable segmentation of 3D medical images and medical videos, including CT lesion propagation, MRI volumes, RECIST-guided prompts, efficient CPU-oriented variants, training, and 3D Slicer integration. Use when generating or validating volumetric masks from sparse prompts or propagating masks through image slices or video frames.
---

# MedSAM2 3D Segmentation

Use MedSAM2 to accelerate annotation and research segmentation. Every generated mask requires anatomical and task-specific quality review before quantitative or clinical use.

## Workflow

1. Define the target anatomy or lesion, modality, acquisition protocol, prompt source, and downstream measurement.
2. De-identify inputs and preserve voxel spacing, orientation, affine, frame order, and original series identifiers in a controlled manifest.
3. Convert DICOM or vendor formats with a validated pipeline. Do not treat array index order as physical orientation.
4. Choose the prompt strategy:
   - point or box prompt for interactive segmentation;
   - RECIST marker or middle-slice box for lesion propagation;
   - initial mask for video propagation.
5. Run a pilot and inspect propagation across the full volume or video, not only the prompted slice or frame.
6. Post-process only with prespecified operations such as component filtering or hole filling, and compare masks before and after each operation.
7. Evaluate Dice, surface Dice, Hausdorff distance, lesion-wise detection, volume error, and inter-reader variability as appropriate.
8. Stratify performance by scanner, site, contrast phase, slice thickness, anatomy, lesion size, and prompt quality.
9. Export masks with the original geometry and retain prompt provenance for audit.

## Guardrails

- Do not use unreviewed masks for diagnosis, radiation planning, surgery, or response assessment.
- Detect missing slices, inconsistent orientation, anisotropic spacing, motion, and corrupted frames.
- Review small lesions and volume boundaries slice by slice.
- Do not evaluate only on datasets used for model development.
- Verify checkpoint, dataset, SAM2, and downstream plugin licenses separately.
- Require qualified clinical annotation and local validation for real-world deployment.

## Output Contract

Return input geometry and provenance, prompt type, checkpoint, preprocessing, segmentation metrics, per-case failures, subgroup analysis, post-processing, exported-mask format, and review status.

Read `references/operations.md` for installation, inference commands, training patterns, and canonical sources.
