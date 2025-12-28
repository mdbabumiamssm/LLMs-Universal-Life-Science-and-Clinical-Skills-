# Universal Biomedical Skills for LLMs

A comprehensive, open-source collection of "Skills" (Prompts, Tools, and Agents) designed for Biomedical, Clinical, Genomics, and Life Science applications. This repository aims to provide standardized, model-agnostic building blocks for the next generation of AI in Healthcare.

## 📂 Repository Structure

- **Skills/**: The core library of capabilities.
    - **Clinical/**: Skills for doctor-patient interactions, EHR summarization, and diagnostics support.
        - `Clinical_Note_Summarization`: Turn unstructured notes into SOAP format.
    - **Genomics/**: Tools for analyzing DNA/RNA sequencing data.
        - `Single_Cell_RNA_QC`: Automated Quality Control for scRNA-seq (scanpy/scverse).
    - **Drug_Discovery/**: Cheminformatics and molecule analysis tools.
        - `Chemical_Property_Lookup`: Calculate molecular properties using RDKit.
    - **Research_Tools/**: General academic research aids (Literature search, etc.).

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
