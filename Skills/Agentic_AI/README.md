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

# Agentic AI (2026)

This directory contains the core cognitive architectures for autonomous systems.

## Key Modules

### 1. Multi-Agent Systems (`Multi_Agent_Systems/`)
Moved beyond simple ReAct loops to hierarchical orchestration.

*   **`orchestrator.py` (NEW):** Implements the **Supervisor Pattern**. A meta-agent ("Supervisor") breaks down a complex objective into sub-tasks and routes them to specialized workers (e.g., Coder, Reviewer).
    *   *Usage:* `python orchestrator.py`
*   **`debate_supervisor.py`:** Simulates a multi-turn debate between agents with opposing viewpoints to reduce hallucination and improve reasoning quality.

### 2. Reasoning Models (`Reasoning_Models/`)
*   **`tree_of_thought.py`:** Explores multiple reasoning paths before committing to a decision.

### 3. Memory Systems (`Memory_Systems/`)
*   **`memory_architecture.py`:** Interfaces for short-term (context window) and long-term (vector store) memory.

## Future Work
*   Integration with **LangGraph** for more robust state management.
*   Implementation of **Language Agent Tree Search (LATS)**.

## 2026 Additions
*   **LangGraph_Platform/** – wires LangChain’s LangGraph/LangSmith stack (GA May 2025) into our swarm so we get stateful supervisors, checkpoints, and Studio observability out of the box.
*   **CrewAI_Pipelines/** – brings CrewAI’s Crews + Flows dual abstraction plus the new Agent Operations Platform / Factory runtimes for governed enterprise launches.
*   **NVIDIA_Blueprints/** – operationalizes NVIDIA’s Secure Data-Driven Agents + Data Flywheel blueprints on top of NIM microservices and the BlueField STX hardware refresh announced at GTC 2026.
*   **OpenHands_Coding_Agent/** – standardizes hand-offs to the OpenHands (ex‑OpenDevin) headless CLI/SDK when we need a persistent IDE-grade coding agent with JSONL traces.
*   **AgentScope_Runtime/** – documents how to deploy AgentScope + AgentScope Runtime sandboxes so BioKernel swarms can call FastAPI-hosted agents with hardened tool execution.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
