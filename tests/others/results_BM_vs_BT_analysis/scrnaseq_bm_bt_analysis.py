# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

#!/usr/bin/env python3
"""
Single-Cell RNA-seq Analysis Pipeline: Normal Bone Marrow (BM) vs Beta-Thalassemia (BT)
Dataset: GSE133181

This pipeline performs comprehensive analysis including:
1. Data loading and QC filtering
2. Integration using scVI
3. Clustering and cell type annotation
4. Differential expression analysis (BM vs BT)
5. Pathway enrichment analysis
6. Visualization and export

Author: AI-assisted analysis
Date: 2024
"""

import os
import sys
import warnings
import numpy as np
import pandas as pd
import scanpy as sc
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import sparse
from scipy.stats import median_abs_deviation
import anndata as ad

warnings.filterwarnings('ignore')

# Set plotting parameters
sc.settings.verbosity = 3
sc.settings.set_figure_params(dpi=150, facecolor='white', frameon=False)
plt.rcParams['figure.figsize'] = (8, 6)

# ============================================================================
# CONFIGURATION
# ============================================================================
DATA_DIR = "/media/drdx/mystorage/ARTIFICIALINTELLIGENCEGROUP/skills/tests/scRNAseqdata/GSE133181_RAW"
OUTPUT_DIR = "/media/drdx/mystorage/ARTIFICIALINTELLIGENCEGROUP/skills/tests/results_BM_vs_BT_analysis"

SAMPLES = {
    "GSM3901485_BM1": {"condition": "BM", "name": "BM1"},
    "GSM3901486_BM2": {"condition": "BM", "name": "BM2"},
    "GSM3901487_BM3": {"condition": "BM", "name": "BM3"},
    "GSM3901489_BT1": {"condition": "BT", "name": "BT1"},
    "GSM3901490_BT2": {"condition": "BT", "name": "BT2"},
    "GSM3901491_BT3": {"condition": "BT", "name": "BT3"},
}

# QC Parameters (MAD-based adaptive filtering)
QC_PARAMS = {
    "min_genes": 200,          # Minimum genes per cell
    "min_cells": 20,           # Minimum cells per gene
    "max_mt_pct": 15,          # Maximum mitochondrial percentage
    "mad_n_genes_by_counts": 5,
    "mad_total_counts": 5,
    "mad_pct_mt": 3,
}

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# FUNCTIONS
# ============================================================================

def load_10x_sample(sample_path, sample_name):
    """Load 10x Genomics data from matrix market format."""
    print(f"Loading {sample_name}...")

    # Try GRCh38 subfolder first (standard 10x output)
    grch38_path = os.path.join(sample_path, "GRCh38")
    if os.path.exists(grch38_path):
        sample_path = grch38_path

    # Read using scanpy
    adata = sc.read_10x_mtx(
        sample_path,
        var_names='gene_symbols',
        cache=True
    )

    # Make var names unique
    adata.var_names_make_unique()

    print(f"  Loaded {adata.n_obs} cells x {adata.n_vars} genes")
    return adata


def calculate_qc_metrics(adata):
    """Calculate QC metrics for single-cell data."""
    # Mitochondrial genes
    adata.var['mt'] = adata.var_names.str.startswith(('MT-', 'mt-'))
    # Ribosomal genes
    adata.var['ribo'] = adata.var_names.str.startswith(('RPS', 'RPL', 'Rps', 'Rpl'))
    # Hemoglobin genes
    adata.var['hb'] = adata.var_names.str.contains('^HB[^(P)]|^Hb[^(p)]', regex=True)

    # Calculate QC metrics
    sc.pp.calculate_qc_metrics(
        adata,
        qc_vars=['mt', 'ribo', 'hb'],
        percent_top=None,
        log1p=False,
        inplace=True
    )

    return adata


