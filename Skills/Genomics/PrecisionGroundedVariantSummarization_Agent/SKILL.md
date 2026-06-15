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
name: 'precision-grounded-variant-summarization'
description: 'Produce evidence-grounded genetic variant summaries with provenance, conflict handling, and hallucination controls.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Precision Grounded Variant Summarization

## Overview

Use this skill to summarize genetic variants by grounding every clinically relevant statement in trusted evidence sources instead of relying on free-form generation. The workflow emphasizes provenance, uncertainty, database disagreement, and clear separation between retrieved evidence, inference, and missing information.

It is intended for auditable variant, gene, disease, and evidence-strength summaries that can support clinical genomics review, research curation, or report drafting without substituting for formal clinical interpretation.

## When to Use This Skill

- A user asks for a trustworthy narrative summary of a genetic variant, gene-disease association, or variant-disease relationship.
- A variant summary must cite source databases, publications, assertions, submitters, review status, or evidence strength.
- Multiple evidence sources disagree and the user needs a concise conflict-aware synthesis.
- The user wants hallucination-resistant summarization with explicit provenance and missing-evidence handling.
- The output will be used for clinical genetics review, research variant curation, molecular tumor board preparation, or patient-report drafting.
- The task is summarization or evidence synthesis, not de novo ACMG/AMP classification unless the user explicitly asks for classification support.

## Core Capabilities

1. **Variant normalization and scope control**: Identify the requested variant using stable nomenclature where available, including gene symbol, transcript, genome build, HGVS, rsID, ClinVar Variation ID, or genomic coordinates.
2. **Evidence source grounding**: Retrieve or use supplied evidence from authoritative sources such as ClinVar, ClinGen, OMIM, gnomAD, PubMed, dbSNP, locus-specific databases, cancer knowledge bases, or institutional curation records.
3. **Provenance-preserving synthesis**: Tie each substantive claim to its supporting source, accession, PMID, database record, assertion date, review status, or submitter context when available.
4. **Conflict detection**: Surface discordant classifications, conflicting disease assertions, transcript mismatches, population-frequency concerns, outdated assertions, and differences between germline and somatic interpretations.
5. **Evidence-strength framing**: Distinguish established evidence, limited evidence, conflicting evidence, computational predictions, population observations, functional studies, segregation data, and expert-panel assertions.
6. **Hallucination controls**: Avoid unsupported claims, mark unavailable evidence as not found, do not infer pathogenicity from gene relevance alone, and separate source facts from model-generated synthesis.
7. **Clinical-readiness formatting**: Produce concise summaries with sections for identity, clinical significance, phenotype or disease context, evidence basis, conflicts or caveats, and recommended verification steps.
8. **Precision Grounding pattern**: Retrieve evidence from trusted databases before synthesis, retain provenance through every claim, reconcile conflicts across ClinVar, gnomAD, and literature, run hallucination checks for unsupported assertions, and route outputs to qualified human review before clinical use.
9. **Precision Grounding architecture and evaluation**: Use database-specific retrieval, normalize evidence into a consistent representation, attach claim-level provenance and source-freshness metadata, preserve conflicting classifications rather than silently resolving them, reject unsupported claims by checking generated statements against retrieved evidence, and require qualified expert review of clinical assertions before clinical use.
10. **Database-augmented Precision Grounding**: Normalize variant representations before retrieving evidence from multiple authoritative databases; preserve source-level provenance; detect conflicts; weight assertions by available review status; reject claims unsupported by retrieved evidence; check source freshness; and evaluate grounded summaries against ungrounded summaries without inventing unsupported performance claims.

## Inputs / Outputs

### Inputs

- Variant identifier: HGVS, rsID, ClinVar Variation ID, genomic coordinate, protein change, VCF row, or free-text variant description.
- Optional context: suspected disease, inheritance mode, phenotype, cancer type, assay type, genome build, transcript, sample type, and whether the use case is germline, somatic, pharmacogenomic, or research.
- Evidence sources: user-provided records, database exports, literature links, PubMed IDs, ClinVar pages, curation notes, or permission to fetch public evidence.
- Output requirements: target audience, length, citation style, report template, and whether to include uncertainty or actionability language.

### Outputs

- Normalized variant identity and any unresolved nomenclature issues.
- Evidence-grounded narrative summary with source-linked claims.
- Table or bullet summary of key evidence records, including database/source, assertion, condition, review level, date, and caveats when available.
- Conflict and limitation section describing discordant classifications, weak evidence, missing data, or interpretation boundaries.
- Recommended verification checklist, such as confirming transcript/build, checking latest ClinVar and ClinGen records, reviewing primary literature, and routing to qualified clinical interpretation when appropriate.

### Workflow

1. **Clarify the interpretation frame**: Determine whether the request is germline, somatic, pharmacogenomic, population genetics, or research summarization.
2. **Normalize the variant**: Resolve identifiers across transcript, protein, genomic, and database representations; state ambiguities instead of silently choosing one.
3. **Collect grounded evidence**: Prefer authoritative databases and primary literature. Record source names, identifiers, dates, review status, and accession numbers.
4. **Extract claims conservatively**: Pull only claims supported by the evidence, such as clinical significance, disease association, frequency, functional effect, segregation, computational prediction, or therapeutic relevance.
5. **Identify conflicts and gaps**: Compare claims across sources and call out disagreement, outdated assertions, lack of expert review, limited phenotype match, population-frequency concerns, or absent functional evidence.
6. **Write the summary**: Separate factual evidence from synthesis. Use cautious language for uncertain findings and avoid upgrading or downgrading clinical significance without explicit criteria.
7. **Validate before finalizing**: Check that each substantive statement is traceable to a source and that missing evidence is represented as unavailable rather than guessed.

### Output Template

```markdown
## Variant Summary

**Variant identity:** [gene, transcript, HGVS, rsID, genome build, coordinates if known]
**Context:** [germline/somatic/research; disease or phenotype if supplied]

**Evidence-grounded interpretation:**
[Concise narrative. Every clinically relevant claim should be linked to a source or explicitly marked as inference.]

**Key evidence:**
| Source | Record | Assertion / Finding | Condition | Date / Review Status | Notes |
|---|---|---|---|---|---|
| [database or PMID] | [accession] | [claim] | [condition] | [date/status] | [caveat] |

**Conflicts and limitations:**
- [Discordant classifications, transcript mismatch, outdated record, missing evidence, or uncertainty.]

**Verification checklist:**
- Confirm genome build and transcript.
- Check current ClinVar, ClinGen, and relevant disease-specific resources.
- Review primary literature for high-impact claims.
- Route clinical conclusions through qualified variant interpretation review.
```

## References

- Du X, Nagy A, Oates MF, Wang Y, Wang X. Precision Grounding: augmenting large language models with evidence-based databases for trustworthy genetic variant summarization. PubMed: https://pubmed.ncbi.nlm.nih.gov/41950627/
- Richards S, Aziz N, Bale S, et al. Standards and guidelines for the interpretation of sequence variants. PubMed: https://pubmed.ncbi.nlm.nih.gov/25741868/
- ClinVar public variant archive: https://www.ncbi.nlm.nih.gov/clinvar/
- ClinGen Variant Curation Interface and Sequence Variant Interpretation resources: https://clinicalgenome.org/
