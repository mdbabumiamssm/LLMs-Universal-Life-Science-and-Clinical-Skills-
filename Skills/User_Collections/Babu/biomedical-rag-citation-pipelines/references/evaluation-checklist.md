# Evaluation Checklist

## Retrieval

- Recall at k for known-answer questions.
- Whether the top results contain the evidence-bearing passage.
- Coverage of synonyms, biomarkers, and disease aliases.

## Generation

- Each major claim links to a source identifier.
- Numeric values in the answer appear in source text.
- Review versus primary evidence is labeled correctly.
- Unsupported claims are omitted or marked uncertain.

## Reporting

- Keep failure examples.
- Separate retrieval misses from model synthesis failures.
- Record corpus version and indexing date.
