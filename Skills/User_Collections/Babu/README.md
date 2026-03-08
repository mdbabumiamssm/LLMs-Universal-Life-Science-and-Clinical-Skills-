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

# Custom Claude Skills for MD BABU MIA, PhD

## Professor of Hematology & Medical Oncology | Mount Sinai

A comprehensive set of specialized skills for Claude, tailored to computational software development, bioinformatics research, single-cell multi-omics, MPN research, and scientific publication workflows.

---

## 📦 Skills Included

| Skill | Description | Use Cases |
|-------|-------------|-----------|
| **computational-software-development** | Full-stack biomedical AI platforms, clinical decision support, multi-LLM ensembles | BioMedAI, MPN Clinical Software, RAG pipelines, Flask apps, PyTorch models |
| **bioinformatics-singlecell** | scRNA-seq, scCITE-seq, scATAC-seq, TotalVI | Cell type annotation, differential expression, UMAP/clustering |
| **ngs-analysis** | Bulk RNA-seq, variant calling, QC pipelines | STAR/Salmon alignment, DESeq2, GATK somatic calling |
| **python-package-builder** | PyPI package development | Converting scripts to pip packages, CLI tools, testing |
| **scientific-manuscript** | High-impact journal writing | Blood, Nature, Cell manuscript preparation, ICMJE compliance |
| **data-visualization-biomedical** | Publication-quality figures | Volcano plots, heatmaps, multi-panel figures |
| **mpn-research-assistant** | MPN domain expertise | JAK2/CALR mutations, PPM1D pathway, fibrosis markers |

---

## 🚀 Installation for Claude Code (Terminal CLI)

### Method 1: Direct Copy to Skills Directory

```bash
# Navigate to your Claude Code skills directory
# On macOS/Linux:
mkdir -p ~/.claude/skills/user

# Copy all skills
cp -r /path/to/skills-for-babu/* ~/.claude/skills/user/
```

### Method 2: Using Claude Code CLI

```bash
# If using Claude Code with custom skills support
claude-code skills install ./skills-for-babu/

# Or install individual skills
claude-code skills install ./skills-for-babu/bioinformatics-singlecell/
claude-code skills install ./skills-for-babu/mpn-research-assistant/
```

### Method 3: Environment Variable Configuration

```bash
# Add to your .bashrc or .zshrc
export CLAUDE_SKILLS_PATH="$HOME/.claude/skills:$HOME/custom-skills"

# Place skills in $HOME/custom-skills/
cp -r skills-for-babu/* ~/custom-skills/
```

---

## 📁 Directory Structure

```
skills-for-babu/
├── computational-software-development/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── bioinformatics-singlecell/
│   ├── SKILL.md
│   ├── references/
│   │   └── cell_markers.md
│   ├── scripts/
│   └── assets/
├── ngs-analysis/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── python-package-builder/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── scientific-manuscript/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── data-visualization-biomedical/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── mpn-research-assistant/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
└── README.md
```

---

## 🔧 Usage Examples

### Computational Software Development
```
User: Build a multi-LLM ensemble for biomedical literature search with citation verification
Claude: [Triggers computational-software-development skill]
```

### Single-Cell Analysis
```
User: Analyze my CITE-seq data using TotalVI for MPN patient samples
Claude: [Triggers bioinformatics-singlecell skill]
```

### Manuscript Writing
```
User: Write a discussion section for our PPM1D paper in Blood journal format
Claude: [Triggers scientific-manuscript + mpn-research-assistant skills]
```

### Package Development
```
User: Convert my GEO search script into a pip package
Claude: [Triggers python-package-builder skill]
```

### Visualization
```
User: Create a volcano plot with highlighted MK markers
Claude: [Triggers data-visualization-biomedical skill]
```

---

## 🧬 MPN-Specific Features

- Driver mutation analysis (JAK2, CALR, MPL)
- HMR mutation cataloging
- PPM1D pathway expertise
- Megakaryocyte subtype markers
- Fibrosis scoring genes
- Clinical trial data (BOREAS, idasanutlin)
- MIPSS70+ prognostic scoring

---

## 📊 Supported Technologies

### Computational Software Development
- Multi-LLM ensemble (Claude, GPT, Gemini APIs)
- PyTorch deep learning, Transformers, sentence-transformers
- FAISS vector databases, hybrid RAG (dense + sparse)
- Flask web applications, async/await patterns
- Conformal prediction, SHAP explainability

### Bioinformatics
- Scanpy, Seurat, scvi-tools, Muon
- STAR, Salmon, BWA-MEM2
- DESeq2, edgeR, Wilcoxon tests
- 10x Genomics, Smart-seq2

### Visualization
- Matplotlib, Seaborn, Plotly
- scanpy plotting suite
- Publication-ready exports (PDF, SVG, PNG)

### Python Development
- pyproject.toml (modern packaging)
- Click CLI framework
- pytest testing
- GitHub Actions CI/CD

---

## 📝 Author

**MD BABU MIA, PhD**  
Assistant Professor of Medicine (Hematology & Medical Oncology)  
Icahn School of Medicine at Mount Sinai  
📧 md.babu.mia@mssm.edu  
🔗 GitHub: @mdbabumiamssm

---

## 📄 License

Proprietary - For personal use by MD BABU MIA

---

## 🔄 Updates

To update skills, simply replace the SKILL.md files with new versions.
Skills are loaded fresh on each Claude Code session.


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
## Recent Additions

| Skill | Description | Use Cases |
|-------|-------------|-----------|
| **skill-library-maintainer** | Audit and curate large skill repositories | Metadata cleanup, frontmatter normalization, reference splitting, validation |
| **biomedical-rag-citation-pipelines** | Citation-grounded biomedical retrieval and generation | PubMed or PMC RAG, claim-to-citation validation, grounded answer evaluation |
