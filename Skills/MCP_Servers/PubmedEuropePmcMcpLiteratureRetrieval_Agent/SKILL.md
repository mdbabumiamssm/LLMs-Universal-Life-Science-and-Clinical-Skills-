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
name: 'pubmed-europe-pmc-mcp-literature-retrieval'
description: 'Search PubMed and Europe PMC through MCP, retrieve article metadata and available full text, and preserve identifiers, citations, and MeSH terms for reproducible biomedical literature workflows.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# PubMed and Europe PMC Literature Retrieval via MCP

## Overview

Use the referenced MCP server to search biomedical literature and retrieve metadata, available full text, citations, and MeSH vocabulary. Produce traceable evidence records so downstream summaries can distinguish retrieved findings from missing or incomplete evidence.

## When to Use This Skill

- A research question requires reproducible PubMed or Europe PMC searches.
- Known article identifiers need metadata, abstracts, citations, or accessible full text.
- A search needs MeSH vocabulary or expansion through related literature.
- An agent needs a local STDIO or Streamable HTTP literature connection.

## Core Capabilities

1. **Connect through MCP.** Configure a compatible client and inspect its discovered tool schemas before calling tools.
2. **Search and refine.** Use `pubmed_search_articles`, `pubmed_europepmc_search`, and `pubmed_lookup_mesh` as appropriate.
3. **Retrieve records.** Use `pubmed_fetch_articles` for PMIDs; use `pubmed_europepmc_fetch` with search-result pairs `{source, epmcId}`.
4. **Retrieve available text.** `pubmed_fetch_fulltext` accepts PMIDs, PMCIDs, or DOIs and tries PMC, Europe PMC, then Unpaywall.
5. **Build references.** Use `pubmed_format_citations`, `pubmed_find_related`, and `pubmed_convert_ids`; conversion covers PMC-indexed articles only.

### Setup and transport

Read the repository's current installation requirements and record the selected release. Its documented local runtime choices are Node.js 24+ or Bun 1.4+; the following client configuration launches the published package through STDIO:

```json
{
  "mcpServers": {
    "pubmed-mcp-server": {
      "command": "npx",
      "args": ["-y", "@cyanheads/pubmed-mcp-server"],
      "env": {"MCP_TRANSPORT_TYPE": "stdio"}
    }
  }
}
```

For local Streamable HTTP, launch:

```sh
MCP_TRANSPORT_TYPE=http MCP_HTTP_PORT=3010 npx -y @cyanheads/pubmed-mcp-server
```

Connect the client to the endpoint reported at startup. Pin a verified package version for repeatable deployments. Keep externally exposed services behind the deployment's authentication controls.

Optional environment settings include `NCBI_API_KEY`, `NCBI_ADMIN_EMAIL`, and `UNPAYWALL_EMAIL`; the last enables Unpaywall. `EUROPEPMC_ENABLED=false` disables Europe PMC access. Keep credentials outside evidence reports.

The allowed shell and fetch tools do not themselves provide an MCP session. Use an available MCP-capable client or shell bridge that supports initialization, tool discovery, and tool calls; if unavailable, report that prerequisite instead of fabricating results.

### Reproducible retrieval workflow

1. Define the question, date boundaries, eligible study types, database coverage, and desired result limit. Avoid including patient-identifying information in queries.
2. Inspect the connected server's tool schemas. Record package version or deployment identity and retrieval time in UTC.
3. Construct a database-specific query. For example, a PubMed starting query is `asthma[Title/Abstract] AND biologic*[Title/Abstract] AND 2020:2025[Date - Publication]`. Treat this as an illustrative search, not a validated review strategy; adapt terminology and record every revision.
4. Save the submitted query, effective query when returned, filters, ordering, total matches, and pagination state. Continue within the agreed limit using the returned pagination mechanism. Report whether retrieval is complete or capped.
5. Fetch selected records and preserve original identifiers. Deduplicate using verified identifier mappings; retain source-specific records when a match remains uncertain. Do not treat an unmapped DOI as proof that an article does not exist.
6. Retrieve full text only when needed. Record provider, license when supplied, truncation, and availability per article. Distinguish search snippets, abstracts, and full text in the evidence report.
7. Attach citations to supported claims. Preserve correction or retraction notices when returned and label preprints separately. Citation formatting does not establish study validity.

### Unavailable content and errors

- For zero matches, inspect syntax, dates, and vocabulary; record any broader retry as a changed search.
- For unavailable full text, retain metadata and the reported reason. Do not reconstruct missing text or bypass access restrictions.
- For partial batches, retain successful records and retry only unresolved items. Follow returned continuation or overflow instructions.
- For rate limits, timeouts, or temporary upstream failures, honor retry guidance and use bounded backoff. Stop after three workflow-level retries or the remaining task time budget; return partial results with unresolved errors.
- For invalid arguments or authentication failures, correct the configuration before retrying. Distinguish a failed request from a successful empty response.

## Inputs / Outputs

**Inputs:** Research question or identifiers; search terms and filters; result limit; requested citation format; full-text requirement; MCP connection configuration and optional credentials.

**Outputs:** A search audit and article records containing available PMID, PMCID, DOI, Europe PMC source/ID, title, publication details, abstract, MeSH terms, source links, citation, and retrieval status. Include full-text provenance, license, and truncation when applicable; mark absent fields as unavailable rather than guessing.

**Completion check:** Within 15 minutes, demonstrate a successful search or identifier lookup and produce validated records for available results, with traceable identifiers and explicit missing-data status. A successful zero-hit search is valid if documented; a connection failure is an incomplete workflow, not successful retrieval. Do not claim exhaustive coverage when pagination or failures leave records outstanding.

## References

- [pubmed-mcp-server — repository, installation, configuration, and tool reference](https://github.com/cyanheads/pubmed-mcp-server)
