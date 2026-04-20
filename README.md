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

## 🧹 Recent Curation (March 2026)

We also started curating the user-focused Babu collection to make the highest-value skills easier to trigger and maintain.

- `Skills/User_Collections/Babu/computational-software-development` now uses a compact workflow-oriented skill definition with supporting references.
- `Skills/User_Collections/Babu/bioinformatics-singlecell`, `ngs-analysis`, and `mpn-research-assistant` were rewritten to reduce prompt bloat and improve reuse.
- Two new skills were added for repository stewardship and grounded literature systems:
  - `Skills/User_Collections/Babu/skill-library-maintainer`
  - `Skills/User_Collections/Babu/biomedical-rag-citation-pipelines`
- The Babu collection README now reflects the curated layout and reference-first organization.
- **New 2026 tech refresh:**
  - `Skills/Software_Engineering/GitHub_Agentic_Workflow` now documents GitHub's Agentic Workflows technical preview so Copilot, Claude Code, and Codex can act as CI/CD participants.
  - `Skills/Lab_Automation/End_to_End_Agentic_AI_Lab` packages the MDalamin5 multi-agent automation lab (LangChain, LangGraph, MCP, n8n) for self-driving wet-lab pilots.
  - `Skills/Genomics/Single_Cell/BioStudio_Alpha_SC` captures GPU-native BioStudio Alpha SC workflows for million-cell atlases on NVIDIA Blackwell systems.
  - `Skills/Multi_Omics/Connected_Multiomics` covers Illumina's Connected Multiomics SaaS for DRAGEN-native single-cell, spatial, proteomic, and methylation studies.
  - `Skills/Drug_Discovery/BioNeMo_Framework` activates NVIDIA's BioNeMo generative AI stack (framework + NIMs) for protein, RNA, and small-molecule design.
  - `Skills/Agentic_AI/LangGraph_Self_Hosted` documents the Aegra self-hosting path so regulated teams can run LangGraph deployments on-prem with hardened dependencies.

## April 2026 LLM + Agentic AI Refresh

We completed a focused curation pass on the repo's LLM and agentic AI surface, with the goal of turning scattered references into first-class, operational skills.

- Added new first-party skills for `OpenAI_Codex_Agents`, `Google_ADK_Agents`, `PydanticAI_Agents`, `Agentic_Evals_Observability`, `MCP_Operations_2026`, `Mistral_Platform_Operations_2026`, `DeepSeek_API_Operations_2026`, and `XAI_Grok_Operations_2026`.
- Rewrote `Automated_Web_Research` and `DeepResearch_Swarm` to be evidence-first, source-aware, and operationally realistic.
- Added missing category indexes for `Skills/AI_Providers/` and `Skills/MCP_Servers/`, and replaced the stale `Skills/Agentic_AI/README.md` with an accurate curation guide.
- Added `docs/strategy/LLM_AGENTIC_AI_CURATION_2026.md` as the source-of-truth playbook for official references, literature watchlists, and refresh discipline.

## Late April 2026 LLM Infrastructure Enrichment

We followed the initial refresh with a second, more operational pass focused on the current coding-agent and cloud-agent landscape.

- Added `Skills/Agentic_AI/Claude_Code_Operations_2026` and `Skills/Agentic_AI/Computer_Use_Agents_2026` to cover terminal-first coding agents, GitHub automation, and browser/desktop control patterns.
- Added dedicated provider skills for `Skills/AI_Providers/Cohere_Platform_Operations_2026`, `Skills/AI_Providers/AWS_Bedrock_Operations_2026`, and `Skills/AI_Providers/Azure_AI_Foundry_Operations_2026` so teams no longer rely on a single combined cloud note.
- Refreshed the official source maps for OpenAI and Anthropic to reflect current model catalogs, Codex, deep research, computer-use, and Claude Code surfaces.
- Expanded `docs/strategy/LLM_AGENTIC_AI_CURATION_2026.md` with a stronger canonical-source map, ecosystem watchlist, and benchmark/literature coverage.

## 📂 Directory Structure

The repository is organized into domain-specific modules:

