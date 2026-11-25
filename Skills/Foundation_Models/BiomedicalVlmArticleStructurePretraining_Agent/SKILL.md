<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'biomedical-vlm-article-structure-pretraining'
description: 'Prepare and audit biomedical VLM pretraining that uses article, figure, and panel relationships, with provenance tracking, matched image-caption baselines, and article-level leakage controls.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Biomedical VLM Pretraining from Article Structure

## Overview

This skill prepares a traceable training and evaluation plan for biomedical vision-language models using relationships within scientific articles. BioLoom motivates preserving exact image-text correspondence while incorporating related figure content, rather than flattening every sample into an independent pair. The fifteen-minute outcome is a readiness report and validated small-sample design, not full-scale pretraining.

## When to Use This Skill

- Curating article-linked biomedical figures, panel crops, captions, and mentioning paragraphs.
- Assessing whether BioLoom-style supervision can improve an existing contrastive pretraining pipeline.
- Comparing structure-aware learning with conventional image-caption training under matched conditions.
- Auditing article overlap, reused figures, or provenance gaps before evaluating retrieval or zero-shot classification.
- Checking whether published resources support an executable reproduction.

## Core Capabilities

1. **Verify evidence and resource readiness.** Read the versioned paper, supplementary method, official repository, dataset cards, model cards, and applicable licenses before documenting executable commands. Record URLs, access dates, repository commits, dataset revisions, weight versions, and unresolved discrepancies. Verify code, dataset, checkpoint, and underlying article reuse terms separately; a paper license does not license its training assets.

   Verification status on 2026-11-25: the arXiv abstract and HTML method were accessible. The PDF fetch exceeded the retrieval tool's size limit, and the project page was inaccessible; complete supplementary details, repository contents, downloadable assets, and their licenses remain unverified. Do not invent repository URLs, installation commands, dataset loaders, or release permissions. Until these gaps are resolved, produce a preparation report with `execution_status: blocked_unverified_resources` and list the exact missing evidence.

2. **Preserve the article-to-image chain.** Build a proposed manifest with `sample_id`, canonical `article_id`, article URL/version, `figure_id`, optional `panel_id`, parent figure ID, image path/hash, crop coordinates and coordinate convention, text ID/source, paragraph references, content type, license evidence, and split. Keep original text distinct from generated descriptions. For generated text, record model revision, prompt revision, input references, and generation settings. Reject orphan panels, missing article identity, invalid crops, unreadable images, and empty paired text from a reproducible training subset.

3. **Represent the published supervision accurately.** BioLoom distinguishes exact matches, different samples from one figure, different figures from one article, and cross-article pairs. Its exact-pair loss masks related samples; its relation loss aligns same-figure samples, masks exact and same-article cross-figure candidates, and increases weights for same-type cross-article negatives. The combined objective uses relation weight 0.05 and hard-negative weight 1.1 in the HTML method. Whole figures retain original captions; panels use concatenated visual descriptions and contextual captions informed by figure captions and mentioning paragraphs. These are paper-reported details, not a verified implementation recipe. [Method, Sections 3.1–3.3](https://arxiv.org/html/2611.33151v1).

   Before implementation, resolve the content-type taxonomy, batch sampler, distributed candidate gathering, normalization, and treatment of anchors without related candidates against the complete method and pinned code. Do not equate all same-article samples with positives or give sibling descriptions the status of exact captions.

4. **Control leakage before generating derivatives.** As a workflow safeguard, group article versions and duplicates before assigning train, validation, and test partitions. Keep every figure, crop, caption variant, and contextual paragraph from each article group in one split. Search for reused images and near-duplicate text across articles and benchmark assets; merge connected duplicate groups or exclude contaminated records. Fit filtering thresholds on training/validation data only. Report unresolved overlap and unknown original checkpoint exposure; an article-disjoint local split cannot establish that a pretrained encoder never saw the benchmark.

5. **Design a fair conventional baseline.** Hold training records, image/text encoders, initialization, preprocessing, tokenizer limits, batch construction, optimizer schedule, updates, and evaluation prompts fixed while comparing ordinary symmetric contrastive loss with structure-aware supervision. Separately ablate caption enrichment and structural relationships so their effects are distinguishable. Include a whole-figure/original-caption condition when testing the data-preparation contribution, and disclose its changed sample composition. Treat comparisons against published checkpoints as contextual evidence, not controlled causal experiments.

6. **Audit evaluation and bounded execution.** Specify zero-shot class prompts and retrieval relevance rules before scoring. Report image-to-text and text-to-image Recall@1 separately and state how their mean is computed; distinguish original and concise caption protocols. For classification, declare task, dataset, and domain aggregation explicitly. Report local measurements separately from paper results, with split sizes, exclusions, and uncertainty where feasible.

   Within fifteen minutes, inspect available evidence, audit a small user-provided sample, and deliver the manifest schema, leakage findings, comparison plan, and readiness decision. If implementation and licenses have subsequently been verified, a user-authorized smoke run may check finite losses/gradients, relation masks, and candidate availability on a small batch. Include same-figure, same-article cross-figure, cross-article same-type, and no-sibling cases. A smoke test does not validate full training or benchmark claims; report unrun checks explicitly.

## Inputs / Outputs

**Inputs**

- Versioned paper and supplementary material; official release links and license documents where accessible.
- Authorized article corpus or representative sample with figures, captions, text references, and stable identifiers.
- Existing preprocessing/training configuration, encoder checkpoints, available compute, and requested comparison scope.
- Evaluation datasets, split definitions, class prompts, retrieval relevance rules, and known pretraining overlap.

**Outputs**

- A source and license evidence ledger distinguishing verified, inaccessible, and unresolved resources.
- A provenance manifest or schema, validation findings, and a relationship specification tied to source evidence.
- An article-group split plan and duplicate/benchmark overlap report, including unresolved leakage risks.
- A matched baseline and ablation plan with explicit evaluation protocols and reproducibility settings.
- A readiness report containing execution status, completed checks, unrun checks, blockers, and next required evidence; actual run logs and metrics only when execution occurred.

**Acceptance criteria:** Every audited retained sample has resolvable provenance; split assignments keep article and known duplicate groups together; relationship categories are unambiguous; resource/license gaps are visible; and no training or evaluation result is presented as reproduced without a corresponding run. A blocked readiness report is a valid preparation deliverable, but must not be labeled successful pretraining.

## References

- [BioLoom: Scaling Biomedical Vision-Language Models by Learning from the Structure of Scientific Articles — arXiv:2611.33151v1](http://arxiv.org/abs/2611.33151v1). Source finding, submitted 2026-11-24.
- [BioLoom HTML method](https://arxiv.org/html/2611.33151v1). Accessible method evidence; complete supplementary verification remains outstanding.
- [BioLoom project page](https://bioloom-clip.github.io/). Official resource pointer supplied by the paper; inaccessible during authoring, so linked code, datasets, models, and licenses were not independently verified.
