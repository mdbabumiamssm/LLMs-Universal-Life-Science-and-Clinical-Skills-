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
name: bio-bgpt-paper-search
description: Search scientific papers and retrieve structured experimental data extracted
  from full-text studies via the BGPT MCP server. Returns 25+ fields per paper including
  methods, results, sample sizes, quality scores, and conclusions. Use for literature
  reviews, evidence synthesis, and finding experimental details not available in abstracts
  alone.
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# BGPT Paper Search

## Overview

BGPT is a remote MCP server that searches a curated database of scientific papers built from raw experimental data extracted from full-text studies. Unlike traditional literature databases that return titles and abstracts, BGPT returns structured data from the actual paper content — methods, quantitative results, sample sizes, quality assessments, and 25+ metadata fields per paper.

## When to Use This Skill

Use this skill when:
- Searching for scientific papers with specific experimental details
- Conducting systematic or scoping literature reviews
- Finding quantitative results, sample sizes, or effect sizes across studies
- Comparing methodologies used in different studies
- Looking for papers with quality scores or evidence grading
- Needing structured data from full-text papers (not just abstracts)
- Building evidence tables for meta-analyses or clinical guidelines

## Setup

BGPT is a remote MCP server — no local installation required.

### Claude Desktop / Claude Code

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "bgpt": {
      "command": "npx",
      "args": ["mcp-remote", "https://bgpt.pro/mcp/sse"]
    }
  }
}
```

### npm (alternative)

```bash
npx bgpt-mcp
```

## Usage

Once configured, use the `search_papers` tool provided by the BGPT MCP server:

```
Search for papers about: "CRISPR gene editing efficiency in human cells"
```

The server returns structured results including:
- **Title, authors, journal, year, DOI**
- **Methods**: Experimental techniques, models, protocols
- **Results**: Key findings with quantitative data
- **Sample sizes**: Number of subjects/samples
- **Quality scores**: Study quality assessments
- **Conclusions**: Author conclusions and implications

## Pricing

- **Free tier**: 50 searches per network, no API key required
- **Paid**: $0.01 per result with an API key from [bgpt.pro/mcp](https://bgpt.pro/mcp)

## Complementary Skills

Pairs well with:
- `literature-review` — Use BGPT to gather structured data, then synthesize with literature-review workflows
- `pubmed-database` — Use PubMed for broad searches, BGPT for deep experimental data
- `biorxiv-database` — Combine preprint discovery with full-text data extraction
- `citation-management` — Manage citations from BGPT search results

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->