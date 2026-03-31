<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
-->

# BioKernel: Autonomous Biomedical AI Skills Platform

**Universal Skill Description Language (USDL) Runtime for Cross-Platform Biomedical AI Orchestration**

[![Version](https://img.shields.io/badge/version-2026.4.0-blue)]()
[![Python](https://img.shields.io/badge/python-3.11%2B-green)]()

> **MD Babu Mia, PhD** — Icahn School of Medicine at Mount Sinai
> Department of Hematology & Medical Oncology

---

## Overview

BioKernel is an autonomous, agentic AI platform that orchestrates **59+ biomedical skills** across multiple LLM providers. It introduces the **Universal Skill Description Language (USDL)** — a write-once, deploy-anywhere specification that enables a single skill definition to execute optimally on Anthropic Claude, OpenAI GPT, Google Gemini, or local models.

### Key Contributions

1. **USDL Transpiler**: Compiles canonical skill specs into provider-specific prompt+schema bundles, optimizing for each platform's strengths (XML for Claude, function schemas for GPT, role cards for Gemini)
2. **Semantic Skill Router**: TF-IDF-based routing that matches natural language queries to the most relevant biomedical skill without requiring GPU-hosted embedding models
3. **DAG Workflow Engine**: Executes multi-agent workflows as directed acyclic graphs with automatic parallelization, retry logic, and provenance tracking
4. **Biomedical Evaluation Framework**: Automated testing with domain-specific assertions (gene entity detection, safety disclaimer validation, citation checking) and LLM-as-judge rubrics

### Architecture

```
User Query
    |
    v
+--------------------------------------------------+
|                  BioKernel Server                 |
|  +----------+  +----------+  +---------------+   |
|  | Semantic  |  | Workflow  |  |  Evaluation   |  |
|  |  Router   |--|  Engine   |--|   Engine      |  |
|  | (TF-IDF) |  |  (DAG)   |  | (Assertions)  |  |
|  +----------+  +----------+  +---------------+   |
|       |                                           |
|       v                                           |
|  +------------------------------------------+    |
|  |     USDL Transpiler (Write Once)          |    |
|  |  +---------+----------+----------+        |    |
|  |  | Claude  |  OpenAI  |  Gemini  |        |    |
|  |  |  XML    |  Funcs   |  Roles   |        |    |
|  |  +---------+----------+----------+        |    |
|  +------------------------------------------+    |
|       |              |              |             |
|       v              v              v             |
|  +---------+  +----------+  +----------+         |
|  |Anthropic|  |  OpenAI  |  |  Gemini  |  Local  |
|  | Adapter |  |  Adapter |  |  Adapter |  Ollama |
|  +---------+  +----------+  +----------+         |
+--------------------------------------------------+
         |
         v
    MCP Server (Model Context Protocol)
    REST API (FastAPI)
    CLI (Interactive + Batch)
```

## Installation

```bash
# Core installation
pip install -e ".[all-providers]"

# With biomedical dependencies
pip install -e ".[full]"
```

## Quick Start

### 1. API Server

```bash
biokernel serve --port 8000
```

### 2. Execute a Query

```bash
biokernel run "Analyze JAK2 V617F mutation in MPN patients" --provider anthropic
```

### 3. Interactive Mode

```bash
biokernel interactive
```

### 4. MCP Server (for Claude Desktop / Claude Code)

```bash
biokernel mcp
```

### 5. List Available Skills

```bash
biokernel skills
```

### 6. Run Evaluations

```bash
biokernel eval tests/eval_cases.yaml --html
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check + system status |
| `POST` | `/v1/agent/run` | Execute a query |
| `POST` | `/v1/workflow/run` | Execute a DAG workflow |
| `GET` | `/v1/skills` | List registered skills |
| `GET` | `/v1/providers` | List available providers |
| `POST` | `/v1/route` | Preview routing without execution |

### Example: Execute Query

```bash
curl -X POST http://localhost:8000/v1/agent/run \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the ACMG criteria for BRCA1 c.68_69del?"}'
```

### Example: Multi-Step Workflow

```bash
curl -X POST http://localhost:8000/v1/workflow/run \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Drug Discovery Pipeline",
    "steps": [
      {"step_id": "mine", "skill_id": "literature-mining",
       "parameters": {"query": "Find targets for resistant AML"}},
      {"step_id": "design", "skill_id": "molecule-designer",
       "depends_on": ["mine"],
       "parameters": {"query": "Design molecules for identified target"}},
      {"step_id": "safety", "skill_id": "safety-review",
       "depends_on": ["design"],
       "parameters": {"query": "Evaluate candidate safety"}}
    ]
  }'
```

## Configuration

Edit `config.yaml` to set providers, routing strategy, and system parameters:

```yaml
default_provider: "anthropic"
providers:
  anthropic:
    model: "claude-sonnet-4-20250514"
    api_key_env: "ANTHROPIC_API_KEY"
routing:
  strategy: "semantic"
  similarity_threshold: 0.35
```

## Execution Modes

BioKernel supports three execution modes:

| Mode | Description | Use Case |
|------|-------------|----------|
| **Autonomous** | Automatic routing + execution | Production APIs, batch processing |
| **Interactive** | User selects from ranked skill matches | Exploratory research |
| **Manual** | User specifies exact skill_id | Debugging, benchmarking |

## Testing

```bash
# Run all tests
pytest platform/tests/ -v

# Run specific test module
pytest platform/tests/test_router.py -v

# Run with coverage
pytest platform/tests/ --cov=platform --cov-report=html
```

## Project Structure

```
platform/
├── __init__.py                   # Package metadata
├── pyproject.toml                # Build configuration
├── config.yaml                   # Runtime configuration
├── cli.py                        # CLI entry point
├── dashboard.py                  # Interactive TUI dashboard
├── observability.py              # Structured logging
├── skills_catalog.py             # SKILL.md scanner
├── biokernel/
│   ├── server.py                 # FastAPI app + BioKernel core
│   ├── router.py                 # TF-IDF semantic skill router
│   ├── workflow_engine.py        # DAG workflow executor
│   └── mcp_server.py             # MCP protocol server
├── adapters/
│   ├── factory.py                # Provider factory
│   ├── anthropic_adapter.py      # Claude API integration
│   ├── openai_runtime_adapter.py # GPT API integration
│   ├── gemini_adapter.py         # Gemini API integration
│   └── local_adapter.py          # Ollama / local model support
├── interface/
│   └── llm_provider.py           # Abstract provider interface
├── schema/
│   └── io_types.py               # Pydantic type system
├── optimizer/
│   ├── meta_prompter.py          # Cross-platform prompt optimizer
│   └── usdl_transpiler.py        # USDL compiler
├── evaluator/
│   └── eval_engine.py            # Assertion + LLM-judge evaluator
└── tests/
    ├── test_router.py            # Router tests (17 tests)
    ├── test_workflow_engine.py   # Workflow DAG tests (9 tests)
    ├── test_eval_engine.py       # Evaluation engine tests (22 tests)
    ├── test_schema.py            # Schema model tests (15 tests)
    └── test_transpiler.py        # USDL transpiler tests (10 tests)
```

## Development Roadmap

- [x] USDL Schema & Transpiler (v1 → v2)
- [x] Claude, OpenAI, Gemini Adapters
- [x] Prompt Optimizer (Meta-Prompter)
- [x] Automated Evaluation Engine with Biomedical Rubrics
- [x] BioKernel Runtime (FastAPI Server)
- [x] Semantic Skill Router (TF-IDF)
- [x] DAG Workflow Engine with Parallel Execution
- [x] MCP Server (Model Context Protocol)
- [x] Rich CLI with Interactive Mode
- [x] Comprehensive Test Suite (70+ tests)
- [ ] Web Dashboard (Streamlit / Gradio)
- [ ] Embedding-based Router (optional GPU upgrade)
- [ ] Federated Skill Registry

## Citation

If you use BioKernel in your research, please cite:

```bibtex
@software{mia2026biokernel,
  author = {Mia, MD Babu},
  title = {BioKernel: Autonomous Biomedical AI Skills Platform with
           Universal Skill Description Language},
  year = {2026},
  institution = {Icahn School of Medicine at Mount Sinai},
  version = {2026.4.0}
}
```

## License

Copyright (c) 2026 MD Babu Mia, PhD. All Rights Reserved.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
