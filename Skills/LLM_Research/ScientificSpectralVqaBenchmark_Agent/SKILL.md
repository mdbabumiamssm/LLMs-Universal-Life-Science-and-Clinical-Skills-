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
name: 'scientific-spectral-vqa-benchmark'
description: 'Evaluate MLLMs on scientific spectral images using SpecVQA-style figure extraction, curve-aware sampling, QA design, and scoring workflows.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Scientific Spectral VQA Benchmark

## Overview

This skill guides spectral visual question answering workflows for scientific images, grounded in the SpecVQA benchmark for multimodal large language model evaluation. Use it to extract spectrum figures, preserve curve information, design expert-style QA tasks, score model answers, and report failure modes for spectroscopy-heavy scientific workflows.

## When to Use This Skill

- Evaluating MLLMs or vision-language models on scientific spectra rather than ordinary natural images or charts.
- Building or adapting SpecVQA-style tasks for spectral scientific-image QA.
- Extracting, sampling, or reconstructing curve information from spectrum figures while preserving essential shape characteristics.
- Designing question-answer pairs for direct information extraction and domain-specific spectral reasoning.
- Comparing model performance across spectrum categories, task types, or prompt/input representations.
- Auditing model errors on axes, peaks, trends, labels, legends, units, or cross-curve relationships in scientific spectra.

## Core Capabilities

1. **Figure and Metadata Triage** - Identify candidate spectral figures from papers, PDFs, image folders, or curated manifests; retain source provenance, figure captions, panel labels, spectrum type, and licensing or reuse constraints.

2. **Spectrum-Aware Preprocessing** - Crop relevant panels, remove unrelated layout noise, normalize orientation and resolution, and preserve axes, legends, labels, color encodings, and curve visibility needed for scientific interpretation.

3. **Curve-Preserving Representation** - Convert spectral curves into compact sampled representations when useful, then reconstruct or interpolate for model input while checking that peak positions, relative intensities, curve ordering, and trend features remain visible.

4. **QA Task Design** - Create QA items that separate direct visual extraction from domain-specific reasoning; include answer types such as categorical labels, short text, numeric values with units, peak comparisons, trend descriptions, and evidence-backed conclusions.

5. **Model Evaluation and Scoring** - Run models with controlled prompts and inputs; score exact or normalized answers for constrained questions, apply explicit tolerances for numeric responses, and use rubric-based review for reasoning answers.

6. **Error Analysis** - Categorize failures by visual parsing, axis or unit interpretation, legend binding, peak localization, curve comparison, domain reasoning, hallucination, refusal, and sensitivity to sampled versus raw image inputs.

7. **Benchmark Reporting** - Produce a reproducible summary with dataset counts, task distribution, model configurations, scoring rules, per-task results, representative successes/failures, and limitations.

## Inputs / Outputs

**Inputs**

- Spectral images, PDF figures, figure panels, or a curated figure manifest.
- Figure captions, article metadata, panel labels, and source URLs when available.
- Spectrum category labels, task labels, and any expert annotations supplied by the user.
- Model endpoints or model output files for evaluation.
- QA schema, numeric tolerances, scoring rubric, and reporting format requirements.

**Outputs**

- A curated figure manifest with source provenance and preprocessing notes.
- Optional sampled or reconstructed spectral curve data with quality checks.
- SpecVQA-style question-answer pairs grouped by task type and spectrum category.
- Model response records with prompt, input representation, answer, score, and error tags.
- A benchmark report or leaderboard-style table that distinguishes extraction, reasoning, and representation effects.

## References

- SpecVQA: A Benchmark for Spectral Understanding and Visual Question Answering in Scientific Images. arXiv:2604.28039v1. http://arxiv.org/abs/2604.28039v1
