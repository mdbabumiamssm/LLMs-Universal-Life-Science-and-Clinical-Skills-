# Pipeline Selection

## Choose by assay

- Bulk RNA-seq: fastp or equivalent QC, STAR or Salmon, featureCounts or transcript quantification, DESeq2 or edgeR downstream.
- Somatic DNA-seq: alignment, duplicate marking, recalibration if applicable, somatic caller, filtering, annotation.
- Germline DNA-seq: alignment, joint or single-sample calling, normalization, annotation, inheritance or cohort analysis.
- Single-cell preprocessing: use assay-native tooling first, then move into Scanpy or Seurat objects.

## Minimum metadata to capture

- Sample identifier and condition.
- Read layout and strandedness.
- Genome build and annotation release.
- Paired design or control sample.
- Reference FASTA and known-sites resources.

## Always report

- Read depth and alignment rate.
- Duplication or complexity metrics.
- Number of retained genes or variants after filtering.
- Any sample exclusions and the reason.
