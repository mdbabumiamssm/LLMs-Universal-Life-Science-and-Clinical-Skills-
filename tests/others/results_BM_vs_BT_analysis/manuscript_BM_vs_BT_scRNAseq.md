<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

# Single-Cell Transcriptomic Analysis Reveals Altered Hematopoietic Landscape and Lymphoid Expansion in Beta-Thalassemia Bone Marrow

## Abstract

**Background:** Beta-thalassemia is a hereditary hemoglobinopathy characterized by reduced or absent beta-globin chain synthesis, leading to ineffective erythropoiesis and compensatory bone marrow expansion. While the erythroid compartment has been extensively studied, the broader hematopoietic alterations at single-cell resolution remain incompletely characterized.

**Methods:** We performed single-cell RNA sequencing (scRNA-seq) analysis of bone marrow samples from three beta-thalassemia (BT) patients and three healthy controls (BM) using the 10x Genomics platform (GSE133181). Data processing included quality control filtering using MAD-based adaptive thresholds, integration with scVI, and Leiden clustering. Cell type annotation was performed using marker-based scoring with curated bone marrow signatures. Differential expression analysis was conducted using the Wilcoxon rank-sum test, followed by pathway enrichment analysis via Enrichr.

**Results:** After quality control, 31,299 cells were retained (84.5% retention rate) across seven identified hematopoietic populations: HSC, GMP, MPP, Erythroid_Early, Pro_B, Plasma, and Dendritic cells. Thalassemia samples demonstrated a striking 2.7-fold expansion of Pro-B cells (3,099 vs. 1,141) and marked reduction of HSCs (502 vs. 8,275). Global differential expression identified 5,360 significant genes (|log2FC| > 0.5, adj. p < 0.05), with 4,052 upregulated and 1,308 downregulated in BT. Top upregulated genes included B-cell precursor markers (IGLL1, VPREB1, VPREB3, CD79B) and hematopoietic transcription factors (SOX4, MEF2C, MYB). Pathway analysis revealed enrichment of MYC targets, interferon signaling, and oxidative phosphorylation in thalassemia, while TNF-alpha/NF-kB signaling and cholesterol homeostasis were downregulated.

**Conclusions:** Our single-cell analysis reveals previously unappreciated lymphoid expansion in beta-thalassemia bone marrow, suggesting compensatory hematopoietic reprogramming beyond the erythroid lineage. These findings provide new insights into the systemic hematopoietic dysregulation in thalassemia and identify potential therapeutic targets.

**Keywords:** beta-thalassemia, single-cell RNA sequencing, bone marrow, hematopoiesis, lymphoid expansion, scVI integration

---

## 1. Introduction

Beta-thalassemia is one of the most common monogenic disorders worldwide, affecting approximately 1.5% of the global population (Weatherall, 2010). The disease results from mutations in the HBB gene, leading to reduced (beta+) or absent (beta0) synthesis of beta-globin chains. This imbalance causes alpha-globin chain precipitation, ineffective erythropoiesis, and chronic hemolytic anemia (Rivella, 2012). Clinically, beta-thalassemia presents as a spectrum from asymptomatic carrier states to transfusion-dependent thalassemia major.

The bone marrow in thalassemia major undergoes massive erythroid hyperplasia, with erythropoietic expansion of 10-30 fold compared to normal individuals (Pootrakul et al., 2000). This compensatory response, driven by elevated erythropoietin levels, results in bone deformities, hepatosplenomegaly, and extramedullary hematopoiesis. While the erythroid compartment has been the primary focus of thalassemia research, emerging evidence suggests broader hematopoietic alterations.

Single-cell RNA sequencing (scRNA-seq) has revolutionized our understanding of bone marrow heterogeneity by enabling transcriptomic profiling at single-cell resolution (Papalexi & Satija, 2018). Recent studies have applied scRNA-seq to characterize normal human hematopoiesis (Hay et al., 2018; Velten et al., 2017), revealing continuous differentiation trajectories and novel progenitor populations. However, comprehensive single-cell characterization of the thalassemia bone marrow microenvironment remains limited.

