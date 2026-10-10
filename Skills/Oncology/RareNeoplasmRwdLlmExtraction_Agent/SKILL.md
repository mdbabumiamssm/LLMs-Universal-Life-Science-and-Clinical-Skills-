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
name: 'rare-neoplasm-rwd-llm-extraction'
description: 'Extract provenance-linked, temporally normalized real-world oncology data from fragmented records for rare neoplasms, including bone sarcomas, with ontology mapping and human review.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Rare Neoplasm Real-World Data LLM Extraction

## Overview

Extract structured real-world data from oncology notes, pathology reports, imaging narratives, treatment records, and registry documents for rare neoplasms. Use a schema-first, evidence-linked workflow to address sparse records, terminology variation, uncertain timelines, and the need for expert adjudication without treating model output as verified clinical truth.

## When to Use This Skill

- Build or update a research registry for a rare tumor cohort.
- Abstract bone sarcoma or other rare-neoplasm variables from unstructured clinical records.
- Harmonize diagnoses, anatomic sites, stages, biomarkers, procedures, therapies, and outcomes across institutions.
- Normalize longitudinal oncology events into a patient-level timeline.
- Map local or historical tumor terms to controlled oncology vocabularies.
- Create provenance-linked candidate data for review by trained abstractors or disease experts.
- Evaluate an LLM-assisted extraction pipeline against a manually curated reference dataset.
- Audit missingness, contradictions, uncertainty, privacy risk, or extraction drift.

## Core Capabilities

1. **Schema-first extraction**
   Define the cohort, unit of analysis, variable dictionary, data types, permitted values, cardinality, and required provenance before processing records. Reject fields that do not conform to the approved schema.

2. **Rare-tumor terminology normalization**
   Preserve the source term while mapping diagnoses, morphology, behavior, grade, and anatomic site to the project-approved versions of resources such as ICD-O, SNOMED CT, NCI Thesaurus, or the applicable WHO tumor classification. Mark ambiguous mappings for review rather than forcing a code.

3. **Document-aware evidence extraction**
   Distinguish pathology, radiology, operative, systemic therapy, radiation, tumor board, and follow-up evidence. Prefer definitive source documents for the fact they establish, and retain exact evidence spans with document identifiers and offsets when available.

4. **Temporal normalization**
   Resolve explicit dates, relative expressions, treatment cycles, specimen dates, and retrospective statements into ISO 8601 values where supported. Keep event date, documentation date, precision, and temporal basis separate.

5. **Longitudinal event construction**
   Represent diagnosis, biopsy, staging, treatment, response, recurrence, progression, metastasis, surveillance, and death as distinct events. Link related events without collapsing clinically meaningful changes over time.

6. **Negation and context handling**
   Separate confirmed findings from suspected, ruled-out, historical, family-history, planned, canceled, and hypothetical statements. Track experiencer and assertion status for every extracted clinical fact.

7. **Missingness and contradiction management**
   Distinguish absent documentation, not assessed, not applicable, unknown, illegible, and explicitly negative values. Preserve conflicting statements as separate candidates until a documented precedence rule or human adjudication resolves them.

8. **Confidence and escalation**
   Assign confidence categories using evidence quality, source authority, mapping ambiguity, temporal certainty, and cross-document agreement. Route low-confidence, contradictory, unsupported, or clinically consequential fields to human review; do not present raw model probabilities as calibrated confidence without validation.

9. **Privacy-preserving processing**
   Apply minimum-necessary access, approved storage and transfer controls, de-identification or limited-data-set rules, access logging, and retention requirements. Never place protected health information in unapproved prompts, logs, examples, or external services.

10. **Registry-based validation**
    Compare extracted fields with a blinded, manually curated reference set using field-appropriate measures. Analyze errors by tumor subtype, document type, institution, time period, missingness pattern, and confidence category before deployment or reuse.

11. **Bone sarcoma validation case**
    Use the 2026 bone sarcoma rare-neoplasm real-world data collection example as a validation pattern for LLM-assisted real-world data collection with schema-first extraction, temporal normalization, oncology ontology mapping, source provenance, privacy controls, clinician adjudication, registry-readiness checks, and error analysis in sparse, fragmented oncology records.

