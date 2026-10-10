"""Stage 3b — Explicit manual cluster->cell-type map (sc-cell-annotation 'manual').

Refines the automatic argmax annotation using verified marker evidence:
  * cluster 14 = pDC (IRF8/PLD4/PLAC8/JCHAIN) -> 'Other', not a B-progenitor
  * cluster 11 = early lymphoid/B-progenitor (CD79A/VPREB1/DNTT/IL7R/IGHM) -> Lym_P
Everything else matches the lineage-score argmax.
"""
import os
import scanpy as sc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import FIG, TAB, CKPT, CELLTYPE_COLORS

adata = sc.read_h5ad(os.path.join(CKPT, "03_annotated.h5ad"))

HSPC = ["0", "1", "2", "5", "9", "10", "13", "17"]
LYMP = ["3", "4", "11", "16"]
MEP  = ["7", "12", "15", "18", "19"]
GMP  = ["6", "8"]
OTHER = ["14"]   # pDC

manual_map = {}
for cl in HSPC: manual_map[cl] = "HSPC"
for cl in LYMP: manual_map[cl] = "Lym_P (B-progenitor)"
for cl in MEP:  manual_map[cl] = "M/E_P (Mega/Erythroid)"
for cl in GMP:  manual_map[cl] = "G/M_P (Granulo/Mono)"
for cl in OTHER: manual_map[cl] = "Other"

adata.obs["cell_type"] = adata.obs["leiden"].map(manual_map).astype("category")
order = [c for c in ["HSPC", "Lym_P (B-progenitor)", "M/E_P (Mega/Erythroid)",
                     "G/M_P (Granulo/Mono)", "Other"]
         if c in adata.obs["cell_type"].cat.categories]
adata.obs["cell_type"] = adata.obs["cell_type"].cat.reorder_categories(order)

print("Final cell-type counts:")
print(adata.obs["cell_type"].value_counts().to_string())
adata.obs[["leiden", "cell_type"]].drop_duplicates().sort_values(
    "leiden", key=lambda s: s.astype(int)).to_csv(
    os.path.join(TAB, "cluster_to_celltype_map.csv"), index=False)

# regenerate cell-type UMAP + canonical marker feature plots
fig, axes = plt.subplots(2, 3, figsize=(19, 11))
ct_pal = [CELLTYPE_COLORS[c] for c in adata.obs["cell_type"].cat.categories]
sc.pl.umap(adata, color="cell_type", ax=axes[0, 0], show=False, palette=ct_pal,
           title="Annotated cell types", legend_fontsize=9)
for ax, gene in zip(axes.ravel()[1:], ["CD34", "CD79A", "VPREB1", "GATA1", "MPO"]):
    sc.pl.umap(adata, color=gene, ax=ax, show=False, cmap="viridis", use_raw=True)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "03_umap_celltype_markers.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

adata.write(os.path.join(CKPT, "03_annotated.h5ad"))
print("Updated checkpoint -> 03_annotated.h5ad")
