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
import matplotlib.pyplot as plt
import seaborn as sns
import scanorama
import os
import gseapy as gp

# 1. Setup
OUTPUT_DIR = "tests/results_analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)
sc.settings.figdir = OUTPUT_DIR
sc.set_figure_params(dpi=150, frameon=False, figsize=(6, 6))

DATA_DIR = "tests/scRNAsedata"
SAMPLES = {
    "BM1": {"path": os.path.join(DATA_DIR, "GSM3901485_BM1"), "condition": "BM"},
    "BM2": {"path": os.path.join(DATA_DIR, "GSM3901486_BM2"), "condition": "BM"},
    "BM3": {"path": os.path.join(DATA_DIR, "GSM3901487_BM3"), "condition": "BM"},
    "BT1": {"path": os.path.join(DATA_DIR, "GSM3901489_BT1"), "condition": "BT"},
    "BT2": {"path": os.path.join(DATA_DIR, "GSM3901490_BT2"), "condition": "BT"},
    "BT3": {"path": os.path.join(DATA_DIR, "GSM3901491_BT3"), "condition": "BT"},
}

print("Starting analysis...")

# 2. Data Loading
adatas = []
for sample_name, info in SAMPLES.items():
    print(f"Loading {sample_name}...")
    try:
        adata = sc.read_10x_mtx(info["path"], var_names='gene_symbols', cache=False)
        adata.var_names_make_unique()
        adata.obs['sample_id'] = sample_name
        adata.obs['condition'] = info["condition"]
        adatas.append(adata)
    except Exception as e:
        print(f"Error loading {sample_name}: {e}")

if not adatas:
    raise ValueError("No data loaded!")

# Concatenate (outer join to keep all genes initially, though intersection is usually safer for integration)
adata = sc.concat(adatas, join='outer')
adata.var_names_make_unique()
print(f"Combined data shape: {adata.shape}")

# 3. Quality Control
print("Performing QC...")
adata.var['mt'] = adata.var_names.str.startswith('MT-')
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)

# Plot QC (Save)
sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
             jitter=0.4, multi_panel=True, show=False)
plt.savefig(os.path.join(OUTPUT_DIR, "qc_violin.png"))
plt.close()

# Filtering
print("Filtering cells...")
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
adata = adata[adata.obs.n_genes_by_counts < 6000, :]
adata = adata[adata.obs.pct_counts_mt < 15, :]
print(f"Data shape after filtering: {adata.shape}")

# 4. Normalization & Log
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
adata.raw = adata # Save raw normalized data

# 5. Feature Selection
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
# Create a subset for integration, but keep full data for annotation
adata_hvg = adata[:, adata.var.highly_variable].copy()
print(f"Highly variable genes: {adata_hvg.shape[1]}")

# 6. Integration (Scanorama)
print("Running Scanorama integration on HVGs...")
adata_hvg.obs['batch'] = adata_hvg.obs['sample_id']
batches = adata_hvg.obs['batch'].unique().tolist()
alldata = {}
for batch in batches:
    alldata[batch] = adata_hvg[adata_hvg.obs['batch'] == batch, :].copy()

adatas_list = [alldata[b] for b in batches]

# correct_scanpy returns a list of corrected AnnData objects
corrected_adatas = scanorama.correct_scanpy(adatas_list, return_dimred=True)

# Concatenate back to get the embedding in the right order
# CAUTION: We must ensure the order matches 'adata'.
# Best way: concatenate the corrected_adatas (which are the hvg subsets) and map to adata.
adata_integrated_hvg = sc.concat(corrected_adatas, join='outer', index_unique='-')

# Map embedding back to main adata
# We need to make sure indices match. sc.concat with index_unique='-' modifies indices.
# We should apply the same index modification to our main 'adata' or rely on order if stable.
# 'scanorama' preserves order within batches. 'sc.concat' preserves order of list.
# So if we concat 'adata' similarly, it should match.

# Let's rebuild the main 'adata' from split batches to ensure perfect alignment
# (Since we haven't split the main 'adata' yet, we can just split it now)
adata.obs['batch'] = adata.obs['sample_id']
alldata_full = {}
for batch in batches:
    alldata_full[batch] = adata[adata.obs['batch'] == batch, :].copy()

adatas_list_full = [alldata_full[b] for b in batches]
adata_full_ordered = sc.concat(adatas_list_full, join='outer', index_unique='-')

# Now verify shapes match
if adata_full_ordered.n_obs != adata_integrated_hvg.n_obs:
    raise ValueError("Observation mismatch between Full and Integrated data")

# Transfer embedding
adata_full_ordered.obsm['X_scanorama'] = adata_integrated_hvg.obsm['X_scanorama']
adata_integrated = adata_full_ordered # Rename for compatibility with rest of script

print(f"Integrated shape (full genes): {adata_integrated.shape}")
print(f"Obsm keys: {adata_integrated.obsm.keys()}")

# 7. Embedding & Clustering
print("Calculating embeddings...")
sc.pp.neighbors(adata_integrated, use_rep='X_scanorama')
sc.tl.umap(adata_integrated)
sc.tl.leiden(adata_integrated, resolution=0.5)

