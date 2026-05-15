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
5.  **Outcome extraction with temporal anchoring**: Identify patient outcome mentions in clinician notes, normalize outcome events and event timing, label temporal relations and current/past/future outcome status, infer explicit or relative dates/times plus event onset and resolution windows, distinguish baseline from follow-up events, classify uncertainty and negation, validate extracted outcomes against chart-review labels for RWE workflows, run longitudinal consistency checks across notes, retain audit-ready source-note evidence spans for each extracted outcome, and generate downstream registry/RWE-ready tables with outcome status, event timing, temporal anchor, uncertainty class, negation, provenance, and audit trails.
6.  **Sparse oncology registry extraction**: Extract entities and outcomes from oncology notes for rare neoplasms such as bone sarcoma, map each abstracted value to registry fields, anchor findings to explicit or relative clinical timelines, route missing or uncertain values to human validation queues, and retain audit-ready provenance linking extracted values to source notes, evidence spans, and validation status.

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
