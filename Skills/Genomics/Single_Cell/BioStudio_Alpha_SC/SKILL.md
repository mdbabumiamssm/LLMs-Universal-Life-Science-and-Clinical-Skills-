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

---
name: biostudio-alpha-sc
description: Run BioTuring's BioStudio Alpha SC GPU stack to accelerate single-cell and spatial multi-omics analysis on NVIDIA Blackwell-class hardware.
keywords:
  - single-cell
  - gpu-acceleration
  - biostudio
  - spatial-transcriptomics
  - multi-omics
measurable_outcome: Process a 1+ million cell atlas (10x HDF5 or FASTQ) end-to-end in BioStudio Alpha SC with QC, clustering, and annotation layers inside one work session.
license: Proprietary (BioTuring EULA)
metadata:
  author: Single-Cell Systems Team
  version: "2026.03"
compatibility:
  - system: BioStudio Alpha SC (cloud or on-prem)
  - system: NVIDIA Blackwell / Hopper GPUs w/ 32GB+ VRAM
allowed-tools:
  - web_fetch
  - read_file
  - run_shell_command
---

# BioStudio Alpha SC Skill

Alpha SC combines BioStudio's GPU-native runtime with curated notebooks so you can ingest scRNA-seq, ATAC, and spatial assays without writing boilerplate pipelines.

## When to Use
- Projects that regularly exceed laptop memory/GPU budgets.
- Cohorts that mix single-cell RNA, spatial transcriptomics, protein panels, or metabolomic overlays.
- Teams that need turnkey NVIDIA Blackwell acceleration with enterprise support.

## Key Capabilities
1. **GPU streaming engine:** Alpha SC offloads PCA, UMAP, Leiden/Phenograph, and batch correction to NVIDIA Blackwell GPUs for 10–30× speedups over CPU clusters.
2. **Unified workbench:** Launch JupyterLab, RStudio, and the BioStudio GUI from one workspace; swap between code and visual layers without data copies.
3. **Cross-modal viewers:** Synchronized single-cell, Visium/Xenium, and CODEX panels for neighborhood statistics.
4. **Notebook library:** Ready-to-run notebooks for QC, trajectory (PyTorch/Scanpy), perturb-seq scoring, and AI copilots for annotation.
5. **Data fabric:** Native connectors for 10x Genomics Cloud, AWS S3, and BioTuring Atlas (45M+ cells) so you can join public atlases with in-house data.

## Setup Checklist
1. **Provision workspace:**
   - Cloud BioStudio account (`Alpha SC` tier) or on-prem appliance with Blackwell GPUs.
   - Attach at least 2×2TB NVMe scratch plus S3-compatible object store for raw FASTQ backup.
2. **Sync data:**
   ```bash
   bs sync --source s3://lab-mpn/raw_fastq/ --target /work/raw_fastq/
   bs convert tenx --input patient1/outs --output /work/h5/alpha_sc/
   ```
3. **Launch environment:** Use the Control Room to start an `Alpha SC` session (recommended: 4 Blackwell GPUs, 512 GB RAM). Enable the `Spatial Explorer` add-on if you have Visium/Xenium slides.
4. **Install add-ons (once per workspace):**
   ```bash
   pip install --user biostudio-alpha-sc kitsune-trajectory==0.7.1
   bs plugins enable ai-annotation
   ```

## Standard Workflow
1. **Quality Control Notebook:** `notebooks/alpha_sc_qc.ipynb`
   - Run ambient RNA removal, mitochondrial filters, and doublet detection.
   - Persist metrics to `/work/results/qc_summary.parquet` for downstream dashboards.
2. **Batch Harmonization:** `scripts/run_scvi_bridge.py`
   - Auto-detects donors/technologies, trains scVI on GPUs, writes harmonized `.h5ad`.
3. **Clustering & Annotation:**
   - Use `Alpha Annotator` (LLM-assisted) to propose marker panels, then verify with manual gating.
   - Export label sets as `.csv` for EMR ingestion.
4. **Spatial Overlay:**
   - Load Visium/Xenium data into the `Spatial Explorer` tab, align with single-cell UMAP clusters, compute ligand-receptor neighborhoods.
5. **Reporting:**
   - Use `biostudio report create --template mpn-clinical.yaml` to bundle figures + provenance, ready for BioTuring Hub or PDF export.

## Tips & Guardrails
- Keep raw + processed layers separate; Alpha SC snapshots entire workspaces, so use object storage lifecycle policies to control cost.
- AI annotation copilots make suggestions—lock final labels only after manual/marker validation.
- Pin notebooks before sharing with clinical collaborators so inference environments remain reproducible.
- For HIPAA/PHI, enable the BioStudio private VPC deployment with audit logging.

## References
1. BioStudio, *Alpha SC GPU-accelerated single-cell stack (Blackwell architecture)*. https://www.biostudio.ai/alpha-sc
2. BioStudio, *Integrated BioStudio platform overview (AI, visualization, HPC)*. https://www.biostudio.ai/
3. BioStudio, *BioStudio B105 workstation for multi-omics acceleration*. https://www.biostudio.ai/b105
4. BioStudio, *BioStudio Alpha SC documentation hub (Beta3 release notes)*. https://help.biostudio.ai/hc/en-us/articles/alpha-sc-beta3

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