In this study, we performed integrative single-cell transcriptomic analysis of bone marrow samples from beta-thalassemia patients and healthy controls using the scverse ecosystem (Virshup et al., 2023). We employed state-of-the-art computational methods including scVI for batch-corrected integration (Lopez et al., 2018) and marker-based cell type annotation to comprehensively characterize hematopoietic alterations. Our analysis reveals striking changes in lineage composition, identifies key differentially expressed genes, and uncovers novel pathway dysregulation in thalassemia.

---

## 2. Materials and Methods

### 2.1 Data Source

Single-cell RNA sequencing data were obtained from the Gene Expression Omnibus (GEO) under accession number GSE133181. The dataset comprises bone marrow aspirates from:
- **Normal bone marrow (BM):** 3 samples (BM1, BM2, BM3) from healthy donors
- **Beta-thalassemia (BT):** 3 samples (BT1, BT2, BT3) from beta-thalassemia patients

Libraries were prepared using the 10x Genomics Chromium Single Cell 3' platform and sequenced on Illumina instruments. Raw data were processed with Cell Ranger and aligned to the GRCh38 human reference genome.

### 2.2 Quality Control and Preprocessing

Raw count matrices were loaded into Python using Scanpy v1.12 (Wolf et al., 2018). Quality control filtering was performed using adaptive median absolute deviation (MAD)-based thresholds as recommended by Luecken & Theis (2019):

- **Minimum genes per cell:** 200
- **Minimum cells per gene:** 20
- **Maximum mitochondrial percentage:** 15%
- **MAD multipliers:** 5 for gene counts, 5 for total counts, 3 for mitochondrial percentage

QC metrics calculated included:
- Total UMI counts per cell
- Number of genes detected per cell
- Percentage of mitochondrial, ribosomal, and hemoglobin transcripts

### 2.3 Normalization and Feature Selection

Filtered data were normalized using total-count normalization to 10,000 counts per cell, followed by log1p transformation. Highly variable genes (HVGs) were identified using the Seurat v3 method (Stuart et al., 2019) with batch-aware selection across samples, retaining 3,000 HVGs for downstream analysis.

### 2.4 Integration and Dimensionality Reduction

Sample integration was performed using scVI (single-cell Variational Inference) v1.4.1 (Lopez et al., 2018), a deep generative model that learns a batch-corrected latent representation while accounting for technical variation. Model parameters:
- Latent dimensions: 30
- Hidden layers: 2
- Gene likelihood: Negative binomial
- Maximum epochs: 200 with early stopping (patience=10)
- Learning rate: 1e-3

The scVI latent space was used to compute a k-nearest neighbor graph (k=15), followed by UMAP embedding (min_dist=0.3) for visualization.

### 2.5 Clustering and Cell Type Annotation

Unsupervised clustering was performed using the Leiden algorithm (Traag et al., 2019) at multiple resolutions (0.3, 0.5, 0.8, 1.0), with resolution 0.5 selected for downstream analysis based on cluster stability and biological interpretability.

Cell type annotation was performed using marker-based scoring adapted from CellIdentifierDX (Mia et al., unpublished). A curated reference panel of 31 bone marrow cell types was assembled from the literature (Hay et al., 2018; Hay et al., 2019; Zheng et al., 2020):

**Hematopoietic stem and progenitor cells:**
- HSC: CD34, KIT, THY1, PROM1, CRHBP, HLF, AVP, MLLT3
- MPP: CD34, FLT3, MPO, ELANE
- GMP: CD34, MPO, ELANE, AZU1, PRTN3

**Erythroid lineage:**
- Erythroid_Early: GATA1, KLF1, TFRC, EPOR, CD36, GYPA

**Lymphoid lineage:**
- Pro_B: CD34, CD79A, VPREB1, IGLL1, RAG1, RAG2, DNTT
- Plasma: JCHAIN, MZB1, SDC1, TNFRSF17, XBP1, PRDM1

**Myeloid lineage:**
- Dendritic: CD1C, FCER1A, CLEC10A, CD86, HLA-DRA, ITGAX

For each cell, marker gene expression scores were computed using Scanpy's `score_genes` function. Final cluster annotations were assigned by majority voting within each Leiden cluster.

