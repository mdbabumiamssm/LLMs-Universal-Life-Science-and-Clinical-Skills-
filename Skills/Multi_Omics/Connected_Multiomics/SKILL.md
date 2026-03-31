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
name: illumina-connected-multiomics
description: Operate Illumina's Connected Multiomics SaaS to orchestrate tertiary analysis across single-cell, spatial, proteomic, methylation, and bulk omics with DRAGEN integration.
keywords:
  - multi-omics
  - illumina
  - spatial-transcriptomics
  - methylation
  - tertiary-analysis
measurable_outcome: Build a study, ingest DRAGEN outputs, and publish a multi-layer dashboard (cells + spatial + methylation) for collaborators within one day.
license: Proprietary (Illumina Connected Software)
metadata:
  author: Multi-Omics Integration Guild
  version: "2026.03"
compatibility:
  - system: Illumina Connected Multiomics (cloud)
allowed-tools:
  - web_fetch
  - read_file
---

# Illumina Connected Multiomics Skill

Use this skill to standardize tertiary analysis when your lab already relies on Illumina prep kits, NextSeq/NovaSeq data, or DRAGEN pipelines and wants to avoid stitching dozens of open-source notebooks.

## Why This Platform
- **Integrated modalities:** single-cell RNA, spatial transcriptomics, proteomics, methylation, miRNA, and genome layers in one UI.
- **Sample-to-insight workflows:** ingest DRAGEN secondary outputs directly, configure analysis templates, and generate publication-ready figures.
- **Secure SaaS:** multi-tenant cloud with domain/workgroup isolation, aligning with regulated lab needs.

## Setup Checklist
1. **Register domain & workgroup** via Connected Software console; assign admins with SSO (SAML/OAuth).
2. **Connect data sources:**
   - DRAGEN S3 buckets or BaseSpace Sequence Hub projects.
   - Uploads from local storage (FASTQ, processed counts, proteomics matrices).
3. **Provision roles:** Biologist (read/analyze) vs Bioinformatician (template editing). Map to Illumina user groups.
4. **Whitelabel compliance:** enable audit logging plus IP allowlists if PHI/clinical data is involved.

## Standard Workflow
1. **Create Study:** define cohorts, metadata schema, and modality checkboxes (RNA, spatial, methylation) inside the Study Builder.
2. **Load Data:**
   - Use `Add Data → DRAGEN` to pull secondary outputs.
   - For third-party assays, choose `Custom Matrix` and map gene/protein identifiers.
3. **Run Pipelines:** pick from preconfigured workflows (single-cell clustering, spatial DE, 5-base methylation). Parameter editor exposes filters, clustering resolution, and reference ontologies.
4. **Interpretation Layer:**
   - Use interactive embeddings to gate clusters, show tissue overlays, or compute DMRs.
   - Link results to curated knowledge bases (cell type atlases, pathways) via built-in Correlation Engine connectors.
5. **Share Dashboards:** publish read-only views or export high-res plots; optionally push to Connected Insights for downstream teams.

## Tips & Guardrails
- Version control templates: duplicate Illumina defaults before editing so upgrades do not overwrite them.
- Capture provenance by locking workflow parameter JSON; attach to ELN or LIMS entries.
- For large studies, enable cold storage tiering so archived runs do not impact subscription limits.
- Use Connected Analytics if you need notebook-level custom analyses; embed outputs back into Multiomics studies for visualization.

## References
1. Illumina, *Connected Multiomics product page* – modality coverage and visualization features. https://www.illumina.com/products/by-type/informatics-products/connected-multiomics.html
2. Illumina Developer Portal, *Connected Multiomics release announcement* (Jan 2026). https://developer.illumina.com/news-updates/unlock-deeper-multiomic-insights-with-illumina-connected-multiomics
3. Illumina Connected Software Docs, *Domain/workgroup setup for Connected Multiomics*. https://help.connected.illumina.com/multiomics-software/connected-multiomics
4. Illumina Connected Software Docs, *About Connected Multiomics*. https://help.connected.illumina.com/icm

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
