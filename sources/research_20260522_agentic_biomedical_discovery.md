# May 22, 2026 Agentic Biomedical Discovery Research Notes

This note records the source-backed research used for the May 2026 repository curation pass.

## Core findings

- OpenAI's current agent stack has moved from isolated API calls toward reusable skills, AGENTS.md guidance, shell/apply_patch execution, tool search, hosted tools, remote MCP, and Codex app/cloud workflows. Repository skills should therefore describe runtime, tool policy, approval boundaries, and reviewable diffs rather than only model prompts.
- MCP adoption is now operationally important enough that skills must include OAuth/resource-discovery guidance, explicit approval policy, tool metadata review, identity propagation, structured errors, egress control, and audit logging.
- Scientific-discovery agents shifted from demos to peer-reviewed biomedical systems in May 2026: Co-Scientist and Robin were published in Nature, CellVoyager appeared in Nature Methods, and SPARK appeared in Nature Medicine.
- The biomedical-agent repository should avoid one-off hype skills. A single curated `scientific-discovery-agents-2026` skill can route users to the right pattern while requiring claim boundaries, human checkpoints, and validation endpoints.
- Agent evaluation should explicitly test for out-of-scope actions, not only final-answer correctness. This matters for repo-writing agents, notebook agents, MCP tool use, and lab-in-the-loop systems.

## Sources

- OpenAI Codex app: https://openai.com/index/introducing-the-codex-app/
- OpenAI Codex web docs: https://developers.openai.com/codex/cloud
- OpenAI Responses tools: https://developers.openai.com/api/docs/guides/tools
- OpenAI Agents SDK update: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- OpenAI Agents SDK tools: https://openai.github.io/openai-agents-python/tools/
- MCP authorization specification: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- LangGraph v1 release notes: https://docs.langchain.com/oss/javascript/releases/langgraph-v1
- PydanticAI MCP docs: https://pydantic.dev/docs/ai/api/pydantic-ai/mcp/
- Google DeepMind Co-Scientist: https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/
- Co-Scientist Nature paper: https://www.nature.com/articles/s41586-026-10644-y
- Robin Nature paper: https://www.nature.com/articles/s41586-026-10652-y
- FutureHouse Robin repository: https://github.com/Future-House/robin
- Nature Portfolio Co-Scientist/Robin summary: https://www.natureasia.com/en/info/press-releases/detail/9330
- CellVoyager Nature Methods paper: https://www.nature.com/articles/s41592-026-03029-6
- SPARK Nature Medicine paper: https://www.nature.com/articles/s41591-026-04357-y
- Biomni repository: https://github.com/snap-stanford/biomni
- OverEager-Bench paper: https://arxiv.org/abs/2605.18583
- MCP production design paper: https://arxiv.org/abs/2603.13417
- MCP tool-poisoning threat model: https://arxiv.org/abs/2603.22489
