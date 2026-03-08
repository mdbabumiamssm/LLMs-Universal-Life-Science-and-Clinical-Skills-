---
name: biomedical-rag-citation-pipelines
description: Design citation-grounded biomedical retrieval and generation systems for literature-heavy assistants. Use when building or improving PubMed or PMC search pipelines, hybrid retrieval, claim-to-citation validation, evidence-aware answer synthesis, or evaluation workflows for biomedical RAG applications.
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
