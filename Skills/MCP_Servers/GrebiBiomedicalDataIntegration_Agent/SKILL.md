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
name: 'grebi-biomedical-data-integration'
description: 'Integrate biomedical knowledge with GrEBI through ontology-aware identifier mapping, provenance-preserving graph queries, and verified HPC pipeline, API, and MCP workflows.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# GrEBI Biomedical Data Integration

## Overview

Use GrEBI to investigate relationships across biomedical resources through aggregated knowledge graphs, ontology mappings, and API or MCP queries. This skill guides source selection, identifier resolution, provenance preservation, and preparation of the containerised Nextflow aggregation pipeline. Scope the 15-minute outcome to a bounded query on an existing deployment or a verified aggregation readiness report; it is not a full HPC build-time guarantee.

## When to Use This Skill

- A question requires relationships spanning multiple biomedical databases.
- Gene, disease, phenotype, chemical, or ontology identifiers need resolution within a selected GrEBI graph.
- An agent needs to discover and use GrEBI's read-only MCP tools or REST query templates.
- A local or HPC aggregation run needs datasource, mapping, resource, and deployment checks.
- Results need traceable source identifiers and relationship-level evidence.

## Core Capabilities

1. **Discover source coverage.** The repository describes aggregation from EMBL-EBI resources, MONARCH, DisMech, ROBOKOP, and Ubergraph. Datasource configurations also include resources such as ChEMBL, GWAS Catalog, and Expression Atlas. Inspect `configs/datasource_configs` and the selected configuration in `configs/subgraph_configs`; a configured source is not proof it is loaded in the chosen deployment. Record actual graph coverage, source versions when available, and missing resources.

2. **Check aggregation prerequisites.** GrEBI uses a containerised Nextflow pipeline with Rust and Python processing. The documented local test route requires Docker, the Compose plugin, and disk space to build its image. Before a production run, inspect the selected launcher, Nextflow configuration, container version, download locations, scheduler settings, CPU and memory requests, and writable work/output storage. Do not treat EBI-specific NFS paths as portable; check configured URL fallbacks. RDF conversion loads the graph into memory, and Parquet conversion reads its input file into memory, so assess source sizes before choosing resources. No universal CPU, RAM, disk, or GPU minimum is established here.

3. **Resolve identifiers and ontology mappings.** GrEBI applies Bioregistry normalisation to string keys and values and uses canonical CURIEs with lowercase prefixes. Preserve original identifiers alongside normalised identifiers and resolved graph node IDs. Inspect `identifier_props` and `additional_equivalence_groups`: shared identifiers cause transitive clique merging, while prefix normalisation alone does not establish biological equivalence. Do not merge entities from label similarity or embedding proximity. Check organism context, ambiguous mappings, obsolete terms, and graph-specific cross-species equivalences before interpreting a merged node.

4. **Prepare provenance-bearing ingestion.** Inputs to the core data model are JSONL node objects; identifier-valued properties create edges when their targets resolve to nodes. Use `grebi:value` and `grebi:properties` to retain annotations on properties and edges. The documented KGX and SSSOM ingest tools carry extra fields as edge metadata; retain source records, mapping predicates, and evidence through transformations. Validate source schemas before ingestion because GrEBI does not supply general schema validation. Inspect rejected or skipped records rather than interpreting an empty ingest as success.

5. **Operate supported interfaces.** The README advertises the development MCP endpoint `https://wwwdev.ebi.ac.uk/spot/grebi/api/v1/mcp`; `docs/mcp.md` instead shows `https://www.ebi.ac.uk/spot/kg/api/v1/mcp`. Both describe Streamable HTTP. Select the intended deployment and verify its availability; do not assume the two hosts have identical data. Discover REST routes from its `/api/v1/openapi.json` and MCP tools from `/api/v1/mcp/catalogue`. The MCP guide documents unauthenticated, read-only access, but verify the chosen deployment's access requirements. PostgreSQL serves the API; Neo4j is used for pipeline query materialisation, with optional live template execution through the Cypher service.

6. **Execute bounded, traceable queries.** Follow the workflow below using discovered tool schemas and graph-specific templates. Return source evidence with each relationship, distinguish observed associations from inference, and record limits or missing provenance rather than inventing support.

### Query workflow

