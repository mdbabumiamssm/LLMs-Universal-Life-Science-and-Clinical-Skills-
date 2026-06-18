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
name: 'clinical-llm-patient-education'
description: 'Translate clinical documents into personalized patient education while preserving diagnostic meaning, uncertainty, next steps, and clinician-review safeguards.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Clinical LLM Patient Education

## Overview

Translate radiology reports and other clinical documents into patient-centered explanations without changing their diagnostic meaning. Apply a governed workflow that preserves uncertainty, adapts reading level, checks against clinician-authored explanations when available, and routes consequential guidance for professional review.

## When to Use This Skill

- Explain an MRI, CT, ultrasound, X-ray, pathology, laboratory, or other clinical report to a patient.
- Convert technical clinical language into plain language for education or shared decision-making.
- Personalize an explanation using documented patient context, preferences, language, or health literacy needs.
- Compare an LLM-generated explanation with a clinician-authored explanation or approved patient resource.
- Review patient education for omissions, false reassurance, alarmism, or harmful simplification.
- Draft educational material that requires a clinician to approve diagnosis, prognosis, treatment, or urgent next-step guidance.

## Core Capabilities

1. **Establish source fidelity.** Identify the document type, findings, impression, recommendations, comparison studies, and explicit limitations. Separate source facts from contextual explanation and never introduce an unsupported diagnosis.

2. **Preserve diagnostic meaning.** Translate technical terms and anatomical descriptions while retaining laterality, location, severity, chronology, measurements, and clinically meaningful qualifiers such as possible, likely, stable, or cannot exclude.

3. **Explain uncertainty.** State what the document shows, what remains uncertain, and what the report cannot determine. Do not convert probabilistic wording into certainty or treat absence of mention as a negative finding.

4. **Personalize safely.** Use only supplied and relevant patient context. Adjust vocabulary, structure, language, and reading level without inferring demographics, history, symptoms, prognosis, or preferences that were not provided.

5. **Describe next steps proportionately.** Restate report recommendations accurately and distinguish routine follow-up, questions for the care team, and time-sensitive escalation. Do not independently prescribe treatment, change medication, or replace clinician instructions.

6. **Compare with clinician-authored content.** When a clinician explanation or approved resource is available, map agreement, omissions, contradictions, tone differences, and unsupported additions. Prefer the clinician-approved interpretation for patient-specific consequential guidance.

7. **Detect harmful simplification.** Check for omitted red flags, lost negation, altered severity, erased uncertainty, misleading analogies, false reassurance, unnecessary alarm, and advice that exceeds the source document.

8. **Require professional review.** Mark the output as a draft requiring qualified review when it contains or could influence diagnosis, prognosis, urgency, treatment, medication, procedure decisions, or follow-up timing. Escalate unresolved contradictions instead of reconciling them speculatively.

9. **Produce an auditable result.** Preserve source traceability and label each statement as source-derived explanation, general education, question for the clinician, or review-required guidance.

## Inputs / Outputs

### Inputs

- The complete clinical document, including impression, findings, recommendations, and addenda when available.
- Patient context explicitly authorized for personalization, such as age range, symptoms, relevant history, preferred language, and target reading level.
- The intended audience and purpose of the explanation.
- Clinician-authored explanations, prior approved materials, or institutional guidance when available.
- Any required format, accessibility, privacy, or review constraints.

Do not proceed from a partial excerpt when omitted sections could materially change the interpretation. Request the missing content or clearly limit the scope of the output.

### Outputs

Produce:

1. **Plain-language summary:** Explain the main findings and overall impression without adding clinical conclusions.
2. **Term-by-term explanation:** Define important anatomy, findings, measurements, and qualifiers in context.
3. **Uncertainty and limitations:** Preserve hedging, differential considerations, technical limitations, and unanswered questions.
4. **Next steps:** Restate documented recommendations and provide questions the patient may ask the care team.
5. **Comparison review:** When a clinician explanation exists, list material agreements, omissions, contradictions, and additions.
6. **Safety review:** Flag possible harmful simplification, unsupported claims, urgency errors, and content requiring professional review.
7. **Review status:** End with `Professional review required` for consequential guidance, or `Educational explanation only; no patient-specific clinical guidance provided` when the output is strictly non-consequential.

Before finalizing, verify:

- Every patient-specific claim is supported by the source document or supplied context.
- Negation, laterality, severity, measurements, time course, and uncertainty remain intact.
- The reading level is appropriate without deleting clinically important content.
- Recommendations match the document and do not become independent medical advice.
- Any emergency warning is based on supplied clinical guidance or clearly framed as general safety information, not a diagnosis.
- Protected health information is minimized and handled according to the user's authorized environment.

## References

- Du K, Li A, Zuo QH, Zhang CY, Guo R. "Comparing large language models and human experts in interpreting MRI reports for personalized patient education." *International Journal of Medical Informatics*. 2026. https://pubmed.ncbi.nlm.nih.gov/41865475/
