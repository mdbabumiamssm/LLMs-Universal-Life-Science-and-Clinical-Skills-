<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'fedready-federation-preparation'
description: 'Prepare task-specific federations with bounded agents, local eligibility checks, digest-bound artifact validation, and an auditable handoff to a federated runtime.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# FedReady Federation Preparation

## Overview

Prepare a federation by discovering candidate sites, verifying task eligibility locally, and producing checked contracts, adapters, and task code before federated training or analysis. Following the supplied FedReady finding, agents propose artifacts while the runtime owns workflow state, artifact acceptance, and site admission; raw records and site-private mappings remain outside cross-site messages. This skill supplies a preparation procedure, not a claim that a FedReady package is installed or that preparation establishes clinical validity.

## When to Use This Skill

- Form a federation for a new biomedical training or analysis task.
- Reassess participating sites when an endpoint, population, label definition, or data contract changes.
- Adapt heterogeneous local datasets without pooling source records or private mappings.
- Investigate readiness failures and assemble evidence for a reproducible runtime handoff.

## Core Capabilities

1. **Verify implementation prerequisites.** Read the selected runtime's documentation and installed configuration before proposing commands. The paper documents an NVFlare analysis application and an artifact/message ledger, but this does not establish compatibility with every NVFlare version or another runtime. Record the implementation revision, available validators, artifact schemas, and documented entry points. If these are unavailable, produce a blocked preparation report with missing prerequisites; do not invent a FedReady CLI, installation command, or executable schema.

2. **Define a bounded preparation request.** Specify the task, population, expected outputs, authorized sites, evidence access, and allowed disclosures. Set a deadline and repair budget before execution. Keep server proposals, site-local proposals, and runtime decisions distinct. Use the 15-minute target for a scoped readiness pass and its report; record incomplete checks explicitly rather than claiming full preparation or training succeeded.

3. **Discover candidates conservatively.** Use approved site summaries to find potential task support, prioritizing recall. Mark unresolved applicability as requiring local verification. Discovery is not admission, and absence of detail from a redacted summary is not sufficient evidence to exclude an otherwise plausible site.

4. **Resolve the shared contract.** Draft a versioned task definition covering input/output schema, label or endpoint meaning, population rules, units, splits where relevant, missingness handling, and measurable acceptance criteria. Attach supporting evidence and unresolved questions. Submit the proposal through the runtime's acceptance mechanism before local execution; changes require a new version and rechecking affected artifacts.

5. **Verify eligibility and adapt locally.** Within each authorized site, inspect source documentation and data structure, then propose an adapter and local manifest. Establish semantic task support before admitting the site. Keep ambiguous endpoints unsupported instead of guessing meanings from convenient column names or plausible values. Distinguish ineligible data, insufficient evidence, and implementation failures; a broken adapter does not prove that a site lacks eligible data.

6. **Validate exact artifacts.** Run the implementation's documented checks against the proposed contract, adapter, materialized outputs, and task code. Associate each result with the digest of the bytes actually checked. Use full-data checks where required; sample success alone cannot certify complete preparation. Reject stale attestations after edits. Only runtime-owned verification can authorize acceptance; an agent's success narrative is insufficient.

7. **Repair within scope.** Return actionable failure evidence to the relevant proposal role and retry within the agreed budget. Keep record-level problems separate from site-level decisions. When unresolved semantics require a contract revision, pause affected acceptance and revalidate against the replacement contract. Stop at the deadline or budget limit with explicit pending, failed, or unsupported dispositions.

8. **Freeze and hand off.** Assemble the accepted contract, admitted-site list, artifact digests, local manifest references, verification evidence, and runtime job configuration. Run documented task-code execution checks before declaring readiness. Freeze accepted inputs and end readiness-agent participation before ordinary federated execution. Report preparation readiness separately from deployment authorization and downstream job completion.

## Inputs / Outputs

**Inputs**

- Task specification, inclusion/exclusion rules, endpoint or label semantics, and success criteria.
- Candidate-site inventory and disclosure-approved summaries.
- Site-local source records, dictionaries, mappings, and execution environments accessible only within their authorized scope.
- Runtime identity/version, implementation documentation, artifact schemas, validators, and job interface.
- Time and repair budgets plus any existing contract and acceptance records.

**Outputs**

- A preparation report with task identity, overall status, unresolved prerequisites, and a per-site eligibility disposition with reasons.
- A versioned shared contract and proposals or accepted task code, clearly distinguished by status.
- Site-local adapters, prepared data, private manifests, and validation records; only approved summaries and references cross site boundaries.
- A handoff manifest associating each accepted artifact with its digest, check results, contract version, and admitted sites.
- A record of changes, bounded repair attempts, unsupported endpoints, and pending checks.

Use these output categories as a reporting convention; serialize executable artifacts only according to the verified implementation's schemas. Declare readiness only when all required checks pass for the exact frozen artifacts and admitted sites. If evidence or tooling is missing, a valid report must state that preparation remains blocked or incomplete.

Keeping raw records out of cross-site messages does not establish isolation from a hosted agent provider or a differential-privacy guarantee. Apply the site's authorized evidence-access and disclosure rules to prompts, logs, summaries, and execution as well as FL transport.

## References

- [FedReady: Bounded Agents for Federation Formation, arXiv:2611.03586v1](http://arxiv.org/abs/2611.03586v1) — source finding and federation-formation design.
- [FedReady full text](https://arxiv.org/html/2611.03586v1) — Sections 3–4 describe acceptance boundaries; Appendix E specifies artifact interfaces; Appendix F describes the NVFlare analysis application and evidence limitations. Verify the linked implementation snapshots before deriving executable instructions.
