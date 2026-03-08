---
name: ngs-analysis
description: Practical next-generation sequencing analysis support for bulk RNA-seq, variant calling, alignment, preprocessing, and workflow assembly. Use when working from FASTQ or BAM/VCF inputs, setting up QC, choosing aligners or quantifiers, organizing reproducible NGS pipelines, or preparing downstream differential or variant analyses.
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
