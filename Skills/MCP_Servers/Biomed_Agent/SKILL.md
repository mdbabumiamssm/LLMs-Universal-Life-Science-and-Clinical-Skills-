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
name: biomed-agent-mcp
description: A general-purpose biomedical knowledge assistant that connects to MCP biomedical data sources (OpenTargets, Monarch, MyGene, MyChem, MyDisease) and synthesizes answers using LLMs.
keywords:
  - mcp
  - biomed-agent
  - general-purpose
  - knowledge-graph
  - data-integration
measurable_outcome: Successfully query at least three distinct biomedical databases (e.g., Monarch, MyGene, OpenTargets) via MCP and synthesize a comprehensive answer in a single workflow.
license: MIT
metadata:
  author: nickzren
  source: "https://github.com/nickzren/biomed-agent"
  version: "2026.04"
compatibility:
  - system: Python 3.10+
allowed-tools:
  - run_shell_command
  - web_fetch
  - read_file
---

# Biomed Agent (MCP Client)

A general-purpose biomedical knowledge assistant that uses the Model Context Protocol (MCP) to access multiple biomedical data sources dynamically. By aggregating capabilities from sources like OpenTargets, Monarch, MyGene, MyChem, and MyDisease, it effectively bridges LLM reasoning with real-time biological data.

## When to Use This Skill
- You need to perform cross-database queries without manually navigating each API.
- You want an LLM to synthesize data on genes, diseases, and chemical compounds seamlessly.
- You are building an agentic workflow that requires standardized, unified access to biological data using MCP.

## Core Capabilities
- **MCP Integration:** Dynamically connects to specialized Model Context Protocol servers.
- **Data Synthesis:** Retrieves raw facts from various databases and synthesizes them into actionable insights.
- **Broad Coverage:** Spans genomics (MyGene), chemistry/pharmacology (MyChem, OpenTargets), and clinical/phenotypic data (Monarch, MyDisease).

## Example Workflow
1. Start the MCP server instances for the required databases.
2. Initialize `biomed-agent` and connect it to the MCP servers.
3. Submit a query (e.g., "Find all approved drugs targeting ERBB2 and detail their associated pathways").
4. The agent retrieves targets from MyGene, drug data from OpenTargets/MyChem, and outputs a synthesized report.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->