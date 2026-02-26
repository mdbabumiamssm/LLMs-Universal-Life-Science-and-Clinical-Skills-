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

# 📋 Comprehensive Skills List for MD BABU MIA, PhD

## Summary of Custom Claude Skills

Based on your profile as a Hematology/Medical Oncology Professor at Mount Sinai with expertise in computational software development, single-cell multi-omics, bioinformatics, and MPN research.

---

## 1️⃣ computational-software-development

**Trigger phrases:**
- "Build AI platform"
- "Multi-LLM ensemble"
- "Clinical decision support system"
- "RAG pipeline"
- "Flask web application"
- "Deep learning for clinical data"
- "Citation verification"
- "Biomedical software"
- "Single-cell analysis tool"
- "PyTorch model"

**Core capabilities:**
- Multi-LLM ensemble architectures (Claude + GPT + Gemini parallel execution)
- Hybrid RAG v3.0 with dense (FAISS) + sparse (BM25) retrieval fusion
- Real-time citation validation (97.8% accuracy) via PubMed API
- Span-level claim verification (92% hallucination reduction)
- Clinical decision support with deep learning ensembles (PyTorch)
- Conformal prediction for uncertainty quantification (90% coverage)
- SHAP-based model explainability for clinical transparency
- Flask web applications with async/await patterns
- Single-cell analysis tools (cellidentifierdx, scvi-tools patterns)
- Production-ready Python package distribution (PyPI)

**Project Portfolio:**
- BioMedAI/LifeScienceBrowser: Multi-LLM biomedical research platform
- MPN Clinical Software V3.0: Myelofibrosis risk stratification system
- cellidentifierdx, tahoe-x1, babu-scvi-tools: Single-cell analysis tools
- Biomedical-Genomics-Personalized-Reasoning-LLM-Agent

---

## 2️⃣ bioinformatics-singlecell

**Trigger phrases:**
- "Analyze single-cell data"
- "scRNA-seq / scCITE-seq / scATAC-seq"
- "Cell type identification"
- "TotalVI integration"
- "UMAP clustering"
- "Differential expression in single cells"
- "Scanpy analysis"

**Core capabilities:**
- Complete scRNA-seq workflow (QC → normalization → clustering → annotation)
- CITE-seq protein + RNA integration with TotalVI
- Multi-batch integration and visualization
- Cell type marker libraries for hematopoiesis
- Publication-quality dot plots, UMAP, violin plots

---

## 3️⃣ ngs-analysis

**Trigger phrases:**
- "RNA-seq pipeline"
- "FASTQ processing"
- "Alignment with STAR/Salmon"
- "Differential expression DESeq2"
- "Variant calling"
- "GEO/SRA download"

**Core capabilities:**
- Complete bulk RNA-seq pipeline
- Quality control (FastQC, MultiQC, fastp)
- Alignment (STAR, BWA-MEM2)
- Quantification (featureCounts, Salmon)
- DESeq2/edgeR differential expression
- GATK somatic variant calling
- GEO/SRA data retrieval automation

---

## 4️⃣ python-package-builder

**Trigger phrases:**
- "Create pip package"
- "Convert script to package"
- "PyPI upload"
- "Package setup"
- "CLI tool development"
- "pyproject.toml"

**Core capabilities:**
- Modern pyproject.toml configuration
- CLI development with Click
- pytest testing framework
- GitHub Actions CI/CD
- PyPI/TestPyPI publishing
- Environment variable configuration

---

## 5️⃣ scientific-manuscript

**Trigger phrases:**
- "Write manuscript"
- "Discussion section"
- "Methods section"
- "Blood journal format"
- "Nature format"
- "Figure legend"
- "Statistical reporting"

**Core capabilities:**
- Journal-specific formatting (Blood, Nature, Cell)
- Structured abstract writing
- Methods with reproducibility standards
- Results with proper statistical reporting
- Discussion structure
- Figure legend templates
- HIPAA/IRB compliance language

---

## 6️⃣ data-visualization-biomedical

**Trigger phrases:**
- "Volcano plot"
- "Heatmap"
- "Publication figure"
- "Multi-panel figure"
- "Statistical annotation"
- "Export for journal"

**Core capabilities:**
- Publication-quality matplotlib settings
- Volcano plots with gene labels
- Hierarchically clustered heatmaps
- Scanpy enhanced visualizations
- Statistical significance annotations
- Multi-panel figure assembly
- Journal-ready exports (PDF, SVG, PNG at 300 DPI)

---

## 7️⃣ mpn-research-assistant

**Trigger phrases:**
- "MPN research"
- "Myelofibrosis"
- "JAK2 CALR MPL mutations"
- "PPM1D pathway"
- "Megakaryocyte markers"
- "Fibrosis genes"
- "MIPSS70 scoring"

**Core capabilities:**
- WHO 2022 MPN classification
- Driver mutation analysis (JAK2V617F, CALR types, MPL)
- HMR mutation cataloging
- PPM1D pathway expertise and therapeutic targets
- Megakaryocyte subtype markers
- Fibrosis gene signatures
- Clinical trial data interpretation (BOREAS, navtemadlin)
- Prognostic scoring (MIPSS70+ v2.0)

---

## 8️⃣ Medea Therapeutic Discovery Agent

**Trigger phrases:**
- "Run multi-omics therapeutic discovery pipeline"
- "Analyze omics data for novel drug targets using Medea"
- "Perform literature reasoning and consensus reconciliation"

**Core capabilities:**
- Multi-step omics research planning
- Transparent code execution for Python/R scripts
- Advanced literature reasoning and synthesis
- Consensus stage evidence reconciliation

---

## 9️⃣ MCPmed Bioinformatics Server

**Trigger phrases:**
- "Query STRING database via MCP"
- "Fetch dataset metadata from GEO using MCPmed"
- "Access UCSC Cell Browser data through MCP"

**Core capabilities:**
- Model Context Protocol (MCP) implementation for biological resources
- GEO dataset metadata retrieval
- STRING protein-protein interaction networks access
- UCSC Cell Browser programmatic integration

---

## 🔗 Skill Combinations

These skills are designed to work together:

| Task | Skills Used |
|------|-------------|
| Build clinical AI platform | computational-software-development + mpn-research-assistant |
| Multi-LLM research tool | computational-software-development + python-package-builder |
| Single-cell analysis software | computational-software-development + bioinformatics-singlecell |
| MPN single-cell analysis | bioinformatics-singlecell + mpn-research-assistant |
| Blood journal figure | data-visualization-biomedical + scientific-manuscript |
| DEG visualization | ngs-analysis + data-visualization-biomedical |
| PPM1D manuscript | scientific-manuscript + mpn-research-assistant |
| Bioinformatics tool development | python-package-builder + ngs-analysis |
| Clinical decision support manuscript | computational-software-development + scientific-manuscript |

---

## 📁 File Locations

After installation:

```
~/.claude/skills/user/
├── computational-software-development/SKILL.md
├── bioinformatics-singlecell/SKILL.md
├── ngs-analysis/SKILL.md
├── python-package-builder/SKILL.md
├── scientific-manuscript/SKILL.md
├── data-visualization-biomedical/SKILL.md
└── mpn-research-assistant/SKILL.md
```

---

## 🎯 Quick Reference Commands

```bash
# List installed skills
ls ~/.claude/skills/user/

# View a skill
cat ~/.claude/skills/user/bioinformatics-singlecell/SKILL.md

# Update a skill
nano ~/.claude/skills/user/mpn-research-assistant/SKILL.md
```

---

*Generated for MD BABU MIA, PhD - Mount Sinai*
*December 2025*


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->