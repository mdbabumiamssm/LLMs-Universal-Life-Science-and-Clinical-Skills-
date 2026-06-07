---
name: aws-bedrock-operations-2026
description: Build and run production workloads on Amazon Bedrock with current model availability, Converse API, agents, guardrails, AgentCore, and IAM controls. Use when implementing Bedrock inference pipelines, managed agents, or provider-agnostic model routing on AWS.
keywords:
  - aws
  - bedrock
  - converse
  - guardrails
  - agents
  - agentcore
measurable_outcome: Produce a working Bedrock operating plan with model choice, IAM posture, invoke path, and rollback criteria documented within 2 hours.
metadata:
  author: MD BABU MIA
  version: "2026.04"
source_reliability:
  - source: official_aws_docs
    score: 1.0
    rationale: Guidance is grounded in Amazon Bedrock user guide and API reference pages checked on 2026-04-20.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# AWS Bedrock Operations (2026)

Use this skill when Bedrock is the production surface, not just a compatibility checkbox.

## Core Capabilities

- For Strands Agents plus Amazon Bedrock AgentCore reference architectures, use the `aws-samples/sample-strands-agent-with-agentcore` pattern as a checklist for TypeScript chatbot boundaries, MCP integrations, browser automation and voice/chatbot tool patterns, A2A interaction paths, identity boundaries, observability, deployment topology, and production security checks.
- Apply the reference architecture to multi-agent chat applications by defining identity boundaries, session-state ownership and lifecycle, MCP and A2A contracts, browser and voice tool controls, end-to-end observability, and production hardening before TypeScript deployment.

## Strands Agents + AgentCore Reference Architecture

- Structure TypeScript chatbot and voice-assistant flows around explicit boundaries for chat or voice client, Strands agent orchestration, Bedrock AgentCore Runtime, and tool adapters; record where request state, memory, and tool results flow.
- Define session-state ownership, persistence, expiration, isolation, and recovery across clients, Strands agents, AgentCore Runtime, memory, and tool adapters.
- Treat MCP, browser automation, voice/chatbot, and A2A integrations as separate tool surfaces with schemas, auth, approval gates, and failure behavior before production enablement.
- Define IAM isolation boundaries for AgentCore runtime, gateway/tool access, memory, browser automation, voice/chatbot integrations, and external service access; split roles or policies when a component can read data, invoke tools, or perform actions.
- Document deployment topology for client/app, agent runtime, tool gateway, Bedrock model access, observability, and infrastructure automation; include rollout and rollback paths.
- Require production guardrails for model/tool allowlists, observability logs/traces, human approval on write-capable tools, prompt/input validation, secrets isolation, and staged rollout.

## Workflow

1. Verify model, region, quota, and service-tier availability in the live Bedrock model catalog before design freeze.
2. Default to `Converse` or `ConverseStream` for cross-model chat workloads; drop to model-specific APIs only when a feature gap forces it.
3. Choose the Bedrock layer deliberately: runtime only, Guardrails, Knowledge Bases, Agents, or AgentCore.
4. Lock IAM, KMS, network, and logging policy before enabling write-capable agents or external tools.
5. Validate latency, cost, guardrail behavior, and fallback behavior in staging before rollout.

## Guardrails

- Require least-privilege IAM roles and explicit model allowlists.
- Treat agent action groups, knowledge bases, and external tool bridges as separate approval surfaces.
- Record `modelId`, region, invocation path, and guardrail config in test evidence.
- Keep cross-region or direct-provider fallback documented before launch.

## Output Requirements

- State the Bedrock model or provider choice and target region.
- State whether the workflow uses Runtime, Converse, Agents, or AgentCore.
- State the IAM/auth pattern and one concrete rollback or failover trigger.

## References

- https://github.com/aws-samples/sample-strands-agent-with-agentcore
