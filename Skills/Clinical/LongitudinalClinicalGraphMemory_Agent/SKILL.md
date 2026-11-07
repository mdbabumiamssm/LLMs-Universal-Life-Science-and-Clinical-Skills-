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
name: 'longitudinal-clinical-graph-memory'
description: 'Build and evaluate dated, person-attributed graph memory for longitudinal clinical dialogue, testing stale patient states, mistaken person attribution, and missing safety evidence.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Longitudinal Clinical Graph Memory

## Overview

Construct and evaluate research memory for medical conversations across visits, preserving changing patient states and their source evidence. The MedGraph finding motivates dated, person-attributed fact chains and a safety profile to address stale evidence, facts assigned to the wrong person, and omitted safety facts. The schema and evaluation procedure below are proposed implementation guidance, not a verified reproduction or evidence of clinical readiness.

## When to Use This Skill

- Prototyping memory for medical dialogue spanning multiple sessions.
- Investigating whether retrieved facts describe the patient, a relative, or another person.
- Answering research questions about current versus historical medication, diagnosis, or measurement states.
- Auditing retrieval for omitted recorded safety facts or outdated evidence.
- Comparing a graph-memory prototype with an existing retrieval system on authorized research data.

## Core Capabilities

1. **Define a bounded research run.** Select an authorized, preferably de-identified dialogue sample, patient identifier, evaluation questions, and evidence cutoff. For the 15-minute workflow, use a small fixture that exercises all three failure modes; report incomplete work explicitly rather than implying a full benchmark run. Keep patient dialogue out of public web queries.

2. **Extract attributable facts.** Read each session into atomic records. Separate the speaker from the person described; attach family-history facts to the relevant relative and relationship. Preserve negation, uncertainty, and whether a statement is reported, hypothetical, or confirmed. Assign unresolved references to an unknown subject pending review, rather than defaulting them to the patient.

3. **Represent time and provenance.** Give every fact a stable identifier, subject, clinical concept, value or status, event time or interval, recording time, session identifier, and exact source span. Preserve raw date expressions and time precision. An undated event remains undated; the session timestamp alone does not establish when the clinical state began.

4. **Maintain state chains.** Group compatible medication, diagnosis, and measurement records by subject and concept. Append changes with explicit links such as `updates`, `stops`, `corrects`, or `contradicts`, retaining prior records. Distinguish a prescription from reported use and a suspected diagnosis from a confirmed one. Repeated measurements form observations over time; a new measurement does not invalidate an old observation. Never merge records solely because their text is similar.

5. **Resolve the requested temporal view.** Identify both the clinical time the question concerns and the information available at the evaluation cutoff. Exclude later-recorded evidence when testing what was known at an earlier visit. Use explicit effective dates and supported transitions to reconstruct state; do not assume the latest recorded statement is automatically correct. Return competing evidence and an unresolved state when contradictions or missing dates prevent a defensible selection.

6. **Retrieve chains with evidence.** Filter to the target subject before ranking relevant chains. Read selected chains at the requested time and attach original dialogue spans to the resulting evidence packet. For questions about relatives, retrieve those subjects explicitly and label the relationship. Distinguish evidence retrieval from answer generation and support each answer claim with fact identifiers and source spans; abstain on unsupported claims.

7. **Include recorded safety evidence.** Maintain a patient profile containing every recorded safety fact, such as explicitly stated allergies or adverse reactions, with dates, status, and provenance. Attach this profile to every question independently of relevance ranking. Preserve retractions and contradictions with their context, and distinguish historical information from the requested state. Missing documentation means unknown, not a negative finding; if the profile cannot fit, report incomplete safety coverage instead of silently dropping entries.

8. **Evaluate the three failure modes.** Label expected subject, temporal state, and required safety evidence for each question before scoring. Include synthetic cases for a medication stopped after an earlier visit, a relative's condition mentioned by the patient, and a safety fact recorded far from the relevant question. Mark these as local fixtures, not MedMemoryBench examples. Compare systems on the same questions, available history, answer model, and declared resource settings.

9. **Report validity and limitations.** Check that all selected facts resolve to source spans, chain links stay within the intended subject and concept, and historical views exclude disallowed future evidence. Report observed failures, sample sizes, retrieval settings, elapsed time, and any untested behavior. Paper-level results do not establish performance on the local sample or clinical deployment safety; deployment claims require separate evidence and clinical evaluation.

## Inputs / Outputs

**Inputs**

- Timestamped dialogue sessions with session IDs, speaker labels, and accessible source text.
- Target patient ID and any available subject/relationship mapping.
- Questions specifying a target time when relevant, plus an information cutoff for retrospective tests.
- A declared set of safety-fact categories and, for scored evaluation, reference labels for subject attribution, state, and required evidence.
- Optional baseline retrieval configuration and a fixed answer model for a controlled comparison.

If subject identity, timestamps, or reference labels are unavailable, retain explicit unknowns and describe the affected checks as unscored. Do not invent patient facts or reference answers to fill gaps.

**Outputs**

- **Fact ledger:** Records with `fact_id`, `subject_id`, `speaker_id`, `concept`, `value_or_status`, `polarity`, `certainty`, `event_time`, `recorded_at`, `session_id`, and `source_span`; use explicit nulls for unknown fields.
- **Memory graph:** Subject nodes, fact nodes, ordered concept chains, typed change links, and retained conflicts. A structured in-memory representation is sufficient for a small run.
- **Safety profile:** All recorded patient safety facts with provenance and temporal status, including unresolved or corrected entries.
- **Question evidence packet:** Target subject, requested time, information cutoff, selected chain states, original source spans, safety profile, and unresolved gaps.
- **Evaluation report:** Per-question expected and retrieved states, failure labels, supporting evidence, settings, and completion status. Include an evidence-linked answer only when answer generation is part of the requested run.

Use these local metric definitions consistently; they are proposed operational measures, not claimed definitions from the paper:

| Measure | Definition |
|---|---|
| Stale-state error rate | Scorable temporal questions with a selected state inconsistent with the reference time / scorable temporal questions. |
| Wrong-person contamination rate | Scored question packets containing another subject's facts presented as the patient's / scored packets. |
| Required safety-evidence recall | Required reference safety facts included with provenance / all required reference safety facts. |
| Provenance coverage | Selected facts with resolvable supporting source spans / all selected facts. |

Report numerator and denominator for each measure; use `N/A` for a zero denominator. Record abstentions separately so omitting evidence cannot appear to eliminate retrieval errors. A valid small-run output contains the ledger, graph, safety profile, evidence packets, and an honest evaluation report within the declared time budget; it does not require a perfect score.

## References

- Donghua Zhang, Zizheng Wang, Ze Dong, Yiding Feng, and Siyu Qian. [MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical Dialogue](http://arxiv.org/abs/2611.08433v1). arXiv:2611.08433v1, submitted November 5, 2026. Source for the three failure modes and the graph-memory approach; the supplied abstract does not specify the complete implementation or establish clinical deployment readiness.
