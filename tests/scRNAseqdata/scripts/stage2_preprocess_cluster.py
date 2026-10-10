"""Stage 2 — Normalize/HVG/PCA, harmony integration, leiden clustering, UMAP.

Implements:  sc-preprocessing  ->  sc-batch-integration (harmony)  ->  sc-clustering
"""
import os
import numpy as np
import scanpy as sc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import FIG, CKPT, COND_COLORS

sc.settings.verbosity = 1
sc.settings.figdir = FIG
sc.settings.n_jobs = 16

adata = sc.read_h5ad(os.path.join(CKPT, "01_filtered.h5ad"))
print(f"Loaded {adata.n_obs} cells x {adata.n_vars} genes")

# ----------------------------------------------------- sc-preprocessing (scanpy)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
adata.raw = adata                              # log-norm, all genes (for markers/plots)
sc.pp.highly_variable_genes(adata, n_top_genes=2000, flavor="seurat",
                            batch_key="sample")
print(f"HVGs selected: {int(adata.var.highly_variable.sum())} (batch-aware seurat)")

# PCA on scaled HVG subset; keep full gene matrix (log-norm) in adata.X
adata_hvg = adata[:, adata.var.highly_variable].copy()
sc.pp.scale(adata_hvg, max_value=10)
sc.pp.pca(adata_hvg, n_comps=50, svd_solver="arpack")
adata.obsm["X_pca"] = adata_hvg.obsm["X_pca"]
adata.uns["pca"] = adata_hvg.uns["pca"]
del adata_hvg
print("PCA: 50 components on scaled HVGs")

# ------------------------------------------------ sc-batch-integration (harmony)
import harmonypy
ho = harmonypy.run_harmony(adata.obsm["X_pca"], adata.obs, ["sample"],
                           max_iter_harmony=20)
Z = np.asarray(ho.Z_corr)
if Z.shape[0] != adata.n_obs:        # harmonypy returns (n_pcs, n_cells)
    Z = Z.T
adata.obsm["X_pca_harmony"] = Z
print(f"Harmony integration done -> X_pca_harmony {adata.obsm['X_pca_harmony'].shape}")

# --------------------------------------------------------------- sc-clustering
sc.pp.neighbors(adata, use_rep="X_pca_harmony", n_neighbors=15, n_pcs=50)
sc.tl.umap(adata, min_dist=0.5, spread=1.0)
sc.tl.leiden(adata, resolution=1.0, key_added="leiden", flavor="leidenalg")
print(f"Leiden clusters (res=1.0): {adata.obs['leiden'].nunique()}")
print(adata.obs["leiden"].value_counts().sort_index())

# ---------------------------------------------------- integration QC UMAPs
fig, axes = plt.subplots(1, 3, figsize=(20, 6))
sc.pl.umap(adata, color="leiden", ax=axes[0], show=False, legend_loc="on data",
           legend_fontsize=8, title="Leiden clusters")
cond_pal = [COND_COLORS[c] for c in adata.obs["condition"].cat.categories]
sc.pl.umap(adata, color="condition", ax=axes[1], show=False, palette=cond_pal,
           title="Condition (batch-integrated)")
sc.pl.umap(adata, color="sample", ax=axes[2], show=False, title="Sample")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "02_umap_overview.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# Per-condition UMAP split (mirrors manuscript Figure 1A)
conds = ["Control", "Thalassemia", "SCD"]
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for ax, c in zip(axes, conds):
    sc.pl.umap(adata, ax=ax, show=False, size=6, color=None)
    mask = adata.obs["condition"] == c
    ax.scatter(adata.obsm["X_umap"][mask.values, 0],
               adata.obsm["X_umap"][mask.values, 1],
               s=4, c=COND_COLORS[c], rasterized=True)
    ax.set_title(f"{c} (n={int(mask.sum())})")
    ax.set_xticks([]); ax.set_yticks([])
fig.suptitle("scRNA-seq cells by condition (cf. Figure 1A)", y=1.02, fontsize=14)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "02_umap_by_condition.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

adata.write(os.path.join(CKPT, "02_clustered.h5ad"))
print("Saved checkpoint -> 02_clustered.h5ad")
