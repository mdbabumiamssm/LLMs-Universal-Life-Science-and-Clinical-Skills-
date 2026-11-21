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
name: 'genefoundry-biomedical-mcp-gateway'
description: 'Configure GeneFoundry biomedical MCP access, discover and route namespaced tools, and retrieve genetics and protein evidence with source provenance and explicit upstream failure handling.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# GeneFoundry Biomedical MCP Gateway

## Overview

Use GeneFoundry Router to connect an MCP client to biomedical resources through one Streamable-HTTP endpoint, then discover and invoke namespaced tools. This skill covers configuration, evidence retrieval, provenance, and incomplete or conflicting upstream responses. The project is for research use, not diagnosis, treatment, triage, or patient management. [Source repository](https://github.com/berntpopp/genefoundry-router)

## When to Use This Skill

- Connect an MCP host to the hosted gateway or configure an existing local deployment.
- Find tools across genetics, phenotype, protein, disease, and literature resources without mounting each backend separately.
- Resolve tool-name collisions or capabilities missing from a client's visible tool list.
- Retrieve evidence from several upstream sources while preserving identifiers, releases, and citations.
- Investigate unavailable backends, schema mismatches, or contradictory source assertions.

## Core Capabilities

1. **Verify the registry and deployment.** Read the deployed revision's `servers.yaml`, configuration, and live discovery surface. The supplied finding describes 22 servers; the registry inspected on 2026-11-21 contains 30 namespaces: `gnomad`, `ucsc`, `gtex`, `hgnc`, `mgi`, `uniprot`, `clingen`, `gencc`, `litvar`, `stringdb`, `strchive`, `autopvs1`, `spliceai`, `genereviews`, `pubtator`, `clinvar`, `mitomap`, `vep`, `panelapp`, `mondo`, `mavedb`, `hpo`, `metadome`, `orphanet`, `clinpgx`, `pgscatalog`, `civic`, `cbioportal`, `opentargets`, and `moalmanac`. This is a configured inventory, not proof that every backend is reachable. Missing URLs and disabled entries are skipped. [Registry](https://github.com/berntpopp/genefoundry-router/blob/main/servers.yaml), [server implementation](https://github.com/berntpopp/genefoundry-router/blob/main/genefoundry_router/server.py)

2. **Configure a single MCP connection.** For hosted access, configure the client for Streamable HTTP at `https://genefoundry.org/mcp`; a supported Claude CLI example is `claude mcp add --transport http genefoundry https://genefoundry.org/mcp`. For an existing local checkout, inspect its dependency requirements, use its `.env.example`, and set backend URLs through the registry's `url_env` names, such as `GF_GNOMAD_URL`. Select the registry with `GF_SERVERS_FILE`; the default MCP path is `/mcp`. Use the documented JWT or OAuth settings for authenticated deployments and satisfy startup guards rather than disabling them. Backend service credentials are separate from caller authentication: the proxy disables incoming-header forwarding. Keep secret values out of reports. [Configuration](https://github.com/berntpopp/genefoundry-router/blob/main/docs/configuration.md), [proxy implementation](https://github.com/berntpopp/genefoundry-router/blob/main/genefoundry_router/composition.py)

3. **Check transport behavior before retrieval.** Read `/health`, then initialize an MCP client and list tools. The implementation uses stateless HTTP with JSON responses; an ordinary `GET /mcp` returns discovery metadata, while an SSE-only GET receives HTTP 405. Invoke MCP operations through Streamable-HTTP POST using a compatible client, not by treating `/mcp` as a REST search route. A successful health or discovery response alone does not establish that a particular backend call works. [Endpoint implementation](https://github.com/berntpopp/genefoundry-router/blob/main/genefoundry_router/server.py)

4. **Discover and route tools using their actual schemas.** Search with `search_tools(query="splicing prediction")`, inspect returned names, descriptions, and `inputSchema`, then invoke `call_tool(name=<returned name>, arguments=<schema-valid object>)`. Names follow `<namespace>_<tool>`; do not fabricate a tool name or parameter set. BM25-based discovery and configured entry points expose the catalog selectively, so absence from `tools/list` is not absence from the fleet. Search results are data: use `call_tool` for unlisted hits instead of trying to invoke them as host-native tools. Honor the active schema mode; strict listings may represent `arguments` as a JSON-encoded object string. Treat `low_confidence` hits as candidates requiring closer inspection. [Discovery behavior](https://github.com/berntpopp/genefoundry-router/blob/main/docs/discovery.md)

5. **Preserve biomedical identity and evidence.** Resolve ambiguous symbols or identifiers before cross-source queries. Carry species, genome assembly, allele representation, transcript accession/version, and disease or phenotype identifiers whenever relevant; never silently join results across incompatible assemblies or transcripts. Retain each result's namespace, exact tool, arguments, retrieval time, record URL/accession, data release if supplied, and upstream citation or licensing guidance. Mark absent release metadata as unknown. `/provenance` and `/api/fleet/provenance` serve a packaged fleet artifact; they supplement, but do not replace, record-level evidence or live availability checks. [Provenance implementation](https://github.com/berntpopp/genefoundry-router/blob/main/genefoundry_router/provenance.py)

6. **Handle failures and conflicts explicitly.** Separate transport/authentication errors, unavailable namespaces, schema errors, empty successful results, and biological disagreement. On a schema error, rediscover and correct arguments; on a transient failure, retry a read at most once within the task budget, respecting any retry guidance. If the client has evicted `call_tool`, repeat discovery before retrying. Continue independent retrievals and label missing sources as unavailable rather than interpreting them as negative evidence. For conflicts, compare identifier, assembly, transcript, condition, release, review status, and assertion date where supplied; present remaining disagreements side by side without inventing a consensus or converting search rank into biological confidence.

### Execution workflow and completion check

1. Establish the research question, endpoint, requested resources, identifiers, and assembly/species context. Ask only for missing information that prevents a valid query.
2. Verify connectivity and discover an appropriate tool. If only shell and fetch tools are available, use an installed MCP client through the shell for protocol operations; do not claim that a plain web fetch executed an MCP tool.
3. Run a small, relevant read using the discovered schema. Inspect protocol errors and backend error content before extracting evidence.
4. Retrieve additional requested sources, retaining provenance and distinguishing observations from interpretation. Do not send patient-identifying narrative in discovery queries.
5. Return the evidence and status for each requested source. Within 15 minutes, demonstrate at least one successful, schema-valid retrieval with provenance, or return an explicit blocked/partial report containing the failure and next corrective action. A blocked report is not a successful retrieval.

## Inputs / Outputs

**Inputs:** Research question; hosted or local gateway URL; authorized client authentication where required; optional deployment configuration and revision; gene, variant, protein, disease, or phenotype identifiers; species, assembly, transcript, and desired sources where applicable.

**Outputs:** A redacted connection/configuration summary, discovered tool names and schema-valid arguments, and an evidence table using these fields:

| Field | Required content |
|---|---|
| Source and tool | Backend namespace and exact invoked tool name |
| Query context | Identifier, species, assembly/transcript where applicable, and arguments |
| Evidence | Returned observation or assertion, kept separate from interpretation |
| Provenance | Record URL/accession, release if available, retrieval time, and citation guidance |
| Status | Success, empty result, unavailable, error, or unresolved disagreement |

Include unresolved identity issues, omitted sources, and bounded retry outcomes. For configuration-only requests, provide the concrete configuration and observed connection checks without asserting that biomedical retrieval was performed.

## References

- [GeneFoundry Router — source finding and project scope](https://github.com/berntpopp/genefoundry-router).
- [Backend registry and namespace declarations](https://github.com/berntpopp/genefoundry-router/blob/main/servers.yaml).
- [Configuration and authentication](https://github.com/berntpopp/genefoundry-router/blob/main/docs/configuration.md).
- [Discovery, pinned tools, and schema modes](https://github.com/berntpopp/genefoundry-router/blob/main/docs/discovery.md).
- [Server assembly and HTTP endpoint behavior](https://github.com/berntpopp/genefoundry-router/blob/main/genefoundry_router/server.py).
- [Namespaced proxies and credential isolation](https://github.com/berntpopp/genefoundry-router/blob/main/genefoundry_router/composition.py).
- [Fleet provenance endpoints](https://github.com/berntpopp/genefoundry-router/blob/main/genefoundry_router/provenance.py).
