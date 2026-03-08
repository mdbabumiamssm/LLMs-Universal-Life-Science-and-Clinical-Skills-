# Biomedical LLM Patterns

## Use LLMs for

- Literature synthesis and claim extraction.
- Structured summarization of analysis outputs.
- Ranking or triage with human review.
- Tool selection and workflow planning.

## Do not rely on LLMs alone for

- Raw statistical computation.
- Variant annotation truth.
- PHI handling without strict controls.
- Citation existence or exact numeric claims.

## Good production pattern

1. Retrieve trusted context.
2. Validate identifiers and citations separately.
3. Ask the model for structured output.
4. Score or check the output.
5. Persist provenance with the final answer.
