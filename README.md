# LLMs Universal Life Science & Clinical Skills

**The Open-Source Operating System for Biomedical AI Agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Production](https://img.shields.io/badge/Status-Production-brightgreen.svg)]()
[![Platform: Multi-LLM](https://img.shields.io/badge/Platform-Claude%20%7C%20ChatGPT%20%7C%20Gemini-purple.svg)]()
[![Skills: 25+](https://img.shields.io/badge/Skills-25%2B-orange.svg)]()

---

## Mission

We build **production-ready, platform-agnostic biomedical AI skills** that empower researchers, clinicians, and developers to deploy advanced AI capabilities across any LLM interface. Whether you use **Claude**, **ChatGPT**, **Gemini**, or custom open-source models, our standardized skills deliver reproducible, validated results for real-world biomedical workflows.

---

## Skills Catalog

### Clinical Skills (8 skills)

| Skill | ID | Description |
|-------|-----|-------------|
| **Clinical Note Summarization** | `biomedical.clinical.note_summarization` | SOAP format clinical notes |
| **Trial Eligibility Agent** | `biomedical.clinical.trial_eligibility` | Patient-trial matching |
| **Precision Oncology Agent** | `biomedical.clinical.precision_oncology` | Multimodal cancer recommendations |
| **Medical Imaging AI** | `biomedical.clinical.medical_imaging` | CT/MRI/X-ray analysis (MONAI) |
| **Clinical NLP Toolkit** | `biomedical.clinical.clinical_nlp` | medspaCy, BioBERT extraction |
| **Digital Pathology** | `biomedical.clinical.digital_pathology` | WSI analysis (QuPath, histolab) |
| **EHR/FHIR Integration** | `biomedical.clinical.ehr_fhir_integration` | Healthcare interoperability |
| **Medical NER** | `biomedical.clinical.medical_ner` | Entity & relation extraction |

### Genomics Skills (7 skills)

| Skill | ID | Description |
|-------|-----|-------------|
| **Single-Cell RNA QC** | `biomedical.genomics.single_cell_qc` | MAD-based adaptive filtering |
| **CRISPR Design Agent** | `biomedical.genomics.crispr_design` | Guide RNA design & off-target |
| **Variant Annotation** | `biomedical.genomics.variant_annotation` | VEP, ClinVar, ACMG classification |
| **Proteomics/MS Analysis** | `biomedical.genomics.proteomics_ms` | AlphaPeptDeep, DeepLC |
| **Spatial Transcriptomics** | `biomedical.genomics.spatial_transcriptomics` | STAgent multimodal analysis |
| **Single-Cell Ecosystems** | `biomedical.genomics.single_cell` | scverse, Seurat, CellAgent |
| **Multi-Agent Workflows** | `biomedical.genomics.biomaster` | BioMaster pipelines |

### Drug Discovery Skills (5 skills)

| Skill | ID | Description |
|-------|-----|-------------|
| **Chemical Properties** | `biomedical.drug_discovery.chemical_properties` | RDKit molecular calculations |
| **AgentD Drug Discovery** | `biomedical.drug_discovery.agentd` | Early-stage discovery |
| **Protein Structure** | `biomedical.drug_discovery.protein_structure` | AlphaFold 2/3, OpenFold |
| **Knowledge Graph** | `biomedical.drug_discovery.knowledge_graph` | Drug repurposing (iKraph, PrimeKG) |
| **Antibody Design** | `biomedical.drug_discovery.antibody_design` | MAGE multistate design |

### Research Tools (3 skills)

| Skill | ID | Description |
|-------|-----|-------------|
| **Data Analysis** | `biomedical.research_tools.data_analysis` | Python, R, SQL, Tableau, Power BI |
| **General Agent (Biomni)** | `biomedical.research_tools.biomni` | 150+ biomedical tools |
| **BioMCP Servers** | `biomedical.mcp_servers.biomcp` | PubMed, ClinicalTrials.gov APIs |

---

## Repository Structure

```
skills/
├── src/                              # Main source code (GitHub submodule)
│   ├── Skills/                       # Production-ready skills
│   │   ├── Clinical/                 # 8 healthcare AI skills
│   │   │   ├── Clinical_Note_Summarization/
│   │   │   ├── Trial_Eligibility_Agent/
│   │   │   ├── Trial_Matching_Agent/ # TrialGPT Implementation
│   │   │   ├── Oncology/Precision_Oncology_Agent/
│   │   │   ├── Medical_Imaging/      # MONAI integration
│   │   │   ├── Clinical_NLP/         # medspaCy, OpenMed
│   │   │   ├── Digital_Pathology/    # QuPath, histolab
│   │   │   ├── EHR_FHIR_Integration/ # FHIR R4, SMART
│   │   │   └── Medical_NER/          # BioBERT, transformers
│   │   │
│   │   ├── Drug_Discovery/           # 5 pharma/cheminformatics skills
│   │   │   ├── Chemical_Property_Lookup/
│   │   │   ├── ChemCrow_Tools/       # ChemCrow Lite
│   │   │   ├── AgentD_Drug_Discovery/
│   │   │   ├── Protein_Structure/    # AlphaFold
│   │   │   ├── Knowledge_Graph/      # Drug repurposing
│   │   │   └── Antibody_Design/      # MAGE
│   │   │
│   │   ├── Genomics/                 # 7 bioinformatics skills
│   │   │   ├── Single_Cell_RNA_QC/
│   │   │   ├── CRISPR_Design_Agent/
│   │   │   ├── Variant_Annotation/   # VEP, ClinVar
│   │   │   ├── Proteomics_MS/        # Mass spectrometry
│   │   │   ├── Single_Cell/          # Ecosystems
│   │   │   ├── Spatial_Transcriptomics/
│   │   │   └── Multi_Agent_Workflows/
│   │   │
│   │   ├── MCP_Servers/              # Model Context Protocol
│   │   │   └── BioMCP_Reference/     # Reference Implementation
│   │   └── Research_Tools/           # General tools
│   │
│   ├── test_demonstration/           # Validation suite
│   └── presentation_materials/       # Tutorials
│
├── skill collections/                # 28+ curated external resources
├── platform/                         # USDL Platform Prototype
├── tests/                            # Local testing
└── docs/                             # Documentation
```

---

## Why This Repository?

| Challenge | Our Solution |
|-----------|--------------|
| Biomedical AI tools are fragmented | **Universal Skill Definition Language (USDL)** compiles once, deploys everywhere |
| AI prompts lack scientific validation | Every skill follows **peer-reviewed methodologies** with citations |
| Integration is complex | **Drop-in Python modules** work with LangChain, AutoGen, Semantic Kernel |
| Results are non-reproducible | **Statistical rigor** (MAD-based filtering, etc.) ensures consistency |
| Clinical data is siloed | **FHIR/EHR integration** enables healthcare interoperability |
| Drug discovery is slow | **Knowledge graphs & AI** accelerate target identification |
| Protein structures unknown | **AlphaFold integration** provides structure predictions |

---

## Latest Updates (January 2026)

### New Skills (This Update)

**Clinical Domain:**
- **Trial Matching Agent (TrialGPT)**: `Skills/Clinical/Trial_Matching_Agent`
  - Hybrid keyword/semantic search (using `sentence-transformers`) to match patient profiles with clinical trials.
  - Features configurable matching logic and "Mock Mode" for testing without heavy dependencies.

**Drug Discovery Domain:**
- **ChemCrow Lite**: `Skills/Drug_Discovery/ChemCrow_Tools`
  - Lightweight implementation of the ChemCrow agent for chemical property analysis.
  - Tools include: Molecular Weight calculator, Safety Checker (heuristic), and SMILES validity.

**Infrastructure (MCP):**
- **BioMCP Reference Server**: `Skills/MCP_Servers/BioMCP_Reference`
  - Reference implementation of the Model Context Protocol (MCP) for biomedical tasks.
  - Connects AI agents (like Claude Desktop) to local Python tools for PubMed searching and Gene Info retrieval.

### Previous Updates (December 2025)

**Clinical Domain:**
- **Medical Imaging AI (MONAI)**: CT, MRI, X-ray analysis with pre-trained models from MONAI Model Zoo
- **Clinical NLP Toolkit**: medspaCy, OpenMed, transformer-based NER and assertion detection
- **Digital Pathology**: Whole slide image analysis with QuPath, histolab, PLIP, UNI foundation models
- **EHR/FHIR Integration**: SMART on FHIR OAuth2, bulk data export, FHIR MCP servers
- **Medical NER & Relation Extraction**: BioBERT, PubMedBERT, ClinicalBERT pipelines

**Genomics Domain:**
- **Variant Annotation**: Ensembl VEP, ClinVar, gnomAD, CADD, ACMG/AMP classification
- **Proteomics & Mass Spectrometry**: AlphaPeptDeep, DeepLC, Prosit for peptide property prediction

**Drug Discovery Domain:**
- **Protein Structure Prediction**: AlphaFold 2/3, OpenFold 3, AlphaFold MCP Server integration
- **Knowledge Graph & Drug Repurposing**: iKraph, PrimeKG, CKG with GNN-based reasoning

### Previously Added (2024-2025)

- **Data Analysis Skill**: Python (Pandas, NumPy), R, SQL, Tableau, Power BI (196+ tutorials)
- **Biomni (Stanford)**: General-purpose biomedical agent with 150+ tools
- **STAgent**: Multimodal spatial transcriptomics analysis
- **BioMaster**: Automated end-to-end bioinformatics workflows
- **CellAgent**: Multi-agent single-cell RNA-seq annotation
- **BioMCP**: Model Context Protocol servers for PubMed & ClinicalTrials.gov
- **TrialGPT (NIH)**: Precision clinical trial matching
- **scverse & Seurat Ecosystems**: Complete single-cell analysis toolkits

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/ARTIFICIALINTELLIGENCEGROUP/skills.git
cd skills

# Install dependencies
pip install langchain anthropic torch transformers
pip install scanpy anndata medspacy fhir.resources monai
```

### Example Usage

```python
from langchain.tools import tool

# Clinical NLP
@tool
def extract_medical_entities(text: str) -> str:
    """Extract entities from clinical notes using medspaCy."""
    import medspacy
    nlp = medspacy.load()
    doc = nlp(text)
    return [{"text": e.text, "label": e.label_} for e in doc.ents]

# Drug Repurposing
@tool
def find_repurposing_candidates(disease: str) -> str:
    """Find drug repurposing candidates using knowledge graphs."""
    from knowledge_graph import query_primekg
    return query_primekg(disease, task="repurposing")

# Variant Annotation
@tool
def annotate_variant(chrom: str, pos: int, ref: str, alt: str) -> str:
    """Annotate genetic variant with VEP, ClinVar, gnomAD."""
    from variant_annotation import annotate_with_vep
    return annotate_with_vep(f"{chrom}-{pos}-{ref}-{alt}")
```

---

## Key Technologies Integrated

| Category | Technologies |
|----------|--------------|
| **Clinical NLP** | medspaCy, OpenMed, BioBERT, ClinicalBERT, PubMedBERT |
| **Medical Imaging** | MONAI, MONAI Deploy, PyTorch, torchvision |
| **Digital Pathology** | QuPath, histolab, OpenSlide, PLIP, UNI, CONCH |
| **Healthcare Interop** | FHIR R4, SMART on FHIR, fhir.resources, HL7 |
| **Genomics** | scanpy, anndata, VEP, ClinVar, gnomAD, CADD |
| **Proteomics** | AlphaPeptDeep, DeepLC, Prosit, MaxQuant |
| **Drug Discovery** | RDKit, AlphaFold, OpenFold, PrimeKG, iKraph |
| **AI Frameworks** | LangChain, AutoGen, MCP, PyTorch, Transformers |

---

## Author & Maintainer

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu

---

## License

[MIT License](LICENSE) - Free for academic and commercial use.

---

## Citation

```bibtex
@software{universal_life_science_skills,
  author = {Mia, MD Babu},
  title = {Universal Life Science and Clinical Skills for LLM Agents},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/ARTIFICIALINTELLIGENCEGROUP/skills}
}
```
