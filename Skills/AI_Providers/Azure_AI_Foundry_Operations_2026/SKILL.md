---
name: azure-ai-foundry-operations-2026
description: Implement and operate Azure AI Foundry and Microsoft Foundry workloads with explicit identity, deployment, model versioning, safety, and agent-service controls. Use when deploying model endpoints, migrating model versions, or setting up production guardrails on Azure.
keywords:
  - azure
  - ai-foundry
  - microsoft-foundry
  - agent-service
  - content-safety
measurable_outcome: Produce a working Azure AI Foundry operating plan with service scope, identity model, deployment strategy, and failover criteria documented within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.04"
source_reliability:
  - source: official_microsoft_docs
    score: 1.0
    rationale: Guidance is grounded in Azure AI Foundry and Microsoft Foundry documentation checked on 2026-04-20.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Azure AI Foundry Operations (2026)

Use this skill when Azure AI Foundry or Microsoft Foundry is the operating surface, not just a generic OpenAI-compatible endpoint.

## Workflow

1. Confirm the service surface first: Azure AI Foundry resource, Azure OpenAI deployment, or Foundry Agent Service.
2. Pin the identity model explicitly: Entra ID, managed identity, or service principal.
3. Pin API versions, deployment names, and region strategy before coding.
4. Enable safety, telemetry, and evaluation controls before broader rollout.
5. Validate region availability, disaster recovery, and data-handling assumptions in staging.

## Guardrails

- Track the Azure AI Foundry to Microsoft Foundry naming transition and document which portal and API surface the team actually uses.
- Keep deployment names and model versions explicit; do not rely on implicit defaults.
- Treat content safety, agent evaluators, and Foundry Agent Service as separate control planes.
- Record identity method, data residency assumptions, and failover region in validation notes.

## Output Requirements

- State the Azure service surface and model deployment strategy.
- State the identity/auth method and secret-handling policy.
- State one safety or evaluation control and one regional failover mechanism.