def detect_outliers_mad(adata, metric, nmads=5):
    """Detect outliers using MAD (Median Absolute Deviation)."""
    M = adata.obs[metric]
    median = np.median(M)
    mad = median_abs_deviation(M)

    # Define bounds
    lower = median - nmads * mad
    upper = median + nmads * mad

    # Identify outliers
    outliers = (M < lower) | (M > upper)

    return outliers


def filter_cells_adaptive(adata, params):
    """Apply adaptive MAD-based filtering."""
    print("\nFiltering cells...")
    initial_cells = adata.n_obs

    # Basic filters
    sc.pp.filter_cells(adata, min_genes=params['min_genes'])
    sc.pp.filter_genes(adata, min_cells=params['min_cells'])

    # MAD-based outlier detection
    outlier_genes = detect_outliers_mad(adata, 'n_genes_by_counts', params['mad_n_genes_by_counts'])
    outlier_counts = detect_outliers_mad(adata, 'total_counts', params['mad_total_counts'])
    outlier_mt = detect_outliers_mad(adata, 'pct_counts_mt', params['mad_pct_mt'])

    # Combined filter with hard MT threshold
    adata = adata[
        ~outlier_genes &
        ~outlier_counts &
        ~outlier_mt &
        (adata.obs['pct_counts_mt'] < params['max_mt_pct'])
    ].copy()

    final_cells = adata.n_obs
    print(f"  Filtered: {initial_cells} -> {final_cells} cells ({100*final_cells/initial_cells:.1f}% retained)")

    return adata


def plot_qc_violin(adata, output_path):
    """Create QC violin plots."""
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))

    metrics = ['n_genes_by_counts', 'total_counts', 'pct_counts_mt', 'pct_counts_ribo']
    titles = ['Genes per Cell', 'UMI Counts', 'Mitochondrial %', 'Ribosomal %']

    for ax, metric, title in zip(axes, metrics, titles):
        sc.pl.violin(adata, metric, groupby='condition', ax=ax, show=False,
                     palette={'BM': '#3498db', 'BT': '#e74c3c'})
        ax.set_title(title)
        ax.set_xlabel('')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved QC violin plot: {output_path}")


def integrate_with_scvi(adata, batch_key='sample'):
    """Integrate samples using scVI."""
    print("\nPerforming scVI integration...")

    import scvi

    # Prepare data
    adata_copy = adata.copy()

    # Select highly variable genes
    sc.pp.highly_variable_genes(
        adata_copy,
        n_top_genes=3000,
        subset=False,
        flavor='seurat_v3',
        batch_key=batch_key
    )

    # Setup scVI model
    scvi.model.SCVI.setup_anndata(
        adata_copy,
        batch_key=batch_key,
        layer=None,
    )

    # Train model
    model = scvi.model.SCVI(
        adata_copy,
        n_layers=2,
        n_latent=30,
        gene_likelihood='nb'
    )

    model.train(
        max_epochs=200,
        early_stopping=True,
        early_stopping_patience=10,
        plan_kwargs={'lr': 1e-3}
    )

    # Get latent representation
    adata.obsm['X_scVI'] = model.get_latent_representation()

    # Store model for later use
    model.save(os.path.join(OUTPUT_DIR, "scvi_model"), overwrite=True)

    print("  scVI integration complete!")
    return adata, model


def cluster_and_embed(adata):
    """Perform clustering and dimensionality reduction."""
    print("\nClustering and embedding...")

    # Neighbors using scVI latent space
    sc.pp.neighbors(adata, use_rep='X_scVI', n_neighbors=15, n_pcs=30)

    # UMAP
    sc.tl.umap(adata, min_dist=0.3)

    # Leiden clustering at multiple resolutions
    for res in [0.3, 0.5, 0.8, 1.0]:
        sc.tl.leiden(adata, resolution=res, key_added=f'leiden_{res}')

    # Use resolution 0.5 as default
    adata.obs['leiden'] = adata.obs['leiden_0.5']

    print(f"  Found {adata.obs['leiden'].nunique()} clusters at resolution 0.5")
    return adata


