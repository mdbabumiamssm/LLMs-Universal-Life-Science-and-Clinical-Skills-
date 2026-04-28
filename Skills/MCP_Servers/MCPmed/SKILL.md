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
name: bio-mcpmed-bioinformatics-server
description: Model Context Protocol (MCP) server for bioinformatics web services like
  GEO, STRING, and UCSC Cell Browser.
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# MCPmed Bioinformatics Web Services

Adapts the Model Context Protocol (MCP) to bioinformatics web server backends. This creates a standardized, machine-actionable layer for LLMs to interact with external biological resources, matching the 2026 standard for agentic tools.

## When to Use This Skill

*   "Query STRING database for protein-protein interactions via MCP"
*   "Fetch dataset metadata from GEO using MCPmed"
*   "Access UCSC Cell Browser data through MCP"

## Core Capabilities

1.  **GEO Integration**: Search and retrieve Gene Expression Omnibus metadata autonomously.
2.  **STRING DB Access**: Query protein-protein interaction networks contextually.
3.  **UCSC Cell Browser**: Programmatic access to single-cell datasets.

## Workflow

1.  **Step 1**: Start the MCPmed server to expose the bioinformatics backend tools.
2.  **Step 2**: Connect the LLM client using MCP to query the integrated databases.

## Example Usage

**User**: "Query the STRING database for interactions with TP53."

**Agent Action**:
```bash
python3 -m mcpmed.cli query string --gene TP53
```

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->