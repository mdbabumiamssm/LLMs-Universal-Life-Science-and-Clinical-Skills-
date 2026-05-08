<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'pubmed-ncbi-mcp-server'
description: 'Use the cyanheads PubMed MCP server to search PubMed, fetch metadata and full text, generate citations, inspect MeSH, and find related research.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# PubMed NCBI MCP Server

## Overview

This skill guides agents in using the `cyanheads/pubmed-mcp-server`, a TypeScript MCP server for the NCBI E-utilities API. It is useful when biomedical literature work needs an agent-facing interface for PubMed search, article metadata retrieval, open full-text discovery, MeSH exploration, related articles, or citation generation.

Use this skill to connect biomedical research prompts to a repeatable PubMed MCP workflow instead of relying on ad hoc web search. It helps preserve traceability by grounding outputs in PubMed records, NCBI identifiers, citation metadata, and related literature links.

## When to Use This Skill

- The user asks to search PubMed, NCBI E-utilities, or biomedical literature through MCP.
- The task needs PubMed article metadata, abstracts, identifiers, journal details, or citation fields.
- The user needs open-access or full-text discovery for PubMed-indexed research.
- The workflow requires MeSH term exploration, PubMed related articles, or research discovery around a biomedical topic.
- The user wants citations generated from PubMed records.
- The environment needs a PubMed MCP server that supports STDIO or Streamable HTTP transport.

## Core Capabilities

1. **PubMed search** - Query PubMed through the NCBI E-utilities-backed MCP surface and return article identifiers and search results suitable for downstream retrieval.
2. **Article metadata retrieval** - Fetch structured PubMed metadata such as titles, authors, abstracts, journal information, publication dates, identifiers, and related bibliographic fields.
3. **Full-text discovery** - Check for full-text or open-access availability through the server's supported discovery mechanisms, including Unpaywall-related workflows where configured.
4. **Citation generation** - Produce citations from PubMed records for research summaries, literature reviews, bibliographies, or agent-generated reports.
5. **MeSH exploration** - Inspect Medical Subject Headings associated with biomedical concepts or articles to refine searches and improve topic coverage.
6. **Related research discovery** - Use PubMed related-article functionality to expand from seed papers into adjacent biomedical literature.
7. **Transport selection** - Run the MCP server over STDIO for local agent integration or Streamable HTTP when a network-accessible MCP endpoint is required.
8. **Provenance-preserving literature workflow** - Keep PubMed metadata retrieval distinct from full-text discovery, respect NCBI E-utilities rate limits, and preserve PMIDs, DOIs, MeSH terms, citation outputs, related-article links, and full-text availability signals in downstream research notes.

## Inputs / Outputs

**Inputs**

- Biomedical topic, keyword query, author name, journal name, PMID, DOI, MeSH term, or seed article.
- Desired operation, such as search, fetch metadata, discover full text, generate citation, inspect MeSH, or find related articles.
- Runtime preferences, including STDIO versus Streamable HTTP transport and any required NCBI or full-text discovery configuration.

**Outputs**

- PubMed search results with identifiers and enough metadata to select relevant records.
- Structured article metadata, abstracts, bibliographic fields, PMIDs, DOIs, and related identifiers when available.
- Full-text availability signals and open-access links when discoverable.
- Citation strings or citation-ready metadata derived from PubMed records.
- MeSH terms and related-article sets for query refinement or literature expansion.
- A concise provenance trail naming PubMed, NCBI E-utilities, and the MCP server repository when reporting results.

## References

- Source repository: https://github.com/cyanheads/pubmed-mcp-server
- NCBI E-utilities documentation: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- PubMed help: https://pubmed.ncbi.nlm.nih.gov/help/
- MeSH browser: https://meshb.nlm.nih.gov/
- Unpaywall: https://unpaywall.org/
