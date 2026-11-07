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
name: 'longitudinal-clinical-memory-evaluation'
description: 'Construct and evaluate patient-state memory across medical dialogue sessions, testing dated state changes, subject attribution, and retrieval of safety-relevant evidence.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Longitudinal Clinical Memory Evaluation

## Overview

This skill builds and evaluates research prototypes of longitudinal patient-state memory, focusing on stale facts, facts attributed to the wrong person, and missing safety-relevant evidence. It translates the supplied MedGraph finding into an auditable workflow for dated facts, linked state histories, and evidence-backed retrieval. Treat the graph approach and reported benchmark findings as research evidence, not validation for clinical deployment or patient-specific treatment decisions.

## When to Use This Skill

- Evaluate an assistant that must recall a patient's history across multiple dialogue sessions.
- Investigate answers that use discontinued medications, superseded diagnoses, or outdated measurements.
- Test whether family history, caregiver reports, or another person's conditions contaminate patient memory.
- Assess whether retrieval includes recorded safety facts needed to answer a question.
- Compare graph memory with an existing memory approach under the same evidence and resource constraints.

## Core Capabilities

1. **Define a bounded evaluation.** Select a small, declared set of de-identified or synthetic longitudinal dialogues and questions that can be processed within 15 minutes. Record the dataset version, patient/session identifiers, available timestamps, model configuration, retrieval budget, and evaluation scope. If inputs or execution access are missing, return an explicit blocked or protocol-only result; do not present it as a completed evaluation.

2. **Extract dated, attributable facts.** Create one record per clinical assertion with the following fields; represent unavailable values explicitly rather than guessing:

   | Field | Required meaning |
   |---|---|
   | `fact_id`, `patient_id`, `subject_id` | Stable fact identifier, dialogue owner, and person the assertion describes |
   | `speaker_id`, `subject_relation` | Who spoke and how the described person relates to the patient |
   | `session_id`, `source_span` | Traceable dialogue location and supporting excerpt |
   | `recorded_at`, `effective_at` | When the assertion was recorded and when the reported event occurred |
   | `concept`, `fact_type`, `value`, `unit` | Medication, diagnosis, measurement, or other assertion and its recorded details |
   | `status`, `polarity`, `certainty` | State, affirmation/negation, and whether asserted, suspected, or uncertain |
   | `valid_until`, `supersedes`, `conflicts_with` | Explicit end time or links to prior or conflicting records, where supported |

   Anchor relative dates to a known session date, retain the original wording, and mark approximate dates. A speaker is not automatically the subject: a patient describing a parent's allergy does not establish a patient allergy. Preserve uncertain attribution for review instead of assigning it silently.

3. **Maintain state chains without erasing history.** Link medication, diagnosis, and measurement records by subject and compatible clinical concept. Preserve dose changes, discontinuations, diagnostic revisions, repeated measurements, and explicit corrections as separate dated events. Do not infer that a new medication replaces an old one, that an unmentioned condition has resolved, or that differing measurements are contradictions. Keep incompatible assertions unresolved unless the dialogue supports a correction; distinguish events occurring later from corrections about an earlier event.

4. **Retrieve evidence at the requested time.** Resolve the question's subject, target time, and evidence cutoff before retrieval. Rank the patient's relevant chains as units, select the state supported at the target time, and include original dialogue spans. For a prospective replay, exclude records captured after the cutoff even when they describe earlier events; for retrospective reconstruction, state that later evidence is permitted. If no target time is given, use the latest available session as the declared default. Never treat the most recently recorded assertion as automatically the most recent clinical event.

5. **Include a traceable safety profile.** Maintain all recorded patient safety facts, such as allergies or prior adverse reactions, with subject, status, dates, and source spans. Attach the profile eligible under the question's evidence cutoff to every retrieval, preserving historical and disputed entries with labels. This implements the supplied finding's safety-profile idea without implying that the record is clinically complete. Report missing or truncated profile entries explicitly; absence of a recorded fact is not evidence of its negation.

