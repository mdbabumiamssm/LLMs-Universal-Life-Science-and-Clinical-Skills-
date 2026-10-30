# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

import sys
import os
import scanpy as sc
import pandas as pd
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# --- Setup Paths to Skills ---
PROJECT_ROOT = "/home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills"
ANNOTATOR_PATH = os.path.join(PROJECT_ROOT, "Skills/Genomics/Single_Cell/Cell_Type_Annotation/RNA")
PATHWAY_PATH = os.path.join(PROJECT_ROOT, "Skills/Genomics/Single_Cell/Pathway_Analysis")

sys.path.append(ANNOTATOR_PATH)
sys.path.append(PATHWAY_PATH)

try:
    from universal_annotator import UniversalAnnotator
    from sc_pathway_scorer import PathwayAnalyzer
    print("Successfully imported Genomics Skills.")
except ImportError as e:
    print(f"Error importing skills: {e}")
    sys.exit(1)

# --- Configuration ---
DATA_DIR = os.path.join(PROJECT_ROOT, "tests/scRNAsedata")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "tests/scRNA_analysis_results")
os.makedirs(OUTPUT_DIR, exist_ok=True)

sc.settings.figdir = OUTPUT_DIR
sc.set_figure_params(scanpy=True, dpi=100, dpi_save=300, format='png')

# --- 1. Data Loading ---
print("Loading data...")
samples = {
    "BM1": os.path.join(DATA_DIR, "GSM3901485_BM1"),
    "BM2": os.path.join(DATA_DIR, "GSM3901486_BM2"),
    "BM3": os.path.join(DATA_DIR, "GSM3901487_BM3")
}

adatas = []
for name, path in samples.items():
    print(f"Reading {name} from {path}...")
    try:
        # scanpy.read_10x_mtx expects the directory
        a = sc.read_10x_mtx(path, var_names='gene_symbols', cache=True)
        a.obs['sample'] = name
        a.var_names_make_unique()
        adatas.append(a)
    except Exception as e:
        print(f"Failed to read {name}: {e}")

if not adatas:
    print("No data loaded. Exiting.")
    sys.exit(1)

adata = sc.concat(adatas, join='outer')
adata.var_names_make_unique()
print(f"Combined dataset: {adata.n_obs} cells x {adata.n_vars} genes.")

# --- 2. Preprocessing ---
print("Preprocessing...")
# Filter cells/genes
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# Normalize
adata.layers["counts"] = adata.X.copy()
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# Highly Variable Genes
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
adata.raw = adata

# PCA & Neighbors
sc.pp.pca(adata, svd_solver='arpack')
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

# UMAP
sc.tl.umap(adata)

# Clustering
print("Clustering...")
try:
    sc.tl.leiden(adata)
except ImportError:
    print("Leiden not found, trying Louvain...")
    try:
        sc.tl.louvain(adata)
    except:
        print("Clustering failed (missing algorithms). Proceeding with UMAP only.")

# --- 3. Cell Type Annotation (Skill Usage) ---
print("Annotating Cell Types...")
annotator = UniversalAnnotator(adata)

# Marker Dictionary for Bone Marrow
bm_markers = {
    'HSC_Progenitors': ['CD34', 'SPINK2', 'MPO'],
    'Erythroid': ['HBA1', 'HBA2', 'HBB', 'ALAS2'],
    'B_Cells': ['CD79A', 'MS4A1', 'CD19'],
    'T_Cells': ['CD3D', 'CD3E', 'CD247'],
    'Monocytes': ['CD14', 'LYZ', 'FCN1'],
    'NK_Cells': ['GNLY', 'NKG7'],
    'Dendritic_Cells': ['CST3', 'HLA-DQA1']
}

annotator.annotate_marker_based(bm_markers)

# --- 4. Pathway Analysis (Skill Usage) ---
print("Performing Pathway Analysis...")
# Convert sparse to dense DataFrame for the scorer (might be slow for huge data, but ok for this demo)
# Using normalized data
if hasattr(adata.X, "todense"):
    expr_df = pd.DataFrame(adata.X.todense(), index=adata.obs_names, columns=adata.var_names)
