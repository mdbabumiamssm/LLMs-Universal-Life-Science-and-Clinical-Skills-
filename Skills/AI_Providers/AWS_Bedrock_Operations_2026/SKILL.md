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
  author: Biomedical OS Team
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
