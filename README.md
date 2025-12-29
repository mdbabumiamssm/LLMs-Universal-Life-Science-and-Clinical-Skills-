# Universal Biomedical Skills for LLMs

A comprehensive, open-source collection of "Skills" (Prompts, Tools, and Agents) designed for Biomedical, Clinical, Genomics, and Life Science applications. This repository aims to provide standardized, model-agnostic building blocks for the next generation of AI in Healthcare.

## 📂 Repository Structure

- **Skills/**: The core library of capabilities.
    - **Clinical/**: Skills for doctor-patient interactions, EHR summarization, and diagnostics support.
        - `Clinical_Note_Summarization`: Turn unstructured notes into SOAP format.
        - `Trial_Eligibility_Agent`: AI screener for matching patients to clinical trials.
    - **Genomics/**: Tools for analyzing DNA/RNA sequencing data.
        - `Single_Cell_RNA_QC`: Automated Quality Control for scRNA-seq (scanpy/scverse).
        - `CRISPR_Design_Agent`: Automated design of sgRNAs and off-target analysis.
    - **Drug_Discovery/**: Cheminformatics and molecule analysis tools.
        - `Chemical_Property_Lookup`: Calculate molecular properties using RDKit.
        - `AgentD_Drug_Discovery`: AI-driven agent for literature mining and molecule generation.
    - **Research_Tools/**: General academic research aids (Literature search, etc.).

## 🆕 New Discoveries (Dec 2025)

### Comprehensive Update (Dec 28, 2025)
Check out [COMPREHENSIVE_SKILLS_UPDATE_DEC_2025.md](COMPREHENSIVE_SKILLS_UPDATE_DEC_2025.md) for an **extensive database update** covering:
- 45+ new biomedical AI agents discovered
- 18 categories including spatial transcriptomics, precision oncology, MCP servers
- High-priority tools: Biomni, STAgent, BioMaster, CellAgent, BioMCP
- 9 curated GitHub awesome lists for ongoing tracking
- Clinical trial AI (TrialGPT, TrialMatchAI), radiology agents (RadGPT, VILA-M3)
- RAG systems (KRAGEN, BiomedRAG, MEGA-RAG)
- Variant interpretation tools (DYNA, AlphaMissense, varCADD)

### Earlier Discoveries
Check out [NEW_SKILLS_DISCOVERY_DEC_2025.md](NEW_SKILLS_DISCOVERY_DEC_2025.md) for the initial report on LLM agents and tools.

## 🚀 Getting Started

Each skill folder is self-contained with its own `README.md` and usage examples.

### For Developers
You can import the Python scripts in `Skills/` directly into your LangChain, Semantic Kernel, or AutoGen workflows.

### For Prompt Engineers
Check the `prompt.md` files in the `Clinical` section for high-quality, tested medical prompts.

## 🤝 Contributing

We welcome contributions! If you have a prompt or tool for:
- Protein folding
- Clinical trial matching
- Medical coding (ICD-10)
- CRISPR guide design

Please submit a Pull Request.

## 📜 License
[MIT License](LICENSE)