def find_marker_genes(adata, groupby='leiden', n_genes=100):
    """Find marker genes for each cluster."""
    print(f"\nFinding marker genes by {groupby}...")

    # Use normalized data for DEG
    sc.tl.rank_genes_groups(
        adata,
        groupby=groupby,
        method='wilcoxon',
        n_genes=n_genes,
        use_raw=False
    )

    return adata


def differential_expression_condition(adata, condition_col='condition',
                                       control='BM', treatment='BT'):
    """Perform differential expression between conditions."""
    print(f"\nDifferential Expression: {treatment} vs {control}...")

    # Create results dataframe
    results = []

    # Per cell type DEG
    for cell_type in adata.obs['cell_type'].unique():
        print(f"  Analyzing {cell_type}...")

        # Subset to cell type
        mask = adata.obs['cell_type'] == cell_type
        adata_sub = adata[mask].copy()

        if adata_sub.obs[condition_col].nunique() < 2:
            continue

        # Check minimum cells per condition
        counts = adata_sub.obs[condition_col].value_counts()
        if counts.min() < 10:
            continue

        # Run DEG
        sc.tl.rank_genes_groups(
            adata_sub,
            groupby=condition_col,
            groups=[treatment],
            reference=control,
            method='wilcoxon',
            n_genes=adata_sub.n_vars
        )

        # Extract results
        deg_df = sc.get.rank_genes_groups_df(adata_sub, group=treatment)
        deg_df['cell_type'] = cell_type
        results.append(deg_df)

    # Combine all results
    if results:
        deg_all = pd.concat(results, ignore_index=True)
        deg_all['abs_logfoldchange'] = deg_all['logfoldchanges'].abs()

        # Significant DEGs (adjusted p < 0.05, |logFC| > 0.5)
        deg_sig = deg_all[
            (deg_all['pvals_adj'] < 0.05) &
            (deg_all['abs_logfoldchange'] > 0.5)
        ].copy()

        print(f"  Found {len(deg_sig)} significant DEGs across all cell types")
        return deg_all, deg_sig

    return pd.DataFrame(), pd.DataFrame()


def global_deg_analysis(adata, condition_col='condition', control='BM', treatment='BT'):
    """Perform global differential expression analysis (all cells)."""
    print(f"\nGlobal DEG Analysis: {treatment} vs {control}...")

    # Create a copy for DEG analysis
    adata_deg = adata.copy()

    # Run DEG
    sc.tl.rank_genes_groups(
        adata_deg,
        groupby=condition_col,
        groups=[treatment],
        reference=control,
        method='wilcoxon',
        n_genes=adata_deg.n_vars,
        pts=True  # Include percentage of cells expressing
    )

    # Extract results
    deg_df = sc.get.rank_genes_groups_df(adata_deg, group=treatment)
    deg_df['abs_logfoldchange'] = deg_df['logfoldchanges'].abs()

    # Add percentage expressing
    try:
        pts_df = pd.DataFrame(adata_deg.uns['rank_genes_groups']['pts'])
        deg_df = deg_df.merge(pts_df, left_on='names', right_index=True, how='left')
    except:
        pass

    # Significant DEGs
    deg_sig = deg_df[
        (deg_df['pvals_adj'] < 0.05) &
        (deg_df['abs_logfoldchange'] > 0.5)
    ].copy()

    deg_up = deg_sig[deg_sig['logfoldchanges'] > 0]
    deg_down = deg_sig[deg_sig['logfoldchanges'] < 0]

    print(f"  Total DEGs: {len(deg_sig)} (Up in BT: {len(deg_up)}, Down in BT: {len(deg_down)})")

    return deg_df, deg_sig