12. **Registry-ready bone sarcoma abstraction**
    For bone sarcoma and analogous rare-neoplasm cohorts, define variables before extraction, anchor each value to clinical time and source spans, normalize outputs to registry-ready tables and oncology ontologies, route uncertain or unsupported fields through adjudication, and validate the resulting dataset against manually abstracted oncology records.

13. **Expert-abstraction validation loop**
    Use the bone sarcoma real-world data collection example to keep rare-neoplasm extraction registry-ready from the start: capture schema-defined variables only, anchor each candidate value to event time and source provenance, normalize source and standard terms through approved ontologies, route ambiguous or contradictory candidates into adjudication queues, and validate candidate tables against expert abstraction before reuse.

14. **Sparse-record schema hardening**
    Use the bone sarcoma rare-neoplasm real-world data collection study to require versioned registry variable definitions before extraction, keep temporal normalization, oncology ontology mapping, and provenance capture as first-class fields, route ambiguous sparse-record candidates into adjudication queues, and report field-appropriate validation metrics without extrapolating beyond the evaluated cohort.

15. **Sarcoma-specific fragmented-note controls**
    For bone sarcoma cohorts, define sarcoma-specific registry variables before extraction, including histology, primary bone site, grade, specimen or procedure, local recurrence, metastasis, surgery, systemic therapy, radiation, response, progression, survival, and last follow-up when approved by the study schema. Extract these as temporally ordered event candidates with ontology mappings, evidence spans, source metadata, registry-ready validation checks, and adjudication triggers for unsupported, contradictory, or fragmented oncology-note evidence.

16. **Fragmented-note validation pattern**
    Use the bone sarcoma rare-neoplasm RWD example as a validation pattern for schema-first variable extraction from fragmented oncology notes, requiring temporal normalization, registry-ready provenance, approved ontology mapping, and adjudication workflows for ambiguous, contradictory, or unsupported candidates.

17. **Registry-ready longitudinal outcome abstraction**
    For sparse bone sarcoma records, extract longitudinal outcome candidates only when tied to source provenance, normalized clinical time, and approved ontology mappings; queue uncertain rare-neoplasm variables for human adjudication before accepting them into registry-ready tables.

18. **Rare-neoplasm chart-abstraction validation case**
    Treat the 2026 bone sarcoma real-world data collection example as a validation case for rare-neoplasm chart abstraction: require schema-first variable extraction, explicit temporality fields, ontology-normalized source and standard terms, provenance for every candidate value, registry-readiness checks before export, adjudication workflow states for uncertain candidates, and field-appropriate performance and error metrics tied to the evaluated cohort and schema version.

19. **Bone sarcoma RWD extraction template**
    Use the 2026 rare-neoplasm bone sarcoma example as a concrete template for LLM-assisted registry abstraction: begin with versioned, registry-ready variable schemas; extract one candidate value per evidence occurrence; normalize clinical dates, relative timing, and event order into explicit temporal fields; map source terms to approved oncology ontologies while preserving source wording; capture document, section, span, rule, model, and configuration provenance; queue ambiguous, contradictory, missing, or unsupported candidates for adjudication; and validate accepted records against manually curated registry data before reuse.

20. **Bone sarcoma manual-abstraction template**
    Apply the PubMed 42021926 bone sarcoma rare-neoplasm RWD example as a concrete extraction template: define schema-first variables, normalize temporality before aggregation, preserve registry provenance for each candidate value, map source and normalized terms to approved oncology ontologies, run privacy checks before prompt or log use, require human adjudication for uncertain candidates, and validate accepted outputs against manually abstracted records.

21. **Bone sarcoma registry-ready extraction pattern**
    Use the bone sarcoma rare-neoplasm example to build registry-ready RWD datasets by extracting only schema-defined variables, normalizing event timing before aggregation, mapping source terms to approved oncology ontologies, preserving document-level provenance, enforcing privacy handling before prompt or log use, and requiring clinician adjudication before accepting uncertain, contradictory, or unsupported candidate values.

22. **Bone sarcoma schema-to-registry workflow**
    Apply the PubMed 42021926 bone sarcoma rare-neoplasm RWD example as a concrete workflow: lock the extraction schema before processing records, extract candidate values with document and evidence-span provenance, normalize dates and event order before aggregation, map source and normalized terms to approved oncology ontologies, route uncertain, contradictory, missing, or unsupported candidates into adjudication queues, enforce privacy controls for prompts, logs, storage, and transfer, and run registry-ready schema and provenance validation before export.