else:
    expr_df = pd.DataFrame(adata.X, index=adata.obs_names, columns=adata.var_names)

pathway_scorer = PathwayAnalyzer(expr_df)

pathways = {
    'Cell_Cycle': ['MKI67', 'PCNA', 'TOP2A', 'CCNB1', 'MCM6'],
    'Interferon_Response': ['ISG15', 'IFI6', 'IFIT1', 'STAT1'],
    'Hypoxia': ['VEGFA', 'SLC2A1', 'LDHA', 'PGK1'],
    'Oxidative_Phosphorylation': ['MT-CO1', 'MT-CO2', 'MT-ATP6']
}

scores_df = pathway_scorer.score_pathways_aucell(pathways, top_k_rank=200)

# Add scores to adata
for col in scores_df.columns:
    adata.obs[col] = scores_df[col]

# --- 5. Visualization & Outputs ---
print("Generating Plots...")

# UMAP with Sample
sc.pl.umap(adata, color=['sample'], save='_batch.png', show=False)

# UMAP with Predicted Cell Type
if 'predicted_cell_type' in adata.obs:
    sc.pl.umap(adata, color=['predicted_cell_type'], save='_celltypes.png', show=False)
    # Filter markers for Dotplot
    valid_markers = {}
    for ct, genes in bm_markers.items():
        existing = [g for g in genes if g in adata.var_names]
        if existing:
            valid_markers[ct] = existing
    
    if valid_markers:
        sc.pl.dotplot(adata, valid_markers, groupby='predicted_cell_type', save='_markers.png', show=False)
    else:
        print("No valid markers found for dotplot.")

# UMAP with Pathway Scores
sc.pl.umap(adata, color=list(pathways.keys()), save='_pathways.png', show=False)

# Save Metadata
metadata_path = os.path.join(OUTPUT_DIR, "cell_metadata.csv")
adata.obs.to_csv(metadata_path)

# --- 6. Interpretation Report ---
print("Generating Report...")
report_path = os.path.join(OUTPUT_DIR, "ANALYSIS_INTERPRETATION.md")

total_cells = adata.n_obs
batches = adata.obs['sample'].value_counts().to_dict()

# Calculate cell type proportions
cell_counts = {}
if 'predicted_cell_type' in adata.obs:
    cell_counts = adata.obs['predicted_cell_type'].value_counts(normalize=True).mul(100).round(2).to_dict()

with open(report_path, 'w') as f:
    f.write("# scRNA-seq Analysis Report: Bone Marrow Samples\n\n")
    f.write(f"**Date:** {pd.Timestamp.now()}\n\n")
    f.write("## 1. Dataset Overview\n")
    f.write(f"- **Total Cells:** {total_cells}\n")
    f.write(f"- **Samples:** {list(samples.keys())}\n")
    f.write(f"- **Batch Distribution:** {batches}\n\n")
    
    f.write("## 2. Cell Type Annotation\n")
    f.write("Cell types were annotated using marker-based scoring (UniversalAnnotator Skill).\n")
    f.write("### Detected Proportions:\n")
    for ct, prop in cell_counts.items():
        f.write(f"- **{ct}:** {prop}%\n")
    
    f.write("\n## 3. Pathway Analysis\n")
    f.write("Pathways were scored using AUCell-like enrichment (PathwayAnalyzer Skill).\n")
    f.write("### Key Observations:\n")
    for pathway in pathways.keys():
        avg_score = adata.obs[pathway].mean()
        f.write(f"- **{pathway}:** Average Activity Score = {avg_score:.4f}\n")

    f.write("\n## 4. Files Generated\n")
    f.write("- `umap_batch.png`: Visualization of batch effects.\n")
    f.write("- `umap_celltypes.png`: Predicted cell types.\n")
    f.write("- `dotplot_markers.png`: Expression of marker genes across types.\n")
    f.write("- `umap_pathways.png`: Activity of biological pathways.\n")
    f.write("- `cell_metadata.csv`: Full cell annotations and scores.\n")

print(f"Analysis complete. Results saved to {OUTPUT_DIR}")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
