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
name: automated-web-research
description: Performs web searches with cited claims, confidence scores, and multi-source synthesis, producing structured research briefs.
keywords:
  - research
  - web
  - synthesis
  - mcp
measurable_outcome: Synthesizes a structured brief from at least 5 different sources with citations.
license: MIT
metadata:
  author: Agentic AI Tools
  version: "1.0.0"
compatibility:
  - system: Multi-platform
allowed-tools:
  - google_web_search
  - web_fetch
---

# Automated Web Research

This skill enables agents to autonomously research topics on the web, evaluate the credibility of sources, and synthesize information into structured, cited reports.

## When to Use This Skill

*   When gathering background information on a new topic.
*   To verify claims or check facts against recent online sources.
*   To compile comprehensive literature or market reviews.

## Core Capabilities

1.  **Autonomous Search**: Formulates queries and traverses search results.
2.  **Source Evaluation**: Assigns confidence scores to retrieved claims.
3.  **Synthesis & Citation**: Generates cohesive briefs with inline citations to source material.

## Example Usage

**User**: "Research recent advancements in solid-state batteries."

**Agent Action**:
```bash
python3 src/research/run_brief.py --topic "solid-state batteries" --format structured
```

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->