23. **Bone sarcoma schema-first RWD capture**
    Use the PubMed 42021926 bone sarcoma rare-neoplasm paper as a concrete RWD extraction pattern: capture only schema-first variables, normalize temporal fields before aggregation, preserve candidate-level provenance, map source terminology to approved oncology ontologies, validate accepted fields against manual abstraction, and run registry-readiness checks before export.

24. **Bone sarcoma registry abstraction pattern**
    Apply the PubMed 42021926 bone sarcoma example as a concrete rare-neoplasm RWD extraction pattern: define registry-ready variables, anchor each candidate value to the relevant clinical event time, map source terms to approved oncology ontologies, preserve minimal provenance snippets with document context, route uncertain candidates through adjudication, and validate accepted outputs against manually abstracted clinical records.

25. **Bone sarcoma validation workflow case**
    Treat the PubMed 42021926 bone sarcoma rare-neoplasm RWD example as a validation case for schema-first extraction, temporal normalization, oncology ontology mapping, candidate-level provenance capture, privacy review before prompt, log, storage, or transfer use, and adjudication workflow states before registry export.

26. **Bone sarcoma reference registry handoff**
    Use the PubMed 42021926 bone sarcoma rare-neoplasm RWD example as a reference workflow for schema-first variable collection, temporal normalization, oncology ontology mapping, candidate-level provenance capture, adjudication, and privacy-preserving registry handoff.

27. **Clinician-adjudicated registry-field capture**
    Use the PubMed 42021926 bone sarcoma rare-neoplasm RWD example as a validation pattern for schema-first variable capture, temporal normalization, oncology ontology mapping, audit trails, and clinician adjudication of LLM-extracted registry fields.

28. **Fragmented oncology-record worked pattern**
    Apply the 2026 bone sarcoma rare-neoplasm RWD workflow as a worked pattern for LLM-assisted variable extraction from fragmented oncology records: normalize temporality, map source terms to approved oncology ontologies, preserve registry-ready provenance for every candidate value, route uncertain outputs through adjudication, and validate accepted variables against manually curated reference data before reuse.

29. **Bone sarcoma registry extraction template**
    Use PubMed 42021926 as a concrete template for bone sarcoma and analogous rare-neoplasm RWD abstraction: predefine registry-ready variables, normalize event dates and relative timing into explicit temporal fields, map diagnosis, site, morphology, treatment, response, progression, recurrence, metastasis, and outcome terms to approved oncology ontologies, preserve candidate-level provenance fields for source document, section, evidence span, offsets, extraction rule, model, configuration, and schema version, assign records to validation samples before performance review, and require human adjudication before accepting uncertain, contradictory, unsupported, or clinically consequential candidates.

30. **Bone sarcoma validation case**
    Treat PubMed 42021926, the 2026 bone sarcoma rare-neoplasm real-world data collection example, as a concrete validation case for schema-first LLM extraction, temporal normalization, oncology ontology mapping, provenance capture, manual adjudication, and registry-ready quality metrics without inventing benchmarks beyond the evaluated study context.

31. **Bone sarcoma schema-first extraction pattern**
    Apply PubMed 42021926 as a concrete bone sarcoma real-world data extraction pattern: define variables in a versioned schema before extraction, normalize temporality at the candidate and event levels before aggregation, capture registry-grade provenance for every candidate value, map source terms and normalized values to approved oncology ontologies, route ambiguous or unsupported candidates into adjudication queues, and validate accepted outputs against manual abstraction before registry reuse.

32. **Bone sarcoma worked use case**
    Use PubMed 42021926 as a worked use case for bone sarcoma real-world data extraction: capture schema-first variables, normalize event dates and relative timing, map oncology terminology to approved ontologies, preserve candidate-level provenance, enforce privacy safeguards for prompts, logs, storage, and transfer, route uncertain or unsupported candidates through adjudication, and validate registry-readiness before export without inventing benchmarks beyond the cited finding.

