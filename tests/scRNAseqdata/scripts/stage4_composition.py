"""Stage 4 — Differential abundance: cell-type composition across conditions.

Implements sc-differential-abundance (per-sample proportion test). Proves:
  * Marked expansion of Lym_P (B-progenitors) in patients   (Fig 1A-C)
  * Relative reduction of HSPC in patients                   (Fig 2 / text)
  * No expansion of erythroid (M/E_P) cells                  (text, NS)
"""
import os
import numpy as np
import pandas as pd
import scanpy as sc
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from common import FIG, TAB, CKPT, CELLTYPE_COLORS

adata = sc.read_h5ad(os.path.join(CKPT, "03_annotated.h5ad"))
PRIMARY = ["Control", "Thalassemia", "SCD"]

# ---- per-sample x cell-type counts and proportions
counts = pd.crosstab(adata.obs["sample"], adata.obs["cell_type"])
props = counts.div(counts.sum(axis=1), axis=0) * 100
samp_cond = adata.obs.drop_duplicates("sample").set_index("sample")["condition"]
props["condition"] = samp_cond
counts.to_csv(os.path.join(TAB, "sample_by_celltype_counts.csv"))
props.to_csv(os.path.join(TAB, "sample_by_celltype_proportions.csv"))
print("Per-sample cell-type proportions (%):")
print(props.round(1).to_string())

# ---- mean proportion per condition (mirror Fig 1B)
cond_mean = props[props.condition.isin(PRIMARY)].groupby("condition")[
    [c for c in CELLTYPE_COLORS if c in counts.columns]].mean()
cond_mean = cond_mean.reindex(PRIMARY)
cond_mean.to_csv(os.path.join(TAB, "condition_mean_celltype_proportions.csv"))
print("\nMean cell-type % per condition (cf. Fig 1B):")
print(cond_mean.round(1).to_string())

# ---- statistics: Control vs Patients (and vs each disease) per cell type
def mw(a, b):
    if len(a) < 2 or len(b) < 2:
        return np.nan
    return stats.mannwhitneyu(a, b, alternative="two-sided").pvalue

ctrl = props[props.condition == "Control"]
thal = props[props.condition == "Thalassemia"]
scd = props[props.condition == "SCD"]
patients = props[props.condition.isin(["Thalassemia", "SCD"])]

rows = []
for ct in [c for c in CELLTYPE_COLORS if c in counts.columns]:
    rows.append({
        "cell_type": ct,
        "Control_mean": ctrl[ct].mean(),
        "Thal_mean": thal[ct].mean(),
        "SCD_mean": scd[ct].mean(),
        "Patients_mean": patients[ct].mean(),
        "p_Ctrl_vs_Patients": mw(ctrl[ct], patients[ct]),
        "p_Ctrl_vs_Thal": mw(ctrl[ct], thal[ct]),
        "p_Ctrl_vs_SCD": mw(ctrl[ct], scd[ct]),
    })
stats_df = pd.DataFrame(rows).set_index("cell_type")
stats_df.to_csv(os.path.join(TAB, "composition_stats.csv"))
print("\nDifferential abundance stats (Mann-Whitney, per-sample replicates):")
print(stats_df.round(3).to_string())

# also AUCell lymphoid fraction per sample (orthogonal to clustering)
auc_frac = (adata.obs.groupby("sample", observed=True)["is_lymphoid_AUC>0.25"]
            .mean() * 100)
auc_tab = pd.DataFrame({"lymphoid_AUC>0.25_pct": auc_frac, "condition": samp_cond})
auc_tab.to_csv(os.path.join(TAB, "lymphoid_aucell_fraction_per_sample.csv"))

# ============================ FIGURES ============================
# (1) stacked bar: mean composition per condition (Fig 1B style)
fig, ax = plt.subplots(figsize=(7, 4.5))
bottom = np.zeros(len(cond_mean))
for ct in cond_mean.columns:
    ax.barh(cond_mean.index, cond_mean[ct], left=bottom,
            color=CELLTYPE_COLORS[ct], label=ct, edgecolor="white")
    for i, v in enumerate(cond_mean[ct]):
        if v > 4:
            ax.text(bottom[i] + v / 2, i, f"{v:.0f}", va="center", ha="center",
                    fontsize=8, color="white", fontweight="bold")
    bottom += cond_mean[ct].values
