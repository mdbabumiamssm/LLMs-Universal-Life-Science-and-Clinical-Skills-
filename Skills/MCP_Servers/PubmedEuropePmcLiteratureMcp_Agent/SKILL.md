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
name: 'pubmed-europe-pmc-literature-mcp'
description: 'Connect to PubMed and Europe PMC through MCP to search biomedical literature, retrieve article metadata and available full text, and produce source-linked citations and MeSH-informed results.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# PubMed and Europe PMC Literature MCP

## Overview

Use this skill to connect biomedical literature retrieval to an MCP-capable workflow. Search PubMed and Europe PMC, retrieve available evidence, and produce traceable records that distinguish abstracts from full text.

## When to Use This Skill

- A research question needs a reproducible biomedical literature search.
- Known identifiers need article metadata, references, or available full text.
- MeSH vocabulary can improve query construction.
- A literature workflow needs a local STDIO or Streamable HTTP connection.

## Core Capabilities

1. **Connect the server.** Use STDIO or Streamable HTTP and discover the deployed tool schemas.
2. **Search literature.** Route PubMed queries to `pubmed_search_articles` and Europe PMC queries to `pubmed_europepmc_search`.
3. **Retrieve records.** Use `pubmed_fetch_articles` for PMIDs; `pubmed_europepmc_fetch` accepts `records: [{source, epmcId}]` copied from search hits.
4. **Resolve identifiers and vocabulary.** Use `pubmed_convert_ids` and `pubmed_lookup_mesh`. ID conversion covers PMC-indexed articles only.
5. **Retrieve accessible text.** `pubmed_fetch_fulltext` accepts PMIDs, PMCIDs, and DOIs, trying PMC, Europe PMC, then Unpaywall.
6. **Build references.** Use `pubmed_format_citations` and `pubmed_find_related` for citations and connected literature.

### Installation and connection

The [upstream repository](https://github.com/cyanheads/pubmed-mcp-server) documents Node.js 24+ or Bun 1.4.4+. For local STDIO, configure the MCP client:

```json
{
  "mcpServers": {
    "pubmed-mcp-server": {
      "command": "npx",
      "args": ["-y", "@cyanheads/pubmed-mcp-server"]
    }
  }
}
```

For local Streamable HTTP:

```sh
MCP_TRANSPORT_TYPE=http MCP_HTTP_PORT=3010 npx -y @cyanheads/pubmed-mcp-server
```

Connect to the endpoint reported at startup. Alternatively, the documented hosted endpoint is `https://pubmed.caseyjhand.com/mcp`.

Optional configuration: `NCBI_API_KEY`, `NCBI_ADMIN_EMAIL`, and `UNPAYWALL_EMAIL`; the last enables Unpaywall. `EUROPEPMC_ENABLED=false` disables Europe PMC.

Choose the connection appropriate to the task; do not install or reconfigure a working deployment unnecessarily. Record the deployed version when available and pin a verified release for repeatability. Keep credentials out of reports.

The allowed shell and fetch tools do not automatically establish an MCP session. Use an available MCP-capable client or shell bridge for initialization, tool discovery, and invocation. If none exists, report the missing prerequisite; do not claim that a normal HTTP fetch executed an MCP tool.

### Retrieval workflow

1. **Set scope.** Capture the research question, date interval, eligible study types, databases, desired result limit, and whether full text is required.
2. **Inspect schemas.** Read the connected server's current tool definitions before constructing arguments. Treat this document's tool names as routing guidance, not a substitute for schema validation.
3. **Construct the search.** Combine concepts with Boolean operators and database-specific fields. An illustrative PubMed query is `asthma[Title/Abstract] AND biologic*[Title/Abstract]`. Adapt vocabulary to the question and use returned MeSH search clauses when appropriate. Do not assume PubMed field syntax transfers unchanged to Europe PMC.
4. **Record and paginate.** Save the submitted query, effective query when available, filters, retrieval time, total matches, and continuation state. Follow the deployed schema's offset or cursor mechanism until the requested limit or completion. Label capped retrieval explicitly.
5. **Fetch selected records.** Validate identifier types before retrieval. Deduplicate by verified identifiers while retaining database provenance. An unsuccessful identifier conversion is not proof that a publication does not exist; try an identifier or title search and verify the candidate metadata.
6. **Assess text availability.** Preserve the returned provider, availability reason, license, and truncation information. Keep metadata-only, abstract-only, partial-text, and full-text records distinct. Follow continuation instructions for deferred content when the task requires it; never reconstruct unavailable passages.
7. **Produce evidence-linked output.** Link each supported claim to the retrieved record. Label preprints and retain correction or retraction notices when available. Separate study findings from interpretation; citation formatting alone does not establish evidence quality.

### Error handling and completion

- For zero matches, check vocabulary and filters; record any broadened query as a separate search.
- For partial batches, retain successful records and retry unresolved items only.
- For transient failures, follow retry guidance with bounded backoff. Stop after three workflow-level retries or when the remaining time budget is exhausted.
- For invalid arguments or authentication failures, correct the cause before retrying. Distinguish failed requests from successful empty responses.
- When full text is unavailable, return the verified metadata and reason; do not bypass access restrictions.

Within 15 minutes, complete a search or identifier lookup and produce traceable results with explicit availability status. A documented successful zero-hit search is valid output. A connection failure is an incomplete workflow and must be reported as such. Do not claim exhaustive coverage while pagination, deferred content, or unresolved failures remain.

## Inputs / Outputs

**Inputs:** Research question or article identifiers; search terms, filters, date boundaries, and result limit; requested citation format and full-text scope; MCP connection details and optional environment configuration.

**Outputs:** A search audit and evidence table or structured records. Include available title, publication details, PMID, PMCID, DOI, Europe PMC source/ID, abstract, MeSH terms, citation, and source URL. For retrieved text, include provider, license when reported, completeness, and availability status. Mark missing fields explicitly rather than guessing.

**Validation:** Confirm that identifiers and links match retrieved records, summaries reflect the material actually inspected, and reported counts distinguish matches from fetched records. List unresolved items and the next action needed without presenting partial retrieval as complete.

## References

- [pubmed-mcp-server: installation, transports, configuration, and tool reference](https://github.com/cyanheads/pubmed-mcp-server)