```text
Skills/                     # 59+ biomedical AI skill domains
├── Agentic_AI/             # Orchestrators, Swarms, Planning Agents
├── Clinical/               # EHR, Radiology, Oncology, Trials
├── Drug_Discovery/         # Antibody Design, Small Molecules, Chemistry
├── Genomics/               # Single Cell, Spatial, CRISPR, Variant Interpretation
├── MCP_Servers/            # BioMCP and other protocol servers
├── Research_Tools/         # Biomni, Literature Mining, Knowledge Graphs
├── Pharma/                 # Regulatory Affairs, Pharmacovigilance
├── Software_Engineering/   # Best Practices (React, Python, Pandas)
└── User_Collections/Babu/  # Curated high-value skill collection

biokernel/                  # BioKernel Runtime Platform (v2026.4.0)
├── biokernel/              # Core orchestration engine
│   ├── server.py           #   FastAPI + semantic routing + execution
│   ├── router.py           #   TF-IDF semantic skill router
│   ├── workflow_engine.py  #   DAG-based multi-agent workflows
│   └── mcp_server.py       #   Model Context Protocol server
├── adapters/               # LLM provider adapters
│   ├── anthropic_adapter.py#   Claude API (real integration)
│   ├── openai_runtime_adapter.py  # GPT API (real integration)
│   ├── gemini_adapter.py   #   Gemini API (real integration)
│   └── local_adapter.py    #   Ollama / local models
├── evaluator/              # Automated evaluation with biomedical rubrics
├── optimizer/              # USDL transpiler + meta-prompter
├── tests/                  # 74 tests (router, workflow, eval, schema, transpiler)
└── cli.py                  # Rich interactive CLI
```

### 🗂️ Documentation Layout (2026 refresh)

All long-form docs now live under `docs/` with a clear index:

| Folder | What's inside |
|--------|---------------|
| `docs/README.md` | Quick index for every doc family. |
| `docs/architecture/` | Repository maps + onboarding (“Where does X live?”). |
| `docs/operations/` | Runbooks (e.g., `medgeclaw_stack.md`). |
| `docs/standards/` | Governance + schemas (`USDL_OVERVIEW.md`, etc.). |

Update these files whenever you add a major capability so downstream teams never
have to guess where specs or runbooks are stored.

## 📜 Standardized Skill Format

The repository is migrating toward a lean **SKILL.md** standard so skills are easier to discover and cheaper to load into context. Curated skills should prefer:
*   **Name:** Hyphen-case skill identifier.
*   **Description:** Concise trigger guidance that states what the skill does and when to use it.
*   **Workflow body:** Short operational instructions rather than large code dumps.
*   **References:** Detailed domain notes moved into `references/` when they are not needed on every invocation.
*   **Agents metadata:** Optional `agents/openai.yaml` for curated skills that should surface cleanly in UI-driven environments.

## 🛠️ Usage Examples

### BioKernel Platform (Recommended)

**1. Start the BioKernel server:**
```bash
cd biokernel && pip install -e ".[all-providers]"
biokernel serve --port 8000
```

**2. Execute a biomedical query (auto-routes to best skill):**
```bash
biokernel run "Analyze JAK2 V617F mutation in MPN patients" --provider anthropic
```

**3. Interactive research session:**
```bash
biokernel interactive
```

**4. MCP server for Claude Desktop / Claude Code:**
```bash
biokernel mcp
```

**5. Run evaluation benchmarks:**
```bash
biokernel eval tests/eval_cases.yaml --html
```

### Direct Skill Invocation

**6. Match a Patient to a Clinical Trial (TrialGPT):**
```bash
python3 Skills/Clinical/Trial_Matching/TrialGPT/run_matching.py --patient_profile ./patient.json
```

**7. Design an Antibody (MAGE):**
```bash
python3 Skills/Drug_Discovery/Antibody_Design/MAGE/generate.py --antigen "spike_protein" --count 5
```

**8. Analyze Spatial Transcriptomics (STAgent):**
```bash
python3 Skills/Genomics/Spatial_Transcriptomics/STAgent/main.py --data ./visium_data.h5ad --task "cluster_domains"
```

## 📄 License

**Copyright (c) 2026 MD BABU MIA, PhD.**  
All rights reserved.

This project is licensed under the MIT License for open-source components, but the unique architectural design and agentic workflows are the intellectual property of the author. **Attribution is mandatory.**
