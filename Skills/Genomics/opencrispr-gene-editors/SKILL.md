---
name: opencrispr-gene-editors
description: Evaluate and operate released Profluent OpenCRISPR gene-editing systems, especially OpenCRISPR-1, for controlled research workflows using its published Cas9-like protein, compatible guide RNA designs, protocols, licensing, specificity testing, and experimental validation. Use when comparing OpenCRISPR-1 with SpCas9, planning nonclinical editing studies, or assessing use in nuclease, nickase, deactivated, base, prime, or epigenome-editing contexts.
---

# OpenCRISPR Gene Editors

Use only released OpenCRISPR systems under institutional biosafety, ethical, and legal oversight. This skill does not authorize de novo editor engineering or clinical use.

## Workflow

1. Define the research purpose, cell or organism system, genomic target, delivery method, and whether nuclease, nickase, or deactivated activity is required.
2. Confirm that the released system and NGG PAM preference fit the target and that the guide design is compatible with the intended editor configuration.
3. Obtain sequence and protocol materials from the official release and record the repository revision, construct, guide, and license status.
4. Design a comparison that includes a validated reference editor, mock control, non-targeting guide, positive control, and multiple independent guides when possible.
5. Pre-register on-target efficiency, indel spectrum, bystander effects, off-target assessment, viability, innate immune response, and delivery metrics.
6. Use orthogonal assays for editing efficiency and specificity; do not rely on a single amplicon, prediction model, or reporter.
7. Confirm the exact editor state and fusion architecture before interpreting base, prime, or epigenome-editing results.
8. Stop escalation when safety, specificity, or reproducibility thresholds are not met.

## Guardrails

- Do not use this skill to design pathogen-enhancing edits, transmissible systems, or unapproved human germline or clinical interventions.
- Do not assume canonical SpCas9 guide compatibility guarantees equivalent activity or specificity.
- Do not omit off-target and structural-variant assessment for consequential experiments.
- Follow institutional biosafety committee, ethics, material-transfer, and licensing requirements.
- Treat commercial therapeutic use as license-controlled even though sequences are public.
- Require qualified experimental review before ordering constructs or initiating wet-lab work.

## Output Contract

Return the use case, editor configuration, licensing status, guide and control strategy, assay plan, predefined acceptance thresholds, biosafety review, failure criteria, and evidence gaps.

Read `references/operations.md` for release facts, access, validation considerations, and canonical sources.