# Plot UMAP by condition and cluster
sc.pl.umap(adata_integrated, color=['condition', 'leiden'], show=False)
plt.savefig(os.path.join(OUTPUT_DIR, "umap_condition_leiden.png"))
plt.close()

# 8. Annotation (Automated Scoring)
print("Annotating cell types...")
marker_genes = {
    'Erythroid': ['HBA1', 'HBB', 'AHSP', 'ALAS2', 'HBM'],
    'HSC_Progenitor': ['CD34', 'SPINK2', 'PROM1'],
    'Myeloid': ['CD14', 'LYZ', 'CST3', 'MPO', 'ELANE'],
    'B_Cell': ['CD79A', 'MS4A1', 'CD19'],
    'T_Cell': ['CD3D', 'CD3E', 'CD2', 'TRAC'],
    'MK': ['PPBP', 'PF4']
}

# Calculate scores
for ct, markers in marker_genes.items():
    # Check which markers are in var_names
    valid_markers = [m for m in markers if m in adata_integrated.var_names]
    if valid_markers:
        sc.tl.score_genes(adata_integrated, valid_markers, score_name=f'score_{ct}')

# Assign max score
score_cols = [f'score_{ct}' for ct in marker_genes.keys()]
def get_max_score_type(row):
    scores = row[score_cols]
    if scores.max() < 0.1: # Threshold for unassigned
        return 'Unknown'
    return scores.idxmax().replace('score_', '')

adata_integrated.obs['cell_type'] = adata_integrated.obs.apply(get_max_score_type, axis=1)

# Plot annotated UMAP
sc.pl.umap(adata_integrated, color='cell_type', show=False)
plt.savefig(os.path.join(OUTPUT_DIR, "umap_annotated.png"))
plt.close()

# 9. Statistics (Cell Counts)
print("Calculating statistics...")
stats_df = adata_integrated.obs.groupby(['condition', 'cell_type'], observed=False).size().reset_index(name='count')
# Calculate percentages
total_counts = adata_integrated.obs.groupby('condition', observed=False).size().reset_index(name='total')
stats_df = stats_df.merge(total_counts, on='condition')
stats_df['percentage'] = (stats_df['count'] / stats_df['total']) * 100

print(stats_df)
stats_df.to_csv(os.path.join(OUTPUT_DIR, "cell_type_stats.csv"))

# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=stats_df, x='cell_type', y='percentage', hue='condition')
plt.title("Cell Type Distribution BM vs BT")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "cell_type_distribution.png"))
plt.close()

# 10. Differential Expression (Erythroid Focus)
print("Running Differential Expression on Erythroid cells...")
erythroid_adata = adata_integrated[adata_integrated.obs['cell_type'] == 'Erythroid'].copy()

# Filter low expressed genes for DE to speed up and reduce noise
# (Using the raw counts or log-normalized counts? DE uses .raw usually or X if normalized)
# Rank genes groups uses .X by default. Our .X is normalized and log transformed (but filtered for HVG).
# We should probably use the full gene set for DE if possible, but for speed and memory in this demo, HVG is okay.
# Actually, let's restore the raw data if we want full genome DE, but we only have HVG in `adata_integrated`.
# We saved `adata.raw` earlier. We can map `erythroid_adata` back to `adata.raw` if needed, but indices changed.
# For this prototype, we'll stick to the HVG set in `adata_integrated`.

if erythroid_adata.n_obs > 10:
    try:
        sc.tl.rank_genes_groups(erythroid_adata, groupby='condition', groups=['BT'], reference='BM', method='wilcoxon')
        
        # Extract DE results
        result = erythroid_adata.uns['rank_genes_groups']
        groups = result['names'].dtype.names
        de_df = pd.DataFrame({
            group + '_' + key: result[key][group]
            for group in groups for key in ['names', 'pvals_adj', 'logfoldchanges']
        })
        de_df.to_csv(os.path.join(OUTPUT_DIR, "DE_Erythroid_BT_vs_BM.csv"))
        
        # Get top upregulated genes in BT for Pathway Analysis
        # Filter for significant and positive LFC
        top_genes = de_df[ (de_df['BT_pvals_adj'] < 0.05) & (de_df['BT_logfoldchanges'] > 0.5) ]['BT_names'].tolist()
        
        print(f"Found {len(top_genes)} upregulated genes in Erythroid BT.")

        # 11. Pathway Analysis
        if len(top_genes) > 5:
            print("Running Pathway Enrichment...")
            enr = gp.enrichr(gene_list=top_genes,
                             gene_sets='GO_Biological_Process_2021',
                             organism='human', 
                             outdir=os.path.join(OUTPUT_DIR, "enrichr_results"))
            
            # Plot dotplot
            try:
                from gseapy import dotplot
                ax = dotplot(enr.res2d, title='GO Biological Process (Erythroid BT up)', cmap='viridis_r')
                plt.savefig(os.path.join(OUTPUT_DIR, "pathway_dotplot.png"))
                plt.close()
            except Exception as e:
                print(f"Could not plot pathway results: {e}")
        else:
            print("Not enough DE genes for pathway analysis.")
            
    except Exception as e:
        print(f"DE Analysis failed: {e}")
else:
    print("Not enough Erythroid cells for DE.")

print("Analysis Complete.")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
