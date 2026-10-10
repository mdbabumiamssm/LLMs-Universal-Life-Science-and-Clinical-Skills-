"""Stage 5 — B-progenitor trajectory (DPT) + CD133/PROM1 analysis.

Implements sc-pseudotime (dpt). Proves:
  * Lymphoid progenitors form an early (IL7R/IGHM) -> late (CD24) B continuum (text/Fig)
  * CD133 (PROM1) is expressed by very few B-progenitors (Fig 2C rationale)
"""
import os
import numpy as np
import pandas as pd
import scanpy as sc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from common import FIG, TAB, CKPT, CELLTYPE_COLORS

sc.settings.verbosity = 1
adata = sc.read_h5ad(os.path.join(CKPT, "03_annotated.h5ad"))

# ---------------- B-lineage subset: HSPC (root) + Lym_P (B-progenitors)
sub = adata[adata.obs["cell_type"].isin(
    ["HSPC", "Lym_P (B-progenitor)"])].copy()
print(f"B-lineage subset: {sub.n_obs} cells")
sc.pp.neighbors(sub, use_rep="X_pca_harmony", n_neighbors=15)
sc.tl.diffmap(sub, n_comps=15)

# root = most stem-like HSPC cell (highest HSPC lineage score)
root_idx = int(np.argmax(sub.obs["score_HSPC"].values))
sub.uns["iroot"] = root_idx
sc.tl.dpt(sub, n_dcs=10)
sc.tl.umap(sub, min_dist=0.4)
print(f"DPT root cell: {sub.obs_names[root_idx]} "
      f"(HSPC score {sub.obs['score_HSPC'].iloc[root_idx]:.2f})")

# ---------------- figure: trajectory UMAP (pseudotime + cell type)
fig, axes = plt.subplots(1, 3, figsize=(19, 5.5))
ct_pal = [CELLTYPE_COLORS[c] for c in sub.obs["cell_type"].cat.categories]
sc.pl.umap(sub, color="cell_type", ax=axes[0], show=False, palette=ct_pal,
           title="B-lineage subset (HSPC + Lym_P)")
sc.pl.umap(sub, color="dpt_pseudotime", ax=axes[1], show=False, cmap="viridis",
           title="DPT pseudotime")
sc.pl.umap(sub, color="condition", ax=axes[2], show=False,
           title="Condition")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "05_trajectory_umap.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------- gene trends along pseudotime (early -> late B markers)
traj_genes = {
    "Stem/HSPC": ["CD34", "AVP", "CRHBP"],
    "Pro-B": ["DNTT", "VPREB1", "CD79A", "EBF1"],
    "Early B (IL7R/IGHM)": ["IL7R", "IGHM"],
    "Late B (CD24+)": ["CD24", "CD19", "MME", "MS4A1"],
}
pt = sub.obs["dpt_pseudotime"].values
bins = np.linspace(0, np.nanpercentile(pt, 99.5), 26)
centers = (bins[:-1] + bins[1:]) / 2
bin_idx = np.digitize(pt, bins) - 1

fig, axes = plt.subplots(1, 4, figsize=(20, 4.8), sharex=True)
expr_all = sub.raw.to_adata() if sub.raw is not None else sub
for ax, (panel, genes) in zip(axes, traj_genes.items()):
    for g in genes:
        if g not in expr_all.var_names:
            continue
        vals = np.asarray(expr_all[:, g].X.todense()).ravel() \
            if hasattr(expr_all[:, g].X, "todense") else np.asarray(expr_all[:, g].X).ravel()
        means = [vals[(bin_idx == b)].mean() if np.any(bin_idx == b) else np.nan
                 for b in range(len(centers))]
        ax.plot(centers, means, label=g, lw=2)
    ax.set_title(panel); ax.set_xlabel("DPT pseudotime")
    ax.set_ylabel("mean log-norm expr"); ax.legend(fontsize=8)
fig.suptitle("B-progenitor maturation along pseudotime: stem -> pro-B -> "
             "early B (IL7R/IGHM) -> late B (CD24)", y=1.04, fontsize=13)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "05_trajectory_gene_trends.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

sub.write(os.path.join(CKPT, "05_blineage_dpt.h5ad"))

# ================= CD133 / PROM1 in B-progenitors (Fig 2C rationale) =========
expr = adata.raw.to_adata()
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
for gene, ax in zip(["PROM1", "CD34"], axes):
    df = pd.DataFrame({
        "cell_type": adata.obs["cell_type"].values,
        "expr": np.asarray(expr[:, gene].X.todense()).ravel()
        if hasattr(expr[:, gene].X, "todense") else np.asarray(expr[:, gene].X).ravel()})
    order = [c for c in CELLTYPE_COLORS if c in df["cell_type"].unique()]
    sns.violinplot(data=df, x="cell_type", y="expr", order=order, ax=ax,
                   palette=CELLTYPE_COLORS, cut=0, inner="box")
    ax.set_title(f"{gene} expression by cell type")
    ax.set_xlabel(""); ax.set_ylabel("log-norm expression")
    ax.tick_params(axis="x", rotation=30)
fig.suptitle("CD34 (PROM1=CD133) expression: CD133 marks HSPC but very few "
             "B-progenitors (cf. Fig 2C)", y=1.03, fontsize=12)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "05_PROM1_CD133.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# % positive cells per cell type
pos = {}
for gene in ["PROM1", "CD34", "CD79A", "VPREB1"]:
    v = (np.asarray(expr[:, gene].X.todense()).ravel()
         if hasattr(expr[:, gene].X, "todense") else np.asarray(expr[:, gene].X).ravel())
    pos[gene] = (pd.Series(v > 0, index=adata.obs_names)
                 .groupby(adata.obs["cell_type"].values, observed=True).mean() * 100)
pos_df = pd.DataFrame(pos).round(1)
pos_df.to_csv(os.path.join(TAB, "marker_pct_positive_by_celltype.csv"))
print("\n% positive cells per cell type:")
print(pos_df.to_string())
print("\nSaved trajectory + CD133 figures.")
