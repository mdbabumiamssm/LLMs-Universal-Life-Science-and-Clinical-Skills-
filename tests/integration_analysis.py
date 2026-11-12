# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

import scanpy as sc
import anndata as ad
import os

# Set settings
sc.settings.verbosity = 3
sc.settings.set_figure_params(dpi=80, facecolor='white')

# Define paths
output_dir = "analyzed_data/integrated_results"
os.makedirs(output_dir, exist_ok=True)

samples = {
    "BM1": "analyzed_data/GSM3901485_BM1_qc/GSM3901485_BM1_filtered.h5ad",
    "BM2": "analyzed_data/GSM3901486_BM2_qc/GSM3901486_BM2_filtered.h5ad",
    "BM3": "analyzed_data/GSM3901487_BM3_qc/GSM3901487_BM3_filtered.h5ad"
}

print("1. Loading and Concatenating Data...")
adatas = []
for sample_id, file_path in samples.items():
    print(f"  Loading {sample_id} from {file_path}")
    adata = ad.read_h5ad(file_path)
    adata.obs['batch'] = sample_id  # Label the batch
    adatas.append(adata)

# Concatenate (Integration Step 1)
adata_integrated = ad.concat(adatas, label="batch", keys=samples.keys())
adata_integrated.obs_names_make_unique()
print(f"  Combined dataset shape: {adata_integrated.shape}")

print("\n2. Preprocessing...")
# Normalize and Log Transform
sc.pp.normalize_total(adata_integrated, target_sum=1e4)
sc.pp.log1p(adata_integrated)

# Highly Variable Genes
sc.pp.highly_variable_genes(adata_integrated, min_mean=0.0125, max_mean=3, min_disp=0.5)
print(f"  Highly variable genes: {sum(adata_integrated.var['highly_variable'])}")

# Preserve raw data before scaling
adata_integrated.raw = adata_integrated

# Scale and PCA
adata_integrated = adata_integrated[:, adata_integrated.var.highly_variable]
sc.pp.scale(adata_integrated, max_value=10)
sc.tl.pca(adata_integrated, svd_solver='arpack')

print("\n3. Neighborhood Graph & UMAP...")
# Compute Neighbors (this effectively integrates the data structure)
sc.pp.neighbors(adata_integrated, n_neighbors=10, n_pcs=40)

# UMAP
sc.tl.umap(adata_integrated)

# Clustering (to see "common cells/types")
sc.tl.leiden(adata_integrated)

print("\n4. Saving Results & Plots...")
# Plot 1: UMAP colored by Batch (Integration Check)
# This answers: "Are common cells expressed?" (Do batches overlap?)
fig_batch = sc.pl.umap(adata_integrated, color='batch', title='Data Integration: Batch Mixing', show=False, return_fig=True)
fig_batch.savefig(f"{output_dir}/umap_integration_batch.png", bbox_inches='tight')

# Plot 2: UMAP colored by Cluster (Cell Types)
fig_cluster = sc.pl.umap(adata_integrated, color='leiden', title='Clustered Cell Types', show=False, return_fig=True)
fig_cluster.savefig(f"{output_dir}/umap_clusters.png", bbox_inches='tight')

# Plot 3: Split view to prove commonality
# Shows each batch on the same UMAP coordinates side-by-side
fig_split = sc.pl.umap(adata_integrated, color='batch', groups=['BM1', 'BM2', 'BM3'], title='Batch Separation Check', show=False, return_fig=True)
fig_split.savefig(f"{output_dir}/umap_split_check.png", bbox_inches='tight')

# Save integrated object
adata_integrated.write(f"{output_dir}/integrated_data.h5ad")

print(f"\nAnalysis Complete.")
print(f"Results saved to: {output_dir}")
print(f"  - umap_integration_batch.png (Check if colors mix -> Common cells found)")
print(f"  - umap_clusters.png")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