def pathway_analysis(deg_df, output_dir, top_n=500):
    """Perform pathway enrichment analysis using gseapy."""
    print("\nPerforming pathway enrichment analysis...")

    try:
        import gseapy as gp
    except ImportError:
        print("  gseapy not installed. Skipping pathway analysis.")
        return None

    results = {}

    # Get up and down-regulated genes
    deg_up = deg_df[
        (deg_df['pvals_adj'] < 0.05) &
        (deg_df['logfoldchanges'] > 0.5)
    ]['names'].tolist()[:top_n]

    deg_down = deg_df[
        (deg_df['pvals_adj'] < 0.05) &
        (deg_df['logfoldchanges'] < -0.5)
    ]['names'].tolist()[:top_n]

    gene_sets = [
        'GO_Biological_Process_2021',
        'GO_Molecular_Function_2021',
        'GO_Cellular_Component_2021',
        'KEGG_2021_Human',
        'Reactome_2022',
        'WikiPathways_2019_Human',
        'MSigDB_Hallmark_2020'
    ]

    for direction, genes in [('upregulated', deg_up), ('downregulated', deg_down)]:
        if len(genes) < 10:
            print(f"  Skipping {direction} (only {len(genes)} genes)")
            continue

        print(f"  Enrichment for {direction} genes ({len(genes)} genes)...")

        try:
            enr = gp.enrichr(
                gene_list=genes,
                gene_sets=gene_sets,
                organism='human',
                outdir=None,
                no_plot=True
            )

            results[direction] = enr.results

            # Save results
            enr.results.to_csv(
                os.path.join(output_dir, f'pathway_enrichment_{direction}.csv'),
                index=False
            )

        except Exception as e:
            print(f"    Error: {e}")

    return results


def plot_pathway_dotplot(enrichment_results, output_path, top_n=15):
    """Create dotplot for pathway enrichment results."""
    fig, axes = plt.subplots(1, 2, figsize=(16, 10))

    for ax, (direction, df) in zip(axes, enrichment_results.items()):
        if df is None or len(df) == 0:
            continue

        # Filter significant and top results
        df_sig = df[df['Adjusted P-value'] < 0.05].head(top_n)

        if len(df_sig) == 0:
            continue

        # Create dotplot
        df_sig['-log10(adj_pval)'] = -np.log10(df_sig['Adjusted P-value'].clip(lower=1e-300))
        df_sig['Gene_Ratio'] = df_sig['Overlap'].apply(
            lambda x: int(x.split('/')[0]) / int(x.split('/')[1]) if '/' in str(x) else 0
        )

        scatter = ax.scatter(
            df_sig['Gene_Ratio'],
            range(len(df_sig)),
            s=df_sig['-log10(adj_pval)'] * 10,
            c=df_sig['-log10(adj_pval)'],
            cmap='viridis',
            alpha=0.7
        )

        ax.set_yticks(range(len(df_sig)))
        ax.set_yticklabels(df_sig['Term'].str[:50])
        ax.set_xlabel('Gene Ratio')
        ax.set_title(f'{direction.capitalize()} in BT vs BM')

        plt.colorbar(scatter, ax=ax, label='-log10(adj. p-value)')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved pathway dotplot: {output_path}")


def plot_umap_panels(adata, output_dir):
    """Create UMAP visualization panels."""

    # UMAP by condition and clusters
    fig, axes = plt.subplots(2, 2, figsize=(14, 14))

    sc.pl.umap(adata, color='condition', ax=axes[0, 0], show=False,
               palette={'BM': '#3498db', 'BT': '#e74c3c'}, title='Condition')
    sc.pl.umap(adata, color='sample', ax=axes[0, 1], show=False, title='Sample')
    sc.pl.umap(adata, color='leiden', ax=axes[1, 0], show=False, title='Leiden Clusters')
    sc.pl.umap(adata, color='cell_type', ax=axes[1, 1], show=False, title='Cell Types')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'umap_overview.png'), dpi=150, bbox_inches='tight')
    plt.close()

    # Cell type specific
    fig, ax = plt.subplots(figsize=(12, 10))
    sc.pl.umap(adata, color='cell_type', ax=ax, show=False,
               legend_loc='on data', legend_fontsize=8)
    plt.savefig(os.path.join(output_dir, 'umap_cell_types.png'), dpi=150, bbox_inches='tight')
    plt.close()

    print(f"Saved UMAP plots to {output_dir}")