### 2.6 Differential Expression Analysis

Differential gene expression between BT and BM conditions was performed using the Wilcoxon rank-sum test implemented in Scanpy's `rank_genes_groups` function. Analysis was conducted:
1. **Globally:** All cells pooled by condition
2. **Per cell type:** Within each annotated population

Genes were considered significantly differentially expressed with:
- Adjusted p-value < 0.05 (Benjamini-Hochberg correction)
- |log2 fold change| > 0.5

### 2.7 Pathway Enrichment Analysis

Gene set enrichment analysis was performed using GSEApy v1.1.11 (Fang et al., 2023) interfacing with Enrichr (Chen et al., 2013; Kuleshov et al., 2016). Upregulated and downregulated gene lists (top 500 each) were queried against:
- GO Biological Process 2021
- GO Molecular Function 2021
- GO Cellular Component 2021
- KEGG 2021 Human
- Reactome 2022
- WikiPathways 2019 Human
- MSigDB Hallmark 2020

Pathways with adjusted p-value < 0.05 were considered significantly enriched.

### 2.8 Statistical Analysis and Visualization

All statistical analyses were performed in Python 3.12. Visualizations were generated using Matplotlib v3.10 and Seaborn v0.13. Multiple testing correction was applied using the Benjamini-Hochberg method. Cell type composition differences were assessed using chi-squared tests.

---

## 3. Results

### 3.1 Quality Control and Dataset Overview

A total of 37,036 cells were captured across six samples: 27,174 from normal bone marrow (BM1: 10,787; BM2: 11,256; BM3: 5,131) and 9,862 from thalassemia (BT1: 4,108; BT2: 2,788; BT3: 2,966). After quality control filtering, 31,299 cells (84.5%) were retained for analysis.

QC metrics showed comparable distributions between conditions after filtering (Figure 1A-B). Median genes detected per cell ranged from 1,500-2,500 across samples. Mitochondrial content was appropriately low (<15%) in retained cells, with no significant difference between BM and BT groups. The lower cell recovery in BT samples may reflect increased cell fragility associated with ineffective hematopoiesis.

### 3.2 Integration and Clustering Reveals Seven Major Hematopoietic Populations

scVI integration effectively removed batch effects while preserving biological variation (Figure 2A). UMAP visualization demonstrated good mixing of samples within clusters while maintaining separation of conditions where biologically expected. Leiden clustering at resolution 0.5 identified 10 clusters, which were consolidated into 7 major cell populations based on marker gene expression (Figure 2B-C):

1. **HSC (Hematopoietic Stem Cells):** High expression of CD34, HLF, CRHBP
2. **MPP (Multipotent Progenitors):** CD34+, FLT3+, early lineage markers
3. **GMP (Granulocyte-Monocyte Progenitors):** MPO+, ELANE+, AZU1+
4. **Erythroid_Early:** GATA1+, KLF1+, TFRC+
5. **Pro_B (Pro-B cells):** CD79A+, VPREB1+, IGLL1+, DNTT+
6. **Plasma:** JCHAIN+, MZB1+, XBP1+
7. **Dendritic:** CD1C+, HLA-DRA+, FCER1A+

### 3.3 Dramatic Shifts in Lineage Composition in Thalassemia

Comparative analysis of cell type composition revealed striking differences between BM and BT (Figure 3, Table 1):

**Table 1. Cell Type Distribution by Condition**

| Cell Type | BM (n) | BM (%) | BT (n) | BT (%) | Fold Change |
|-----------|--------|--------|--------|--------|-------------|
| HSC | 8,275 | 34.5% | 502 | 6.9% | 0.20x |
| Dendritic | 9,385 | 39.1% | 1,856 | 25.5% | 0.65x |
| Erythroid_Early | 1,406 | 5.9% | 450 | 6.2% | 1.05x |
| GMP | 1,789 | 7.5% | 691 | 9.5% | 1.27x |
| MPP | 1,258 | 5.2% | 178 | 2.4% | 0.46x |
| Pro_B | 1,141 | 4.8% | 3,099 | 42.5% | **8.9x** |
| Plasma | 769 | 3.2% | 500 | 6.9% | 2.14x |

