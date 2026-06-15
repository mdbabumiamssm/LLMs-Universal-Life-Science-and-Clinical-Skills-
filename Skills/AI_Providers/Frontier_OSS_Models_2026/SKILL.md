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
name: frontier-oss-models-2026
description: Work with leading open or openly available model ecosystems from Meta, Mistral, DeepSeek, and xAI. Use when evaluating self-hosted or hybrid deployment paths, model tradeoffs, and integration patterns across non-single-vendor stacks.
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
  - read_file
  - run_shell_command
---

# Frontier OSS Models (2026)

## Core Capabilities

- Clinical on-premises assessment for compact distilled reasoning models: require independent diagnostic benchmarking, calibration evaluation, hardware profiling, privacy review, and explicit comparison with hosted frontier models before adopting DeepSeek-R1 derivatives.
- Clinical deployment caution for distilled DeepSeek-R1 or other open-source medical diagnosis models: compare benchmark performance with deployment risk, weigh on-premises privacy benefits against calibration limits and hallucination checks, and require model governance plus clinician oversight before clinical use.
- Clinical self-hosting review for distilled DeepSeek-R1/open-weight medical diagnosis deployments: benchmark against licensed frontier and domain models, require local evaluation sets, calibration and abstention checks, privacy/on-prem controls, and clinical safety gates before diagnostic workflow use.
- Clinical validation requirements from the 2026 comparative study: for distilled DeepSeek-R1 and other open-source reasoning models, require on-prem validation against local diagnostic workflows, treat diagnosis benchmarks as deployment caveats rather than approval evidence, enforce PHI governance, measure calibration and refusal behavior, and require human clinical review before any clinical use.
- Clinical on-premises deployment of distilled reasoning models: treat diagnostic benchmark degradation from distillation or quantization as an evaluation risk; benchmark locally, test calibration and latency on target hardware, document privacy and hardware tradeoffs, perform structured failure analysis, and require clinician validation before deployment.

## Clinical On-Premises Deployment

- For distilled DeepSeek-R1/open-weight models used in medical diagnosis, benchmark against licensed frontier and domain models before selection.
- Require local diagnostic evaluation sets, calibration and abstention checks, privacy/on-prem controls, and clinical safety gates before use in diagnostic workflows.
- Profile target hardware and compare independently measured diagnostic performance with hosted frontier models before adoption.
- Compare unquantized and candidate quantized configurations for diagnostic quality, calibration, latency, memory use, and hardware feasibility; do not assume that a smaller distilled model preserves the source model's clinical performance.
- Analyze diagnostic failures by case type, error mode, confidence, and quantization configuration; define escalation and abstention criteria from the observed failures.
- Keep protected clinical data within approved on-premises privacy controls, and require documented clinician validation of the model and its failure controls before deployment as well as clinician review of every model-assisted diagnostic output.

## Workflow

1. Identify target deployment mode: hosted API, self-hosted, or hybrid.
2. Review provider-specific docs and repos in `references/sources.md`.
3. Compare model choice by licensing, latency, and hardware profile.
4. Define eval set before changing production model baselines.
5. Roll out through canary traffic with measurable success thresholds.

## Output Requirements

- State selected model family and deployment mode.
- List one licensing/compliance check.
- List one rollback condition tied to quality or cost.

## References

- https://pubmed.ncbi.nlm.nih.gov/42062641/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