def plot_cell_type_composition(adata, output_path):
    """Plot cell type composition by condition."""
    # Calculate proportions
    composition = pd.crosstab(
        adata.obs['cell_type'],
        adata.obs['condition'],
        normalize='columns'
    ) * 100

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Stacked bar plot
    composition.T.plot(kind='bar', stacked=True, ax=axes[0], colormap='tab20')
    axes[0].set_xlabel('Condition')
    axes[0].set_ylabel('Cell Type Proportion (%)')
    axes[0].set_title('Cell Type Composition by Condition')
    axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0)

    # Heatmap
    sns.heatmap(composition, annot=True, fmt='.1f', cmap='YlOrRd', ax=axes[1])
    axes[1].set_title('Cell Type Proportion Heatmap (%)')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved composition plot: {output_path}")


def annotate_cell_types_bayesian(adata, markers_dict):
    """Annotate cell types using marker-based scoring."""
    print("\nAnnotating cell types...")

    # Score each cell type
    for cell_type, markers in markers_dict.items():
        # Get genes that exist in the dataset
        valid_markers = [g for g in markers if g in adata.var_names]
        if len(valid_markers) > 0:
            sc.tl.score_genes(adata, valid_markers, score_name=f'score_{cell_type}')

    # Get all score columns
    score_cols = [c for c in adata.obs.columns if c.startswith('score_')]

    if not score_cols:
        print("  No valid markers found. Using leiden clusters as cell types.")
        adata.obs['cell_type'] = 'Cluster_' + adata.obs['leiden'].astype(str)
        return adata

    # Assign cell type based on highest score per cell
    scores_df = adata.obs[score_cols]
    cell_types = scores_df.idxmax(axis=1).str.replace('score_', '')
    adata.obs['cell_type'] = cell_types

    # Refine by cluster majority vote
    cluster_cell_types = {}
    for cluster in adata.obs['leiden'].unique():
        mask = adata.obs['leiden'] == cluster
        majority = adata.obs.loc[mask, 'cell_type'].mode()[0]
        cluster_cell_types[cluster] = majority

    adata.obs['cell_type'] = adata.obs['leiden'].map(cluster_cell_types)

    print(f"  Annotated {adata.obs['cell_type'].nunique()} cell types")
    return adata


# ============================================================================
# BONE MARROW CELL TYPE MARKERS
# ============================================================================