33. **Registry-quality bone sarcoma data-element validation**
    Apply the PubMed 42021926 bone sarcoma rare-neoplasm RWD collection example as a schema-first extraction pattern: anchor each candidate value to clinical time, perform oncology ontology normalization while preserving source wording, retain provenance fields for document context and evidence spans, route uncertain or conflicting candidates through manual adjudication, and validate accepted outputs against registry-quality data elements before reuse.

34. **Bone sarcoma registry-ready field extraction**
    Use the PubMed 42021926 bone sarcoma RWD finding to require schema-first variable definitions, temporal normalization before aggregation, approved oncology ontology mapping, candidate-level provenance capture, adjudication queues for ambiguous or unsupported values, and validation against registry-ready fields before export.

35. **Rare-neoplasm registry quality controls**
    For bone sarcoma and analogous rare-neoplasm registries, keep variable definitions schema-first, normalize temporal fields before aggregation, map source terminology to approved ontologies, capture provenance for each candidate value, report field-appropriate extraction quality metrics, enforce privacy controls for prompts, logs, storage, and transfer, and require adjudication before accepting uncertain, contradictory, or unsupported outputs.

36. **Fragmented rare-cancer schema-first example**
    Treat PubMed 42021926, the 2026 bone sarcoma rare-neoplasm real-world data collection paper, as a concrete example for fragmented rare cancer records: define registry variables before LLM extraction, normalize dates and event order, map oncology terms to approved ontologies while preserving source wording, capture document and evidence-span provenance, route ambiguous candidates to adjudication, and run registry-readiness checks before export.

37. **Schema-first rare-neoplasm RWD strengthening**
    Use the PubMed 42021926 bone sarcoma example to strengthen rare-neoplasm real-world data extraction by requiring tumor entity normalization, temporal anchoring for treatment and outcome variables, registry-ready variable definitions before extraction, adjudication workflow states for uncertain candidates, and candidate-level provenance for fragmented clinical records.

38. **Bone sarcoma validation pattern**
    Use the PubMed 42021926 bone sarcoma rare-neoplasm real-world-data extraction example as a validation pattern for registry-ready outputs: define variables schema-first, normalize temporal context, map oncology terms to approved ontologies, capture source provenance, complete privacy review before prompt, log, storage, or transfer use, and require human adjudication for uncertain or unsupported candidates.

39. **Clinician-note bone sarcoma extraction pattern**
    Apply PubMed 42021926 as a concrete pattern for schema-first extraction from clinician notes in bone sarcoma and analogous rare neoplasms: normalize temporal events before aggregation, map source terms to approved oncology ontologies while retaining original wording, route ambiguous or unsupported candidates into adjudication queues, and require registry-quality provenance checks before accepting values.

40. **Bone sarcoma registry-variable validation pattern**
    Use PubMed 42021926 as a concrete rare-neoplasm RWD collection pattern for schema-first LLM extraction: predefine registry-quality variables, normalize temporal context before aggregation, map source terminology to approved oncology ontologies, capture provenance for every candidate value, route ambiguous or unsupported candidates through adjudication, and validate accepted fields against registry-quality variables before reuse.

41. **Bone sarcoma manual-validation guardrail**
    Use the PubMed 42021926 bone sarcoma rare-neoplasm study to reinforce schema-first RWD extraction: map rare tumor source terms to approved ontologies, normalize dates and relative event timing, capture provenance for every candidate value, run privacy checks before prompt, log, storage, or transfer use, route uncertain candidates to adjudication queues, and validate accepted fields against manual abstraction before registry reuse.

42. **Bone sarcoma registry-quality RWD workflow**
    Refresh rare-neoplasm RWD extraction workflows using the PubMed 42021926 bone sarcoma example: start from a schema-first variable list, normalize temporality before aggregation, map source terminology to approved oncology ontologies, preserve candidate-level provenance, enforce privacy controls for prompts, logs, storage, and transfer, route uncertain or conflicting outputs through adjudication, and report registry-quality validation metrics tied to the evaluated schema and cohort.

43. **Schema-first source-note validation**
    Use the 2026 bone sarcoma rare-neoplasm paper to strengthen schema-first RWD extraction by validating registry-ready variables against source-note provenance, normalized temporal fields, approved ontology mappings, privacy controls, and adjudication workflow states before accepting LLM-generated candidates.

