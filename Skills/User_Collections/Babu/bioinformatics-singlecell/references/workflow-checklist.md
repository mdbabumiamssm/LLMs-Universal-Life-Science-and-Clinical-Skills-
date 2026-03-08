# Single-Cell Workflow Checklist

## Inputs to confirm

- Assay: scRNA-seq, CITE-seq, multiome, scATAC-seq, or targeted panel.
- Source: 10x, SMART-seq, Parse, BD Rhapsody, or custom.
- Species and genome build.
- Sample grouping: donor, condition, timepoint, batch, tissue.
- Deliverables: QC report, integrated object, DE tables, annotation, figure set.

## Recommended execution order

1. Ingest raw matrices and metadata.
2. Compute cell-level QC metrics and inspect distributions by sample.
3. Remove obvious low-quality cells, likely empty droplets, and severe outliers.
4. Detect doublets before final clustering.
5. Normalize and identify highly variable features.
6. Integrate or batch-correct only when batches distort biologic structure.
7. Build neighbor graph, embeddings, and clusters.
8. Annotate clusters with markers plus reference mapping if needed.
9. Run differential testing with the correct unit of replication.
10. Export h5ad or mudata objects, tables, and plots with clear filenames.

## Report explicitly

- QC thresholds and justification.
- Number of cells retained per sample.
- Integration method and latent representation.
- Cluster resolution and annotation evidence.
- Whether DE is cell-level or pseudobulk.