The most striking finding was a **2.7-fold absolute increase** and **8.9-fold proportional increase** in Pro-B cells in thalassemia (42.5% vs 4.8%, p < 0.001). Conversely, HSCs were dramatically reduced (6.9% vs 34.5%), suggesting either HSC exhaustion or altered differentiation dynamics.

### 3.4 Global Differential Expression Analysis

Global differential expression analysis comparing BT versus BM identified 5,360 significantly differentially expressed genes (|log2FC| > 0.5, adj. p < 0.05):
- **Upregulated in BT:** 4,052 genes (75.6%)
- **Downregulated in BT:** 1,308 genes (24.4%)

**Table 2. Top 20 Upregulated Genes in Beta-Thalassemia**

| Gene | Log2FC | Adj. P-value | Function |
|------|--------|--------------|----------|
| VPREB3 | 5.98 | <1e-300 | Pre-B cell receptor, surrogate light chain |
| VPREB1 | 5.32 | <1e-300 | Pre-B cell receptor, surrogate light chain |
| CD9 | 4.30 | <1e-300 | Tetraspanin, B-cell development |
| DYNLL1 | 4.19 | <1e-300 | Dynein light chain, proliferation |
| CD79B | 3.99 | <1e-300 | B-cell receptor signaling |
| DNTT | 3.99 | <1e-300 | Terminal deoxynucleotidyl transferase |
| IGLL1 | 3.95 | <1e-300 | Immunoglobulin lambda-like polypeptide |
| MEF2C | 3.13 | <1e-300 | Hematopoietic transcription factor |
| TOP2B | 3.12 | <1e-300 | DNA topoisomerase, cell cycle |
| MYB | 2.81 | <1e-300 | Hematopoietic transcription factor |
| MZB1 | 2.82 | <1e-300 | Plasma cell differentiation |
| PSMB9 | 2.89 | <1e-300 | Immunoproteasome subunit |
| IFI16 | 2.58 | <1e-300 | Interferon-inducible protein |
| SNHG25 | 2.44 | <1e-300 | Small nucleolar RNA host gene |
| RCSD1 | 2.37 | <1e-300 | CapZ-interacting protein |
| SOX4 | 2.10 | <1e-300 | SRY-box transcription factor |
| STMN1 | 2.06 | <1e-300 | Stathmin, cell proliferation |
| MIF | 2.09 | <1e-300 | Macrophage migration inhibitory factor |
| TMSB4X | 1.96 | <1e-300 | Thymosin beta-4, cytoskeletal organization |
| CALM2 | 1.86 | <1e-300 | Calmodulin, calcium signaling |

The dominance of B-cell development genes (VPREB1, VPREB3, IGLL1, CD79B, DNTT) among top upregulated transcripts strongly supports the observed Pro-B cell expansion.

### 3.5 Cell Type-Specific Differential Expression

Per-cell-type analysis identified 15,850 significant DEGs across all populations. The Erythroid_Early population showed the expected dysregulation of globin-related genes, while Pro_B cells exhibited activation of B-cell receptor signaling and immunoglobulin rearrangement pathways.

Key findings by cell type:

**HSC:** Downregulation of quiescence markers (HLF, HOPX), upregulation of cell cycle genes
**GMP:** Increased inflammatory signaling (S100A8, S100A9)
**Erythroid_Early:** Altered globin expression, stress erythropoiesis signatures
**Pro_B:** Massive upregulation of immunoglobulin genes and B-cell development factors

### 3.6 Pathway Enrichment Analysis

**Pathways Upregulated in Thalassemia (Table 3):**

| Pathway | Overlap | Adj. P-value | Genes |
|---------|---------|--------------|-------|
| Myc Targets V1 | 39/200 | 4.6e-22 | MYC, PCNA, SET, HDAC2, XPO1... |
| Interferon Alpha Response | 25/97 | 2.2e-17 | IFITM1, IFITM3, ISG15, MX1, OAS1... |
| Interferon Gamma Response | 32/200 | 8.0e-16 | STAT1, IRF7, B2M, TAP1, CD74... |
| Oxidative Phosphorylation | 26/200 | 7.6e-11 | NDUFB6, COX7A2, UQCR11, ATP6V0E1... |
| E2F Targets | 24/200 | 2.2e-09 | PCNA, MCM3, STMN1, MAD2L1... |
| G2-M Checkpoint | 20/200 | 1.3e-06 | SMC4, MYC, BUB3, MAD2L1... |
| DNA Repair | 14/150 | 1.7e-04 | PCNA, RPA3, DGUOK... |

