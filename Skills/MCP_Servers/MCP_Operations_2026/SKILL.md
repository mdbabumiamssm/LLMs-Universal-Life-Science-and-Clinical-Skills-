---
name: mcp-operations-2026
description: Implement and operate Model Context Protocol systems safely. Use when designing MCP clients or servers, selecting transports, configuring auth, onboarding remote servers, or enforcing approval and egress controls.
keywords:
  - mcp
  - model-context-protocol
  - remote-servers
  - auth
  - security
measurable_outcome: Produce a working MCP operational plan with transport, auth, approval, and logging rules documented within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.05"
source_reliability:
  - source: official_protocol_docs
    score: 1.0
    rationale: Workflow is grounded in the official MCP docs, authorization specification, SDK docs, and registry pages checked on 2026-05-22.
  - source: official_vendor_integrations
    score: 0.98
    rationale: OpenAI and Anthropic integration guidance is pulled from official vendor documentation.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# MCP Operations (2026)

Use this skill when MCP is part of the architecture, not just a buzzword in the prompt.

## Workflow

1. Decide whether the use case needs local MCP, remote MCP, or both.
2. Choose transport deliberately: stdio for local simplicity, Streamable HTTP for modern remote deployments, SSE only when required for compatibility.
3. For remote MCP, verify OAuth 2.1, protected-resource metadata discovery, authorization-server discovery, scopes, and client registration behavior before connecting users.
4. Define approval, egress, identity propagation, timeout budget, and structured-error policy before connecting any sensitive server.
5. Review tool metadata for prompt-injection or tool-poisoning instructions before exposing it to the model.
6. Prefer official or registry-listed servers over random community clones.
7. Validate the integration with the SDK/inspector path and log every tool import and call.

## Guardrails

- Require explicit approval for sensitive actions by default.
- Restrict outbound access and block private-address abuse where applicable.
- Do not trust redirect targets or OAuth discovery endpoints blindly.
- Keep per-server allowlists for tools, domains, and scopes.
- Do not expose dynamic tool lists without static metadata checks and user-visible tool-call summaries.
- Treat missing identity propagation, unbounded tool retries, and unstructured errors as production blockers.

## Output Requirements

- State the transport and why.
- State the auth and approval policy.
- State the audit or logging path and one concrete security risk.
