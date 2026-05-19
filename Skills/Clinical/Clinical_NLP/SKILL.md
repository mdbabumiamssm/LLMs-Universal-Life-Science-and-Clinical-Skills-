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
name: 'clinical-nlp-extractor'
description: 'Extracts medical entities (Diseases, Medications, Procedures), patient outcomes with temporal anchors, and registry-oriented real-world data from unstructured clinical text using regex and simple rules (or LLM wrappers).'
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
  - read_file
  - run_shell_command
---


# Clinical NLP Entity Extractor

The **Clinical NLP Skill** converts free-text clinical notes into structured data. It identifies key medical entities like problems/diagnoses, medications, and procedures.

## When to Use This Skill

*   When analyzing unstructured EHR notes.
*   To populate a patient's problem list or medication reconciliation.
*   To de-identify text (phi-removal) - *Basic version*.

## Core Capabilities

1.  **NER (Named Entity Recognition)**: Extracts Problems, Drugs, Procedures.
2.  **Negation Detection**: (Basic) Checks if a finding is denied ("No fever").
3.  **Structuring**: Returns JSON format compatible with FHIR/USDL.
4.  **Rare-neoplasm RWD abstraction with LLMs**: For registry-quality capture in rare neoplasms such as bone sarcoma, design entity and outcome schemas before extraction, map outputs to registry fields, anchor temporal events such as diagnosis, treatment, progression, recurrence, and follow-up, normalize low-prevalence entities to the cohort vocabulary, preserve criterion-level provenance and source-note evidence for each extracted item, label uncertain values, run abstraction QA against expected field formats and clinician-defined vocabularies, and route sarcoma-style sparse-cohort or low-confidence cases through clinician adjudication loops.
5.  **LLM-assisted rare-neoplasm RWD collection**: For bone sarcoma-like low-volume cohorts, use LLM-assisted abstraction from clinician notes to map extracted facts to registry variables, attach temporal anchors to diagnosis, treatment, response, progression, recurrence, and follow-up events, handle PHI through the project de-identification or secure processing workflow before secondary use, sample extractions for validation against manual review, and send ambiguous, discordant, or clinically critical fields to clinician adjudication before release.
6.  **Outcome extraction with temporal anchoring**: Identify patient outcome mentions in clinician notes, normalize outcome events and event timing, label temporal relations and current/past/future outcome status, infer explicit or relative dates/times plus event onset and resolution windows, distinguish baseline from follow-up events, classify uncertainty and negation, validate extracted outcomes against chart-review labels for RWE workflows, run longitudinal consistency checks across notes, retain audit-ready source-note evidence spans for each extracted outcome, and generate downstream registry/RWE-ready tables with outcome status, event timing, temporal anchor, uncertainty class, negation, provenance, and audit trails.
7.  **Sparse oncology registry extraction**: Extract entities and outcomes from oncology notes for rare neoplasms such as bone sarcoma, map each abstracted value to registry fields, anchor findings to explicit or relative clinical timelines, route missing or uncertain values to human validation queues, and retain audit-ready provenance linking extracted values to source notes, evidence spans, and validation status.
8.  **Rare-neoplasm RWD variable extraction**: Before extracting oncology rare-neoplasm real-world data, define registry variables for stage, treatments, outcomes, and follow-up; extract stage, treatment, and outcome fields from notes with explicit temporal anchors; support sparse and variable terminology common in rare cohorts; and validate extracted variables against manual abstraction before using them in downstream analyses.
9.  **Clinician-note outcome timing extraction**: Identify outcome mentions in clinician notes, normalize event dates and clinically described time windows, distinguish historical, current, and future outcomes, retain uncertainty labels, and emit evidence spans suitable for registry or real-world-data workflows.
10. **Outcome temporal anchoring from clinician notes**: Identify outcome mentions, normalize explicit dates and relative intervals, distinguish current versus historical events, attach evidence spans to each outcome-timing assertion, and flag uncertain timing for review.
11. **Criterion-level rare-neoplasm registry abstraction**: Use LLMs to abstract registry variables from oncology notes for rare neoplasms, preserve criterion-level provenance for each extracted value, handle sparse disease-specific vocabularies such as bone sarcoma terminology, and validate extracted variables against manual abstraction before downstream real-world-data use.
12. **Rare-neoplasm registry workflow fields**: For rare-neoplasm real-world-data extraction, define registry fields for tumor subtype, treatment lines, response, progression, and follow-up dates before running LLM extraction; require uncertainty labels for extracted values and manual QA before releasing sparse rare cancer cohort datasets.
13. **Rare-neoplasm clinician-note RWD extraction mode**: Use LLM-assisted abstraction from clinician notes for sparse rare-neoplasm cohorts such as bone sarcoma, predefine registry-style fields and allowed values, validate temporal consistency across diagnosis, treatment, response, progression, recurrence, and follow-up dates, and route ambiguous or low-evidence abstractions to manual adjudication before registry use.
14. **Real-world oncology abstraction audit workflow**: For rare-neoplasm clinical notes, use LLMs to extract registry variables, temporal outcomes, treatment lines, and evidence snippets, then run audit sampling against source-note snippets and send uncertain, discordant, or sampled fields to human adjudication before registry release.
15. **Rare-neoplasm clinician-note RWD extraction pattern**: For oncology real-world-data studies in rare neoplasms, start from registry variable dictionaries, normalize tumor-specific entities such as bone sarcoma terms to study vocabularies, attach temporal anchors to diagnosis, treatment, response, progression, recurrence, and follow-up events, emit missingness flags for absent or indeterminate variables, run human abstraction audit on extracted fields and evidence spans, and export structured registry-ready tables for downstream oncology RWD analysis.
16. **Clinician-note outcome identification and timing validation**: Use LLM-assisted extraction to identify patient outcomes in clinician notes, anchor each outcome to event time, handle negated or uncertain outcome mentions, reconcile outcome status across longitudinal notes, and validate structured outputs against chart-reviewed labels before downstream use.
17. **LLM rare-neoplasm registry abstraction pattern**: For rare-neoplasm RWD collection from clinician notes, extract registry fields with bone sarcoma example variables such as tumor subtype, anatomic site, stage or extent, treatment lines, response, progression, recurrence, and follow-up dates; attach source-span evidence to each field, emit uncertainty and missingness flags, route low-confidence or discordant fields to adjudication queues, and validate extracted registry values against manual abstraction before analysis.
18. **Clinician-note outcome event timing aggregation**: Extract patient outcome events from clinician notes with timing normalization, source-span evidence, and uncertainty labels; aggregate event status and timing longitudinally at the patient level; and validate extracted event/timing outputs against chart review before registry or real-world-evidence use.
19. **Bone sarcoma rare-neoplasm RWD extraction validation**: For registry-oriented rare-neoplasm extraction, use bone sarcoma as the exemplar for predefined entity schemas, temporal anchors, and outcome/event tables; route ambiguous, discordant, or clinically critical fields through adjudication loops; and validate precision and recall against manually abstracted charts before downstream registry or real-world-data analysis.
20. **Patient outcome extraction with temporal anchoring**: Identify outcome mentions in clinician notes, normalize event timing, classify outcome status and uncertainty, link each structured assertion to source-note evidence spans, reconcile timing across longitudinal clinical datasets, and validate extracted outcome/timing labels against chart-review labels before downstream use.
21. **Rare-neoplasm real-world-data extraction from clinician notes**: Define registry variables before abstraction, extract treatment and outcome fields from clinician notes, handle sparse bone sarcoma examples with explicit missingness and uncertainty labels, and require abstraction QA with clinician adjudication for ambiguous, discordant, or clinically critical fields.
22. **Patient outcome timing tables for RWE**: Extract patient outcomes from clinician notes with temporal anchoring, normalize event times from explicit and relative note context, assign uncertainty labels, route ambiguous outcome status or timing to adjudication queues, and emit longitudinal outcome tables for real-world evidence workflows.

## Workflow

1.  **Input**: A string of clinical text or a text file.
2.  **Process**: Tokenizes and matches against patterns/dictionaries.
3.  **Output**: JSON list of entities with spans and types.

## Example Usage

**User**: "Extract entities from this note."

**Agent Action**:
```bash
python3 Skills/Clinical/Clinical_NLP/entity_extractor.py \
    --text "Patient has diabetes type 2. Prescribed Metformin 500mg. No chest pain." \
    --output entities.json
```

```

## References

*   https://pubmed.ncbi.nlm.nih.gov/42021926/
*   https://pubmed.ncbi.nlm.nih.gov/41886942/

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