6. **Build independent reference cases.** Annotate expected subject, target time, supported state, required evidence spans, required safety facts, and answerability from the source dialogues rather than generated memory. Include state-change questions, historical questions, other-person distractors, safety-dependent questions, and unanswerable cases. Keep questions and labels out of memory construction, split by patient when tuning versus testing, and flag unresolved annotation disagreements instead of manufacturing a reference answer.

   Use these synthetic probes as local checks, not as a named or validated benchmark:

   | Probe | Dialogue pattern | Expected behavior |
   |---|---|---|
   | Stale state | Session A records medication use; session B explicitly stops it | Current-state retrieval reports the stop; a question about A retains the earlier use |
   | Wrong subject | Patient reports a sibling's allergy | Do not attach the allergy to the patient; retain its family attribution |
   | Missing safety evidence | An early session records a patient allergy; a later question requires it | Include the recorded allergy and its source despite topical or temporal distance |
   | Future leakage | A later session revises an earlier assertion | Earlier prospective replay cannot use the later revision |
   | Insufficient evidence | Conflicting records lack a resolving statement | Expose the conflict and mark the answer unresolved |

7. **Score retrieval and answers separately.** Run the selected memory systems on identical questions and eligible dialogue prefixes. Hold the answering model, prompt, and resource limits fixed where possible; disclose configuration differences and profile token overhead. Record per-question retrieved fact IDs, source spans, selected state, safety-profile contents, answer, and failure labels. Use multi-label errors because one answer may fail in several ways.

   | Metric | Operational definition |
   |---|---|
   | Evidence recall | Required reference evidence items retrieved / required reference evidence items |
   | Stale-state error rate | Temporal questions with an incorrect retrieved state / scorable temporal questions; also report the answer-level rate |
   | Wrong-person contamination | Questions with other-person facts treated as patient facts / scorable attribution questions; score retrieval and answers separately |
   | Safety-fact coverage | Required recorded safety facts included / required recorded safety facts for safety-dependent questions |
   | Safety-omission rate | Safety-dependent questions missing at least one required recorded fact / scorable safety-dependent questions |
   | Answer correctness | Answers matching the reference subject, time, state, and required facts without unsupported claims / scorable answerable questions |
   | Unsupported-answer rate | Unanswerable questions receiving a definite unsupported answer / scorable unanswerable questions |

   Report numerators and denominators, mark empty denominators as not applicable, and list excluded cases. Distinguish evidence that was never extracted, evidence stored but not retrieved, incorrect state selection, and evidence retrieved but ignored during answering. Measure construction time, retrieval/answer latency, and token usage only when instrumentation is available; label estimates and unavailable measurements.

8. **Audit mechanisms and report limits.** When time permits, compare full memory with removal of temporal chain selection, subject filtering, or the safety profile, changing one mechanism at a time. Treat these as proposed local ablations, not claimed details of the paper. Report paired question-level changes and representative failure traces. Stop at the time budget and disclose the evaluated subset, unfinished work, and limitations; a small pilot cannot establish clinical safety or generalization.

## Inputs / Outputs

**Inputs**

- Authorized, de-identified or synthetic session transcripts with patient/session IDs, speaker labels, dates when available, and traceable source locations.
- Evaluation questions with target times and evidence cutoffs, plus independently annotated expected states, attribution, safety dependencies, and answerability when available.
- Candidate memory implementation or inspectable memory records, an optional comparison system, model settings, and a declared time/token budget.
- Optional source paper text for checking implementation details beyond the supplied abstract-level finding. Do not upload identifiable dialogue to external services without authorization.

**Outputs**

- A fact ledger, linked state histories, and a dated patient safety profile, with uncertainty and provenance preserved.
- A per-question audit table containing evidence cutoff, selected subject/state, retrieved evidence, required and missing safety facts, answer, and failure labels.
- A concise evaluation report with actual counts and denominators, separate retrieval/answer results, measured resource use, comparison settings, and unfinished or unscorable cases.
- A completion status: `completed pilot`, `partial`, `protocol only`, or `blocked`, with reasons. Return artifacts inline unless the user requests saved outputs.

**Completion check:** Every selected state and safety assertion must trace to a source; no other-person fact may silently become a patient fact; prospective outputs must contain no future evidence; reported metrics must be recomputable from the audit table. Describe any violated check as a finding, not as a successful validation. The 15-minute outcome applies to a bounded pilot, not a full benchmark reproduction.

## References

- [MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical Dialogue](http://arxiv.org/abs/2611.08433v1), arXiv:2611.08433v1. Source basis: the supplied finding describes dated fact extraction, subject attribution, linked clinical histories, chain retrieval with original dialogue, and a safety profile. Its MedMemoryBench results are reported research findings; this workflow does not independently reproduce them or establish clinical readiness. Implementation schemas, local probes, and metric definitions above are evaluation recommendations rather than verified paper specifications.
