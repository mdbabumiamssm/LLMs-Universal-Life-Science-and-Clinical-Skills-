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
import pandas as pd
import os

# Settings
sc.settings.verbosity = 3
sc.logging.print_header()
sc.settings.set_figure_params(dpi=150, facecolor='white', frameon=False)

results_dir = 'tests/results_BM_vs_BT'
os.makedirs(results_dir, exist_ok=True)
sc.settings.figdir = results_dir

data_dir = '/home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills/tests/scRNAsedata'
samples = {
    'BM1': 'GSM3901485_BM1',
    'BM2': 'GSM3901486_BM2',
    'BM3': 'GSM3901487_BM3',
    'BT1': 'GSM3901489_BT1',
    'BT2': 'GSM3901490_BT2',
    'BT3': 'GSM3901491_BT3'
}

adatas = []
for sample_name, folder in samples.items():
    path = os.path.join(data_dir, folder)
    print(f"Loading {sample_name} from {path}")
    try:
        # read_10x_mtx automatically looks for matrix.mtx, genes.tsv/features.tsv, barcodes.tsv
        adata = sc.read_10x_mtx(path, var_names='gene_symbols', cache=False)
    except Exception as e:
        print(f"Error reading {path}: {e}")
        continue
        
    adata.obs['sample'] = sample_name
    adata.obs['condition'] = 'BM' if 'BM' in sample_name else 'BT'
    adata.var_names_make_unique()
    adatas.append(adata)

if not adatas:
    raise ValueError("No data loaded")

print("Concatenating samples...")
if len(adatas) > 1:
    adata = adatas[0].concatenate(adatas[1:], batch_key='batch_sample')
else:
    adata = adatas[0]

print(f"Combined data shape: {adata.shape}")

# QC
print("Calculating QC metrics...")
adata.var['mt'] = adata.var_names.str.startswith('MT-') 
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)

# Plot QC
sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
             jitter=0.4, multi_panel=True, show=False, save='_qc.png')

# Filter
print("Filtering...")
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
adata = adata[adata.obs.n_genes_by_counts < 6000, :] 
adata = adata[adata.obs.pct_counts_mt < 15, :] 

print(f"Data shape after filtering: {adata.shape}")

# Normalize & Log
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# HVGs
print("Finding HVGs...")
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
sc.pl.highly_variable_genes(adata, show=False, save='_hvg.png')

# PCA
print("Running PCA...")
sc.tl.pca(adata, svd_solver='arpack')
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.umap(adata)

# Clustering
print("Clustering (Leiden)...")
sc.tl.leiden(adata)

# DEGs/Markers per cluster
print("Finding markers per cluster...")
sc.tl.rank_genes_groups(adata, 'leiden', method='wilcoxon')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, show=False, save='_markers_clusters.png')

# Annotation guess (simple check for markers)
# Erythroid: HBA1, HBB
# HSC/Progenitor: CD34
# T-cells: CD3D, CD3E, CD4, CD8A
# B-cells: CD79A, CD19
# Monocytes: CD14, LYZ
# NK: NKG7
marker_genes = ['HBA1', 'HBB', 'CD34', 'CD3D', 'CD3E', 'CD79A', 'CD19', 'CD14', 'LYZ', 'NKG7']
available_markers = [g for g in marker_genes if g in adata.var_names]
if available_markers:
    sc.pl.umap(adata, color=['leiden', 'condition'] + available_markers, show=False, save='_umap_markers.png')

# DE Analysis BM vs BT
print("Performing Differential Expression BM vs BT...")
# We perform this analysis to find genes up/down in BT compared to BM
sc.tl.rank_genes_groups(adata, 'condition', method='wilcoxon', groups=['BT'], reference='BM')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, show=False, save='_BM_vs_BT_DEG.png')

# Export significant DEGs
result = adata.uns['rank_genes_groups']
groups = result['names'].dtype.names
dfs = []
for group in groups:
    # rank_genes_groups can produce structured arrays
    gene_names = result['names'][group]
    logfc = result['logfoldchanges'][group]
    pvals = result['pvals'][group]
    pvals_adj = result['pvals_adj'][group]
    
    df = pd.DataFrame({
        'gene': gene_names,
        'log2fc': logfc,
        'pval': pvals,
        'pval_adj': pvals_adj
    })
    df['comparison_group'] = group
    dfs.append(df)

if dfs:
    degs = pd.concat(dfs)
    output_csv = os.path.join(results_dir, 'BM_vs_BT_DEGs.csv')
    degs.to_csv(output_csv, index=False)
    print(f"Saved DEGs to {output_csv}")
    
    # Let's print the top 10 DEGs for the log
    print("\nTop 10 Upregulated Genes in BT (vs BM):")
    print(degs.sort_values('log2fc', ascending=False).head(10))
    
    print("\nTop 10 Downregulated Genes in BT (vs BM):")
    print(degs.sort_values('log2fc', ascending=True).head(10))

print("Analysis Complete.")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
