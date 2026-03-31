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
name: github-agentic-workflows
description: Configure GitHub's Agentic Workflows technical preview so Copilot, Claude Code, or Codex can act as CI/CD participants with human-in-the-loop safety.
keywords:
  - github-actions
  - agentic-automation
  - cicd
  - repo-maintenance
  - continuous-ai
measurable_outcome: Ship an issue-triage and CI-investigation Agentic Workflow that runs successfully on a target repository within one working session.
license: MIT
metadata:
  author: Bioinformatics Oxford
  version: "2026.03"
compatibility:
  - system: GitHub Actions (Enterprise or preview-enabled org)
allowed-tools:
  - run_shell_command
  - web_fetch
  - read_file
---

# GitHub Agentic Workflows (Technical Preview · February 2026)

GitHub now lets AI coding agents run as first-class actors inside Actions jobs. Use this skill whenever a biomedical repo needs intent-driven automation (issue triage, CI failure diagnosis, documentation upkeep) without leaving the GitHub stack.

## When to Use
- You maintain regulated or research repos that need 24/7 hygiene but must keep humans in the approval loop.
- You want Copilot, Claude Code, or OpenAI Codex to read repo context, reason about failures, and draft fixes directly from Actions.
- You are piloting GitHub's **Continuous AI** vision (agents always-on, humans review before merge).

## Prerequisites
1. Organization with GitHub Copilot Enterprise **or** Agentic Workflows preview enabled (`Settings → Copilot → Agentic Workflows`).
2. GitHub Actions allowed for the repository plus an PAT/enterprise secret for Anthropic or OpenAI if those agents are used.
3. Repository secrets:
   - `ANTHROPIC_API_KEY` for Claude Code.
   - `OPENAI_API_KEY` for Codex.
   - Optional vendor keys for downstream automation (PagerDuty, Slack, etc.).

## Enable the Preview
```text
Org → Settings → Copilot → Agentic Workflows → Enable Technical Preview
Repo → Settings → Code and automation → Actions → Agentic Workflows → Enable
```
GitHub enforces a **human review guardrail**: agents can open or update pull requests but cannot merge them. Keep CODEOWNERS in place so reviews stay deterministic.

## Reference Implementation

### 1. AI Issue Triage
`.github/workflows/agent-triage.yml`
```yaml
name: AI Issue Triage
on:
  issues:
    types: [opened, edited]
jobs:
  triage:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: github/agentic-workflows@v1
        with:
          agent: copilot   # claude-code or codex also supported
          task: |
            Review the new issue, label it, request clarifications, and detect duplicates.
            Never close issues; escalate unclear reports via a comment.
          context: |
            Repo: ${{ github.repository }}
            Issue: ${{ github.event.issue.number }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 2. CI Failure Investigator
`.github/workflows/agent-investigate-ci.yml`
```yaml
name: AI CI Failure Investigation
on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]
jobs:
  investigate:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
      checks: read
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: github/agentic-workflows@v1
        with:
          agent: claude-code
          task: |
            Download the failed logs, summarize root cause, and propose/code a fix.
            Post a PR comment with repro steps and affected files.
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### 3. Test Coverage Drafter (Optional)
Use Claude Code or Codex to inspect diffs, detect missing unit tests, and open draft PRs with coverage patches. Remember to set `contents: write` permissions when allowing auto-commits.

## Operational Checklist
- Map objectives to agents: Copilot (native repo context), Claude Code (deep reasoning on large diff sets), Codex (fast refactors/tests).
- Budget for Actions minutes **plus** model tokens; monitor `usage` tab weekly.
- Gate every agent job with `if:` statements to avoid recursive triggers.
- Store prompts/goals in version control so reviewers can audit agent intent.

## Troubleshooting
- **Agent fails silently:** ensure preview flag is enabled at both org and repo scopes.
- **Rate-limit hits:** stagger workflows with `workflow_run` filters or `workflow_call` fan-ins to keep under Actions concurrency caps.
- **Security review:** tie workflow outputs to CODEOWNERS and branch protection so unpublished agent branches cannot merge.

## References
1. GitHub, *Introducing GitHub Agentic Workflows – intent-driven repository automation* (YouTube premiere, 13 Feb 2026). https://www.youtube.com/watch?v=3_i03fGXs9U
2. Subagentic.ai, *GitHub Agentic Workflows Technical Preview* (24 Feb 2026). https://subagentic.ai/howtos/github-agentic-workflows-technical-preview-cicd/

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
