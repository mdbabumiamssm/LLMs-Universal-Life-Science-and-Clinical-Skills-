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

# Strategy Improvement Plan: The "Optimizer" & Runtime Evolution

**Version**: 1.1 (Evolution of Strategy v1.0)
**Focus**: Optimization, Dynamic Runtime, and Continuous Evaluation

## 1. The Core Shift: From "Static Adapters" to "Intelligent Optimization"

The original plan focused on *syntactic* translation (YAML → JSON). The improved plan adds *semantic* optimization. A prompt that works for GPT-4o is not necessarily optimal for Claude 3.5 Sonnet.

### 1.1 The "Optimizer" Build Step
Instead of a simple deterministic conversion, we introduce an AI-driven build step:

```
[USDL Source] 
     │
     ▼
[Optimizer Agent (Teacher Model)] ───► "Rewrite this prompt for Claude's XML style"
     │                               "Rewrite this prompt for Gemini's structured input"
     │
     ▼
[Platform-Specific Optimized Artifacts]
```

*   **Claude**: Rewrites prompts to use `<input>`, `<instructions>` XML tags; pre-fills "Assistant" responses for steering.
*   **Gemini**: Restructures prompts to leverage long-context window efficiently; optimizes for Google Search grounding.
*   **OpenAI**: Optimizes for concise system messages and specific function calling definitions.

### 1.2 The Evaluation Loop ("The Testbed")
We cannot claim a skill is "optimized" without metrics.

*   **USDL Addition**: Add `evals` section to skill definitions.
    ```yaml
    evals:
      - input: "Find inhibitors for EGFR"
        assertions:
          - contains: "Gefitinib"
          - type: "molecule_list"
    ```
*   **`bioskills test`**: A CLI command that runs these evals against all adapters (Claude, OpenAI, Gemini) and generates a **Scorecard**.
    *   *Result*: "Skill A is 95% accurate on GPT-4o but only 70% on Gemini Flash. Recommendation: Use GPT-4o for this skill."

---

## 2. The Universal Runtime ("BioKernel")

Static files (JSON/YAML) are hard to manage for end-users. We propose a lightweight local server, **BioKernel**.

*   **Architecture**: A Python/Rust local server that implements the **Model Context Protocol (MCP)** and **OpenAI API** natively.
*   **Dynamic Routing**:
    *   User asks: "Analyze this DNA sequence."
    *   BioKernel Config: "Routing Strategy = Cost/Performance Hybrid"
    *   BioKernel Decision: "This is a complex reasoning task -> Route to **Claude 3.5 Sonnet**."
    *   *Next Request*: "Summarize this short abstract."
    *   BioKernel Decision: "This is a simple summary -> Route to **Gemini Flash** (Cheaper/Faster)."
*   **Benefit**: The user installs *one* piece of software. They don't need to manually upload files to OpenAI or Claude. The Kernel handles the connections.

---

## 3. Revised Roadmap

### Phase 1: The Optimizer (Month 1-2)
*   [ ] Implement `bioskills optimize <skill.yaml>` using a meta-prompt.
*   [ ] Create "Style Guides" for each LLM as system prompts for the Optimizer.
*   [ ] Update Adapters to accept "Optimized Prompts".

### Phase 2: The Evaluation Engine (Month 3)
*   [ ] Define `evals` schema in USDL.
*   [ ] Build `bioskills test` runner.
*   [ ] Generate HTML reports comparing model performance per skill.

### Phase 3: The BioKernel Runtime (Month 4-6)
*   [ ] Build a local MCP server that can load *any* USDL skill.
*   [ ] Implement the "Router" logic.
*   [ ] Expose a unified API (OpenAI-compatible) so other apps can use BioKernel.

---

## 4. Software Architecture Diagram (Target State)

```mermaid
graph TD
    User[User / Client App] -->|Unified API / MCP| Kernel[BioKernel Runtime]
    
    subgraph "The Intelligence Layer"
        Kernel -->|Route| Router[Model Router]
        Router -->|Complex Task| Claude[Claude Adapter]
        Router -->|Fast Task| Gemini[Gemini Adapter]
        Router -->|Creative Task| OpenAI[OpenAI Adapter]
    end
    
    subgraph "The Registry"
        Repo[Skills Repo (USDL)] -->|Build & Optimize| Optimized[Optimized Skill Store]
        Optimized --> Kernel
    end
    
    Claude -->|API Call| AnthropicAPI
    Gemini -->|API Call| GoogleVertexAPI
    OpenAI -->|API Call| OpenAI_API
```


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->