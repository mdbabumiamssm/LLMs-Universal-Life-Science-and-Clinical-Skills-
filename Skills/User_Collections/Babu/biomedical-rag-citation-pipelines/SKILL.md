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
name: bio-biomedical-rag-citation-pipelines
description: Design citation-grounded biomedical retrieval and generation systems
  for literature-heavy assistants. Use when building or improving PubMed or PMC search
  pipelines, hybrid retrieval, claim-to-citation validation, evidence-aware answer
  synthesis, or evaluation workflows for biomedical RAG applications.
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# Biomedical RAG Citation Pipelines

Build biomedical RAG systems that can defend their answers with traceable evidence.

## Workflow

1. Define the retrieval target first: abstracts, full text, trial records, internal documents, or mixed corpora.
2. Choose indexing and chunking around the evidence unit you need to cite, not around arbitrary token counts alone.
3. Use hybrid retrieval when terminology drift, gene aliases, diseases, and abbreviations matter.
4. Keep retrieval, reranking, generation, and citation validation as separate stages with inspectable outputs.
5. Require structured answers that bind each claim to a supporting source identifier or passage.
6. Evaluate retrieval quality and citation faithfulness separately; good prose does not imply grounded answers.

## Guardrails

- Do not present uncited synthesis as evidence-backed.
- Track PMID, PMCID, DOI, trial ID, or internal document IDs explicitly.
- Flag review articles versus primary studies.
- Separate source existence checks from claim relevance checks.

## References

- Read `references/system-patterns.md` for pipeline design choices.
- Read `references/evaluation-checklist.md` for retrieval and citation evaluation.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->