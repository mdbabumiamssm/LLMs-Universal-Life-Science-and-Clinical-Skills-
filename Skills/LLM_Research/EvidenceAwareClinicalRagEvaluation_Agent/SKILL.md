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
name: 'evidence-aware-clinical-rag-evaluation'
description: 'Evaluate clinical RAG retrieval using evidence-span relevance, overlap-aware chunk mapping, controlled retriever comparisons, and annotation-coverage audits while assessing answer quality separately.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Evidence-Aware Clinical RAG Evaluation

## Overview

Evaluate clinical literature retrieval by mapping accepted evidence spans to every containing chunk and measuring how annotation coverage affects retrieval scores. Compare chunking, hybrid retrieval, and reranking under controlled conditions, then assess generated answers separately. This workflow is grounded in a breast-lesion management development study with 18 documents and 18 queries; its results do not establish clinical validity or evidence sufficiency.

## When to Use This Skill

- Compare dense, BM25, hybrid, or cross-encoder-reranked retrieval over clinical literature.
- Audit apparently irrelevant results that may contain unannotated supporting evidence.
- Evaluate chunk size and overlap without penalizing equivalent evidence in overlapping chunks.
- Explain score changes after relevance annotations expand while retrieval rankings remain fixed.
- Separate evidence retrieval, answer faithfulness, and clinical correctness in a RAG evaluation report.

## Core Capabilities

1. **Freeze the evaluation contract.** Record corpus and query versions, document hashes, extraction method, tokenizer, index configuration, retrieval depth, cutoffs, and relevance version. Specify whether queries are Yes/No or WH-questions and identify development versus held-out queries. For a bounded 15-minute run, use available rankings and annotations or a small declared comparison; label incomplete experiments rather than inventing results.

2. **Represent relevance as evidence spans.** Store each annotation as `query_id`, `document_id`, `span_id`, `start`, `end`, `evidence_text`, and `annotation_version`, with an acceptance rationale. Use half-open character offsets into a frozen extracted document and verify that the text slice matches the annotated evidence. Review whether the span preserves necessary qualifications, population, and management context; a topical mention alone is not sufficient evidence.

3. **Map evidence to all containing chunks.** Store each chunk's document ID, unique chunk ID, source offsets, token count, and configuration ID. Mark a chunk relevant when its source interval fully contains an accepted span in the same document: `chunk.start <= span.start` and `span.end <= chunk.end`. Include every overlapping chunk that contains that evidence, deduplicate chunk IDs in the relevance set, and retain span-to-chunk provenance. Flag spans split across boundaries or unmappable after extraction changes; do not silently count partial containment or alter the evidence solely to improve scores. Remap annotations independently for each chunking configuration.

4. **Compare retrieval configurations under controlled conditions.** Keep corpus, queries, annotation version, candidate depth, fusion policy, and reranker settings fixed except for the factor being tested. Record exact embedding, lexical retrieval, fusion, and reranker implementations and versions. The source explored chunk sizes from 128 to 1024 tokens, overlaps from 0 to 20%, and four retriever configurations; these are study settings, not universal defaults. Its selected hybrid configuration used 384-token chunks with 20% overlap. Do not infer unspecified configuration details from the supplied summary.

5. **Compute explicit retrieval metrics.** For each query, let `G` be the unique relevant chunk IDs for its configuration, `R = |G|`, and `L` be the ranked unique retrieved chunk IDs. Use binary relevance and disclose these conventions:

   - `Recall@K = |G intersect L[:K]| / R`.
   - `R-Precision = |G intersect L[:R]| / R`; retrieve at least `R` ranks or mark the result unavailable when the saved ranking is truncated.
   - Reciprocal rank at `K` is `1 / first_relevant_rank` when a relevant chunk appears by `K`, otherwise zero. `MRR@K` is its mean across eligible queries.
   - `DCG@K = sum(rel_i / log2(i + 1))` for ranks `i = 1..K`; divide by the ideal DCG containing `min(R, K)` relevant items to obtain `nDCG@K`.
   - When `R = 0`, report an annotation gap and undefined relevance-dependent metrics; exclude the query from macro averages and disclose the exclusion count. Do not convert missing ground truth into a retrieval failure or success.
   - Treat absent results as nonrelevant only when the run genuinely returned fewer results, not when the ranking export was truncated. Report per-query values, macro averages, cutoffs, and eligible denominators.

   These are chunk-level metrics: retrieving one evidence span can leave Recall@K below one when several chunks contain that span. Optionally report distinct evidence-span coverage as a separately named diagnostic, with its own denominator; do not substitute it for chunk recall.