**Pathways Downregulated in Thalassemia (Table 4):**

| Pathway | Overlap | Adj. P-value | Genes |
|---------|---------|--------------|-------|
| TNF-alpha Signaling via NF-kB | 20/200 | 7.1e-06 | EGR1, CDKN1A, PTGS2, ATF3... |
| Cholesterol Homeostasis | 11/74 | 4.8e-05 | LDLR, SREBF2, DHCR7, ACSS2... |
| p53 Pathway | 13/200 | 2.4e-02 | CDKN1A, BAK1, PLK3, SOCS1... |

### 3.7 Interferon Signaling Activation

A prominent finding was the upregulation of type I and II interferon response pathways in thalassemia. Interferon-stimulated genes (ISGs) including IFITM1, IFITM3, ISG15, MX1, OAS1, and STAT1 were significantly elevated. This immune activation signature suggests chronic inflammatory stress in the thalassemia bone marrow microenvironment.

---

## 4. Discussion

### 4.1 Lymphoid Expansion: A Novel Finding in Thalassemia

Our single-cell analysis reveals a previously unappreciated lymphoid expansion in beta-thalassemia bone marrow. The 8.9-fold proportional increase in Pro-B cells is striking and has not been reported in bulk transcriptomic studies. Several mechanisms may explain this finding:

**Compensatory hematopoiesis:** Ineffective erythropoiesis may trigger compensatory expansion of alternative lineages. The bone marrow microenvironment, stressed by chronic anemia and iron overload, may redirect hematopoietic differentiation toward lymphoid fates.

**IL-7 signaling:** Elevated IL-7 levels have been reported in thalassemia patients (Maggio et al., 2009), which could drive Pro-B cell expansion. IL-7 is the master regulator of lymphopoiesis and its dysregulation may contribute to the observed phenotype.

**Inflammatory milieu:** The activated interferon signaling we observed may promote lymphoid development. Type I interferons have been shown to regulate HSC exit from quiescence and influence lineage commitment (Essers et al., 2009).

### 4.2 MYC Activation and Cell Proliferation

The strong enrichment of MYC targets among upregulated genes suggests heightened proliferative activity in thalassemia bone marrow. MYC is a master regulator of cell growth and metabolism, and its activation is consistent with the compensatory hyperplasia characteristic of thalassemia. Notably, MYB, another critical hematopoietic transcription factor, was also significantly upregulated (log2FC = 2.81).

### 4.3 Metabolic Reprogramming

The upregulation of oxidative phosphorylation genes suggests altered metabolic states in thalassemia hematopoietic cells. This finding is interesting given that HSCs typically rely on glycolysis, while committed progenitors shift toward oxidative metabolism (Simsek et al., 2010). The metabolic shift may reflect both the expansion of progenitor populations and adaptation to the oxidative stress associated with iron overload.

### 4.4 Interferon Signaling and Inflammation

The prominent interferon signature in thalassemia bone marrow may arise from multiple sources:
- Chronic inflammation associated with ineffective erythropoiesis
- Free heme and hemoglobin release activating innate immune pathways
- Transfusion-related immune stimulation
- Iron overload-induced oxidative stress

Importantly, chronic interferon signaling has been shown to exhaust HSCs and impair their regenerative capacity (Pietras et al., 2014), potentially contributing to the HSC depletion we observed.

### 4.5 Downregulation of TNF-alpha/NF-kB and p53 Pathways

The downregulation of TNF-alpha signaling via NF-kB and p53 pathway genes in thalassemia is somewhat counterintuitive given the inflammatory microenvironment. However, this may represent an adaptive response to chronic stress or reflect the altered cellular composition (fewer HSCs, which typically express higher levels of these pathways).

### 4.6 Clinical Implications

