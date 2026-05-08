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
name: 'prosthetix-ai-prosthetic-recommendations'
description: 'Guide evidence-based prosthetic recommendation workflows inspired by ProsthetiX-AI clinical decision support for limb-loss care with clinician review.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# ProsthetiX-AI Prosthetic Recommendations

## Overview

This skill supports structured, evidence-based prosthetic recommendation workflows for people with limb loss or limb difference. It organizes patient functional status, amputation level, comorbidities, rehabilitation goals, and contraindications into a clinician-reviewable decision support output rather than treating model output as a prescription.

Use this skill to produce transparent prosthetic option summaries, identify missing clinical information, and document why each recommendation may or may not fit the patient's needs. Final device selection, fitting, and medical decisions must remain with qualified clinicians and the care team.

## When to Use This Skill

- A user asks for prosthetic device, component, socket, suspension, or control-system recommendations.
- A case involves lower-limb or upper-limb amputation, congenital limb difference, or prosthetic replacement planning.
- The task requires matching prosthetic options to activity goals, mobility level, vocational needs, or rehabilitation priorities.
- The user needs a structured clinical decision support note for prosthetist, physiatrist, surgeon, therapist, or multidisciplinary review.
- The workflow must surface contraindications, precautions, uncertainty, or missing assessment data before recommending options.

## Core Capabilities

1. Patient profile structuring: Extract and organize amputation level, laterality, residual limb status, age, occupation, environment, prior prosthesis history, and care-team context.
2. Functional needs assessment: Summarize mobility, dexterity, balance, endurance, transfers, pain, skin tolerance, activities of daily living, and patient-stated goals.
3. Clinical constraint screening: Identify factors that can alter prosthetic suitability, including vascular disease, diabetes, neuropathy, wound risk, cognitive status, cardiopulmonary limits, infection, contracture, and fall risk.
4. Prosthetic option mapping: Compare plausible sockets, suspension approaches, feet, knees, terminal devices, control strategies, liners, and interface considerations at a high level.
5. Evidence-aware reasoning: Ground the recommendation in available case facts and cited clinical sources; distinguish documented evidence from inference or expert-consensus-style reasoning.
6. Safety and escalation checks: Flag urgent medical issues, incomplete evaluations, unrealistic goals, or cases requiring in-person assessment before device selection.
7. Clinician-reviewable output: Produce a concise recommendation matrix with rationale, contraindications, required follow-up questions, and explicit human review requirements.

## Inputs / Outputs

Inputs this skill can consume:

- Patient demographics relevant to prosthetic planning.
- Amputation or limb difference level, side, cause, date, surgical history, and residual limb findings.
- Current prosthesis details, fit issues, pain, skin status, device failures, and patient satisfaction.
- Functional status, mobility aids, gait observations, hand function, activities of daily living, occupational demands, and recreational goals.
- Comorbidities, medications, wound history, cognition, vision, balance, cardiopulmonary tolerance, and rehabilitation progress.
- Insurance, service setting, access, maintenance capacity, and follow-up constraints when relevant.

Outputs this skill should produce:

- A structured case summary with missing or uncertain information clearly marked.
- A prosthetic recommendation matrix listing candidate approaches, rationale, benefits, limitations, and contraindications.
- Clinical questions to ask before final selection or fitting.
- Risk, safety, and referral notes for clinician review.
- A final statement that the output is decision support only and requires prosthetist or qualified clinician confirmation.

## References

- PubMed: Kumar V, Pratihar DK. "ProsthetiX-AI: An LLM-based clinical decision support system for evidence-based prosthetic recommendations." Health Information Science and Systems. 2026 Dec. https://pubmed.ncbi.nlm.nih.gov/41978836/
