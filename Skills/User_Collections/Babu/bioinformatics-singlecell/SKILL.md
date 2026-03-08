---
name: bioinformatics-singlecell
description: Single-cell and multi-omic analysis for hematology, oncology, and translational biology. Use when working with scRNA-seq, CITE-seq, scATAC-seq, multiome, trajectory analysis, batch correction, cell typing, differential expression, or publication-ready figures in Scanpy, scvi-tools, Seurat, or MuData workflows.
---

# Single-Cell Analysis

Run practical single-cell analysis workflows with emphasis on QC discipline, interpretable annotations, and reproducible outputs.

## Workflow

1. Confirm assay type, species, reference build, sample design, and expected outputs before touching code.
2. Inspect raw inputs and metadata first; check barcode structure, feature naming, batch labels, and sample-level covariates.
3. Apply assay-appropriate QC thresholds rather than hard-coding generic cutoffs across datasets.
4. Normalize, integrate, cluster, and annotate with methods that match the study design; preserve raw counts when downstream models need them.
5. Separate exploratory clustering from biologic claims; validate major labels with marker genes, orthogonal metadata, or reference mapping.
6. Report thresholds, software versions, random seeds, and the exact objects written to disk.

## Guardrails

- Flag doublets, ambient RNA, batch leakage, and low-complexity samples before interpreting clusters.
- Do not overstate automated annotation; list competing labels when marker support is mixed.
- For disease cohorts, distinguish malignant state, lineage identity, and treatment effect.
- Preserve donor and sample identity through every merge or integration step.

## References

- Read `references/cell_markers.md` for lineage and megakaryocyte markers.
- Read `references/workflow-checklist.md` for a compact end-to-end checklist.