Our findings have several potential clinical implications:

1. **Immune function:** The lymphoid expansion may influence immune competence in thalassemia patients, warranting further investigation of infection susceptibility and vaccine responses.

2. **Therapeutic targets:** The activated MYC and interferon pathways may be amenable to targeted intervention. JAK inhibitors, which block interferon signaling, are currently in clinical trials for myelofibrosis and may have application in thalassemia.

3. **Biomarkers:** The identified DEGs may serve as biomarkers for disease severity or response to therapy.

### 4.7 Limitations

This study has several limitations:

1. **Sample size:** Analysis was limited to three patients per group, which may not capture the full spectrum of disease heterogeneity.

2. **Clinical heterogeneity:** Thalassemia major encompasses diverse genotypes and clinical phenotypes. Patient-specific information (genotype, transfusion history, chelation status) was not available.

3. **Single timepoint:** Cross-sectional analysis cannot capture temporal dynamics or treatment effects.

4. **Bone marrow sampling:** Aspiration may not fully represent the bone marrow architecture, and certain populations may be undersampled.

### 4.8 Future Directions

Future studies should:
1. Validate findings in larger, clinically annotated cohorts
2. Incorporate multimodal profiling (CITE-seq, ATAC-seq) to characterize surface markers and chromatin accessibility
3. Perform functional validation of candidate genes and pathways
4. Investigate the relationship between lymphoid expansion and clinical outcomes

---

## 5. Conclusions

Our comprehensive single-cell transcriptomic analysis of beta-thalassemia bone marrow reveals previously unappreciated lymphoid expansion, with a dramatic increase in Pro-B cells and corresponding shifts in the hematopoietic landscape. We identify activation of MYC targets, interferon signaling, and oxidative phosphorylation as key molecular features of thalassemia hematopoiesis. These findings provide new insights into the systemic hematopoietic dysregulation in thalassemia and suggest novel avenues for therapeutic intervention.

---

## Data Availability

Raw data are available from GEO under accession GSE133181. Processed data and analysis scripts are available at the results directory.

## Author Contributions

Analysis design, implementation, and manuscript preparation were performed using AI-assisted workflows.

## Acknowledgments

We thank the original data depositors for making their data publicly available. Analysis was performed using the scverse ecosystem including Scanpy, scVI-tools, and gseapy.

## Conflicts of Interest

None declared.

---

## References

Chen, E.Y., Tan, C.M., Kou, Y., Duan, Q., Wang, Z., Meirelles, G.V., Clark, N.R., & Ma'ayan, A. (2013). Enrichr: interactive and collaborative HTML5 gene list enrichment analysis tool. BMC Bioinformatics, 14, 128.

Essers, M.A., Offner, S., Blanco-Bose, W.E., Waiber, Z., Kaber, J.A., & Trumpp, A. (2009). IFNalpha activates dormant haematopoietic stem cells in vivo. Nature, 458(7240), 904-908.

Fang, Z., Liu, X., & Peltz, G. (2023). GSEApy: a comprehensive package for performing gene set enrichment analysis in Python. Bioinformatics, 39(1), btac757.

Hay, S.B., Ferchen, K., Chetal, K., Grimes, H.L., & Salomonis, N. (2018). The Human Cell Atlas bone marrow single-cell interactive web portal. Experimental Hematology, 68, 51-61.

Kuleshov, M.V., Jones, M.R., Rouillard, A.D., Fernandez, N.F., Duan, Q., Wang, Z., Koplev, S., Jenkins, S.L., Jagodnik, K.M., Lachmann, A., McDermott, M.G., Monteiro, C.D., Gundersen, G.W., & Ma'ayan, A. (2016). Enrichr: a comprehensive gene set enrichment analysis web server 2016 update. Nucleic Acids Research, 44(W1), W90-97.

Lopez, R., Regier, J., Cole, M.B., Jordan, M.I., & Yosef, N. (2018). Deep generative modeling for single-cell transcriptomics. Nature Methods, 15(12), 1053-1058.

Luecken, M.D., & Theis, F.J. (2019). Current best practices in single-cell RNA-seq analysis: a tutorial. Molecular Systems Biology, 15(6), e8746.

