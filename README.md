# LLMs Universal Life Science & Clinical Skills

**The Open-Source Operating System for Biomedical AI Agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Production](https://img.shields.io/badge/Status-Production-brightgreen.svg)]()
[![Platform: Multi-LLM](https://img.shields.io/badge/Platform-Claude%20%7C%20ChatGPT%20%7C%20Gemini-purple.svg)]()

---

## Mission

We build **production-ready, platform-agnostic biomedical AI skills** that empower researchers, clinicians, and developers to deploy advanced AI capabilities across any LLM interface. Whether you use **Claude**, **ChatGPT**, **Gemini**, or custom open-source models, our standardized skills deliver reproducible, validated results for real-world biomedical workflows.

---

## Repository Structure

This workspace is organized into several key components:

```
skills/
├── src/                         # Main source code (GitHub submodule)
│   ├── Skills/                  # Production-ready skills
│   │   ├── Clinical/            # Healthcare AI capabilities
│   │   ├── Drug_Discovery/      # Cheminformatics & pharma
│   │   └── Genomics/            # Bioinformatics & sequencing
│   ├── test_demonstration/      # Skill validation suite
│   └── presentation_materials/  # Presentations & tutorials
│
├── skill collections/           # Extensive library of curated AI resources
│   ├── Awesome-Biomedical-LLM-Agents/ # Latest agents (STAgent, Biomni, etc.)
│   └── (Other curated repositories)
│
├── platform/                    # USDL Platform Prototype
│   ├── adapters/                # USDL to platform converters
│   ├── schema/                  # USDL JSON schemas
│   └── evaluator/               # Cross-platform evaluation
│
├── tests/                       # Local testing & sample datasets
└── docs/                        # Project documentation & strategy
```

---

## Why This Repository?

| Challenge | Our Solution |
|-----------|--------------|
| Biomedical AI tools are fragmented | **Universal Skill Definition Language (USDL)** compiles once, deploys everywhere |
| AI prompts lack scientific validation | Every skill follows **peer-reviewed methodologies** with citations |
| Integration is complex | **Drop-in Python modules** work with LangChain, AutoGen, Semantic Kernel |
| Results are non-reproducible | **Statistical rigor** (MAD-based filtering, etc.) ensures consistency |

---

## Recent Updates (December 2025)

We have extensively enriched the collection with the latest (2024-2025) AI agents and frameworks:

- **Biomni (Stanford)**: General-purpose agent with 150+ tools.
- **STAgent**: Multimodal spatial transcriptomics analysis.
- **BioMaster**: Automated end-to-end bioinformatics workflows.
- **CellAgent**: Multi-agent single-cell RNA-seq annotation.
- **BioMCP**: Model Context Protocol servers for PubMed & ClinicalTrials.
- **TrialGPT (NIH)**: Precision clinical trial matching.
- **scverse & Seurat Ecosystems**: Local clones and tutorials for the complete single-cell stack.

---

## Author & Maintainer

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu

## License

[MIT License](LICENSE) - Free for academic and commercial use.