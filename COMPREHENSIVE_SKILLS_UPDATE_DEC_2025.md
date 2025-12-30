# Comprehensive Biomedical AI Skills Database Update (December 2025)

This document contains an extensive compilation of newly discovered LLM agents, AI tools, frameworks, and resources for biomedical research, identified through systematic web searches in late December 2025.

---

## 1. Single-Cell RNA-seq & Spatial Transcriptomics Agents

### CompBioAgent
- **Source**: [bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.03.17.643771v1)
- **Description**: LLM-powered web application for single-cell RNA-seq data exploration
- **Features**: Integrates with CellDepot, uses Cellxgene VIP for visualizations
- **Status**: Candidate for `Skills/Genomics/Single_Cell`

### BioMaster
- **Source**: [bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.01.23.634608v1)
- **Description**: Multi-agent system for automated bioinformatics analysis
- **Features**: Role-based agents, RAG for domain knowledge, supports RNA-seq, ChIP-seq, scRNA-seq, Hi-C
- **Status**: High priority for `Skills/Genomics`

### scExtract
- **Source**: [Genome Biology 2025](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03639-x)
- **Description**: LLM agent for automated scRNA-seq annotation and multi-dataset integration
- **Features**: Prior-informed integration, automated preprocessing
- **Status**: Candidate for `Skills/Genomics/Single_Cell`

