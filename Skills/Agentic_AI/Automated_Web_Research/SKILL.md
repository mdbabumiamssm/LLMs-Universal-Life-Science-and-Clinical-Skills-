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
name: automated-web-research
description: Run evidence-first web research with multi-query search, page fetch, source vetting, and cited synthesis. Use when the answer depends on recent information, official documentation, or current external services.
keywords:
  - research
  - web
  - citations
  - verification
  - official-docs
measurable_outcome: Produce a cited brief grounded in at least 5 sources, with source-quality notes and unresolved gaps called out, within 20 minutes.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow is grounded in official provider docs and protocol docs checked on 2026-04-13.
  - source: official_repositories
    score: 0.95
    rationale: Supporting implementation references come from maintainer-owned repositories or official registries.
allowed-tools:
  - google_web_search
  - web_fetch
  - read_file
  - run_shell_command
---

# Automated Web Research

Use this skill when the user needs current facts, current product or provider behavior, or a recent-document synthesis that cannot be answered safely from model memory alone.

## Workflow

1. Rewrite the task into 3 to 6 targeted search queries instead of one vague search.
2. Bias the search toward official docs, primary sources, standards bodies, and maintainer-owned repositories before using secondary summaries.
3. Fetch and read the top sources, then cross-check the answer across multiple sources before drafting conclusions.
4. Separate what is directly supported by sources from what is your inference.
5. Explicitly flag stale, missing, conflicting, or low-trust evidence.

## Guardrails

- Prefer official docs and vendor-owned GitHub repos over blogs or aggregators.
- Do not present a single-source claim as settled if independent confirmation is missing.
- If the topic is safety-critical, regulatory, financial, or medical, require stronger source quality and higher agreement.
- If a page is clearly outdated, treat it as historical context rather than current truth.

## Output Requirements

- Include source links.
- Label the most authoritative source used.
- Call out unresolved uncertainty in one short section.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
