# Architecture Patterns

## Choose the simplest viable shape

- Library: when the main value is reusable scientific code.
- CLI: when users need batch execution or workflow chaining.
- API: when analysis must be triggered remotely or integrated with apps.
- Web app: when domain experts need interactive review of outputs.
- Agent workflow: when the task truly benefits from planning, tool routing, and synthesis.

## Minimum delivery standard

- Clear entry point.
- Reproducible environment specification.
- Tests for core domain logic.
- Structured logging or status output.
- Example invocation.

## Failure points to design around

- Missing columns or malformed metadata.
- Large-file memory pressure.
- Provider timeouts and rate limits.
- Hallucinated citations or mismatched identifiers.
- Hidden side effects in notebooks.
