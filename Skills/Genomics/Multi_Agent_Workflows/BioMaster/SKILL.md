---
name: biomaster-workflows
description: "Multi-agent pipeline orchestrator for RNA-seq, ChIP-seq, single-cell, and Hi-C workflows that manages YAML-driven configs, tool versioning, QC reporting, and reproducible output packaging."
compatibility: "Python 3.9+"
allowed-tools: "run_shell_command, read_file"
metadata:
  author: BioMaster Team
  version: "1.0.0"
  keywords: "workflows, RNAseq, ChIPseq, automation, YAML"
  measurable_outcome: "Execute a configured pipeline end-to-end (including QC report + summary) within 24 hours of receiving inputs, logging every tool/parameter."
  license: MIT
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

# BioMaster Workflows

Orchestrate BioMaster’s multi-agent pipelines (RNA-seq, ChIP-seq, single-cell, Hi-C) using YAML-driven configs to deliver reproducible, auditable outputs.

Use when running end-to-end genomics pipelines that require coordinated tool execution, automatic QC reporting, and full parameter logging across multiple analysis stages.

## When to Use

- **Bulk RNA-seq or ChIP-seq** — running alignment, quantification, and peak-calling pipelines with automated QC.
- **Single-cell analysis** — orchestrating preprocessing, clustering, and annotation workflows.
- **Hi-C analysis** — managing contact matrix generation and downstream 3D genome analysis.
- **Reproducibility audits** — when every tool version and parameter must be logged for publication or compliance.

## Workflow

1. **Prepare config** — populate YAML with tool paths, reference genomes, and workflow selection (`rnaseq`, `chipseq`, `singlecell`, `hic`).
2. **Set up environment** — run `pip install -r requirements.txt` in the repo root (or use the provided container).
3. **Launch pipeline** — execute `python repo/run.py --config repo/config.yaml` and monitor progress.
4. **Handle errors** — BioMaster agents retry failing stages automatically; review logs for missing reference/index files.
5. **Package outputs** — collect BAMs/counts/peaks, QC reports, and a narrative summary of parameters and runtimes.

## Guardrails

- Fail fast when reference files or indices are absent to avoid wasted compute.
- Record tool versions for every stage (alignment, quantification, peak-calling).
- Require confirmation before deleting intermediates or rerunning destructive steps.

## References

- Full workflow descriptions, supported modalities, and repo links in `README.md`.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->