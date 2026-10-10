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
name: 'gi-cancer-ai-management-agent'
description: 'Use clinician-governed AI workflows for GI cancer endoscopy, imaging, pathology, profiling, treatment selection, trials, and surveillance.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# GI Cancer AI Management Agent

## Overview

Use this skill to structure clinician-governed AI support for gastrointestinal cancer management across endoscopy, imaging, pathology, molecular profiling, treatment selection, trial routing, and surveillance. It helps transform heterogeneous patient data into auditable decision-support outputs while keeping final diagnosis, treatment selection, and consent under qualified clinical authority.

## When to Use This Skill

- Use when asked to design, review, or execute an AI-assisted workflow for management of GI cancers, including colorectal, gastric, esophageal, pancreatic, hepatobiliary, anal, small bowel, or neuroendocrine malignancies.
- Use when synthesizing endoscopy, radiology, pathology, biomarker, genomic, treatment-history, or surveillance data for a clinician-facing oncology summary.
- Use when evaluating where AI may help with lesion detection, image interpretation, pathology review, molecular profiling, risk stratification, treatment matching, trial prescreening, or longitudinal monitoring.
- Use when preparing tumor board support, care-navigation logic, trial-routing criteria, or surveillance follow-up recommendations that require explicit uncertainty and escalation rules.
- Use when documenting safety, validation, bias, privacy, and human-oversight requirements for AI tools used in GI oncology.
- Do not use as a substitute for emergency care, independent diagnosis, autonomous treatment selection, or patient-specific medical advice without responsible clinician review.

## Core Capabilities