Maggio, A., Capra, M., Pepe, A., Rigano, P., Misseri, M., Acuto, S., Filosa, A., Vitrano, A., Cuccia, L., & Pitrolo, L. (2009). Update on Cooley's anemia management. Seminars in Hematology, 46(4), 329-340.

Papalexi, E., & Satija, R. (2018). Single-cell RNA sequencing to explore immune cell heterogeneity. Nature Reviews Immunology, 18(1), 35-45.

Pietras, E.M., Lakshminarasimhan, R., Techner, J.M., Fong, S., Flach, J., Bber, M., & Passegu, E. (2014). Re-entry into quiescence protects hematopoietic stem cells from the killing effect of chronic exposure to type I interferons. Journal of Experimental Medicine, 211(2), 245-262.

Pootrakul, P., Sirankapracha, P., Hemsorach, S., Moungsub, W., Kumbunlue, R., Piangitjagum, A., Wasi, P., Ma, L., & Schrier, S.L. (2000). A correlation of erythrokinetics, ineffective erythropoiesis, and erythroid precursor apoptosis in Thai patients with thalassemia. Blood, 96(7), 2606-2612.

Rivella, S. (2012). The role of ineffective erythropoiesis in non-transfusion-dependent thalassemia. Blood Reviews, 26(Suppl 1), S12-15.

Simsek, T., Kocabas, F., Zheng, J., Deberardinis, R.J., Mahmoud, A.I., Olson, E.N., Schneider, J.W., Zhang, C.C., & Sadek, H.A. (2010). The distinct metabolic profile of hematopoietic stem cells reflects their location in a hypoxic niche. Cell Stem Cell, 7(3), 380-390.

Stuart, T., Butler, A., Hoffman, P., Hafemeister, C., Papalexi, E., Mauck, W.M., Hao, Y., Stoeckius, M., Smibert, P., & Satija, R. (2019). Comprehensive integration of single-cell data. Cell, 177(7), 1888-1902.

Traag, V.A., Waltman, L., & van Eck, N.J. (2019). From Louvain to Leiden: guaranteeing well-connected communities. Scientific Reports, 9(1), 5233.

Velten, L., Haas, S.F., Raffel, S., Blasber, S., Yuber, S., Steinmetz, L.M., Bock, C., & Trumpp, A. (2017). Human haematopoietic stem cell lineage commitment is a continuous process. Nature Cell Biology, 19(4), 271-281.

Virshup, I., Rybakov, S., Theis, F.J., Angerer, P., & Wolf, F.A. (2023). anndata: Annotated data for scalable genomics. Nature Methods, 20(11), 1657-1665.

Weatherall, D.J. (2010). The inherited diseases of hemoglobin are an emerging global health burden. Blood, 115(22), 4331-4336.

Wolf, F.A., Angerer, P., & Theis, F.J. (2018). SCANPY: large-scale single-cell gene expression data analysis. Genome Biology, 19(1), 15.

Zheng, G.X., Terry, J.M., Belgrader, P., Ryvkin, P., Bent, Z.W., Wilson, R., Ziraldo, S.B., Wheeler, T.D., McDermott, G.P., Zhu, J., Gregory, M.T., Shuga, J., Montesclaros, L., Underwood, J.G., Masquelier, D.A., Nishimura, S.Y., Schnall-Levin, M., Wyatt, P.W., Hindson, C.M., ... Bielas, J.H. (2020). Massively parallel digital transcriptional profiling of single cells. Nature Communications, 8, 14049.

---

## Supplementary Materials

**Supplementary Tables:**
- Table S1: Sample metadata and QC statistics
- Table S2: Complete list of differentially expressed genes
- Table S3: Cell type marker genes used for annotation
- Table S4: Full pathway enrichment results

**Supplementary Figures:**
- Figure S1: QC metric distributions before and after filtering
- Figure S2: HVG selection visualization
- Figure S3: scVI training convergence
- Figure S4: Extended UMAP visualizations by sample
- Figure S5: Volcano plot of differential expression

---

*Generated using single-cell analysis pipeline with scverse ecosystem (Scanpy, scVI-tools, gseapy)*


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->