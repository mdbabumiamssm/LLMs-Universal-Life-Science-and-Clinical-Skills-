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
name: clinical-workflow-automation
description: An autonomous agentic system for automating and streamlining clinical workflows and healthcare administrative tasks.
keywords:
  - clinical-workflow
  - healthcare-ai
  - automation
  - ehr-integration
measurable_outcome: Automate routine clinical documentation, scheduling, or data entry tasks to save clinical staff time by over 50%.
license: MIT
metadata:
  author: OpenSource Healthcare AI Community
  version: "1.0.0"
compatibility:
  - system: Python 3.9+
allowed-tools:
  - run_shell_command
  - python_repl
  - read_file
---

# Clinical Workflow Automation Agent

A specialized agent designed to streamline administrative and clinical workflows within healthcare settings. It uses LLMs to interpret unstructured clinical notes, update Electronic Health Records (EHRs), and automate patient scheduling and follow-ups.

## When to Use This Skill
- You need to automate data extraction from clinical documents.
- You are building an integration with EHR systems to reduce manual data entry.
- You want to implement autonomous triaging or scheduling based on patient communications.

## Core Capabilities
- **EHR Integration:** Connects with standard FHIR APIs to read and write patient data securely.
- **Unstructured Data Parsing:** Extracts key entities (diagnoses, medications, lab results) from free-text clinical notes.
- **Workflow Orchestration:** Coordinates multi-step administrative processes like prior authorizations and referrals.

## Example Workflow
1. Provide the agent with access to a repository of patient intake forms.
2. Invoke `clinical-workflow-automation` to parse the forms.
3. The agent autonomously extracts relevant data points and drafts standard EHR updates.
4. Review and approve the proposed updates before the agent commits them to the system.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
