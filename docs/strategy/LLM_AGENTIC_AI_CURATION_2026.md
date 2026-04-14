# LLM and Agentic AI Curation Strategy (April 2026)

This document is the repository's operating guide for keeping the LLM and agentic AI surface current without turning the repo into a pile of stale links and cloned hype.

## What Changed In This Refresh

- Added curated first-party skills for `OpenAI_Codex_Agents`, `Google_ADK_Agents`, `PydanticAI_Agents`, `Agentic_Evals_Observability`, `MCP_Operations_2026`, `Mistral_Platform_Operations_2026`, `DeepSeek_API_Operations_2026`, and `XAI_Grok_Operations_2026`.
- Rewrote `Automated_Web_Research` and `DeepResearch_Swarm` to emphasize source quality, verification, and explicit evidence gaps.
- Added category-level READMEs for `AI_Providers` and `MCP_Servers`, and replaced the stale `Agentic_AI/README.md` with an accurate index.
- Standardized new and upgraded skills around lean `SKILL.md`, `references/sources.md`, `agents/openai.yaml`, and reliability metadata.

## Tier 1 Canonical Sources

Use these first. If a new skill cannot be grounded in these kinds of sources, it is usually not ready for first-party curation.

### Provider docs and SDKs

- OpenAI Developers + API docs: <https://developers.openai.com/>
- OpenAI Agents SDK: <https://openai.github.io/openai-agents-python/>
- Anthropic Claude docs: <https://platform.claude.com/docs/>
- Google ADK docs: <https://adk.dev/>
- PydanticAI docs: <https://pydantic.dev/docs/ai/overview/>
- Mistral docs: <https://docs.mistral.ai/>
- DeepSeek API docs: <https://api-docs.deepseek.com/>
- xAI docs: <https://docs.x.ai/>

### Maintainer-owned repositories

- OpenAI Agents SDK: <https://github.com/openai/openai-agents-python>
- OpenAI skills catalog: <https://github.com/openai/skills>
- Google ADK Python: <https://github.com/google/adk-python>
- PydanticAI: <https://github.com/pydantic/pydantic-ai>
- Mistral AI org: <https://github.com/mistralai>
- xAI Python SDK: <https://github.com/xai-org/xai-sdk-python>

### Protocol and interoperability sources

- MCP intro/spec/SDK/registry: <https://modelcontextprotocol.io/>
- OpenAI MCP/connectors guide: <https://developers.openai.com/api/docs/guides/tools-connectors-mcp>
- Anthropic MCP connector docs: <https://platform.claude.com/docs/en/agents-and-tools/mcp-connector>

### Evals and observability sources

- LangSmith docs: <https://docs.langchain.com/langsmith/reference-overview>
- Braintrust eval docs: <https://www.braintrust.dev/docs/evaluation>
- Phoenix docs: <https://arize.com/docs/phoenix>
- OpenTelemetry GenAI semantic conventions: <https://github.com/open-telemetry/semantic-conventions/tree/main/docs/gen-ai>

## What We Should Curate First

Prioritize skills that are both high-value and repeatedly needed:

1. Provider operations for vendors we actively use or benchmark.
2. Agent frameworks with clear adoption and official docs (OpenAI Agents SDK, ADK, PydanticAI).
3. Protocol infrastructure (MCP, remote tools, auth, approval, registry, security).
4. Evals, tracing, rollback, and quality discipline.
5. Coding-agent operations that directly improve software delivery velocity.

## What We Should Not Do

- Do not bulk-clone random "awesome" repos into first-party categories.
- Do not promote community wrappers to first-party status when official SDKs already exist.
- Do not keep stale placeholder skills with unrealistic outcome claims.
- Do not duplicate the same trigger across multiple folders just because the vendor changed the branding.

## Literature Watchlist

Keep a small set of foundational papers visible so the repo stays conceptually grounded, not just API-driven.

- ReAct: Synergizing Reasoning and Acting in Language Models - <https://arxiv.org/abs/2210.03629>
- Toolformer: Language Models Can Teach Themselves to Use Tools - <https://arxiv.org/abs/2302.04761>
- Self-Refine: Iterative Refinement with Self-Feedback - <https://arxiv.org/abs/2303.17651>
- The Rise and Potential of Large Language Model Based Agents: A Survey - <https://arxiv.org/abs/2309.07864>

## Monthly Refresh Checklist

- Re-check model catalogs, changelogs, and deprecations for OpenAI, Anthropic, Google, Mistral, DeepSeek, and xAI.
- Re-check MCP specification changes, registry updates, and security guidance.
- Audit `Skills/Agentic_AI`, `Skills/AI_Providers`, and `Skills/MCP_Servers` for thin skills without references.
- Promote only the best external material into first-party skills after rewriting it into local standards.
- Rebuild `skills_catalog.json` and `skills_reliability_report.json` after meaningful curation changes.

## High-Priority Next Candidates

These are still good candidates, but were left out of this pass to keep the refresh coherent:

- Claude Code operations
- Cohere platform operations
- Azure AI Foundry dedicated operations
- AWS Bedrock dedicated operations
- Browser/computer-use agent operations
- Security-focused agent red-teaming and guardrail evaluation