1. Capture the biological question, identifiers, organism, intended graph, desired relationship types, and result limit. Prefer an existing graph for a short investigation.
2. Retrieve the deployment's catalogue and OpenAPI description. When an MCP client is available, initialise its Streamable HTTP connection and inspect the `grebi://graphs` and `grebi://query_templates` resources. The declared tools in this skill do not themselves guarantee an MCP client; use schema-verified REST calls when one is unavailable.
3. Choose a graph whose loaded sources cover the question. Use discovered `lookup_nodes` or `search_nodes` schemas to resolve inputs, then inspect candidates with `get_node`. Every MCP tool requires a `graph` argument. Do not fabricate template names, parameters, or node IDs.
4. Select an advertised query template or follow relationships with `list_node_edges`. Template pagination uses `pageNum` and `pageSize` with a documented maximum page size of 100; sorting uses `sortBy` and `sortDir`. Follow the discovered schema for page numbering and allowed sort fields. The MCP guide documents a 4,096-character text-argument limit and 300 calls per minute per client; respect any stricter deployed limit.
5. Check completeness. Template responses include `rows`, `totalNumRows`, and `totalNumPages`. Full node responses truncate property values according to `maxValues` (default 20, maximum 500), report cuts in `grebi:truncated`, and omit embeddings. Use paginated edges for relationship coverage; do not call a truncated node response exhaustive.
6. Produce a result table or JSON containing graph, node and source IDs, relationship predicate and direction, available evidence metadata, and mapping decisions. Record endpoint, retrieval time, template/tool or REST route, parameters, pagination, and source release information when exposed. Verify at least one returned relationship against its node/edge metadata. An empty result is valid only with confirmed coverage and successful requests; distinguish it from connection or parsing failures.

### Aggregation workflow

- Pin the repository revision and selected graph/datasource configuration. Check download permissions, source licences, expected formats, and resource settings before launching work.
- Run the configured download stage before ingestion. Catalogue discovery and cached downloads are separate: refreshing a catalogue does not necessarily refresh a file at an unchanged URL.
- Follow the checked-in launcher for ingest, ID assignment, merge, indexing, linking, Neo4j creation, query materialisation, and PostgreSQL creation. Preserve logs, source release metadata, mapping configuration, and database artefact locations.
- For an authorised local smoke test, the README documents `docker build -t ghcr.io/ebispot/grebi_combined:dev .` followed by `bash tests/run_e2e.sh test_clique_merge` from the checkout root. This validates a synthetic fixture, not production source completeness; runtime is not guaranteed here.
- If infrastructure or downloads are unavailable, return a readiness report naming the missing prerequisites and verified next command. Mark aggregation as unexecuted; do not claim a successful build or launch a full HPC job merely to satisfy the 15-minute target.

## Inputs / Outputs

**Inputs:** A biomedical question or ingestion objective; identifiers and organism context; intended deployment and graph; source/configuration selection; optional repository revision, local checkout, compute allocation, and result bounds.

**Outputs:** A provenance-bearing table or JSON with resolved identifiers and relationships, a reproducible query record, and explicit coverage/truncation notes. Aggregation work additionally yields validated configurations, execution status and logs, and Neo4j/PostgreSQL artefact locations when built; preparation-only work yields a readiness report with unresolved prerequisites.

**Completion check:** For query mode, confirm the request succeeded, the response matches its schema, identifiers resolve or are explicitly reported unresolved, and pagination and provenance gaps are disclosed. For readiness mode, confirm the selected sources, interfaces, launcher, and resource constraints were checked and clearly state that no aggregation results were produced.

## References

- [GrEBI repository and source finding](https://github.com/EBISPOT/GrEBI).
- [README: pipeline overview, development endpoint, and local tests](https://github.com/EBISPOT/GrEBI/blob/dev/README.md).
- [Deployment guide: data model, normalisation, ingestion, and database roles](https://github.com/EBISPOT/GrEBI/blob/dev/docs/deploying.md).
- [MCP guide: transport, discovery, tools, and response limits](https://github.com/EBISPOT/GrEBI/blob/dev/docs/mcp.md).
- [API reference: OpenAPI discovery](https://github.com/EBISPOT/GrEBI/blob/dev/docs/api.md).
- [Datasource configurations](https://github.com/EBISPOT/GrEBI/tree/dev/configs/datasource_configs) and [subgraph configurations](https://github.com/EBISPOT/GrEBI/tree/dev/configs/subgraph_configs).
