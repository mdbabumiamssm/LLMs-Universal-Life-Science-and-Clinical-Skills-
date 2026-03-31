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

# Tutorial: The USDL Transpiler (Optimizer 2.0)

**Component:** Universal Skill Definition Language
**Goal:** Write Once, Run on OpenAI/Anthropic/Gemini
**Key Feature:** Bidirectional Transpilation

## Introduction

Managing different prompt formats for different models is a nightmare.
*   **OpenAI** wants JSON Schemas.
*   **Anthropic** wants XML tags and `<thinking>` blocks.
*   **Gemini** wants clear Input/Output constraints.

The **USDL Transpiler** solves this. You define a skill *once* in a generic JSON format, and the transpiler generates the perfect prompt/schema for your target model.

## Step 1: Define a Skill (The Universal Spec)

Create a file named `my_skill.json`:

```json
{
  "name": "Drug Interaction Checker",
  "description": "Checks if two drugs have adverse interactions.",
  "inputs": [
    {"name": "drug_a", "description": "Name of first drug", "type": "string"},
    {"name": "drug_b", "description": "Name of second drug", "type": "string"}
  ],
  "outputs": [
    {"name": "interaction_severity", "description": "None, Mild, Moderate, Severe", "type": "string"},
    {"name": "explanation", "description": "Clinical mechanism of interaction", "type": "string"}
  ],
  "safety_checks": [
    "Cite specific CYP450 pathways if known.",
    "Do not invent interactions."
  ]
}
```

## Step 2: Transpile for OpenAI

Run the CLI:

```bash
python3 usdl_transpiler.py --file my_skill.json --provider openai
```

**Result:** A JSON object containing the `system` prompt and strict `json_schema` ready for the OpenAI API.

## Step 3: Transpile for Anthropic

```bash
python3 usdl_transpiler.py --file my_skill.json --provider anthropic
```

**Result:** An XML-heavy prompt template that encourages the model to use `<thinking>` tags before answering.

## Why use this?

1.  **Portability:** Swap models without rewriting 50 prompts.
2.  **Optimization:** The transpiler automatically adds best practices (like "Think step-by-step") appropriate for each model.
3.  **Governance:** You can inject "Safety Checks" into every prompt globally.


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->