ax.set_xlabel("% of CD34+ cells"); ax.set_xlim(0, 100)
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
ax.set_title("Cell-type composition by condition (cf. Figure 1B)")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "04_composition_stacked_bar.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# (2) per-sample stacked bars
fig, ax = plt.subplots(figsize=(11, 4.5))
sp = props.loc[[s for s in adata.obs["sample"].cat.categories]]
bottom = np.zeros(len(sp))
for ct in [c for c in CELLTYPE_COLORS if c in counts.columns]:
    ax.bar(sp.index, sp[ct], bottom=bottom, color=CELLTYPE_COLORS[ct],
           label=ct, edgecolor="white", linewidth=0.4)
    bottom += sp[ct].values
ax.set_ylabel("% of cells"); ax.set_ylim(0, 100)
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
ax.set_title("Per-sample cell-type composition")
plt.xticks(rotation=90)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "04_composition_per_sample.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# (3) box+strip of key lineages: Control vs Thal vs SCD with p-values (Fig 1C style)
def star(p):
    return "ns" if (np.isnan(p) or p > 0.05) else ("*" if p > 0.01 else
            ("**" if p > 0.001 else "***"))

key_cts = ["Lym_P (B-progenitor)", "HSPC", "M/E_P (Mega/Erythroid)", "G/M_P (Granulo/Mono)"]
fig, axes = plt.subplots(1, 4, figsize=(18, 5))
pal = {"Control": "#4daf4a", "Thalassemia": "#377eb8", "SCD": "#e41a1c"}
for ax, ct in zip(axes, key_cts):
    d = props[props.condition.isin(PRIMARY)].copy()
    sns.boxplot(data=d, x="condition", y=ct, order=PRIMARY, ax=ax, palette=pal,
                width=0.6, fliersize=0)
    sns.stripplot(data=d, x="condition", y=ct, order=PRIMARY, ax=ax, color="k",
                  size=6, jitter=0.15)
    pcp = stats_df.loc[ct, "p_Ctrl_vs_Patients"]
    ax.set_title(f"{ct}\nCtrl vs Patients: {star(pcp)} (p={pcp:.3f})", fontsize=10)
    ax.set_xlabel(""); ax.set_ylabel("% of CD34+ cells")
fig.suptitle("Cell-type abundance across conditions (per-sample; cf. Figure 1C)",
             y=1.03, fontsize=13)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "04_abundance_boxplots.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# (4) Lym_P: Control vs Patients pooled (direct Fig 1C analogue) + AUCell
fig, axes = plt.subplots(1, 2, figsize=(11, 5))
props2 = props.copy()
props2["grp"] = props2["condition"].map(
    {"Control": "Control", "Thalassemia": "Patients", "SCD": "Patients"})
d = props2[props2["grp"].isin(["Control", "Patients"])]
for ax, (yval, ylab, src) in zip(
        axes,
        [("Lym_P (B-progenitor)", "B-progenitors (% of CD34+)", props2),
         ("lymphoid_AUC>0.25_pct", "Lymphoid AUCell>0.25 (% of cells)", None)]):
    if src is None:
        dd = auc_tab.copy()
        dd["grp"] = dd["condition"].map(
            {"Control": "Control", "Thalassemia": "Patients", "SCD": "Patients"})
        dd = dd[dd["grp"].isin(["Control", "Patients"])]
        yy = "lymphoid_AUC>0.25_pct"
    else:
        dd, yy = d, yval
    sns.barplot(data=dd, x="grp", y=yy, order=["Control", "Patients"], ax=ax,
                palette={"Control": "#4daf4a", "Patients": "#984ea3"},
                errorbar="se", capsize=0.15)
    sns.stripplot(data=dd, x="grp", y=yy, order=["Control", "Patients"], ax=ax,
                  color="k", size=7, jitter=0.12)
    p = mw(dd[dd.grp == "Control"][yy], dd[dd.grp == "Patients"][yy])
    ax.set_title(f"{ylab}\nCtrl vs Patients: {star(p)} (p={p:.3f})", fontsize=10)
    ax.set_xlabel(""); ax.set_ylabel(ylab)
fig.suptitle("B-lymphoid progenitor expansion in patients (cf. Figure 1C)",
             y=1.03, fontsize=13)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "04_Bprogenitor_ctrl_vs_patients.png"), dpi=150, bbox_inches="tight")
plt.close(fig)
print("\nSaved composition figures.")
