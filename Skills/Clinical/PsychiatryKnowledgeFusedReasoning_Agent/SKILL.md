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
name: 'psychiatry-knowledge-fused-reasoning'
description: 'Psychiatry CDS workflow for knowledge-fused augmented reasoning across diagnosis, risk assessment, medication reasoning, and care planning.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Psychiatry Knowledge-Fused Reasoning

## Overview

This skill guides psychiatry-focused clinical decision support using knowledge-fused augmented reasoning inspired by PKFAR: psychiatry knowledge-fused augmented reasoning with large language models. It supports structured psychiatric assessment, diagnostic reasoning, risk assessment, medication reasoning, and care planning while keeping outputs evidence-grounded, clinically cautious, and appropriate for clinician review.

## When to Use This Skill

- A user asks for psychiatry-oriented clinical decision support, diagnostic reasoning, differential diagnosis, or treatment planning.
- A user needs structured reasoning for symptoms involving mood, anxiety, psychosis, trauma, substance use, cognition, personality, sleep, or suicidality.
- A user asks for psychiatric risk assessment, including suicide risk, self-harm risk, violence risk, inability to care for self, intoxication, withdrawal, or acute decompensation.
- A user requests medication reasoning for psychiatric drugs, adverse effects, interactions, monitoring, tapering considerations, or adherence barriers.
- A user needs an evidence-grounded care plan that integrates symptoms, history, psychosocial context, safety needs, and follow-up.
- A user asks to transform clinical notes, interviews, or case vignettes into a structured psychiatry reasoning summary.

## Core Capabilities

1. **Case structuring** - Extract presenting concerns, timeline, symptoms, functional impairment, psychiatric history, medical history, medications, substance use, family history, trauma history, social context, and protective factors.
2. **Knowledge-fused diagnostic reasoning** - Map case findings to psychiatric diagnostic constructs and differential diagnoses while separating observed facts, patient-reported claims, and clinical inferences.
3. **Risk assessment** - Identify acute and chronic risk factors, protective factors, warning signs, missing safety data, and escalation needs for suicide, self-harm, violence, grave disability, intoxication, or withdrawal.
4. **Medication reasoning** - Summarize candidate medication classes, contraindication checks, interaction concerns, side-effect burdens, monitoring needs, and patient-specific considerations without substituting for prescribing judgment.
5. **Care planning** - Produce clinician-reviewable next steps for assessment, safety planning, psychotherapy considerations, medication discussion, labs or monitoring when relevant, coordination of care, and follow-up acuity.
6. **Uncertainty management** - State confidence limits, competing explanations, missing information, and reasons to defer or escalate to urgent clinical evaluation.
7. **PKFAR-style reasoning controls** - Retrieve relevant psychiatry specialty knowledge before answering, keep diagnostic, risk, and medication reasoning separated, ground clinical claims in citations when sources are used, and audit outputs for hallucinated claims, unsafe advice, and missing differential diagnoses.

## Inputs / Outputs

**Inputs**

- Patient age range or developmental stage when available.
- Presenting symptoms, duration, severity, triggers, course, and functional impact.
- Mental status observations, collateral information, relevant medical data, current medications, allergies, substance use, and psychosocial context.
- Prior psychiatric diagnoses, hospitalizations, therapy, medication trials, response, adverse effects, and adherence history.
- Immediate safety information, including suicidal ideation, intent, plan, access to means, prior attempts, homicidal ideation, psychosis, intoxication, withdrawal, abuse, neglect, and ability to care for self.
- User's requested output type, such as differential diagnosis, risk formulation, medication reasoning, care plan, note summary, or clinician-facing checklist.

**Outputs**

- Structured psychiatry case summary with explicit facts, relevant negatives, and missing information.
- Differential diagnosis or diagnostic formulation with supporting and conflicting evidence.
- Risk formulation that distinguishes acute risk, chronic risk, protective factors, and recommended escalation thresholds.
- Medication reasoning summary covering rationale, cautions, monitoring, interactions, and questions for the prescribing clinician.
- Care plan draft suitable for clinician review, including safety actions, follow-up timing, psychotherapy or psychosocial interventions, and coordination needs.
- Clear limitation statement that the output is clinical decision support and not a substitute for emergency services, licensed diagnosis, or prescribing.

## References

- PubMed: PKFAR: psychiatry knowledge-fused augmented reasoning with large language models. https://pubmed.ncbi.nlm.nih.gov/41982804/
