---
name: biomcp-server
description: "Deploy and operate a BioMCP Model Context Protocol server that provides MCP-compatible clients (Claude Desktop, LobeChat, BioKernel) with unified access to PubMed, ClinicalTrials.gov, PubTator3 annotations, and genomic variant lookups."
compatibility: "MCP-compliant clients"
allowed-tools: "web_fetch"
metadata:
  author: BioMCP Team
  version: "1.0.0"
  keywords: "MCP, PubMed, ClinicalTrials, server, uv"
  measurable_outcome: "Stand up a working BioMCP endpoint (pip or uv) and return ≥1 PubMed + ≥1 ClinicalTrials.gov response to the client within 10 minutes."
  license: MIT
---

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

# BioMCP Server

Deploy and operate the BioMCP server so MCP-compatible clients can query biomedical databases via a single standardized interface.

Use when an MCP client needs unified access to PubMed literature, ClinicalTrials.gov metadata, PubTator3 entity annotations, or genomic variant lookups without writing bespoke API wrappers.

## When to Use

- **Literature search** — running PubMed/PMC queries from inside an MCP client.
- **Entity normalization** — mapping free text to genes, diseases, chemicals, or species via PubTator3.
- **Trial discovery** — retrieving ClinicalTrials.gov metadata and protocols.
- **Variant lookups** — fetching gene/variant summaries from connected genomic sources.

## Workflow

1. **Install dependencies** — run `uv sync` (preferred) or `pip install .` in the repo root.
2. **Start server** — execute `python -m biomcp.server` or `make run`; Docker Compose is also provided.
3. **Configure client** — add the command/args snippet from `README.md` into the MCP client config (Claude Desktop, BioKernel, LobeChat).
4. **Validate endpoints** — invoke PubMed, ClinicalTrials, and variant tools to confirm connectivity.
5. **Monitor** — capture logs, rate-limit statuses, and data-source versions for audit.

## Guardrails

- Keep API keys and env secrets outside the repo.
- Respect upstream rate limits to avoid throttling or bans.
- Document which data sources are enabled per deployment and update when they change.

## References

- Source repo, configuration examples, and Docker setup in `README.md`, `repo/docker-compose.yml`, and `repo/Makefile`.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->