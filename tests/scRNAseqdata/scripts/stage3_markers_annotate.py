"""Stage 3 — Cluster markers, lineage scoring, cell-type annotation, AUCell.

Implements:  sc-markers (wilcoxon)  ->  sc-pathway-scoring (AUCell lymphoid sig)
             ->  sc-cell-annotation (marker/score-based manual mapping)
"""
import os
import scanpy as sc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import (FIG, TAB, CKPT, MARKERS, CELLTYPE_COLORS,
                    LYMPHOID_SIGNATURE, aucell_score)

sc.settings.verbosity = 1
sc.settings.figdir = FIG

adata = sc.read_h5ad(os.path.join(CKPT, "02_clustered.h5ad"))
print(f"Loaded {adata.n_obs} cells x {adata.n_vars} genes, "
      f"{adata.obs['leiden'].nunique()} clusters")

# --------------------------------------------------- sc-markers (wilcoxon)
sc.tl.rank_genes_groups(adata, "leiden", method="wilcoxon", use_raw=True)
mk = sc.get.rank_genes_groups_df(adata, group=None)
mk.to_csv(os.path.join(TAB, "cluster_markers_wilcoxon.csv"), index=False)
top = (mk.sort_values(["group", "scores"], ascending=[True, False])
       .groupby("group").head(10))
print("\nTop markers per cluster (first few clusters):")
for g in sorted(adata.obs['leiden'].cat.categories, key=int)[:8]:
    genes = top.loc[top.group == g, "names"].tolist()
    print(f"  cluster {g:>2}: {', '.join(genes)}")

# ------------------------------- sc-pathway-scoring: lineage + lymphoid signature
for ct, genes in MARKERS.items():
    present = [g for g in genes if g in adata.var_names]
    sc.tl.score_genes(adata, present, score_name=f"score_{ct}", use_raw=True)

# AUCell-style lymphoid B-progenitor signature (manuscript: AUC>0.25)
auc, used_genes, amr = aucell_score(adata, LYMPHOID_SIGNATURE,
                                    auc_max_rank_frac=0.05, use_raw_counts=True)
adata.obs["lymphoid_AUC"] = auc
adata.obs["is_lymphoid_AUC>0.25"] = (auc > 0.25)
print(f"\nAUCell lymphoid signature {used_genes} (aucMaxRank={amr})")
print(f"  cells with AUC>0.25: {int((auc>0.25).sum())} "
      f"({100*(auc>0.25).mean():.1f}%)")

# ----------------------------------- per-cluster lineage score -> annotation
score_cols = [f"score_{ct}" for ct in MARKERS]
cluster_scores = adata.obs.groupby("leiden", observed=True)[score_cols].mean()
# z-score each lineage score across clusters so they are comparable
z = (cluster_scores - cluster_scores.mean()) / cluster_scores.std()
cluster_scores.to_csv(os.path.join(TAB, "cluster_lineage_scores.csv"))
assign = z.idxmax(axis=1).str.replace("score_", "", regex=False)

# also bring in AUCell lymphoid fraction per cluster as corroboration
auc_frac = adata.obs.groupby("leiden", observed=True)["is_lymphoid_AUC>0.25"].mean()
print("\nPer-cluster lineage assignment (argmax z-scored signature):")
mapping = {}
for cl in sorted(assign.index, key=int):
    label = assign[cl]
    # Strong lymphoid AUCell fraction overrides ambiguous calls
    if auc_frac[cl] > 0.5:
        label = "Lym_P (B-progenitor)"
    mapping[cl] = label
    print(f"  cluster {cl:>2}: {label:25s} (lymphoid AUC>0.25 frac={auc_frac[cl]:.2f})")

adata.obs["cell_type"] = adata.obs["leiden"].map(mapping).astype("category")
adata.obs["cell_type"] = adata.obs["cell_type"].cat.reorder_categories(
    [c for c in CELLTYPE_COLORS if c in adata.obs["cell_type"].cat.categories])

print("\nCell-type totals:\n", adata.obs["cell_type"].value_counts().to_string())

# ----------------------------------------------------------------- figures
# (a) marker dotplot across clusters
flat_markers = []
for genes in MARKERS.values():
    flat_markers += [g for g in genes if g in adata.var_names]
sc.pl.dotplot(adata, {k: [g for g in v if g in adata.var_names] for k, v in MARKERS.items()},
              groupby="leiden", use_raw=True, standard_scale="var", show=False,
              save="_03_markers_by_cluster.png")

# (b) UMAP colored by cell type + key marker feature plots
fig, axes = plt.subplots(2, 3, figsize=(19, 11))
ct_pal = [CELLTYPE_COLORS[c] for c in adata.obs["cell_type"].cat.categories]
sc.pl.umap(adata, color="cell_type", ax=axes[0, 0], show=False, palette=ct_pal,
           title="Annotated cell types", legend_fontsize=9)
for ax, gene in zip(axes.ravel()[1:], ["CD34", "CD79A", "VPREB1", "GATA1", "MPO"]):
    sc.pl.umap(adata, color=gene, ax=ax, show=False, cmap="viridis", use_raw=True)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "03_umap_celltype_markers.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# (c) lymphoid AUCell on UMAP + distribution by condition
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
sc.pl.umap(adata, color="lymphoid_AUC", ax=axes[0], show=False, cmap="magma",
           title="Lymphoid AUCell score (CD79A/B,VPREB1/3,EBF1)")
import seaborn as sns
order = ["Control", "Thalassemia", "SCD"]
sub = adata.obs[adata.obs["condition"].isin(order)]
sns.violinplot(data=sub, x="condition", y="lymphoid_AUC", order=order, ax=axes[1],
               palette={"Control": "#4daf4a", "Thalassemia": "#377eb8", "SCD": "#e41a1c"},
               cut=0)
axes[1].axhline(0.25, ls="--", c="k", lw=1)
axes[1].set_title("Lymphoid AUCell by condition (gate AUC>0.25)")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "03_lymphoid_aucell.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

adata.write(os.path.join(CKPT, "03_annotated.h5ad"))
print("\nSaved checkpoint -> 03_annotated.h5ad")
