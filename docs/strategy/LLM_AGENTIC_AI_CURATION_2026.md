# LLM and Agentic AI Curation Strategy (April 2026)

This document is the repository's operating guide for keeping the LLM and agentic AI surface current without turning the repo into a pile of stale links, cloned hype, and thin wrappers.

## What Changed In This Refresh

- Added curated first-party skills for `Claude_Code_Operations_2026`, `Computer_Use_Agents_2026`, `Cohere_Platform_Operations_2026`, `AWS_Bedrock_Operations_2026`, and `Azure_AI_Foundry_Operations_2026`.
- Refreshed the OpenAI and Anthropic source maps so the repo reflects current Codex, deep research, computer-use, and Claude Code surfaces rather than older generic API notes.
- Expanded the canonical-source map to include official provider docs, coding-agent repos, cloud managed-agent platforms, and benchmark literature worth monitoring.
- Kept the first-party standard lean: `SKILL.md`, `references/sources.md`, `agents/openai.yaml`, and reliability metadata.

## Tier 1 Canonical Sources

Use these first. If a new skill cannot be grounded in these kinds of sources, it is usually not ready for first-party curation.

### Provider docs and SDKs

- OpenAI Developers + API docs: <https://developers.openai.com/>
- OpenAI model guides and catalog: <https://developers.openai.com/api/docs/models>
- OpenAI Agents SDK docs: <https://openai.github.io/openai-agents-python/>
- Anthropic Claude docs: <https://docs.anthropic.com/>
- Anthropic Claude Code docs: <https://docs.anthropic.com/en/docs/claude-code/overview>
- Cohere docs and models: <https://docs.cohere.com/docs/models>
- Cohere API and SDK reference: <https://docs.cohere.com/v1/reference>
- Cohere changelog: <https://docs.cohere.com/v2/changelog>
- Amazon Bedrock docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/>
- Azure AI Foundry docs: <https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/>
- Google ADK docs: <https://adk.dev/>
- PydanticAI docs: <https://pydantic.dev/docs/ai/overview/>
- Mistral docs: <https://docs.mistral.ai/>
- DeepSeek API docs: <https://api-docs.deepseek.com/>
- xAI docs: <https://docs.x.ai/>

### Maintainer-owned repositories

- OpenAI Agents SDK: <https://github.com/openai/openai-agents-python>
- OpenAI skills catalog: <https://github.com/openai/skills>
- Anthropic Claude Code: <https://github.com/anthropics/claude-code>
- Anthropic Claude Code Action: <https://github.com/anthropics/claude-code-action>
- Cohere Python SDK: <https://github.com/cohere-ai/cohere-python>
- Cohere TypeScript SDK: <https://github.com/cohere-ai/cohere-typescript>
- Google ADK Python: <https://github.com/google/adk-python>
- PydanticAI: <https://github.com/pydantic/pydantic-ai>
- xAI Python SDK: <https://github.com/xai-org/xai-sdk-python>

### Protocol and computer-use sources

- MCP intro, spec, SDKs, and registry: <https://modelcontextprotocol.io/>
- OpenAI MCP and connectors guide: <https://developers.openai.com/api/docs/guides/tools-connectors-mcp>
- OpenAI `computer-use-preview`: <https://developers.openai.com/api/docs/models/computer-use-preview>
- Anthropic computer use tool: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use-tool>
- Anthropic bash tool: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/bash-tool>
- Anthropic text editor tool: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool>
- Anthropic Claude Code MCP guide: <https://docs.anthropic.com/en/docs/claude-code/mcp>

### Cloud managed-agent platforms

- Amazon Bedrock Converse API: <https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html>
- Amazon Bedrock Agents: <https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html>
- Amazon Bedrock Guardrails: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- Amazon Bedrock AgentCore: <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html>
- Azure AI Foundry inference endpoints: <https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/inference>
- Azure AI Foundry deployment overview: <https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/deployments-overview>
- Azure AI Foundry model versions: <https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/concepts/model-versions>
- Microsoft Foundry Agent Service: <https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview>
- Azure AI Content Safety: <https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview>

### Evals, observability, and safety