44. **Bone sarcoma RWD validation case**
    Treat PubMed 42021926 as a validation case for rare-neoplasm RWD extraction: perform schema-first variable extraction, temporal normalization, approved oncology ontology mapping, candidate-level provenance capture, privacy checks before prompt, log, storage, or transfer use, adjudication of uncertain candidates, and registry-readiness metric reporting tied to the evaluated schema and cohort without adding benchmarks not present in the finding.

45. **Fragmented oncology record schema controls**
    Use the bone sarcoma rare-neoplasm example to strengthen extraction from fragmented oncology records by requiring schema-defined treatment and outcome variables, normalized event timing before aggregation, approved ontology mappings with source terms retained, provenance for every candidate value, adjudication queues for ambiguous or conflicting candidates, and registry-ready validation metrics tied to the evaluated schema and cohort.

46. **Bone sarcoma accelerated RWD collection example**
    Apply the PubMed 42021926 bone sarcoma example to accelerate rare-neoplasm real-world data collection by extracting only schema-first variables, anchoring candidate values to temporal clinical events, tracking registry completeness metrics against the approved schema, completing privacy review before prompt, log, storage, or transfer use, and requiring human adjudication for ambiguous entities before registry acceptance.

47. **Bone sarcoma validation case with registry mapping**
    Treat PubMed 42021926 as a concrete validation case for rare-neoplasm real-world data collection: perform schema-first extraction, normalize temporal fields before aggregation, map candidates to approved registry variables and oncology ontology terms, report missingness using the project schema, route uncertain, contradictory, missing, or unsupported values to adjudication queues, and preserve privacy-protective provenance for source document context.

48. **Bone sarcoma manually abstracted registry-field check**
    Use PubMed 42021926 as a bone sarcoma rare-neoplasm RWD extraction example: capture schema-defined variables first, normalize dates and event order, map source terms to approved oncology ontologies, link each candidate value to provenance, route uncertain candidates to clinician adjudication, and validate accepted outputs against manually abstracted registry fields.

49. **Bone sarcoma registry-readiness example**
    Use PubMed 42021926 as a rare-neoplasm RWD extraction example for bone sarcoma: capture only schema-first variables, normalize temporal values and event order, map extracted terms to approved oncology ontologies while preserving source wording, retain provenance fields for each candidate value, route ambiguous or unsupported values through adjudication, and run registry-readiness checks before export.

50. **Bone sarcoma fragmented-note RWD collection**
    Apply PubMed 42021926 as a bone sarcoma real-world data collection pattern for fragmented clinical notes: extract only schema-defined diagnosis, treatment, and outcome events; normalize event temporality before aggregation; map rare-neoplasm terminology to approved ontologies; retain uncertainty flags, privacy controls, and clinician adjudication before accepting records into registry-quality datasets.

51. **Tumor-specific schema-first RWD extraction**
    Use the PubMed 42021926 bone sarcoma rare-neoplasm example to strengthen schema-first extraction by defining tumor-specific variable dictionaries before processing, anchoring diagnosis-treatment-outcome timelines to explicit clinical events, preserving source provenance for every candidate value, running registry-readiness checks before export, and routing sparse or fragmented-record candidates through adjudication before acceptance.

52. **Bone sarcoma sparse-record validation case**
    Treat the PubMed 42021926 bone sarcoma rare-neoplasm real-world data collection example as a validation case for sparse rare-cancer records: require schema-first extraction, temporal normalization, oncology ontology mapping, source provenance, adjudication workflow states, privacy handling for prompts, logs, storage, and transfer, and registry-readiness checks before accepting or exporting candidate records.

53. **Bone sarcoma registry deployment example**
    Operationalize PubMed 42021926 as a bone-sarcoma deployment example by versioning extraction schemas; normalizing diagnosis, treatment, recurrence, progression, metastasis, follow-up, and outcome observations into longitudinal events; encoding absent documentation, not assessed, not applicable, unknown, and explicit negatives as distinct missingness states; retaining record-level source, document, evidence-span, schema, model, and adjudication provenance; and validating a stratified manual-adjudication sample that includes uncertain, contradictory, missing, and randomly selected accepted records. Report field-level counts with precision, recall, F1, exact-match or agreement as appropriate, missingness concordance, temporal-event accuracy, adjudication rate, and confidence intervals where sample size permits; do not claim performance beyond the evaluated rare-tumor registry cohort, schema, or source systems.