### CellAgent
- **Source**: [arXiv 2407.09811](https://arxiv.org/html/2407.09811v1)
- **Description**: LLM-driven multi-agent framework for automated single-cell analysis
- **Features**: Multiple bio-expert LLM roles, automated complex analysis tasks
- **Status**: HIGH PRIORITY - `Skills/Genomics/Single_Cell`

### scBaseCamp & SRAgent
- **Source**: [bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.02.27.640494v1)
- **Description**: AI agent-curated single-cell data repository with SRA querying
- **Features**: Hierarchical workflow, automated metadata extraction, LangGraph-based

### CellAtria
- **Source**: [bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.07.31.667880v1)
- **Description**: Agentic AI framework for ingestion and standardization of scRNA-seq
- **Features**: Chatbot interface, document-to-analysis automation

### STAgent (Spatial Transcriptomics Agent)
- **Source**: [GitHub - LiuLab-Bioelectronics-Harvard](https://github.com/LiuLab-Bioelectronics-Harvard/STAgent)
- **Description**: Multimodal LLM-based AI agent for deep spatial transcriptomics research
- **Features**: Dynamic code generation, visual reasoning, literature retrieval, publication-style reports
- **Status**: HIGH PRIORITY - `Skills/Genomics/Spatial_Transcriptomics`

### SpatialAgent
- **Source**: Wang et al., 2025
- **Description**: Interprets spatial transcriptomics data to propose mechanistic hypotheses
- **Features**: Tissue organization analysis, cellular interaction predictions

### FOCUS
- **Source**: [bioRxiv Dec 2025](https://www.biorxiv.org/content/10.64898/2025.12.23.696267v1)
- **Description**: Foundational generative model for cross-platform ST enhancement
- **Features**: Trained on >1.7M H&E-ST pairs, multimodal integration

### scAgent
- **Source**: Mao et al., 2025
- **Description**: Universal single-cell annotation via LLM agent
- **Features**: Automated cell type annotation

---

## 2. Drug Discovery & Chemistry Agents

### ChemCrow
- **Source**: [Nature Machine Intelligence](https://www.nature.com/articles/s42256-024-00832-8)
- **Description**: LLM chemistry agent with 18 expert-designed tools
- **Features**: Organic synthesis, drug discovery, materials design, autonomous experiment planning
- **Tools**: Molecular Similarity, ModifyMol, PatentCheck, RDKit integration
- **Status**: Already tracked - UPDATE tools count to 18

### CheMatAgent
- **Description**: Two-tiered agent with 137 Python-wrapped chemical tools
- **Features**: Frozen base LLM orchestrating chemical tools library
- **Status**: Candidate for `Skills/Drug_Discovery`

### CACTUS
- **Description**: Chemistry agent using MRKL/ReAct paradigm within LangChain
- **Features**: Cheminformatics libraries, property prediction, PubChem APIs

### GAMES (SwRI)
- **Source**: [Phys.org 2025](https://phys.org/news/2025-08-chemistry-llm-faster-drug-discovery.html)
- **Description**: Custom LLM for drug design generating valid SMILES strings
- **Features**: Integration with Rhodium software, LoRA/QLoRA fine-tuning
- **Status**: Candidate for `Skills/Drug_Discovery`

### ChatChemTS
- **Description**: LLM-powered chatbot for molecule design
- **Features**: Chat-based interaction, automated reward function construction

---

## 3. Clinical & Healthcare Agents

### MedAgentBench
- **Source**: [NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144)
- **Description**: Virtual EHR environment to benchmark medical LLM agents
- **Features**: 300 patient-specific tasks, 100 patient profiles with 700K+ data elements
- **Status**: Candidate for `Skills/Clinical/Benchmarks`

### ChatEHR (Stanford)
- **Source**: [Stanford Med](https://med.stanford.edu/news/all-news/2025/06/chatehr.html)
- **Description**: AI software for clinicians to interact with patient medical records
- **Features**: Natural language queries, automatic chart summarization
- **Status**: Candidate for `Skills/Clinical/EHR`

### AIPatient
- **Source**: [Nature Communications Medicine](https://www.nature.com/articles/s43856-025-01283-x)
- **Description**: Simulated patient system for medical education
- **Features**: RAG framework, 6 task-specific LLM agents for complex reasoning

### TrialGPT (NIH)
- **Source**: [NIH News](https://www.nih.gov/news-events/news-releases/nih-developed-ai-algorithm-matches-potential-volunteers-clinical-trials)
- **Description**: LLM-based clinical trial matching framework
- **Features**: ClinicalTrials.gov integration, eligibility screening, ranked trial recommendations
- **Status**: HIGH PRIORITY - `Skills/Clinical/Trial_Matching`

### TrialMatchAI
- **Source**: [arXiv 2505.08508](https://arxiv.org/abs/2505.08508)
- **Description**: End-to-end AI-powered clinical trial recommendation system
- **Features**: Heterogeneous clinical data processing, 92% relevant trial retrieval

### Synapsis (Dyania Health)
- **Description**: AI platform for clinical trial recruitment
- **Features**: 7x more eligible patients identified, 100% positive predictive value, EMR integration

---

## 4. Genomics & Bioinformatics Agents

### CRISPR-GPT
- **Source**: [Nature Biomedical Engineering 2025](https://www.nature.com/articles/s41551-025-01463-z)
- **Description**: LLM agent for automated gene-editing experiment design
- **Features**: 4 editing modalities (knockout, base-editing, prime-editing, epigenetic), 22 automated tasks, 3 interaction modes
- **Status**: Already tracked - UPDATE with full capabilities

### OpenCRISPR-1
- **Source**: [CRISPR Medicine News](https://crisprmedicinenews.com/news/opencrispr-1-generative-ai-meets-crispr/)
- **Description**: First AI-designed CRISPR gene editor
- **Features**: LLM-expanded CRISPR-Cas protein diversity (4.8x expansion)

### GeneAgent
- **Source**: [GitHub - ncbi-nlp/GeneAgent](https://github.com/ncbi-nlp/GeneAgent)
- **Description**: Gene set analysis with domain database access
- **Status**: Already tracked

### Biomni (Stanford)
- **Source**: [GitHub - snap-stanford/Biomni](https://github.com/snap-stanford/Biomni)
- **Description**: General-purpose biomedical AI agent
- **Features**: 150 tools, 105 software packages, 59 databases, autonomous hypothesis generation
- **Performance**: 402% improvement over base LLM, 74.4% DbQA accuracy
- **Status**: HIGH PRIORITY - `Skills/Research_Tools/General_Agent`

### Agent Laboratory
- **Source**: Schmidgall et al., 2025
- **Description**: Framework for autonomous research from idea to report
- **Features**: Literature review, experimentation, report writing automation

### AutoBA
- **Source**: Zhou et al., 2024
- **Description**: Autonomous multi-omic analysis pipeline construction
- **Features**: Minimal user input, adaptive pipelines

---

## 5. Protein & Structural Biology

### AlphaFold 3
- **Source**: [Google DeepMind](https://blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/)
- **Description**: Protein structure prediction with DNA, RNA, ligands, ions
- **Features**: 50%+ improvement for protein interactions, doubled accuracy for key categories

### ESMFold
- **Source**: [Science](https://www.science.org/doi/10.1126/science.ade2574)
- **Description**: 15B parameter protein language model for structure prediction
- **Features**: Faster than AlphaFold2, ESM Metagenomic Atlas (600M+ proteins)

### MAGE (Monoclonal Antibody Generator)
- **Source**: [VUMC News 2025](https://news.vumc.org/2025/11/04/ai-can-speed-antibody-design-to-thwart-novel-viruses-study/)
- **Description**: Protein language model for antibody design
- **Features**: Generates antibodies against unseen viral strains
- **Funding**: $30M ARPA-H award
- **Status**: Candidate for `Skills/Drug_Discovery/Antibody_Design`

### RFdiffusion for Antibodies
- **Source**: UW Research 2025
- **Description**: AI-guided de novo antibody design
- **Features**: Epitope-specific VHH antibody design, atomic-precision validation

---

## 6. Medical LLM Benchmarks & Models

### Med-PaLM 2
- **Performance**: 86.5% on MedQA (USMLE), preferred by physicians on 8/9 clinical axes
- **Status**: Reference benchmark

### MedXpertQA
- **Source**: Tsinghua University, Jan 2025
- **Description**: Challenging specialty board exam benchmark
- **Features**: Filtered for difficulty, specialty-specific scenarios

### AgentClinic
- **Description**: Agentic environment benchmark for medical LLMs
- **Features**: Claude-3.5 achieved 62.1% accuracy (highest as of Oct 2024)

### LEADS
- **Source**: [Nature Communications 2025](https://www.nature.com/articles/s41467-025-62058-5)
- **Description**: Specialized LLM for literature mining
- **Features**: Largest benchmark for AI in systematic review/meta-analysis
- **Status**: Candidate for `Skills/Research_Tools/Literature_Mining`

---

## 7. Oncology & Precision Medicine Agents

### Autonomous Clinical AI Agent (Precision Oncology)
- **Source**: [Nature Cancer 2025](https://www.nature.com/articles/s43018-025-00991-6)
- **Description**: GPT-4 with multimodal precision oncology tools
- **Features**: Vision transformers for MSI/KRAS/BRAF detection, OncoKB/PubMed integration
- **Performance**: 87.2% decision-making accuracy (vs 30.3% for GPT-4 alone)
- **Status**: HIGH PRIORITY - `Skills/Clinical/Oncology`

### LLM Drug Combination Predictor
- **Source**: [bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.08.10.669494v1)
- **Description**: RAG-based prediction of synergistic oncology drug combinations
- **Features**: 50K+ drug pair assays, 1.6K+ clinical trial entries integrated

### MOMLN
- **Description**: Multimodal multi-omics machine learning framework
- **Performance**: 0.989 AUC for drug response classification in breast cancer

---

## 8. MCP Servers & Claude Plugins

### BioMCP
- **Source**: [LobeHub](https://lobehub.com/mcp/genomoncology-biomcp)
- **Description**: Open source biomedical MCP toolkit
- **Features**: PubMed/PMC search, PubTator3 API, clinical trials, genomic variants
- **Status**: HIGH PRIORITY - `Skills/MCP_Servers`

### BioContextAI Registry
- **Source**: [biocontext.ai](https://biocontext.ai/registry/biocontext-ai/skill-to-mcp)
- **Description**: Community-driven MCP server catalog for biomedical research

### Healthcare MCP Server Collection
- **Source**: [awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers/blob/main/docs/healthcare--life-sciences.md)
- **Features**: FDA drug info, PubMed, medRxiv, NCBI Bookshelf, clinical trials, ICD-10, DICOM

### Eka MCP Server
- **Description**: Healthcare workflow grounding in verified medical data

### MCP-on-FHIR
- **Description**: FHIR application with MCP Knowledge Graph capabilities

### AgentCare-MCP
- **Description**: EMR integration (Cerner, Epic), FHIR data interaction

---

## 9. Radiology & Medical Imaging

### VILA-M3 (NVIDIA)
- **Description**: Multimodal radiology agent framework
- **Features**: Integration with MONAI, brain tumor MRI interpretation

### RadGPT (Stanford)
- **Source**: [Stanford News 2025](https://news.stanford.edu/stories/2025/06/large-language-model-radiology-reports-rad-gpt-ai)
- **Description**: LLM for patient-facing radiology report explanation
- **Features**: Concept extraction, follow-up question suggestions
- **Status**: Candidate for `Skills/Clinical/Radiology`

### Virtual Tumor Board
- **Description**: Multi-agent system for oncological diagnosis
- **Features**: MRI, pathology, genomic data analysis agents with central orchestrator

---

## 10. Neuroscience & Mental Health

### BRANT (Brain Neural Transformer)
- **Description**: Multi-layer transformers for intracranial EEG
- **Features**: Generalized neural decoding across patients/tasks

### MindEye2
- **Description**: fMRI-based image reconstruction
- **Features**: Transformer alignment of voxel patterns with visual embeddings

### AI-TMS Integration
- **Description**: fMRI-guided, DTI-modeled, EEG/MEG-optimized TMS
- **Features**: Real-time parameter adjustment with AI algorithms

---

## 11. Multi-Omics Integration

### Multi-Omics Foundation Models
- **Description**: Large models trained on heterogeneous biomedical data
- **Features**: Fine-tuning for clinical tasks with smaller datasets

### Illumina-NVIDIA Partnership (May 2025)
- **Features**: 5-10x speedup in multiomics data processing

### Cell Foundation Models
- **Description**: Extract information from each omics layer using unlabeled data

---

## 12. Knowledge Graphs & RAG Systems

### KRAGEN
- **Source**: [Bioinformatics Oxford](https://academic.oup.com/bioinformatics/article/40/6/btae353/7687047)
- **Description**: Knowledge graph-enhanced RAG for biomedical problem solving
- **Features**: Graph-of-thoughts (GoT), vector database conversion
- **Status**: Candidate for `Skills/Research_Tools/Knowledge_Graphs`

### BiomedRAG
- **Source**: [PubMed](https://pubmed.ncbi.nlm.nih.gov/39814274/)
- **Performance**: 9.95% average improvement, 4.97% over baselines

### MEGA-RAG
- **Description**: Multi-source evidence retrieval for public health
- **Features**: FAISS + BM25 + knowledge graphs, 40%+ hallucination reduction

### fastbmRAG
- **Description**: Fast Graph-based RAG for biomedical literature
- **Features**: 10x+ speedup for graph-RAG processing

---

## 13. Variant Interpretation & Pathogenicity

### DYNA
- **Source**: [Nature Machine Intelligence 2025](https://www.nature.com/articles/s42256-025-01016-8)
- **Description**: Disease-specific genomic foundation model fine-tuning
- **Features**: Siamese network, cardiovascular VEP, RNA splicing regulation

### AlphaMissense
- **Description**: Structure-based pathogenicity prediction
- **Features**: AlphaFold pre-training, fine-tuned for pathogenicity

### GPN-MSA
- **Description**: DNA language model trained on 100-species MSA
- **Features**: Evolutionary information leverage

### ESM1b for VEP
- **Description**: 650M parameter protein language model
- **Features**: Predicts all ~450M possible human missense variants

### varCADD
- **Source**: [Genome Medicine 2025](https://link.springer.com/article/10.1186/s13073-025-01517-6)
- **Description**: Genome-wide pathogenicity prediction with standing variation
- **Status**: Candidate for `Skills/Genomics/Variant_Interpretation`

---

## 14. Literature Mining & NLP

### LLM-IE
- **Source**: [PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11901043/)
- **Description**: Python package for biomedical generative information extraction
- **Features**: NER, entity attribute extraction, relation extraction, "Prompt Editor" agent

### LEADSInstruct
- **Description**: Largest benchmark for AI in literature mining
- **Features**: Study selection, data extraction, PubMed/ClinicalTrials.gov querying

---

## 15. Microbiome & Metagenomics

### AI Systems for Microbiome
- **Features**: Taxonomic profiling, functional annotation, microbe-host interactions, metabolic modeling

### Protein/DNA Language Models for Microbiome
- **Description**: Two classes - protein LMs and DNA/genomic LMs
- **Applications**: Viromics, biosynthetic gene clusters, knowledge integration

---

## 16. Workflow Automation

### LLM-Based Workflow Conversion
- **Source**: [briefideas.org](https://beta.briefideas.org/ideas/4724fe12f939175b4ac3c0ca6ed89a56)
- **Description**: Snakemake to Nextflow conversion using fine-tuned LLMs
- **Features**: nf-core module identification

### Scientific Workflow Generation Study
- **Source**: [arXiv 2025](https://arxiv.org/html/2507.20122v1)
- **Findings**: Gemini 2.5 Flash best for Galaxy, DeepSeek-V3 for Nextflow, GPT-4o with structured prompts

---

## 17. GitHub Awesome Lists (Essential Resources)

| Repository | Description | URL |
|------------|-------------|-----|
| Awesome-LLM-Agents-Scientific-Discovery | LLM agents in biomedical research | [GitHub](https://github.com/zhoujieli/Awesome-LLM-Agents-Scientific-Discovery) |
| awesome-bioagent-papers | Daily-updated bio-agent papers | [GitHub](https://github.com/aristoteleo/awesome-bioagent-papers) |
| Awesome-AI-Agents-Medicine | Medical AI agents survey | [GitHub](https://github.com/AIM-Research-Lab/Awesome-AI-Agents-Medicine) |
| MedLLMsPracticalGuide | Nature Reviews featured guide | [GitHub](https://github.com/AI-in-Health/MedLLMsPracticalGuide) |
| awesome-AI_Scientist-agents-biology-papers | AI scientist biology papers | [GitHub](https://github.com/OmicsML/awesome-agents-biology-papers) |
| Awesome-LLM-Scientific-Discovery (HKUST) | EMNLP2025 survey resources | [GitHub](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery) |
| Awesome-Scientific-Language-Models | EMNLP'24 scientific LLMs | [GitHub](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) |
| papers_for_protein_design_using_DL | Protein design DL papers | [GitHub](https://github.com/Peldom/papers_for_protein_design_using_DL) |
| awesome-deep-learning-single-cell-papers | Single-cell DL papers | [GitHub](https://github.com/OmicsML/awesome-deep-learning-single-cell-papers) |

---

## 18. Frameworks & Platforms

### LangChain for Life Sciences
- **Source**: [O'Reilly Book](https://www.oreilly.com/library/view/langchain-for-life/9781098162627/)
- **Features**: AlphaFold team, DNA generation agents, DeepSeek fine-tuning, LangGraph superagents

### AutoGen (Microsoft)
- **Source**: [GitHub](https://github.com/microsoft/autogen)
- **Features**: Multi-agent conversation, event-driven architecture

### CrewAI
- **Description**: Role-based task execution for team-oriented agents

---

## Summary Statistics

- **Total New Agents Discovered**: 45+
- **New MCP Servers**: 8+
- **GitHub Awesome Lists**: 9
- **High Priority Items**: 12
- **Categories Covered**: 18

---

## Recommended Actions

1. **Immediate Integration**:
   - Biomni (Stanford) - general-purpose agent
   - STAgent - spatial transcriptomics
   - BioMaster - multi-agent bioinformatics
   - CellAgent - single-cell analysis
   - BioMCP - MCP server

2. **Skills Directory Updates**:
   - Create `Skills/Genomics/Spatial_Transcriptomics/`
   - Create `Skills/MCP_Servers/`
   - Create `Skills/Clinical/Oncology/`
   - Update `Skills/Drug_Discovery/` with antibody design tools

3. **Reference Tracking**:
   - Add all GitHub awesome lists to reference collection
   - Subscribe to arxiv feeds for bio-agent papers

---

*Generated: December 28, 2025*
*Sources: Web searches across PubMed, bioRxiv, Nature, arXiv, GitHub, and specialized biomedical AI resources*
