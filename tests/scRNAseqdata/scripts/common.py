"""Shared configuration for the GSE133181 reproduction analysis.

Reproduces the scRNA-seq findings of:
  Hua P, Roy N, de la Fuente J, et al.
  "Single-cell analysis of bone marrow-derived CD34+ cells from children with
   sickle cell disease and thalassemia." Blood 2019;134(23):2111-2115.
  GEO: GSE133181

Methodology follows the OmicsClaw single-cell skills:
  sc-standardize-input, sc-qc, sc-filter, sc-preprocessing,
  sc-batch-integration (harmony), sc-clustering (leiden/umap),
  sc-markers (wilcoxon), sc-cell-annotation (manual/markers),
  sc-pathway-scoring (AUCell-style lymphoid signature),
  sc-differential-abundance, sc-pseudotime (dpt).
"""
import os
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
pd.set_option("compute.use_bottleneck", False)
pd.set_option("compute.use_numexpr", False)

BASE = "/media/drdx/mystorage/ARTIFICIALINTELLIGENCEGROUP/skills/tests/scRNAseqdata"
EXTRACTED = os.path.join(BASE, "extracted")
OUT = os.path.join(BASE, "analysis_results")
FIG = os.path.join(OUT, "figures")
TAB = os.path.join(OUT, "tables")
CKPT = os.path.join(OUT, "checkpoints")
for d in (OUT, FIG, TAB, CKPT):
    os.makedirs(d, exist_ok=True)

# Sample -> condition. Matches manuscript cohort: 4 controls, 3 thalassemia, 5 SCD.
# C1 is the extra unselected-CD34 control sample (supplemental Fig 9A); kept
# separate so the primary 3-group comparison mirrors Figure 1A exactly.
SAMPLES = {
    "BM1": "Control", "BM2": "Control", "BM3": "Control", "BM4": "Control",
    "BT1": "Thalassemia", "BT2": "Thalassemia", "BT3": "Thalassemia",
    "SCD1": "SCD", "SCD2": "SCD", "SCD3": "SCD", "SCD4": "SCD", "SCD5": "SCD",
    "C1": "Control_C1",
}
# The three groups used for the headline composition comparison (Figure 1A/B).
PRIMARY_CONDITIONS = ["Control", "Thalassemia", "SCD"]
COND_COLORS = {"Control": "#4daf4a", "Thalassemia": "#377eb8",
               "SCD": "#e41a1c", "Control_C1": "#999999"}

# Manuscript's lymphoid B-progenitor signature (used with AUCell, AUC>0.25).
LYMPHOID_SIGNATURE = ["CD79A", "CD79B", "VPREB1", "VPREB3", "EBF1"]

# Canonical CD34+ bone-marrow lineage markers for annotation.
MARKERS = {
    "HSPC":  ["CD34", "CRHBP", "AVP", "HLF", "MEIS1", "MLLT3", "HOPX", "PROM1"],
    "Lym_P (B-progenitor)": ["CD79A", "CD79B", "VPREB1", "VPREB3", "EBF1",
                             "IGLL1", "DNTT", "CD19", "MME", "IL7R", "CD24", "IGHM"],
    "M/E_P (Mega/Erythroid)": ["GATA1", "GATA2", "KLF1", "HBB", "HBD", "GYPA",
                               "TFRC", "PPBP", "PF4", "ITGA2B", "VWF"],
    "G/M_P (Granulo/Mono)": ["MPO", "ELANE", "PRTN3", "AZU1", "LYZ", "CTSG",
                             "CSF3R", "CEBPE", "S100A8"],
}

CELLTYPE_COLORS = {
    "HSPC": "#56B4E9",
    "Lym_P (B-progenitor)": "#7d2a8c",
    "M/E_P (Mega/Erythroid)": "#a50f15",
    "G/M_P (Granulo/Mono)": "#41ab5d",
    "Other": "#bdbdbd",
}


def aucell_score(adata, gene_set, auc_max_rank_frac=0.05, use_raw_counts=True):
    """Lightweight AUCell implementation (Aibar et al. 2017).

    For each cell, genes are ranked by expression (ties broken randomly via
    a small jitter on the dense rank). The AUC is the area under the gene-set
    recovery curve within the top `auc_max_rank` ranked genes, normalised to
    [0, 1]. Mirrors the manuscript's AUCell usage (AUC>0.25 gate).
    """
    import scipy.sparse as sp
    genes = [g for g in gene_set if g in adata.var_names]
    if not genes:
        raise ValueError("None of the signature genes are present.")
    X = adata.layers["counts"] if (use_raw_counts and "counts" in adata.layers) else adata.X
    if sp.issparse(X):
        X = X.toarray()
    X = np.asarray(X, dtype=float)
    n_cells, n_genes = X.shape
    auc_max_rank = max(1, int(np.ceil(auc_max_rank_frac * n_genes)))
    gene_idx = [adata.var_names.get_loc(g) for g in genes]

    aucs = np.zeros(n_cells)
    # Rank genes descending per cell; rank 1 = highest expressed.
    # Add tiny deterministic jitter so zeros don't all share rank.
    rng = np.random.default_rng(0)
    for i in range(n_cells):
        row = X[i]
        jitter = rng.random(n_genes) * 1e-6
        order = np.argsort(-(row + jitter))           # indices sorted by expr desc
        ranks = np.empty(n_genes, dtype=int)
        ranks[order] = np.arange(1, n_genes + 1)      # rank per gene
        set_ranks = np.sort(ranks[gene_idx])
        set_ranks = set_ranks[set_ranks <= auc_max_rank]
        # area under recovery curve (counts genes recovered at each rank step)
        if len(set_ranks) == 0:
            aucs[i] = 0.0
        else:
            area = np.sum(auc_max_rank - set_ranks + 1)
            aucs[i] = area / (auc_max_rank * len(genes))
    return aucs, genes, auc_max_rank
