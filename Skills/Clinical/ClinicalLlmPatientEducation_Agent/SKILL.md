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

10. **Support surgical and perioperative communication.** Draft preoperative procedure explanations, consent-adjacent education, discharge education, and postoperative instructions from approved source material; explain the procedure's purpose and what it involves; frame benefits, risks, alternatives, likely outcomes, and uncertainty proportionately; set expectations for preparation, expected recovery, restrictions, warning signs, and documented follow-up; run a readability check and adapt vocabulary and structure to the patient's health literacy while preserving clinically important detail and uncertainty; avoid presenting education as informed consent or replacing surgeon counseling and the surgeon-led consent discussion; flag multilingual risks such as mistranslation or loss of clinical meaning and require qualified review of translated versions for meaning and readability; state when and how to escalate postoperative warning signs using surgeon-approved instructions; include teach-back prompts; and require surgeon review and sign-off before delivery to the patient.

11. **Support surgical patient-physician communication use cases.** Produce plain-language procedure explanations, informed-consent support materials within educational limits, and perioperative instruction summaries from surgeon-approved source material, using literacy checks and teach-back prompts to help patients prepare questions for their care team. Preserve uncertainty while describing documented risks, benefits, alternatives, recovery expectations, and instructions without presenting the draft as informed consent or replacing surgeon counseling; require surgeon review before release.

12. **Translate surgical notes and plans for communication workflows.** Convert surgeon-approved operative notes, clinic notes, and surgical plans into patient-centered explanations, consent-support questions, perioperative instructions, risk/benefit summaries, and follow-up prompts. Label drafts as education or question preparation rather than procedural advice; preserve documented risks, alternatives, uncertainty, and follow-up timing; require clinician review; and flag overconfident, unsupported, or procedure-directing guidance for removal or escalation.

13. **Structure surgery-specific patient-physician communication.** Create perioperative counseling summaries, consent-question preparation prompts, and post-op instruction drafts only from clinician-approved source material; perform readability checks without removing clinically important detail; include documented escalation triggers for warning signs, urgent concerns, or unanswered consent questions; and keep messaging within clinician-approved constraints for diagnosis, prognosis, procedure decisions, follow-up timing, and surgeon-patient counseling.

14. **Use surgery communication templates within review boundaries.** Generate pre-op and post-op explanation templates from surgeon-approved source material, including the procedure purpose, expected course, documented risks, uncertainty, recovery instructions, warning signs, and follow-up prompts; check readability and preserve clinically important detail; keep consent-support language limited to education and question preparation rather than informed consent or surgical decision-making; and require surgeon review and sign-off before any patient-facing use.

15. **Benchmark MRI report interpretation for patient education.** Map MRI terminology to plain language while preserving key radiology terms, diagnostic uncertainty, negation, laterality, location, severity, and measurements; personalize only within supplied patient context, flag missing clinical context that limits interpretation, and do not infer missing history, symptoms, prognosis, or preferences; set and assess an audience-appropriate readability target; trace plain-language statements back to the source report findings, impression, and recommendations; compare the explanation with a human-expert interpretation when available for agreement, omissions, contradictions, unsupported additions, and distorted meaning; explicitly check for omitted findings and fabricated claims; and require clinician review before any personalized explanation is delivered to a patient.

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
- Clement EA, Lee L. "Artificial Intelligence to Improve Patient-Physician Communication in Surgery." *Clinics in Colon and Rectal Surgery*. 2026 May. https://pubmed.ncbi.nlm.nih.gov/41948164/