BONE_MARROW_MARKERS = {
    # Hematopoietic Stem/Progenitor Cells
    'HSC': ['CD34', 'KIT', 'THY1', 'PROM1', 'CRHBP', 'HLF', 'AVP', 'MLLT3'],
    'HSPC': ['CD34', 'CD38', 'FLT3', 'PTPRC', 'KIT', 'SPN'],
    'MPP': ['CD34', 'FLT3', 'MPO', 'ELANE'],

    # Erythroid lineage
    'Erythroid_Early': ['GATA1', 'KLF1', 'TFRC', 'EPOR', 'CD36', 'GYPA'],
    'Erythroid': ['HBB', 'HBA1', 'HBA2', 'GYPA', 'ALAS2', 'ANK1', 'SLC4A1'],
    'Erythroid_Late': ['HBB', 'HBA1', 'HBA2', 'SPTA1', 'EPB42', 'RHAG'],

    # Myeloid lineage
    'GMP': ['CD34', 'MPO', 'ELANE', 'AZU1', 'PRTN3'],
    'Neutrophil': ['ELANE', 'MPO', 'PRTN3', 'CTSG', 'AZU1', 'LCN2', 'S100A8', 'S100A9'],
    'Monocyte': ['CD14', 'LYZ', 'CST3', 'VCAN', 'FCN1', 'S100A8', 'S100A9'],
    'Macrophage': ['CD68', 'CD163', 'MRC1', 'MSR1', 'MARCO', 'C1QA', 'C1QB'],
    'Dendritic': ['CD1C', 'FCER1A', 'CLEC10A', 'CD86', 'HLA-DRA', 'ITGAX'],
    'pDC': ['IL3RA', 'CLEC4C', 'NRP1', 'TCF4', 'IRF7', 'IRF8'],
    'Mast': ['TPSAB1', 'CPA3', 'KIT', 'MS4A2', 'HDC'],
    'Basophil': ['CLC', 'HDC', 'GATA2', 'MS4A2'],
    'Eosinophil': ['CLC', 'EPX', 'PRG2', 'RNASE2', 'RNASE3'],

    # Megakaryocyte lineage
    'MEP': ['GATA1', 'ITGA2B', 'PF4', 'GP9'],
    'Megakaryocyte': ['ITGA2B', 'GP9', 'PF4', 'PPBP', 'GP1BA', 'TUBB1', 'TREML1'],
    'Platelet': ['PF4', 'PPBP', 'GP9', 'ITGA2B'],

    # Lymphoid lineage
    'CLP': ['CD34', 'IL7R', 'FLT3', 'DNTT'],
    'T_Cell': ['CD3D', 'CD3E', 'CD3G', 'TRAC', 'CD4', 'CD8A', 'CD8B'],
    'CD4_T': ['CD3D', 'CD4', 'IL7R', 'TCF7', 'LEF1'],
    'CD8_T': ['CD3D', 'CD8A', 'CD8B', 'GZMK', 'GZMB'],
    'NK': ['NCAM1', 'NKG7', 'GNLY', 'KLRD1', 'KLRF1', 'KLRB1', 'PRF1'],
    'B_Cell': ['CD79A', 'CD79B', 'MS4A1', 'CD19', 'PAX5', 'BANK1', 'IGHM'],
    'Pro_B': ['CD34', 'CD79A', 'VPREB1', 'IGLL1', 'RAG1', 'RAG2', 'DNTT'],
    'Pre_B': ['CD79A', 'VPREB1', 'IGLL1', 'CD19', 'PAX5'],
    'Plasma': ['JCHAIN', 'MZB1', 'SDC1', 'TNFRSF17', 'XBP1', 'PRDM1'],

    # Stromal cells
    'MSC': ['CXCL12', 'LEPR', 'KITLG', 'VCAM1', 'PDGFRA', 'THY1'],
    'Stromal': ['COL1A1', 'COL1A2', 'DCN', 'LUM', 'PDGFRA', 'PDGFRB'],
    'Endothelial': ['PECAM1', 'VWF', 'CDH5', 'KDR', 'FLT1', 'EMCN'],
    'Adipocyte': ['ADIPOQ', 'PPARG', 'LEP', 'FABP4', 'PLIN1'],
}


# ============================================================================
# MAIN ANALYSIS PIPELINE
# ============================================================================

