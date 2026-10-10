"""Stage 1 — Load 13 10X samples, standardize, compute QC, filter.

Implements:  sc-standardize-input  ->  sc-qc  ->  sc-filter
"""
import os
import numpy as np
import pandas as pd
import scanpy as sc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from common import EXTRACTED, FIG, TAB, CKPT, SAMPLES, COND_COLORS

sc.settings.verbosity = 1
sc.settings.figdir = FIG

# ---------------------------------------------------------------- load + merge
adatas = []
for sample, condition in SAMPLES.items():
    path = os.path.join(EXTRACTED, sample)
    a = sc.read_10x_mtx(path, var_names="gene_symbols", make_unique=True)
    a.obs["sample"] = sample
    a.obs["condition"] = condition
    a.obs_names = [f"{sample}_{bc}" for bc in a.obs_names]
    adatas.append(a)
    print(f"  loaded {sample:5s} ({condition:12s}): {a.n_obs} cells x {a.n_vars} genes")

adata = sc.concat(adatas, join="outer", index_unique=None)
adata.obs["condition"] = adata.obs["condition"].astype("category")
adata.obs["sample"] = adata.obs["sample"].astype("category")
print(f"\nMerged: {adata.n_obs} cells x {adata.n_vars} genes")

# sc-standardize-input contract: X = counts, layers['counts'] = counts
adata.layers["counts"] = adata.X.copy()

# ------------------------------------------------------------------ sc-qc
adata.var["mt"] = adata.var_names.str.startswith("MT-")
adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
sc.pp.calculate_qc_metrics(adata, qc_vars=["mt", "ribo"], inplace=True, percent_top=None)
print("QC metrics computed (n_genes_by_counts, total_counts, pct_counts_mt, pct_counts_ribo)")

# Pre-filter QC summary table
qc_pre = (adata.obs.groupby("sample", observed=True)
          .agg(n_cells=("total_counts", "size"),
               median_genes=("n_genes_by_counts", "median"),
               median_counts=("total_counts", "median"),
               median_pct_mt=("pct_counts_mt", "median"))
          .join(adata.obs.groupby("sample", observed=True)["condition"].first()))
qc_pre.to_csv(os.path.join(TAB, "qc_prefilter_per_sample.csv"))
print("\nPre-filter per-sample QC:\n", qc_pre)

# -------------------------------------------------------- QC gallery (sc-qc)
fig, axes = plt.subplots(1, 3, figsize=(16, 4.2))
for ax, metric, title in zip(
        axes,
        ["n_genes_by_counts", "total_counts", "pct_counts_mt"],
        ["Genes per cell", "UMI counts per cell", "Mitochondrial %"]):
    data = [adata.obs.loc[adata.obs["sample"] == s, metric].values
            for s in adata.obs["sample"].cat.categories]
    sns.violinplot(data=data, ax=ax, cut=0, inner="box", linewidth=0.6)
    ax.set_xticks(range(len(adata.obs["sample"].cat.categories)))
    ax.set_xticklabels(adata.obs["sample"].cat.categories, rotation=90, fontsize=8)
    ax.set_title(title)
    if metric != "pct_counts_mt":
        ax.set_yscale("log")
fig.suptitle("QC metrics before filtering (sc-qc)", y=1.02, fontsize=13)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "01_qc_prefilter_violins.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots(figsize=(6, 5))
sc_obs = adata.obs
sca = ax.scatter(sc_obs["total_counts"], sc_obs["n_genes_by_counts"],
                 c=sc_obs["pct_counts_mt"], s=3, cmap="viridis", vmax=20)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("total_counts"); ax.set_ylabel("n_genes_by_counts")
ax.set_title("QC scatter (color = % mito)")
plt.colorbar(sca, ax=ax, label="pct_counts_mt")
fig.savefig(os.path.join(FIG, "01_qc_scatter.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------- sc-filter
n_before = adata.n_obs
MIN_GENES, MAX_MT, MIN_CELLS = 200, 15.0, 3   # CD34+ HSPC-appropriate thresholds
# upper gene cap to drop likely multiplets (robust 99.5th pct)
MAX_GENES = int(np.percentile(adata.obs["n_genes_by_counts"], 99.5))
sc.pp.filter_cells(adata, min_genes=MIN_GENES)
adata = adata[adata.obs["n_genes_by_counts"] <= MAX_GENES].copy()
adata = adata[adata.obs["pct_counts_mt"] < MAX_MT].copy()
sc.pp.filter_genes(adata, min_cells=MIN_CELLS)
print(f"\nsc-filter: min_genes={MIN_GENES}, max_genes={MAX_GENES}, "
      f"max_mt={MAX_MT}%, min_cells={MIN_CELLS}")
print(f"  cells {n_before} -> {adata.n_obs}  |  genes -> {adata.n_vars}")

qc_post = (adata.obs.groupby("condition", observed=True)
           .agg(n_cells=("total_counts", "size"),
                median_genes=("n_genes_by_counts", "median"),
                median_pct_mt=("pct_counts_mt", "median")))
qc_post.to_csv(os.path.join(TAB, "qc_postfilter_per_condition.csv"))
print("\nPost-filter per-condition:\n", qc_post)

adata.write(os.path.join(CKPT, "01_filtered.h5ad"))
print("\nSaved checkpoint -> 01_filtered.h5ad")
