# Universal Biomedical Skills & Agents (Biomedical OS - 2026)

![Status](https://img.shields.io/badge/Status-Active-green)
![Architecture](https://img.shields.io/badge/Architecture-Biomedical%20OS-blueviolet)
![Domain](https://img.shields.io/badge/Domain-Biotech%20%7C%20Clinical%20%7C%20Genomics-purple)
![Tech](https://img.shields.io/badge/Tech-MCP%20%7C%20DeepSeek%20%7C%20Gemini-orange)

> **⚠️ IMPORTANT DISCLAIMER & COPYRIGHT NOTICE**
> 
> This repository, its architecture, agent designs, and specific implementations are the intellectual property of **MD BABU MIA, PhD**.
> 
> While open-source components are licensed under MIT, the unique curation, "Biomedical OS" architecture, and agentic workflows are proprietary to the author. 
> 
> **If you fork, clone, or copy this repository for public use, you MUST:**
> 1.  Retain this copyright notice.
> 2.  Explicitly credit **MD BABU MIA, PhD** as the original author.
> 3.  Link back to the original repository.
> 
> *Plagiarism or uncredited redistribution is strictly prohibited.*

---

## 🚀 Overview

This repository acts as a **Biomedical Operating System (BioOS)**, orchestrating a comprehensive library of **skills, agents, and mathematical foundations** for modern (2026) Artificial Intelligence. 

Unlike standard codebases, this project transforms static scripts into **Agentic Workflows**—where autonomous systems plan, execute, use tools, and correct themselves to solve complex scientific problems. It is designed to support high-impact research, clinical decision support, and automated lab operations.

## 👤 Author & Maintainer

**MD BABU MIA, PhD**  
*Assistant Professor of Hematology & Medical Oncology, Machine Learning -AI | Mount Sinai*  
Mount Sinai Tisch Cancer Institute
Icahn School of Medicine at Mount Sinai
Mount Sinai Hospital
One Gustave L. Levy Place
New York, NY 10029
Desk phone:(212) 241-2764 (x42764)
Mobile phone:(332) 256-3038
Email: md.babu.mia@mssm.edu
Specializing in Hemato-Oncology,and Machine Learning-LLM-AI.
 

---

## 🌟 Major Updates (February 2026)

We have significantly expanded the **Skills** directory to align with the 2026 roadmap, introducing the `SKILL.md` metadata standard and deploying high-performance agents across key domains.

### 🧬 Genomics & Bioinformatics
*   **BioMaster:** `Skills/Genomics/Multi_Agent_Workflows/BioMaster` - A master orchestrator for RNA-seq, ChIP-seq, and Hi-C pipelines.
*   **CellAgent:** `Skills/Genomics/Single_Cell/CellAgent` - Autonomous single-cell annotation and quality control.
*   **CompBioAgent:** `Skills/Genomics/Single_Cell/CompBioAgent` - Interactive scRNA-seq explorer and visualization tool.
*   **STAgent:** `Skills/Genomics/Spatial_Transcriptomics/STAgent` - Spatial transcriptomics analysis for Visium/Xenium data.

### 🏥 Clinical & Operations
*   **ChatEHR:** `Skills/Clinical/EHR/ChatEHR` - Clinical assistant for summarizing patient records and answering queries.
*   **TrialGPT:** `Skills/Clinical/Trial_Matching/TrialGPT` - Intelligent patient-to-trial matching and ranking.
*   **RadGPT:** `Skills/Clinical/Radiology/RadGPT` - Radiology report summarizer and patient-friendly explainer.
*   **Autonomous Oncology Agent:** Precision oncology treatment planning using multimodal data (H&E + Genomics).

### 🧪 Drug Discovery & Chemistry
*   **MAGE:** `Skills/Drug_Discovery/Antibody_Design/MAGE` - Generative antibody design using protein language models.
*   **CheMatAgent:** `Skills/Drug_Discovery/CheMatAgent` - Computational chemistry agent for molecule design and property prediction.
*   **Biomni:** `Skills/Research_Tools/Biomni` - General-purpose biomedical research agent with access to 150+ tools.

### 🔍 Knowledge & Research
*   **KRAGEN:** `Skills/Research_Tools/Knowledge_Graphs/KRAGEN` - Knowledge Graph-Enhanced RAG for complex reasoning.
*   **LEADS:** `Skills/Research_Tools/Literature_Mining/LEADS` - Automated systematic review and meta-analysis agent.
*   **BioMCP:** `Skills/MCP_Servers/BioMCP` - Model Context Protocol server for connecting LLMs to PubMed, ClinicalTrials.gov, and more.

## 📂 Directory Structure

The repository is organized into domain-specific modules:

```text
Skills/
├── Agentic_AI/           # Orchestrators, Swarms, Planning Agents
├── Clinical/             # EHR, Radiology, Oncology, Trials
├── Drug_Discovery/       # Antibody Design, Small Molecules, Chemistry
├── Genomics/             # Single Cell, Spatial, CRISPR, Variant Interpretation
├── MCP_Servers/          # BioMCP and other protocol servers
├── Research_Tools/       # Biomni, Literature Mining, Knowledge Graphs
├── Pharma/               # Regulatory Affairs, Pharmacovigilance
└── Software_Engineering/ # Best Practices (React, Python, Pandas)
```

## 📜 Standardized Skill Format

All skills now adhere to the **SKILL.md** standard, making them discoverable and executable by the BioKernel. Each skill definition includes:
*   **Description:** Concise summary of capabilities.
*   **Keywords:** Core terms for indexing.
*   **Measurable Outcome:** SMART goals (e.g., "Rank 5 trials in <3 mins").
*   **Allowed Tools:** Security sandboxing for agent execution.

## 🛠️ Usage Examples

**1. Match a Patient to a Clinical Trial (TrialGPT):**
```bash
python3 Skills/Clinical/Trial_Matching/TrialGPT/run_matching.py --patient_profile ./patient.json
```

**2. Design an Antibody (MAGE):**
```bash
python3 Skills/Drug_Discovery/Antibody_Design/MAGE/generate.py --antigen "spike_protein" --count 5
```

**3. Analyze Spatial Transcriptomics (STAgent):**
```bash
python3 Skills/Genomics/Spatial_Transcriptomics/STAgent/main.py --data ./visium_data.h5ad --task "cluster_domains"
```

## 📄 License

**Copyright (c) 2026 MD BABU MIA, PhD.**  
All rights reserved.

This project is licensed under the MIT License for open-source components, but the unique architectural design and agentic workflows are the intellectual property of the author. **Attribution is mandatory.**