6. **Audit annotation sensitivity with frozen rankings.** Save baseline annotations before inspecting retrieved results. Review potentially missing evidence, record accepted additions and rationale, and distinguish retrieval-informed curation from independent annotation. Recompute metrics against baseline and expanded relevance sets using exactly the same ranked IDs and configurations. Report span counts, relevant chunk counts, unmapped spans, changed judgments, and per-query score deltas. Expanded relevance can raise or lower individual metrics because their denominators and ideal rankings change; it does not itself prove a better retriever. Reserve independent queries and expert review for validation after development selection.

7. **Assess generation independently.** If answers are available, record the generation index, retrieved context, `K`, prompt, generator, judge, and evaluator versions. Evaluate claim support against supplied context separately from correctness against accepted evidence; surface unsupported claims, contradictions, omissions, and clinically important qualifiers. The source evaluated generation on a separate 512-token index at `K = 1..5`, using DeepEval claim-level metrics with `deepseek-v4-pro` as judge, plus BLEU/ROUGE. Treat these as reported settings, not required tools, and do not merge that experiment with the 384-token retrieval results. Lexical overlap and LLM-judge scores do not establish clinical correctness; radiologist review of evidence sufficiency remains necessary for clinical validation.

8. **Produce a traceable, bounded conclusion.** Separate observed run results from source-study findings. The supplied study summary reports accepted evidence in the top three results for 17 of 18 queries and reports Recall@3, R-Precision, MRR@3, and nDCG@3 of 0.94. It also reports growth from 25 to 37 evidence spans and 36 to 51 accepted chunk targets without changing retrieval rankings. Do not treat these as expected performance, deployment thresholds, or independently reproduced results. Explain the small development benchmark, one-question-per-document construction, selection effects, and retrieval-informed curation; state that independent validation and radiologist assessment remain outstanding.

## Inputs / Outputs

**Required inputs**

- Frozen corpus text with document IDs and stable source offsets.
- Query IDs, question text, and development or held-out designation.
- Versioned accepted evidence spans with source provenance and acceptance rationale.
- Chunk manifests and saved rankings, or access to a configured retriever to generate them.
- Requested cutoffs and configurations to compare.

**Optional inputs**

- Baseline and expanded annotation versions for a sensitivity comparison.
- Generated answers, contexts, reference answers, and evaluator settings.
- Independent expert assessments of evidence sufficiency and answer correctness.

**Expected outputs**

- An evaluation manifest identifying corpus, annotation, chunking, and retrieval versions.
- An evidence-to-chunk relevance map with unmapped and boundary-split spans flagged.
- A per-query metric table and aggregate table with cutoffs, denominators, and exclusions.
- A fixed-ranking annotation audit showing accepted changes and metric deltas, when two annotation versions exist.
- A separate generation assessment when answer artifacts are supplied.
- A concise limitations statement and list of unresolved evidence or validation gaps.

**Completion check:** Every scored relevant chunk traces to an accepted span; all configurations use their own remapped relevance sets; every metric has a declared cutoff and denominator; annotation-only comparisons preserve rankings; and the report distinguishes retrieval success from clinical validation. If required inputs are missing, return a specific gap report and mark evaluation incomplete without fabricating annotations, rankings, or scores.

## References

- [How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions](http://arxiv.org/abs/2610.31606v1), arXiv:2610.31606v1, published October 22, 2026. Study details above derive from the supplied finding summary; unspecified implementation details require checking the full paper before claiming replication.
