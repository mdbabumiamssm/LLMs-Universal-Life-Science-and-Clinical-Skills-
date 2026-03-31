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

---
name: langgraph-self-hosted
description: Deploy LangGraph Platform-compatible backends (Aegra) to run regulated biomedical agent workflows on private infrastructure with security guardrails.
keywords:
  - langgraph
  - self-hosted
  - agentic-ai
  - fastapi
  - postgres
measurable_outcome: Stand up a LangGraph-compatible deployment (API + persistence) behind your firewall, register at least one graph, and route traffic through it within 4 hours.
license: Apache-2.0 (Aegra)
metadata:
  author: Agentic Architecture Guild
  version: "2026.03"
compatibility:
  - system: Docker / Kubernetes
  - system: PostgreSQL 14+
allowed-tools:
  - docker
  - run_shell_command
  - web_fetch
---

# LangGraph Self-Hosted Skill

LangGraph Platform launched managed hosting, but biomedical programs often need on-prem control, data residency, and custom auth. Use this skill to deploy Aegra—a drop-in, open-source implementation of LangGraph Deployments that speaks the same SDK and Agent Protocol APIs.

## Architecture Overview
- **API layer:** FastAPI app that implements LangGraph Deployments endpoints (graph registry, runs, state streaming).
- **State store:** PostgreSQL for graph metadata, run state, audit logs.
- **Execution nodes:** Containerized workers (Kubernetes or Docker Compose) running LangGraph clients to execute graphs.
- **Observability:** Prometheus/Grafana optional; integrate with LangSmith or OpenTelemetry exporters.

## Quickstart (Docker Compose)
```bash
git clone https://github.com/ibbybuilds/aegra.git
cd aegra
cp .env.example .env
# set DATABASE_URL, SECRET_KEY, and upstream LangGraph credentials
make compose-up
```
- API served on `http://localhost:8000`.
- PostgreSQL seeded with migrations via Alembic.
- LangGraph SDK points to `Aegra_BASE_URL` in your `.env`.

## Registering a Graph
```bash
langgraph up \
  --url http://localhost:8000 \
  --api-key $AEGRA_API_KEY \
  --graph app.graph:graph
```
- Graph definitions remain unchanged—same YAML/graph builder code as hosted LangGraph.
- Use the LangGraph Python client or REST API to create deployments, schedule runs, and stream events.

## Hardening Steps
1. **Rotate secrets** – set `SECRET_KEY`, `AEGRA_SERVICE_TOKEN`, and database credentials via a vault service.
2. **Network segmentation** – run API behind an internal ingress with mTLS; expose only necessary webhook endpoints.
3. **Patch dependencies** – LangChain/LangGraph recently shipped fixes for remote-code-execution bugs triggered via untrusted tool definitions; pin patched versions (`langchain>=0.3.12`, `langgraph>=0.1.22`) and redeploy promptly. (Ref. 3)
4. **Audit logging** – enable PostgreSQL logical decoding or ship logs to SIEM for FDA/21 CFR Part 11 traceability.
5. **Availability** – run two API replicas + managed Postgres (Aurora, AlloyDB) with PITR.

## Integration Tips
- **Agent Protocol** – Aegra implements the Agent Protocol so you can connect client SDKs or third-party orchestrators without glue code (Ref. 2).
- **LangGraph Platform (managed)** – If you later migrate to LangGraph’s hosted platform, the SDK endpoints remain the same (Ref. 1). Keep staging + prod environments consistent by storing graph configs in Git.
- **Cost control** – Autoscale worker deployments and leverage spot instances for non-critical experiments.

## References
1. LangChain, *LangGraph Platform* overview (stateful agent orchestration + deployments). https://www.langchain.com/platform/langgraph
2. Toolerific, *Aegra – self-hosted LangGraph platform alternative* (FastAPI + PostgreSQL implementation, Apache license). https://toolerific.ai/ai-tools/opensource/ibbybuilds-aegra
3. TechRadar Pro, *LangChain fixes serious vulnerabilities giving attackers ability to run malicious code* (February 2026). https://www.techradar.com/pro/security/langchain-fixes-serious-vulnerabilities-that-gave-hackers-the-ability-to-run-malicious-code

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
