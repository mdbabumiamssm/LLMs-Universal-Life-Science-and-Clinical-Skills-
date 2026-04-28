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

---
name: bio-medea-therapeutic-discovery
description: An AI agent for therapeutic discovery that executes transparent, multi-step
  omics analyses including research planning, code execution, and literature reasoning.
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# Medea Therapeutic Discovery Agent

Medea is a multi-stage AI agent designed for therapeutic discovery, modeled after 2026 state-of-the-art open source architectures. It executes transparent, multi-step omics analyses.

## When to Use This Skill

*   "Run multi-omics therapeutic discovery pipeline"
*   "Analyze omics data for novel drug targets using Medea"
*   "Perform literature reasoning and consensus reconciliation for target X"

## Core Capabilities

1.  **Research Planning**: Formulates step-by-step omics analysis plans.
2.  **Code Execution**: Generates and executes Python/R scripts for data processing.
3.  **Literature Reasoning**: Retrieves and synthesizes current literature.
4.  **Consensus Stage**: Reconciles experimental evidence with literature to propose high-confidence targets.

## Workflow

1.  **Step 1**: Initialize Medea agent with target disease or omics dataset.
2.  **Step 2**: Execute the multi-stage pipeline across planning, coding, literature review, and consensus validation.

## Example Usage

**User**: "Run Medea analysis on the provided breast cancer multi-omics dataset."

**Agent Action**:
```bash
python3 -m medea.agent --dataset breast_cancer_omics.h5ad --mode full_discovery
```

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->