def main():
    print("="*80)
    print("Single-Cell RNA-seq Analysis: BM vs BT (GSE133181)")
    print("="*80)

    # -------------------------------------------------------------------------
    # 1. LOAD DATA
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 1: Loading Data")
    print("="*40)

    adatas = []
    for sample_id, info in SAMPLES.items():
        sample_path = os.path.join(DATA_DIR, sample_id)
        adata = load_10x_sample(sample_path, info['name'])
        adata.obs['sample'] = info['name']
        adata.obs['condition'] = info['condition']
        adatas.append(adata)

    # Concatenate
    adata = ad.concat(adatas, join='outer', label='sample', index_unique='-')
    adata.obs_names_make_unique()
    print(f"\nCombined dataset: {adata.n_obs} cells x {adata.n_vars} genes")

    # -------------------------------------------------------------------------
    # 2. QUALITY CONTROL
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 2: Quality Control")
    print("="*40)

    # Calculate QC metrics
    adata = calculate_qc_metrics(adata)

    # Plot pre-filter QC
    plot_qc_violin(adata, os.path.join(OUTPUT_DIR, 'qc_prefilter.png'))

    # Apply filtering
    adata = filter_cells_adaptive(adata, QC_PARAMS)

    # Plot post-filter QC
    plot_qc_violin(adata, os.path.join(OUTPUT_DIR, 'qc_postfilter.png'))

    # Save filtered counts for later
    adata.layers['counts'] = adata.X.copy()

    # -------------------------------------------------------------------------
    # 3. NORMALIZATION
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 3: Normalization")
    print("="*40)

    # Log-normalize
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)

    # Store normalized data
    adata.raw = adata.copy()

    # Highly variable genes
    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=3000,
        flavor='seurat_v3',
        batch_key='sample',
        subset=False
    )

    print(f"  Identified {adata.var['highly_variable'].sum()} highly variable genes")

    # Plot HVG
    sc.pl.highly_variable_genes(adata, show=False, save='_selection.png')
    # Move scanpy's output to our directory
    import shutil
    hvg_src = os.path.join(sc.settings.figdir, 'filter_genes_dispersion_selection.png')
    if os.path.exists(hvg_src):
        shutil.move(hvg_src, os.path.join(OUTPUT_DIR, 'hvg_selection.png'))

    # -------------------------------------------------------------------------
    # 4. INTEGRATION
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 4: Integration (scVI)")
    print("="*40)

    try:
        adata, model = integrate_with_scvi(adata)
    except ImportError:
        print("  scVI not available. Using PCA instead.")
        sc.pp.scale(adata, max_value=10)
        sc.tl.pca(adata, n_comps=50)
        adata.obsm['X_scVI'] = adata.obsm['X_pca'][:, :30]

    # -------------------------------------------------------------------------
    # 5. CLUSTERING
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 5: Clustering and Embedding")
    print("="*40)

    adata = cluster_and_embed(adata)

    # -------------------------------------------------------------------------
    # 6. MARKER GENES
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 6: Finding Marker Genes")
    print("="*40)

    adata = find_marker_genes(adata, groupby='leiden')

    # Export marker genes for CellIdentifierDX
    marker_results = []
    for cluster in adata.obs['leiden'].unique():
        genes = sc.get.rank_genes_groups_df(adata, group=cluster)
        genes['Cluster'] = int(cluster)
        marker_results.append(genes)

    markers_df = pd.concat(marker_results)
    markers_df = markers_df.rename(columns={
        'names': 'Gene',
        'pvals_adj': 'Adjusted P-value',
        'logfoldchanges': 'Log2FoldChange',
        'scores': 'Score',
        'pvals': 'P-value'
    })
    markers_df.to_csv(os.path.join(OUTPUT_DIR, 'cluster_markers.csv'), index=False)

    # -------------------------------------------------------------------------
    # 7. CELL TYPE ANNOTATION
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 7: Cell Type Annotation")
    print("="*40)

    adata = annotate_cell_types_bayesian(adata, BONE_MARROW_MARKERS)

    # Plot UMAP
    plot_umap_panels(adata, OUTPUT_DIR)

    # Cell type composition
    plot_cell_type_composition(adata, os.path.join(OUTPUT_DIR, 'cell_type_composition.png'))

    # -------------------------------------------------------------------------
    # 8. DIFFERENTIAL EXPRESSION
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 8: Differential Expression Analysis")
    print("="*40)

    # Global DEG
    deg_all, deg_sig = global_deg_analysis(adata)
    deg_all.to_csv(os.path.join(OUTPUT_DIR, 'DEG_global_all.csv'), index=False)
    deg_sig.to_csv(os.path.join(OUTPUT_DIR, 'DEG_global_significant.csv'), index=False)

    # Per cell type DEG
    deg_celltype_all, deg_celltype_sig = differential_expression_condition(adata)
    if len(deg_celltype_all) > 0:
        deg_celltype_all.to_csv(os.path.join(OUTPUT_DIR, 'DEG_by_celltype_all.csv'), index=False)
        deg_celltype_sig.to_csv(os.path.join(OUTPUT_DIR, 'DEG_by_celltype_significant.csv'), index=False)

    # Volcano plot
    fig, ax = plt.subplots(figsize=(10, 8))
    deg_plot = deg_all.copy()
    deg_plot['significant'] = (deg_plot['pvals_adj'] < 0.05) & (deg_plot['abs_logfoldchange'] > 0.5)
    deg_plot['-log10_pval'] = -np.log10(deg_plot['pvals_adj'].clip(lower=1e-300))

    colors = ['#CCCCCC' if not sig else ('#e74c3c' if lfc > 0 else '#3498db')
              for sig, lfc in zip(deg_plot['significant'], deg_plot['logfoldchanges'])]

    ax.scatter(deg_plot['logfoldchanges'], deg_plot['-log10_pval'], c=colors, alpha=0.5, s=5)
    ax.axhline(-np.log10(0.05), ls='--', c='gray', alpha=0.5)
    ax.axvline(0.5, ls='--', c='gray', alpha=0.5)
    ax.axvline(-0.5, ls='--', c='gray', alpha=0.5)
    ax.set_xlabel('Log2 Fold Change (BT vs BM)')
    ax.set_ylabel('-log10(adjusted p-value)')
    ax.set_title('Differential Expression: BT vs BM')

    # Label top genes
    top_up = deg_plot[deg_plot['logfoldchanges'] > 0].nlargest(10, '-log10_pval')
    top_down = deg_plot[deg_plot['logfoldchanges'] < 0].nlargest(10, '-log10_pval')
    for _, row in pd.concat([top_up, top_down]).iterrows():
        ax.annotate(row['names'], (row['logfoldchanges'], row['-log10_pval']),
                    fontsize=6, alpha=0.8)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'volcano_plot.png'), dpi=150, bbox_inches='tight')
    plt.close()

    # -------------------------------------------------------------------------
    # 9. PATHWAY ANALYSIS
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 9: Pathway Enrichment Analysis")
    print("="*40)

    pathway_results = pathway_analysis(deg_all, OUTPUT_DIR)
    if pathway_results:
        plot_pathway_dotplot(pathway_results, os.path.join(OUTPUT_DIR, 'pathway_dotplot.png'))

    # -------------------------------------------------------------------------
    # 10. SAVE RESULTS
    # -------------------------------------------------------------------------
    print("\n" + "="*40)
    print("STEP 10: Saving Results")
    print("="*40)

    # Save annotated object
    adata.write(os.path.join(OUTPUT_DIR, 'adata_annotated.h5ad'))
    print(f"  Saved annotated data: {os.path.join(OUTPUT_DIR, 'adata_annotated.h5ad')}")

    # Save cell type summary
    cell_summary = adata.obs.groupby(['condition', 'cell_type']).size().unstack(fill_value=0)
    cell_summary.to_csv(os.path.join(OUTPUT_DIR, 'cell_type_counts.csv'))

    # Save sample summary
    sample_summary = adata.obs.groupby(['sample', 'condition']).agg({
        'n_genes_by_counts': ['mean', 'std'],
        'total_counts': ['mean', 'std'],
        'pct_counts_mt': ['mean', 'std']
    }).round(2)
    sample_summary.to_csv(os.path.join(OUTPUT_DIR, 'sample_qc_summary.csv'))

    print("\n" + "="*80)
    print("ANALYSIS COMPLETE!")
    print("="*80)
    print(f"\nResults saved to: {OUTPUT_DIR}")
    print(f"  - adata_annotated.h5ad: Full annotated dataset")
    print(f"  - DEG_global_significant.csv: Significant DEGs (BT vs BM)")
    print(f"  - DEG_by_celltype_significant.csv: Cell type-specific DEGs")
    print(f"  - pathway_enrichment_*.csv: Pathway analysis results")
    print(f"  - Various plots (PNG format)")

    return adata


if __name__ == "__main__":
    adata = main()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
