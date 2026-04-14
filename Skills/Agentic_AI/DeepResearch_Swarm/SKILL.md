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
name: deep-research-swarm
description: Coordinate a multi-agent research workflow for difficult literature or market-intelligence questions that need parallel search, verification, synthesis, and explicit evidence tracking.
keywords:
  - research
  - literature
  - swarm
  - multi-agent
  - verification
measurable_outcome: Produce a structured research package with search log, verified evidence summary, and open questions within 30 minutes for a focused topic.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
source_reliability:
  - source: official_docs
    score: 1.0
    rationale: Workflow relies on official model, tool, and protocol documentation checked on 2026-04-13.
  - source: primary_literature_and_registries
    score: 0.95
    rationale: Recommended evidence sources include primary databases, standards, and protocol registries rather than blog-only summaries.
allowed-tools:
  - google_web_search
  - web_fetch
  - read_file
  - run_shell_command
---

# DeepResearch Swarm

Use this skill when one agent is not enough: the task needs parallel search, claim checking, evidence consolidation, and a final synthesis that preserves provenance.

## Recommended Agent Roles

- **Searcher** - expands the query set and collects candidate sources.
- **Verifier** - checks dates, source authority, conflicts, and duplicate claims.
- **Synthesizer** - groups findings, writes conclusions, and records open questions.

## Workflow

1. Define a narrow research question, success criteria, and stop condition before searching.
2. Run parallel searches across official docs, primary repositories, and trusted databases.
3. Verify the strongest claims independently before they enter the final synthesis.
4. Group evidence into: supported findings, weak signals, and unresolved gaps.
5. Produce a final brief with citations, assumptions, and next-step recommendations.

## Guardrails

- Do not reward volume over evidence quality.
- Keep a search log so the next agent can reproduce the path taken.
- Distinguish clearly between verified findings and speculative hypotheses.
- Escalate conflicting or low-confidence evidence instead of smoothing it over.

## Output Requirements

- Include a source-backed findings section.
- Include a short conflicts or uncertainty section.
- Include a short next-actions section if the research task is incomplete.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
