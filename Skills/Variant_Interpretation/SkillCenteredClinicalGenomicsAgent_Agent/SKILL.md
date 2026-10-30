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
name: 'skill-centered-clinical-genomics-agent'
description: 'Organize research genomic interpretation through task-specific skill retrieval, dependency-aware execution, traceable guideline and database evidence, and expert review, informed by ClinGeX.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Skill-Centered Clinical Genomics Agent

## Overview

This skill organizes a research workflow for integrating genomic guidelines, database records, and computational evidence into a traceable interpretation for specialist review. It draws on the ClinGeX architecture while keeping the paper's reported results separate from the capabilities of the local implementation. This document does not install ClinGeX or establish clinical validation; outputs are research drafts requiring qualified expert review before clinical use.

## When to Use This Skill

- Investigating criterion-level evidence for a germline variant.
- Assessing a gene–disease relationship or prioritizing rare-disease hypotheses.
- Reviewing somatic variant evidence in a specified tumor and treatment context.
- Designing or evaluating an agent that retrieves and composes genomic analysis skills.
- Auditing provenance, conflicting findings, or missing dependencies in a genomic interpretation.

## Core Capabilities

1. **Extract and delimit the source architecture.** Before implementing a reproduction, inspect the versioned paper's Methods and Supplementary sections A.2–A.4 and record what was actually verified. ClinGeX reports 105 executable skills: 27 guide, 40 search, and 38 analysis. Its selector retrieves task-specific skills, expands related skills and prerequisites, and progressively exposes instructions; the agent iteratively executes and synthesizes evidence while retaining actions and outputs. Keep relatedness edges distinct from execution dependencies. These are reported design features, not a claim that this skill provides that library. [Source paper](https://arxiv.org/html/2610.40556v1)

2. **Scope the case and normalize identifiers.** Establish the research question and choose germline classification, gene–disease validity, or somatic actionability as the primary task. Capture genome assembly, reference and alternate alleles, transcript accession and version, disease, inheritance, and relevant phenotype or tumor context. Check reference-allele consistency and document normalization or transcript changes. Do not silently resolve ambiguous variants, mix assemblies, or infer unprovided pedigree relationships. Request missing essentials or return an explicitly incomplete assessment.

3. **Retrieve a minimal executable workflow.** Inspect available local skill metadata and select capabilities that match the question. Build a dependency table with skill identifier, version, required inputs, prerequisites, expected outputs, and availability. Load detailed instructions only for selected skills, resolve prerequisite closure, check for cycles, and order execution accordingly. Missing tools, credentials, or prerequisite outputs block dependent steps; record them instead of simulating execution. Do not assume that paper-specific skill names exist locally.

4. **Retrieve applicable guidance and database evidence.** Identify the current applicable framework and any gene-, disease-, or variant-specific specifications before assigning criteria. Retrieve authoritative guidance and relevant public evidence through available tools; record publication/version dates and access dates. Candidate sources include ClinGen and ClinVar for germline interpretation and curated oncology resources for somatic questions. Treat a database assertion as attributed evidence whose review status, context, date, and supporting literature need inspection. Preserve conflicting submissions and distinguish unavailable evidence from evidence against a hypothesis.

5. **Integrate computational evidence without double counting.** Run only available, documented annotation or prediction tools with explicit versions, settings, assembly, and transcript. Store raw output alongside the interpreted result and applicability limitations. Assess overlapping inputs and correlated predictors before combining support; several predictions do not automatically constitute independent evidence. Apply a computational result to a criterion only when the selected framework supports that use, and avoid treating predictions as experimental confirmation.

6. **Produce a criterion-level evidence ledger.** For each evidence item, record its identifier, source URL or accession, version, retrieval date, relevant excerpt or result, case context, proposed criterion and strength, rationale, dependencies, and uncertainty. Separate observations from agent inferences. For each criterion report supported, not supported, or undetermined with reasons. Derive any provisional classification using the explicitly named framework and combination rules; keep pathogenicity, gene–disease validity, and treatment actionability as separate conclusions.

7. **Evaluate research performance honestly.** The paper reports 71.7% macro-averaged task-level concordance on 223 temporally held-out cases versus 45.7% for its strongest comparator. Its counterbalanced study involved 45 professionals and 135 cases; the exploratory month-long assessment collected feedback from 11 professionals on 96 self-selected episodes. These findings concern the studied system and settings, not local accuracy or clinical validation. [Source finding](http://arxiv.org/abs/2610.40556v1)

   For a local evaluation, freeze cases, reference answers, source dates, model/tool versions, and scoring rules before execution. Keep answer-bearing reference records separate from permitted evidence retrieval and audit leakage. Report task-specific concordance and denominators before macro-averaging; distinguish criterion-level from case-level results. Record failed executions, abstentions, time, and expert disagreement. Treat self-reported adoption or time savings as observational feedback rather than patient-outcome evidence.

8. **Support expert adjudication and bounded completion.** Present conflicts, missing data, provenance gaps, and the reasoning behind each proposed criterion to a qualified reviewer. Capture the review decision, corrections, unresolved issues, and disposition separately from the agent draft. Do not convert a research report into an autonomous diagnosis, treatment instruction, or signed clinical report.

   Use a 15-minute execution budget for one bounded research question: approximately two minutes for scope and dependency checks, six for retrieval and available computations, four for synthesis, and three for output validation. This is a workflow target, not a performance claim from the paper. At the limit, return a valid partial report with blocked steps and next actions; do not manufacture completion or rush expert review.

## Inputs / Outputs

**Inputs**

- A defined research question, task type, and desired evidence cutoff date.
- De-identified variant identifiers or sequencing-derived records with assembly and transcript information where applicable.
- Relevant phenotype, pedigree/inheritance, disease, or tumor context; distinguish supplied facts from assumptions.
- Available skill inventory, tool versions, permitted data sources, and applicable institutional interpretation procedures.
- For evaluation only: a separately held reference standard and predefined scoring protocol.

Use the minimum necessary case information. Send patient-derived material only to services authorized for that data; prefer public identifiers for external evidence retrieval.

**Outputs**

Return one structured research report containing:

- `status`: complete, partial, or blocked, plus elapsed time and reason.
- `case_context`: normalized identifiers, task scope, missing inputs, and assumptions.
- `source_verification`: paper version inspected, verified architecture/evaluation facts, and any unverified reproduction details.
- `workflow`: selected skills, versions, prerequisite relationships, step status, and execution errors.
- `evidence_ledger`: source-linked observations, computed results, criteria, strength rationales, and uncertainty.
- `interpretation`: framework/version, provisional conclusion or abstention, conflicts, limitations, and unresolved questions.
- `review`: pending or completed expert adjudication, corrections, and required follow-up.
- `evaluation`: only when requested, metrics with denominators, reference separation, leakage checks, and failures.

**Completion checks:** Every material claim must resolve to a retrieved source or labeled inference; every computation must have an execution record; every classification must identify its framework and supporting criteria. No downstream step may claim success when an essential prerequisite failed. A structurally valid partial report satisfies the reporting requirement but does not count as a completed interpretation or successful benchmark case. Expert review may remain pending beyond the execution budget and must be labeled accordingly.

## References

- [Advancing Clinical Genomic Analysis with a Skill-Centred Agent, arXiv:2610.40556v1](http://arxiv.org/abs/2610.40556v1). Source finding and reported evaluation; research preprint.
- [Versioned full text](https://arxiv.org/html/2610.40556v1). Methods and Supplementary sections A.2–A.4 provide architecture, skill selection, dependency handling, and benchmark details.
