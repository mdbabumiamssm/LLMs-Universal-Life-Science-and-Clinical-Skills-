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
name: 'biocontext-ai-mcp-registry'
description: 'Use the BioContextAI Registry to discover, compare, and select biomedical MCP servers for bioinformatics, systems biology, and biomedical AI workflows.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# BioContextAI MCP Registry

## Overview

This skill guides agents through using the BioContextAI Registry, a curated GitHub registry for biomedical Model Context Protocol (MCP) servers. Use it to discover relevant biomedical data and tool servers, compare registry entries, and choose MCP integrations that fit a specific bioinformatics, systems biology, or biomedical AI task.

The workflow emphasizes source-grounded selection, basic trust checks, and concise recommendations so agents can avoid ad hoc server discovery when a registry-driven option is available.

## When to Use This Skill

- A user asks for biomedical MCP server discovery, registry lookup, or MCP server comparison.
- A workflow needs candidate MCP servers for bioinformatics, systems biology, biomedical AI, or related scientific data access.
- You need to evaluate whether a biomedical MCP server is appropriate for a task before connecting or recommending it.
- You are building or documenting an agent workflow that should cite registry-backed MCP server options.
- Existing individual biomedical skills do not identify which MCP server should be selected first.

## Core Capabilities

1. Registry-driven discovery: Search the BioContextAI Registry for MCP servers relevant to the user's biomedical domain, data type, organism, method, or task.

2. Candidate triage: Compare candidate servers by stated purpose, covered resources, implementation language, repository health signals, documentation, and maintenance recency when available.

3. Trust and suitability checks: Prefer servers with clear source repositories, documented capabilities, transparent configuration, and alignment with the user's data sensitivity and workflow requirements.

4. Integration planning: Summarize installation, connection, environment variable, and authentication requirements from the server documentation before recommending use.

5. Output synthesis: Produce a short ranked recommendation with the selected server or servers, why each fits, key limitations, and links needed for follow-up.

## Inputs / Outputs

**Inputs**

- User goal, biomedical domain, data source, organism, assay, or analysis task.
- Any constraints on MCP client, runtime environment, credentials, network access, or local-only execution.
- Registry URL or repository contents when already provided in context.

**Outputs**

- Ranked MCP server candidates from the BioContextAI Registry.
- A brief rationale for each recommended candidate, grounded in registry or repository evidence.
- Setup notes, authentication requirements, and operational cautions when documented.
- Reference links to the registry entry, source repository, and closely related MCP documentation when useful.

## References

- BioContextAI Registry GitHub repository: https://github.com/biocontext-ai/registry
- Model Context Protocol documentation: https://modelcontextprotocol.io/