- LangSmith docs: <https://docs.langchain.com/langsmith/reference-overview>
- Braintrust eval docs: <https://www.braintrust.dev/docs/evaluation>
- Phoenix docs: <https://arize.com/docs/phoenix>
- OpenTelemetry GenAI semantic conventions: <https://github.com/open-telemetry/semantic-conventions/tree/main/docs/gen-ai>
- Azure agent evaluators: <https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators>
- Amazon Bedrock Guardrails: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>

### Ecosystem references worth watching

These are useful ecosystems, but they should only become first-party skills after rewrite and verification.

- Browser Use org: <https://github.com/browser-use>
- Browser Use core repo: <https://github.com/browser-use/browser-use>
- OpenHands: <https://github.com/OpenHands/OpenHands>

## Benchmark and Literature Watchlist

Keep a small set of operationally relevant papers and benchmarks visible so the repo stays grounded in evaluation, not just API churn.

- ReAct: Synergizing Reasoning and Acting in Language Models - <https://arxiv.org/abs/2210.03629>
- Toolformer: Language Models Can Teach Themselves to Use Tools - <https://arxiv.org/abs/2302.04761>
- Self-Refine: Iterative Refinement with Self-Feedback - <https://arxiv.org/abs/2303.17651>
- The Rise and Potential of Large Language Model Based Agents: A Survey - <https://arxiv.org/abs/2309.07864>
- Cognitive Architectures for Language Agents - <https://arxiv.org/abs/2309.02427>
- AgentBench: Evaluating LLMs as Agents - <https://arxiv.org/abs/2308.03688>
- SWE-bench: Can Language Models Resolve Real-World GitHub Issues? - <https://arxiv.org/abs/2310.06770>
- VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks - <https://arxiv.org/abs/2401.13649>
- OSWORLD: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments - <https://arxiv.org/abs/2404.07972>

## What We Should Curate First

Prioritize skills that are both high-value and repeatedly needed:

1. Provider operations for vendors we actively use or benchmark.
2. Coding-agent operations that directly improve software delivery velocity.
3. Computer-use and browser-control agents with explicit safety boundaries.
4. Agent frameworks with clear adoption and official docs (OpenAI Agents SDK, ADK, PydanticAI).
5. Protocol infrastructure (MCP, remote tools, auth, approval, registry, security).
6. Evals, tracing, rollback, and quality discipline.
7. Managed cloud agent platforms (Bedrock, AgentCore, Azure AI Foundry / Microsoft Foundry).

## What We Should Not Do

- Do not bulk-clone random "awesome" repos into first-party categories.
- Do not promote community wrappers to first-party status when official SDKs already exist.
- Do not keep stale placeholder skills with unrealistic outcome claims.
- Do not duplicate the same trigger across multiple folders just because a vendor changed branding.
- Do not treat benchmark papers as implementation guides without matching them to current platform docs.

## Monthly Refresh Checklist

- Re-check model catalogs, changelogs, and deprecations for OpenAI, Anthropic, Cohere, Google, Mistral, DeepSeek, xAI, AWS Bedrock, and Azure AI Foundry.
- Re-check Claude Code install guidance, hooks, MCP integration, and GitHub Action behavior.
- Re-check OpenAI and Anthropic computer-use surfaces, tool versions, and approval/security guidance.
- Re-check Bedrock model cards, Converse API, Guardrails, Agents, and AgentCore updates.
- Re-check Azure AI Foundry / Microsoft Foundry deployment types, Agent Service, safety defaults, and agent evaluators.
- Audit `Skills/Agentic_AI`, `Skills/AI_Providers`, and `Skills/MCP_Servers` for thin skills without references.
- Promote only the best external material into first-party skills after rewriting it into local standards.
- Rebuild `skills_catalog.json` and `skills_reliability_report.json` after meaningful curation changes.

## High-Priority Next Candidates

These are still good candidates, but were left out of this pass to keep the refresh coherent:

- Google Vertex AI dedicated operations
- Anthropic/OpenAI security and guardrail red-teaming operations
- Long-running agent memory and state management
- Browser Use or OpenHands dedicated operational skills, but only after first-party rewrite and evidence-backed scoping
