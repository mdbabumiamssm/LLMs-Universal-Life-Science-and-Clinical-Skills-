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
name: 'ontology-constrained-biomedical-metadata-standardization'
description: 'Standardize legacy biomedical metadata against ontology-constrained templates using verified term mappings, preserved provenance, ambiguity review, and curated-reference validation.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Ontology-Constrained Biomedical Metadata Standardization

## Overview

Transform legacy biomedical metadata into a target schema while grounding controlled values in authoritative terminology. The related full-methods preprint describes runtime retrieval of CEDAR templates and BioPortal terms; this skill adds explicit provenance, review, and release checks for reusable curation workflows.

## When to Use This Skill

- Migrating heterogeneous sample, assay, or experimental metadata to a community template.
- Resolving free-text values to terms permitted by a specified ontology or branch.
- Auditing historical mappings after a schema or ontology release changes.
- Comparing proposed standardization with expert-curated mappings before deployment.

## Core Capabilities

The source-grounded approach below follows Sections 2.1–2.3 of the [full-methods preprint](https://arxiv.org/pdf/2604.08552): retrieve the complete template, map fields using their meanings and values, revisit unused source fields, query constrained terminology, and retain unresolved information in a log. The versioning, review policies, and acceptance checks below are operational recommendations, not reported experimental results.

1. **Define scope and select constraints.** Start with a bounded pilot that can finish within 15 minutes; record the selected records and fields. Read requiredness, cardinality, datatypes, enumerations, and ontology restrictions from the target specification. Prefer its mandated terminology. If none is mandated, propose one based on domain coverage, granularity, licensing, and maintained identifiers; document that choice before applying it.

2. **Preserve source evidence.** Keep original records immutable and assign stable record identifiers. Retain source field paths, raw values, and source hashes. Store normalized search text separately so spelling or whitespace cleanup cannot erase evidence. Distinguish absent, unknown, and explicitly inapplicable values according to the target schema.

3. **Map fields and retrieve candidates.** Use template definitions and record context to identify correspondences, then examine unassigned fields for missed matches. Query the permitted ontology or branch for controlled values; select enumerated values only from the allowed list. Preserve unconstrained content except for justified formatting or datatype conversion. Do not invent missing experimental facts.

4. **Enforce term validity.** Retrieve candidate identifiers, preferred labels, definitions, and relevant synonyms. Independently verify identifier existence, ontology membership, branch membership, and deprecation status against the selected release. Record whether a branch restriction includes its root. Never accept a plausible label or a model-generated identifier without verification. Use the target's required label or identifier representation, retaining both in the audit record.

5. **Resolve ambiguity conservatively.** Require supporting context for ambiguous abbreviations or more specific concepts. Flag competing candidates, conflicting source fields, obsolete terms without an unambiguous replacement, and broader or narrower mappings for review. Record alternatives and a concise evidence-based rationale. Model confidence alone is not an acceptance criterion. Leave unresolved target values empty where permitted; otherwise mark the record invalid and retain its raw value in the audit output.

6. **Make decisions reproducible.** Pin template and ontology versions where available; otherwise capture retrieval time and response hashes. Record terminology endpoints, query parameters, model and prompt versions, mapping policy, and reviewer decisions. Reuse cached results only under matching constraints and versions. On service failure, use an identified compatible snapshot or mark lookup failure; do not substitute model memory for authoritative evidence.

7. **Validate and report.** Check schema structure, required fields, cardinality, datatype, permitted values, and term restrictions independently of generation. Compare a held-out curated mapping set using a declared equality rule: identifiers for concept agreement and exact labels when required by the output schema. Report exact matches, substitutions, missing values, unsupported insertions, and review counts with denominators, stratified by field and unique source value. Keep schema compliance separate from semantic agreement. If curated mappings are unavailable, report semantic validation as pending rather than claiming accuracy.

## Inputs / Outputs

**Inputs**

- Legacy CSV, TSV, or JSON records with stable IDs and relevant contextual fields.
- Target schema or CEDAR template identifier, including its version and field constraints.
- Approved terminology access or versioned snapshots; optional curated mapping set and acceptance thresholds.

**Outputs**

- Standardized records in the requested schema, with validity and completion status reported separately.
- Mapping audit containing `record_id`, `source_field`, `raw_value`, `target_field`, `term_id`, `preferred_label`, `ontology_version`, `template_version`, `evidence`, `status`, and `review_decision`.
- Review queue with candidate alternatives and reasons such as `ambiguous`, `no_match`, `deprecated`, `lookup_failed`, or `constraint_violation`.
- Validation report with scope, processed and remaining counts, schema failures, curated-comparison results, and unresolved issues.

**Completion gate:** Every processed value has an auditable disposition, every accepted controlled term passes verification, and released records satisfy the target schema. Return a clearly marked partial pilot if the time limit is reached; unresolved required fields block release of the affected records. Never label an entire corpus complete based on a pilot or silently replace original metadata.

## References

- [Supplied PubMed finding: Automated standardization of legacy biomedical metadata using an ontology-constrained LLM agent, PMID 42918280](https://pubmed.ncbi.nlm.nih.gov/42918280/). The supplied journal/date metadata were not independently verified because the record was inaccessible during authoring.
- [Related same-title arXiv preprint, arXiv:2604.08552](https://arxiv.org/abs/2604.08552), [full methods](https://arxiv.org/pdf/2604.08552), Sections 2.1–2.3. Used for methodological grounding; do not assume preprint and journal versions are identical. No benchmark performance is promised by this skill.