1. **Clinical question framing** - Define the cancer site, disease state, decision point, intended AI role, responsible clinician, and actionability threshold before analysis.
2. **Data sufficiency review** - Check whether staging, pathology, imaging, endoscopy, molecular testing, performance status, comorbidities, prior therapies, and patient goals are adequate for the requested output.
3. **Multimodal evidence synthesis** - Organize relevant findings from endoscopy, radiology, pathology, laboratory results, biomarkers, genomic profiling, operative reports, and treatment history into a traceable clinical narrative.
4. **AI-use-case mapping** - Match the task to appropriate AI support categories such as detection, segmentation, report summarization, risk prediction, molecular interpretation, trial prescreening, or surveillance flagging.
5. **Treatment-decision support** - Produce clinician-facing options, contraindication checks, biomarker dependencies, missing-data prompts, and multidisciplinary discussion points without presenting unreviewed model output as a final plan.
6. **Trial and referral routing** - Identify structured eligibility fields, unresolved criteria, referral triggers, and required source documents for clinical trial or specialty-care prescreening.
7. **Surveillance and response monitoring** - Summarize longitudinal imaging, tumor markers, endoscopy intervals, toxicity, symptoms, and recurrence-risk signals with clear dates and uncertainty.
8. **Governance and safety controls** - Require source attribution, date-stamped evidence, validation status, bias considerations, privacy safeguards, and escalation to qualified clinicians for high-impact decisions.
9. **2026 ASCO workflow refresh** - Use the 2026 ASCO Educational Book GI cancer management review as a high-level source for clinician-governed AI workflows, separating mature image-based use cases such as endoscopy and imaging from emerging patterns involving LLM summarization, molecular profiling, trial matching, surveillance support, and decision support; document evidence limits, escalation rules, and explicit limits on autonomous recommendations.
10. **GI cancer continuum coverage** - When applying the ASCO educational review, explicitly account for endoscopy, imaging, pathology, molecular profiling, treatment planning, clinical trial prescreening, surveillance, and clinician governance in the workflow scope.
11. **Clinician-governed workflow map** - Map AI-assisted GI cancer recommendations across endoscopy, imaging, pathology, molecular profiling, treatment selection, clinical trials, and surveillance, placing explicit human review checkpoints before diagnosis, regimen choice, trial referral, surveillance interval changes, or other patient-facing recommendations.
12. **ASCO evidence update for decision support** - Incorporate the 2026 ASCO Educational Book review when designing GI cancer AI workflows across endoscopy, imaging, pathology, treatment selection, and surveillance, treating AI outputs as clinician-reviewed decision support rather than autonomous management.
13. **Current ASCO clinical framing** - Use the 2026 ASCO Education Book review as a current clinical framing source for GI cancer AI workflows spanning endoscopy, imaging, pathology, molecular profiling, treatment selection, clinical trials, surveillance, governance, and clinician-in-the-loop safeguards.
14. **ASCO Educational Book domain update** - Apply the 2026 ASCO Educational Book review as a domain update for clinician-led AI use across GI cancer management, explicitly covering endoscopy, imaging, pathology, molecular profiling, treatment planning, clinical trials, surveillance, and governance boundaries.
15. **ASCO GI cancer AI management review** - Use Goyal, Chung, Mori, Hall, and Kehl's 2026 ASCO Educational Book review as a current source when scoping clinician-governed AI workflows across screening/endoscopy, imaging, pathology, molecular profiling, treatment planning, trial matching, surveillance, and governance limits.
16. **ASCO current synthesis workflow check** - Treat the 2026 ASCO Educational Book review as a current synthesis for GI cancer AI workflows across endoscopy, pathology, radiology, molecular profiling, treatment planning, trial matching, surveillance, and clinician-governed implementation boundaries.
17. **ASCO handoff-point integration** - Use the 2026 ASCO Education Book review to keep endoscopy, imaging, pathology, molecular profiling, treatment planning, trial routing, and surveillance outputs tied to explicit clinician-governed handoff points before clinical action.
18. **ASCO audit-ready governance** - For GI cancer AI workflows informed by the 2026 ASCO Educational Book review, require clinician-governed use across endoscopy, imaging, pathology, molecular profiling, treatment selection, trial matching, and surveillance, with documented evidence sources, model limitations, review decisions, and audit trails before patient-facing action.
19. **ASCO clinical-scoping checkpoint** - Use the 2026 ASCO Educational Book GI cancer AI management review as a current clinical-scoping reference across endoscopy, imaging, pathology, molecular profiling, treatment selection, trial routing, and surveillance; explicitly document limitations and clinician-governance checkpoints before acting on AI-supported outputs.
20. **ASCO safety-handoff workflow** - Use the 2026 ASCO GI cancer management review to structure clinician-governed AI workflows across endoscopy, imaging, pathology, molecular profiling, treatment selection, trial routing, and surveillance, requiring explicit safety handoff to the responsible clinician before diagnosis, therapy, trial, or follow-up actions.
21. **ASCO validation-and-monitoring frame** - Use the 2026 ASCO Educational Book review as current clinical framing for GI cancer AI workflows across endoscopy, pathology, imaging, molecular profiling, treatment selection, clinical trials, toxicity monitoring, and surveillance; require clinician governance and workflow-specific validation before clinical use.
22. **ASCO evidence-traceable deployment pathway** - Apply Goyal et al.'s 2026 ASCO Educational Book review as a clinical workflow reference spanning endoscopy, imaging, pathology, molecular profiling, treatment selection, clinical trials, and surveillance, with traceable evidence links and clinician-governed deployment boundaries for any AI-supported management output.
23. **ASCO human-review gates** - Use the 2026 ASCO GI cancer management review to require explicit clinician review gates for AI outputs across endoscopy, imaging, pathology, molecular profiling, treatment selection, clinical trial routing, and surveillance before patient-facing decisions or workflow changes.
24. **ASCO-style management boundary** - Scope GI cancer AI support across endoscopy, radiology, pathology, molecular profiling, treatment selection, trial referral, surveillance, and governance while clearly labeling outputs as clinician decision support and excluding autonomous diagnosis, regimen selection, referral, or surveillance recommendations without responsible clinician review.
25. **ASCO Educational Book overview alignment** - Incorporate Goyal et al.'s 2026 ASCO Educational Book review as a current overview for clinician-governed AI use across GI cancer management, spanning endoscopy, imaging, pathology, molecular profiling, treatment planning, clinical trial matching, surveillance, and safety monitoring.
26. **ASCO clinical workflow update** - Apply the 2026 ASCO Educational Book review as a workflow update for GI cancer AI management across endoscopy, imaging, pathology, molecular profiling, treatment selection, clinical trials, and surveillance; document validation limits and clinician-governed adoption checkpoints before using AI-supported outputs in care pathways.

## Inputs / Outputs

**Inputs**

- Patient context: age range when needed, cancer site and subsite, stage, histology, disease setting, performance status, comorbidities, organ function, goals of care, and relevant constraints.
- Clinical artifacts: endoscopy reports, imaging reports, pathology reports, operative notes, labs, tumor markers, molecular or germline testing, prior treatments, adverse events, and surveillance timeline.
- Task context: requested AI use, intended clinical workflow, available institutional protocols, guideline or evidence sources to check, deployment setting, and responsible reviewer.
- Safety context: urgency, symptoms needing immediate escalation, data provenance, consent/privacy limits, model validation status, and known population or site-specific limitations.

**Outputs**

- A clinician-facing GI oncology AI management brief with decision point, data inventory, key findings, missing information, and recommended next review steps.
- A multimodal evidence map linking each conclusion to available source artifacts and dates.
- A structured AI workflow recommendation describing intended use, human oversight, validation needs, failure modes, and escalation thresholds.
- Treatment, trial, referral, or surveillance support notes that separate confirmed facts, model-assisted inferences, and clinician-only decisions.
- A safety and governance checklist covering privacy, bias, auditability, source currency, uncertainty, and documentation requirements.

## References

- Goyal L, Chung C, Mori Y, Hall WA, Kehl KL. "Harnessing Artificial Intelligence for the Management of Patients With GI Cancers." *ASCO Educational Book*. 2026 Jun. PubMed: https://pubmed.ncbi.nlm.nih.gov/42044465/
