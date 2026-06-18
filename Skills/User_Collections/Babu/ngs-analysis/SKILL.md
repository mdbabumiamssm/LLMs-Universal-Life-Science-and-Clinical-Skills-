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
name: bio-ngs-analysis
description: Practical next-generation sequencing analysis support for bulk RNA-seq,
  variant calling, alignment, preprocessing, and workflow assembly. Use when working
  from FASTQ or BAM/VCF inputs, setting up QC, choosing aligners or quantifiers, organizing
  reproducible NGS pipelines, or preparing downstream differential or variant analyses.
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# NGS Analysis

Run NGS tasks with explicit sample tracking, reproducible commands, and pipeline choices that match the assay.

## Workflow

1. Identify assay, read structure, reference assets, and expected endpoint before running tools.
2. Check file integrity, sample sheet consistency, lane structure, and naming conventions first.
3. Run QC before major processing and keep pre-filter and post-filter metrics.
4. Choose assay-specific tooling rather than forcing one generic pipeline across RNA-seq, DNA-seq, and single-cell data.
5. Preserve provenance for every intermediate: command, version, reference, and parameter changes.
6. Summarize outputs in terms a collaborator can act on: pass-fail QC, counts, variant sets, DE tables, or missing inputs.

## Guardrails

- Never mix genome builds or annotation releases silently.
- Keep tumor-normal pairing, replicate structure, and strandedness explicit.
- Treat aligner defaults as starting points, not biological truth.
- Separate workflow failures from biologic negatives.

## References

- Read `references/pipeline-selection.md` to choose the right NGS path.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->