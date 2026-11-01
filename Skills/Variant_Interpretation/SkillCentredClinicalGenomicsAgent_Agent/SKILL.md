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
name: 'skill-centred-clinical-genomics-agent'
description: 'Coordinate modular evidence retrieval and versioned, traceable genomic interpretation for research review of variants, rare disease findings, and molecular oncology evidence.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Skill-Centred Clinical Genomics Agent

## Overview

This skill organizes research interpretation of genomic findings into explicit evidence tasks with reproducible inputs, source versions, and reviewable conclusions. It adapts the skill-centred approach described in [the ClinGeX preprint](https://arxiv.org/abs/2610.40556v1) to produce an evidence dossier for expert review. It is an independent workflow specification, not the original software or a clinically validated diagnostic system.

## When to Use This Skill

- Assemble a criterion-level research assessment of a specified variant.
- Investigate whether candidate variants plausibly explain rare disease findings.
- Separate molecular oncology evidence, biological significance, and context-specific actionability.
- Reassess an interpretation after a database, guideline, or publication update.
- Audit source attribution, evidence conflicts, missing prerequisites, or interpretation reproducibility.

## Core Capabilities

1. **Scope and identity control.** Establish the exact analytical question and verify variant, transcript, genome assembly, disease, and sample context before attaching evidence.
2. **Modular execution.** Select available guide, search, and analysis operations; represent prerequisites explicitly and execute only when required inputs are valid.
3. **Versioned evidence retrieval.** Record source releases, retrieval dates, query parameters, and record identifiers so later changes can be explained.
4. **Traceable interpretation.** Link each proposed criterion or conclusion to evidence, a specific rule, and any assumptions or unresolved conflicts.
5. **Expert review and research evaluation.** Produce an auditable draft with review gates; keep successful workflow execution separate from classification correctness or clinical benefit.

### Method grounding and limits

ClinGeX describes 105 curated skills, task-specific retrieval, dependency closure, and progressive instruction loading. Its development combined resource screening, expert selection, iterative testing, and a graph separating relatedness from prerequisites. The original code was not public at publication; this file does not supply that library.

The reported benchmark used 223 temporally held-out cases and achieved 71.7% macro-averaged task concordance versus 45.7% for the strongest comparator. The counterbalanced collaboration study involved 45 professionals and 135 cases; the exploratory assessment collected 96 self-selected episodes from 11 professionals. Concordance measures agreement with reference interpretations, not patient benefit. Reported timing and adoption are not independent clinical validation; exploratory use was non-interventional. Scenario and centre were linked, limiting generalization. These findings motivate the safeguards below, not a performance guarantee. See [Methods, evaluation, and limitations](https://arxiv.org/html/2610.40556v1).

### Operational workflow

The following implementation choices define this research workflow; they are not claimed to reproduce the paper's software or experimental configuration.

**1. Establish a bounded question and clock.**

Record start time and choose variant classification, gene–disease assessment, phenotype integration, or oncology evidence assessment. Treat 15 minutes as the time budget for a bounded dossier, not a deadline for forcing a classification. For a large case set, process an explicitly identified subset and list the remainder.

Use de-identified case material. Keep patient-level files in the approved environment; public searches should use only the minimum non-identifying entities needed. If required data cannot be used safely or are unavailable, return a blocked or partial dossier with the reason.

**2. Validate identities and context.**

Capture the supplied representation and its normalized equivalent, assembly, genomic coordinates and alleles, transcript accession with version, gene identifier, and relevant zygosity or allele fraction. Check consistency across HGVS and genomic representations; never silently assume an assembly or transcript.

For rare disease questions, record phenotype terms, onset, family structure, inheritance hypothesis, and available segregation data. For oncology, record tumour type, specimen, assay limitations, treatment setting, and whether the variant's germline or somatic origin is established. Distinguish absent findings from unassessed findings. Flag uncertain text or pedigree extraction for confirmation.

**3. Select rules and available operations.**

Retrieve the applicable authoritative guideline and any relevant gene- or disease-specific specification. Record its title, version/date, scope, and exact section used. For a historical analysis, freeze the requested evidence cutoff; for a current analysis, check for superseding guidance. If the applicable rule cannot be obtained, label the interpretation provisional and do not invent its requirements.

Build a small operation registry in the dossier:

| Field | Required content |
| --- | --- |
| Operation | Stable identifier and guide/search/analysis role |
| Interface | Required inputs and expected output |
| Dependency | Operations whose validated results are required |
| Version | Skill/tool version or content hash, when available |
| Evidence | Resource and applicable rule |
| Status | Pending, succeeded, failed, blocked, or skipped |

Use installed, documented operations only. If an operation is unavailable, use a documented manual procedure when defensible and disclose the substitution; otherwise block dependent work. Do not claim to have executed a named tool merely because its expected result is familiar.

**4. Resolve prerequisites and execute.**

Select operations that answer the question, recursively include their prerequisites, and order them so prerequisites finish first. Related operations are optional; prerequisite operations are mandatory. Detect cycles or incompatible inputs before execution and mark affected steps blocked.

Load detailed instructions when an operation is reached. Validate its outputs before passing them downstream. Record input identifiers, invocation or query, versions, timestamp, result location, and failure state. Retry transient retrieval once; persistent failure becomes an explicit evidence gap. Never treat a failed query as a negative biological finding.

**5. Build an evidence ledger.**

For each finding record:

- Evidence ID, exact variant/gene/disease/sample scope, and claim.
- Source URL or accession, source release or update date, and UTC retrieval time.
- Query, filters, pagination/completeness, and record version where supplied.
- Supporting passage or data location, study type, and relevant population or assay context.
- Supporting or conflicting direction, limitations, and duplicate/cohort linkage.
- Proposed rule or criterion, strength, applicability, and rationale.

Use explicit `unknown` for an unavailable source version; a retrieval date is not a database release. Distinguish primary observations from database summaries and model predictions. Verify that cited individuals, variants, and experiments actually support the assessed entity. Deduplicate shared cohorts and publications before combining evidence.

**6. Synthesize without hiding uncertainty.**

Keep observed facts, tool outputs, and interpretive inferences separate. For each proposed criterion, show the exact guideline provision, evidence IDs, proposed strength, and status: supported, not met, unresolved, or not applicable. Apply only the combination procedure specified by the selected framework and check for dependent evidence being counted twice.

Preserve disagreements between submitters, experiments, predictions, and guidelines. A database label alone is not an independently established classification. Do not convert uncertain findings into a diagnosis or treatment recommendation to complete the workflow.

Keep variant pathogenicity, gene–disease validity, phenotype fit, and therapeutic actionability as separate conclusions. If multiple variant origins remain possible, provide conditional interpretations and identify the information needed to discriminate them.

**7. Validate and hand off.**

Check that every material claim has a retrievable evidence ID; each applied rule has a versioned source; dependent operations have valid inputs; and all unresolved conflicts appear in the summary. Confirm calculations from recorded inputs and expose missing evidence.

Return a research draft with expert review pending. Ask the reviewing specialist to accept, modify, or reject proposed evidence assignments and conclusions, documenting the reason and review date. This workflow does not authorize clinical reporting or patient-management changes.

At the time limit, return the available dossier with incomplete steps and next actions. A valid partial output satisfies the reporting contract but must not be described as a completed interpretation.

### Evaluation contract

When evaluating this workflow, define the reference standard, evidence cutoff, task denominators, and scoring rules before running cases. Keep benchmark labels inaccessible during execution and audit retrieval logs for reference-answer leakage; ordinary research interpretation may legitimately consult curated classifications.

Report task-level concordance separately from case-level agreement, repeat consistency, execution failures, unsupported evidence assignments, and observed runtime. Count failures explicitly rather than silently dropping cases. Keep expert acceptability and self-reported time savings separate from objective correctness. Results from this implementation must be measured independently and must never inherit ClinGeX's reported performance.

## Inputs / Outputs

### Inputs

- A bounded research question and de-identified case or variant data.
- Genome assembly, variant representation, transcript version, and sample context where relevant.
- Available phenotypes, inheritance/segregation information, and assay limitations.
- Requested evidence cutoff, jurisdiction or guideline scope, and approved source access.
- Available skill/tool inventory and any prior interpretation to compare.

Missing identity-critical information blocks the affected interpretation. Missing optional context should narrow the claim and remain visible in the output.

### Outputs

Return one structured research dossier containing:

| Component | Minimum content |
| --- | --- |
| Run manifest | Case alias, question, start/end time, evidence cutoff, completion status |
| Identity record | Original and normalized entities, assembly/transcript, unresolved mappings |
| Execution record | Selected operations, dependency order, inputs, versions, outcomes and failures |
| Source manifest | Guideline editions, database releases, retrieval times and unavailable versions |
| Evidence ledger | Claims, evidence IDs, provenance, conflicts, independence and limitations |
| Interpretation matrix | Rules, evidence links, proposed strengths, conditional conclusions |
| Review handoff | Expert-review status, missing data, unresolved questions and next actions |

Use `complete`, `partial`, or `blocked` for workflow status and a separate `pending` or `reviewed` field for expert review. Do not equate `complete` with a definitive classification.

A successful bounded run returns all applicable components within 15 minutes, with missing values explicitly identified and no unsupported definitive claim. Record actual elapsed time; if the budget is exceeded, state that the timing target was not met.

## References

- [Advancing Clinical Genomic Analysis with a Skill-Centred Agent — arXiv:2610.40556v1](http://arxiv.org/abs/2610.40556v1), 29 October 2026. Source finding and research performance context.
- [Full text, including Methods §4.1–4.3 and supplementary evaluation definitions](https://arxiv.org/html/2610.40556v1). Basis for architectural and evaluation distinctions; verify the version before comparisons.

