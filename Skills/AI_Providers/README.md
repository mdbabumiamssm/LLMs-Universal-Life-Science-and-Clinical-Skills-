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

# AI Providers (2026)

This category curates provider-specific operational skills for the LLM stacks we actually care about in production.
Use these skills when model selection, SDK behavior, deprecations, tool use, or cloud/provider-specific limits matter.

## Core Skills

- `OpenAI_Platform_Operations_2026/` - Responses API, models, tools, migration, and platform operations.
- `Anthropic_Claude_Operations_2026/` - Claude API operations, deprecations, tool use, and rollout decisions.
- `Google_Gemini_Operations_2026/` - Gemini model and GenAI SDK operations.
- `Cohere_Platform_Operations_2026/` - Cohere models, SDKs, rerank/embedding/transcribe surfaces, and release-aware operations.
- `Cloud_AI_Operations_AWS_Azure_2026/` - cross-cloud deployment tradeoffs across Bedrock and Azure AI/Azure OpenAI.
- `AWS_Bedrock_Operations_2026/` - Bedrock model routing, Converse API, Guardrails, Agents, and AgentCore.
- `Azure_AI_Foundry_Operations_2026/` - Azure AI Foundry / Microsoft Foundry deployments, identity, safety, and agent service operations.
- `Frontier_OSS_Models_2026/` - open/openly-available model ecosystems and deployment tradeoffs.
- `AI_Provider_GitHub_Maintainers_2026/` - maintenance health for provider-owned repos.

## Additional Dedicated Coverage

- `Mistral_Platform_Operations_2026/`
- `DeepSeek_API_Operations_2026/`
- `XAI_Grok_Operations_2026/`

## What Belongs Here

- Model and endpoint selection tied to one provider.
- SDK migration or deprecation planning.
- Provider-native tools, files, agents, conversations, connectors, or rate-limit behavior.
- Security, retries, timeouts, and rollout rules that differ by vendor.

## What Does Not Belong Here

- Generic multi-agent orchestration guidance - keep that in `Skills/Agentic_AI/`.
- Protocol-level MCP guidance - keep that in `Skills/MCP_Servers/`.
- Raw third-party repo mirrors - keep those under `External_Collections/` until curated.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
