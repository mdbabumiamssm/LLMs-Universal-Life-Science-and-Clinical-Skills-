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
name: 'pubmed-europe-pmc-mcp'
description: 'Search PubMed and Europe PMC through MCP, retrieve article metadata and available full text, resolve identifiers, and extract evidence with citations and MeSH-guided queries.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# PubMed and Europe PMC via MCP

## Overview

Use this skill to conduct reproducible biomedical literature searches and assemble traceable evidence from retrieved articles. The referenced MCP server connects literature discovery, metadata, available full text, citations, and MeSH vocabulary through STDIO or Streamable HTTP.

## When to Use This Skill

- Search a biomedical question using keywords, controlled vocabulary, and explicit eligibility criteria.
- Retrieve articles from PMIDs, PMCIDs, DOIs, or incomplete references.
- Check whether full text is available before extracting detailed results.
- Build a cited evidence table or expand a search through related literature.
- Configure a client to use this literature server.

## Core Capabilities

1. **Connect and inspect capabilities.** Use the repository documentation in References to confirm requirements for the installed release. A local STDIO client configuration is:

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

   For Streamable HTTP, configure the client with the chosen deployment's MCP endpoint; the repository documents `MCP_TRANSPORT_TYPE=http`. Optional server settings include `NCBI_API_KEY`, `NCBI_ADMIN_EMAIL`, and `UNPAYWALL_EMAIL`; `EUROPEPMC_ENABLED=false` disables Europe PMC. Keep credentials out of reports. Inspect the connected server's tool schemas before calling tools; do not infer arguments from names. If the host only exposes the allowed file, shell, and fetch tools, use an existing MCP client through its documented interface. A web fetch alone does not establish an MCP session; report a missing client as a prerequisite.

2. **Construct and record searches.** Translate the question into concept groups, joining synonyms with OR and concepts with AND. Use `pubmed_lookup_mesh` to verify headings, then `pubmed_search_articles`; use `pubmed_europepmc_search` for complementary coverage. Illustrative PubMed query:

   ```text
   ("Asthma"[MeSH Terms] OR asthma[Title/Abstract])
   AND ("Air Pollution"[MeSH Terms] OR air pollution[Title/Abstract])
   ```

   Validate query syntax separately for each database. Record exact queries, filters, search time, counts, and pagination state. Inspect returned query interpretation when available. Follow pagination until the agreed scope is covered; label partial searches. For unexpectedly sparse results, check spelling and restrictive filters before concluding that evidence is absent.

3. **Retrieve and reconcile records.** Use `pubmed_fetch_articles` or `pubmed_europepmc_fetch` for complete metadata. Preserve PMID, PMCID, DOI, and Europe PMC source/identifier pairs separately. Use `pubmed_convert_ids` when applicable, recognizing its PMC coverage limitation; a failed conversion does not prove an article is absent. Deduplicate using verified identifiers, retaining provenance and distinguishing preprints from published versions.

4. **Check and retrieve full text.** Use `pubmed_fetch_fulltext`, which supports PMC, Europe PMC, and Unpaywall retrieval routes. Record the answering provider, URL, license when supplied, and retrieval status. Distinguish a discovery link from successfully retrieved text. Inspect truncation and retrieve omitted relevant sections before claiming comprehensive coverage. If unavailable, retain the abstract and explicitly limit extraction to that material.

5. **Resolve and format citations.** Use `pubmed_lookup_citation` for incomplete references, `pubmed_find_related` to expand discovery, and `pubmed_format_citations` for bibliography output. Verify resolved records against the supplied title, journal, and year. Preserve ambiguity rather than selecting an unsupported match; carry correction or retraction notices into the evidence report.

6. **Extract source-grounded evidence.** For each included record, capture study design, population, intervention or exposure, comparator, outcomes, and limitations only where reported. Link each substantive finding to its identifier and abstract or full-text section. Separate reported results from interpretation; mark missing values as not reported. Do not treat citation counts, search rank, or full-text availability as evidence quality.

## Inputs / Outputs

**Inputs:** Research question or identifiers; inclusion and exclusion criteria; date, language, and publication-type limits; desired citation style; retrieval scope; and an available MCP connection.

**Outputs:** Search log, deduplicated record set, full-text availability ledger, evidence table, and bibliography. Suggested evidence columns are identifier, source, study design, population, finding, supporting section, limitations, and retrieval status.

**Completion check:** Within the stated time budget, verify that each included row has a resolvable source identifier, each extracted finding has supporting retrieved text, and all exclusions, unresolved identifiers, unavailable text, and incomplete pagination are disclosed. Honor returned batch limits and retry guidance; retry transient failures within the budget, then return partial results with explicit gaps. Report connection failures separately from zero search results. The time budget is a workflow target, not a guarantee of exhaustive retrieval.

## References

- [PubMed MCP server: configuration, tools, and current schemas](https://github.com/cyanheads/pubmed-mcp-server).
