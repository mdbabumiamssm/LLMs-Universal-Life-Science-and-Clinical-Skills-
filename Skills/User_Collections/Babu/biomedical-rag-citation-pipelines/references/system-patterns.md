# System Patterns

## Recommended stages

1. Query understanding and synonym expansion.
2. Retrieval from trusted biomedical sources.
3. Lightweight reranking.
4. Passage assembly with identifiers preserved.
5. Answer generation with structured citations.
6. Citation existence and relevance checks.
7. Offline evaluation with failure review.

## Good evidence units

- Abstract paragraph with PMID.
- Full-text section with PMCID and section title.
- Trial inclusion criteria block with NCT ID.
- Internal SOP paragraph with document version.

## Common failure modes

- Gene alias mismatch.
- Retriever finds the right paper but wrong passage.
- Model cites a source not present in context.
- Review article cited for a primary-result claim.
- Over-compressed chunks lose the statement needed for verification.
