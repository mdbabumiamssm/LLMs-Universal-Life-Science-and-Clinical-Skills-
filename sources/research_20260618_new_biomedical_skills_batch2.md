# New Biomedical Skills Research — Batch 2 — 2026-06-18

## Objective

Extend the first gap-driven update with additional operational skills that are distinct from the repository's broad agents and imported collections.

## Selection Standard

Candidates required:

1. an official repository, model card, release, or first-party documentation;
2. a recurring operational workflow with a clear trigger;
3. meaningful differentiation from existing first-party skills;
4. enough public detail to encode setup, provenance, limitations, and validation;
5. current maintenance or continuing scientific relevance.

## Selected Skills

| Skill | Distinct Gap | Source Status Observed |
|---|---|---|
| `txgemma-therapeutics` | Therapeutic prediction versus conversational TxGemma workflows | Google model card v1.0.0; 2B, 9B, and 27B releases |
| `protenix-structure-prediction` | Current open AlphaFold3-style co-folding and inference-time scaling | bytedance/Protenix; Apache-2.0; v2.0.0 on 2026-04-07 |
| `medsam2-3d-segmentation` | Promptable propagation through 3D medical volumes and videos | bowang-lab/MedSAM2; Apache-2.0 repository; official checkpoints |
| `opencrispr-gene-editors` | Operational evaluation of released AI-designed gene editors | Profluent-AI/OpenCRISPR; OpenCRISPR-1 plus protocol and Nature paper |
| `monai-medical-imaging` | Reproducible domain framework, bundles, labeling, and deployment | Project-MONAI/MONAI; Apache-2.0; v1.6.0 on 2026-06-11 |
| `transcriptformer-cell-embeddings` | Cross-species generative cell and contextual gene embeddings | czi-ai/transcriptformer; MIT; v0.6.1 |

## Overlap Decisions

- TxGemma is separated from generic chemoinformatics because its predictive and chat variants require model-specific prompts, splits, and validation.
- Protenix complements Boltz-2: Protenix focuses open structure co-folding, templates, constraints, and cutoff-controlled model selection; Boltz-2 adds model-specific affinity outputs.
- MedSAM2 and MONAI are both included because one is a promptable segmentation model and the other is a general medical-imaging framework and packaging ecosystem.
- TranscriptFormer is separated from the broad single-cell foundation-model agent because it has model-specific raw-count, species-embedding, and output-schema requirements.
- OpenCRISPR is limited to released systems and validation planning, not unrestricted de novo editor design.

## Deferred Candidates

- TotalSegmentator: strong operational candidate, but deferred to avoid over-concentrating this batch on segmentation.
- Tahoe-100M dataset operations: valuable, but no single official code repository was identified during this audit; existing scvi-tools notebooks already provide local entry points.
- Chai-1 and AlphaFold3: existing first-party structure-prediction coverage already includes direct workflows.

## Canonical Sources

- https://developers.google.com/health-ai-developer-foundations/txgemma/model-card
- https://github.com/google-gemini/gemma-cookbook/tree/main/TxGemma
- https://github.com/bytedance/Protenix
- https://github.com/bowang-lab/MedSAM2
- https://github.com/Profluent-AI/OpenCRISPR
- https://github.com/Project-MONAI/MONAI
- https://github.com/czi-ai/transcriptformer