## Workflow

1. **Confirm governance and purpose**
   Record the research question, authorized cohort, permitted data environment, privacy constraints, intended users, and whether outputs are research-only or eligible for downstream operational use.

2. **Specify the extraction schema**
   For each field, define:

   - Canonical name and clinical meaning.
   - Data type, allowed values, units, and cardinality.
   - Inclusion, exclusion, and precedence rules.
   - Accepted source document types.
   - Ontology and version, if applicable.
   - Temporal representation and precision.
   - Required evidence and adjudication conditions.

3. **Prepare records**
   Inventory documents, remove exact duplicates, retain document identifiers and timestamps, identify document type, and preserve section boundaries. Do not silently merge records from different patients or encounters.

4. **Extract candidate facts**
   Produce one candidate per fact and evidence occurrence. Include the original text span, normalized value, assertion status, temporality, source metadata, mapping details, and confidence rationale.

5. **Normalize and reconcile**
   Apply deterministic normalization before free-form inference. Use documented source-precedence rules, retain unresolved conflicts, and avoid inferring unstated stage, response, progression, or treatment intent.

6. **Validate each record**
   Check schema conformance, value ranges, unit consistency, impossible dates, event ordering, duplicate events, unsupported mappings, missing provenance, and contradictions. Fail closed when a required evidence link is absent.

7. **Queue human adjudication**
   Present reviewers with the candidate value, surrounding context, source document, alternatives, reason for escalation, and an explicit accept-correct-reject action. Preserve reviewer identity, timestamp, and rationale according to governance policy.

8. **Evaluate and monitor**
   Split development and evaluation records at the patient level. Report per-field performance and error categories without claiming generalizability beyond the evaluated cohort. Revalidate after prompt, model, schema, ontology, source-system, or workflow changes.

## Inputs / Outputs

### Inputs

- Authorized clinical text or document extracts with stable patient, document, and encounter identifiers.
- Cohort definition and rare-neoplasm inclusion or exclusion criteria.
- Versioned extraction schema and data dictionary.
- Project-approved ontology versions and local terminology crosswalks.
- Source-precedence, confidence, escalation, and adjudication rules.
- Privacy, security, retention, and data-use requirements.
- Optional manually curated registry records for validation.

### Outputs

- Schema-valid patient, tumor, specimen, treatment, and outcome tables or equivalent structured records.
- A normalized longitudinal event table with date precision and temporal provenance.
- Original source terms plus ontology identifiers, labels, versions, and mapping status.
- Evidence spans linked to document identifiers, sections, and offsets when available.
- Assertion, missingness, contradiction, confidence, and adjudication fields.
- A human-review queue for unresolved or policy-triggered cases.
- Validation and error-analysis summaries tied to the evaluated cohort and schema version.
- An audit manifest containing model or extraction configuration, schema version, ontology versions, processing time, and quality-control status.

### Minimum Candidate Record

```json
{
  "patient_id": "authorized-pseudonymous-id",
  "field_name": "histologic_diagnosis",
  "source_value": "source wording",
  "normalized_value": "normalized label or null",
  "ontology": {
    "system": "project-approved ontology",
    "version": "version",
    "code": "code or null",
    "mapping_status": "exact|broader|narrower|ambiguous|unmapped"
  },
  "assertion": "confirmed|suspected|negated|historical|planned",
  "event_date": "YYYY-MM-DD or null",
  "date_precision": "day|month|year|interval|unknown",
  "document_id": "stable-document-id",
  "evidence_span": "minimum sufficient source text",
  "evidence_location": "section and offsets when available",
  "missingness": "present|not_documented|not_assessed|not_applicable|unknown",
  "confidence": "high|medium|low",
  "confidence_rationale": "brief evidence-based rationale",
  "review_status": "not_required|pending|accepted|corrected|rejected"
}
```

## References

- Teterycz P, Rynkun S, Szostakowski B, Wągrodzki M, Rutkowski P. “Accelerating real-world data collection using large language models in rare neoplasms: a bone sarcoma example.” *ESMO Real World Data and Digital Oncology*. 2026 Jun. [PubMed PMID: 42021926](https://pubmed.ncbi.nlm.nih.gov/42021926/)
- Source URL: https://pubmed.ncbi.nlm.nih.gov/42021926/
