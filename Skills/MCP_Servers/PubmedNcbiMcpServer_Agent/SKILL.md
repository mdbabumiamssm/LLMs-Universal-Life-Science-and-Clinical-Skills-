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
9. **Richer evidence-review MCP comparison** - For broader biomedical evidence-review workflows, compare against multi-source PubMed MCP alternatives such as `u9401066/pubmed-search-mcp`, which reports 40 tools, search across PubMed, Europe PMC, CORE, and OpenAlex, full-text access, citation-network exploration, and PICO analysis; prefer `cyanheads/pubmed-mcp-server` when the task needs a lightweight NCBI E-utilities-aligned PubMed workflow, PubMed fidelity, or focused PMID/MeSH/citation handling, and prefer broader evidence-review servers when the task explicitly needs cross-index search, full-text access beyond PubMed, citation-network exploration, or PICO-oriented review support.
10. **Lower-adoption MCP vetting** - Before relying on a newer or low-adoption biomedical literature MCP such as `u9401066/pubmed-search-mcp` (9 GitHub stars in the source finding), inspect the repository, tool surface, data-source coverage, credential and rate-limit handling, install path, and sample outputs against known PubMed records.
11. **Trust review for feature-rich alternatives** - When considering `u9401066/pubmed-search-mcp` or similar feature-rich PubMed MCP alternatives, verify the advertised multi-source coverage, full-text access, citation-network tools, and PICO analysis on a small known-query smoke test; prefer the simpler NCBI E-utilities server when the request only needs PubMed search, PMID metadata, MeSH, related articles, or citation output.
12. **Alternative MCP maturity and overlap checks** - Evaluate `u9401066/pubmed-search-mcp` when PICO analysis, multi-source biomedical literature search, citation networks, or Europe PMC/OpenAlex coverage are required, but first check repository maturity, maintenance signals, setup requirements, and tool overlap against `cyanheads/pubmed-mcp-server`; confirm shared PubMed search, metadata, full-text, and citation workflows do not duplicate or conflict before mixing outputs.
13. **Current upstream capability surface** - Treat `cyanheads/pubmed-mcp-server` as a TypeScript MCP server for NCBI E-utilities search, PubMed metadata and full-text retrieval, citation generation, MeSH exploration, and related-article discovery; choose STDIO for local agent wiring or Streamable HTTP for endpoint-style deployments, and keep usage rate-limit-safe by batching requests conservatively, honoring NCBI E-utilities limits, and preserving identifiers for traceable retries.
14. **Focused versus broader literature MCP selection** - Compare richer biomedical literature MCP alternatives such as `u9401066/pubmed-search-mcp` when a workflow needs its reported 40-tool Python surface, multi-source search across PubMed, Europe PMC, CORE, and OpenAlex, full-text retrieval, citation networks, or PICO extraction; check current maintenance and adoption signals, including the source finding's 9 GitHub stars, and prefer a focused NCBI E-utilities server for PMID-centered PubMed search, metadata, MeSH, related-article, and citation tasks.
15. **cyanheads PubMed MCP operations** - Use `cyanheads/pubmed-mcp-server` for NCBI E-utilities PubMed search, article metadata and full-text retrieval, MeSH exploration, citation generation, and related-article discovery; configure STDIO for local agent use or Streamable HTTP for endpoint deployments, apply conservative NCBI rate limiting and retry discipline, and carry PMIDs, DOIs, MeSH terms, citation outputs, full-text availability, and source URLs through provenance-preserving literature workflows.
16. **Preferred PubMed E-utilities MCP option** - Prefer `cyanheads/pubmed-mcp-server` for standard PubMed E-utilities MCP workflows: select STDIO or Streamable HTTP transport, use the server's search and fetch surfaces for PubMed records, generate citations from returned metadata, explore MeSH terms for query refinement, treat full-text retrieval as bounded by available open/full-text discovery signals, honor NCBI rate limits with conservative batching and retries, and verify biomedical citation outputs against PMIDs, DOIs, article metadata, and source URLs before using them in literature-review or clinical-adjacent workflows.
17. **Broader literature MCP handoff** - Prefer a broader literature MCP such as `u9401066/pubmed-search-mcp` when the request requires its reported multi-source search across PubMed, Europe PMC, CORE, and OpenAlex plus full-text retrieval, citation networks, or PICO analysis; keep the focused NCBI E-utilities server as the default for PubMed-only search, PMID metadata, MeSH, related-article discovery, and citation workflows.
18. **Preferred PubMed MCP reference** - Use `cyanheads/pubmed-mcp-server` as the preferred PubMed MCP reference for NCBI E-utilities workflows: run it in STDIO mode for local agent wiring or Streamable HTTP mode for endpoint deployments, use its PubMed search, article metadata and full-text retrieval, citation generation, MeSH exploration, and related-article discovery features, and apply conservative batching, retry, and rate-limit handling around NCBI E-utilities requests.
19. **Feature-rich biomedical literature MCP comparison** - Include `u9401066/pubmed-search-mcp` in comparison notes when a workflow needs its reported 40-tool Python surface, multi-source search across PubMed, Europe PMC, CORE, and OpenAlex, full-text retrieval, citation networks, or PICO analysis; retain `cyanheads/pubmed-mcp-server` as the higher-adoption default for standard PubMed/NCBI E-utilities MCP workflows.
20. **Reference PubMed MCP implementation** - Treat `cyanheads/pubmed-mcp-server` as the reference PubMed MCP implementation for NCBI E-utilities search, article metadata fetch, full-text and citation workflows, MeSH exploration, and related-article discovery; choose STDIO for local agent integration or Streamable HTTP for endpoint deployments, handle NCBI rate limits with conservative batching and retries, and preserve PMIDs, DOIs, citation metadata, MeSH terms, full-text availability signals, related-article links, repository URL, and source timestamps in provenance notes.

## Alternatives and Comparison

- Use a richer biomedical literature MCP such as `u9401066/pubmed-search-mcp` when the user needs combined PubMed, Europe PMC, CORE, and OpenAlex search, full-text access, citation-network exploration, or PICO analysis in one MCP workflow.
- Prefer the PubMed-only `cyanheads/pubmed-mcp-server` when the task is centered on NCBI E-utilities, PMID-based retrieval, MeSH exploration, related PubMed records, or citation generation from PubMed metadata.
- Treat `u9401066/pubmed-search-mcp` as a lower-adoption option despite its broader claimed tool surface: the source finding reports 9 GitHub stars, so confirm the advertised tools exist, run a small PMID/query smoke test, review dependency and credential requirements, and preserve source names in outputs so cross-source results remain traceable.

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
- Current source finding: https://github.com/cyanheads/pubmed-mcp-server
- NCBI E-utilities documentation: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- PubMed help: https://pubmed.ncbi.nlm.nih.gov/help/
- MeSH browser: https://meshb.nlm.nih.gov/
- Unpaywall: https://unpaywall.org/
- Richer literature MCP comparison source: https://github.com/u9401066/pubmed-search-mcp
- Source finding: https://github.com/cyanheads/pubmed-mcp-server
- Preferred PubMed E-utilities MCP source: https://github.com/cyanheads/pubmed-mcp-server
- Source finding: https://github.com/u9401066/pubmed-search-mcp
- Preferred PubMed MCP reference source: https://github.com/cyanheads/pubmed-mcp-server
- Feature-rich biomedical literature MCP comparison source: https://github.com/u9401066/pubmed-search-mcp
- Reference PubMed MCP implementation source: https://github.com/cyanheads/pubmed-mcp-server
