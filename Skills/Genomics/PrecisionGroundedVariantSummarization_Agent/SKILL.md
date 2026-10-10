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
11. **Versioned evidence joins and abstention**: Join normalized variant identities to versioned database records, retain accession/version, retrieval date, and claim-level citation links for traceability, present conflicting classifications with their source context and freshness, and abstain from a conclusion when retrieved support is insufficient or cannot be reliably matched.
12. **Precision Grounding evaluation pattern**: Use database-specific retrieval, assertion-level citations, and versioned provenance; reconcile conflicting classifications without hiding disagreement; disclose missing evidence; run hallucination checks against retrieved records; and require expert review of clinical significance summaries.
13. **Precision Grounding architecture and review controls**: Select authoritative databases appropriate to the variant and clinical context; normalize identifiers before joining records; preserve evidence-level provenance; present conflicting classifications with their supporting context; check for stale records; verify citation completeness and test generated summaries for hallucinated claims against retrieved evidence; and require expert review of generated variant summaries.
14. **Precision Grounding clinical-claim safeguards**: Require evidence-database grounding for every clinical claim, cite provenance for each claim, handle conflicts across ClinVar, gnomAD, and literature sources, check generated statements for hallucinated or unsupported assertions, and keep known pathogenicity evidence separate from model-generated interpretation.
15. **Precision Grounding named workflow**: Use Precision Grounding as the named workflow for trustworthy genetic variant summarization: perform database-grounded retrieval, preserve provenance-linked claims, handle conflicts across ClinVar, gnomAD, and literature, check for hallucinated or unsupported statements, and produce report-ready variant summaries.
16. **Precision Grounding evidence-boundary pattern**: For genetic variant summarization, retrieve ClinVar, gnomAD, ACMG, disease, and literature evidence; preserve provenance; expose conflicts; keep generated prose separate from database facts; and require review-status-aware uncertainty statements.
17. **Precision Grounding evidence-database augmentation**: Rank sources by relevance and evidence role for the requested variant summary; preserve ClinVar, gnomAD, and literature provenance at claim level; present conflicts rather than forcing consensus; attach confidence labels tied to retrieved support; and use hallucination-resistant templates that mark unsupported, missing, or inference-only statements explicitly.
18. **Database-backed claim validation**: Validate each generated genetic variant summary claim against trusted evidence-based databases before finalizing; capture provenance for supporting records; flag conflicts or missing support; and remove, qualify, or mark any hallucinated or database-unsupported assertion.
19. **Primary Precision Grounding pattern**: Treat Precision Grounding as the primary pattern for evidence-based genetic variant summarization by using database-backed retrieval before generation, displaying provenance for each clinical claim, preserving and explaining source conflicts, applying hallucination controls to unsupported assertions, and validating generated summaries against expert-curated summaries when available.
20. **Clinician-reviewable Precision Grounding workflow**: For genetic variant summarization, retrieve evidence from evidence-based databases before drafting; track provenance for each clinically relevant claim; handle conflicts across ClinVar records and literature explicitly; apply hallucination controls to unsupported statements; and produce final summaries suitable for qualified clinician review.
21. **Evidence-database augmentation for trustworthy summaries**: Apply Precision Grounding by augmenting LLM drafting with evidence-based databases; include provenance tables, handle ClinVar, gnomAD, and literature conflicts explicitly, run hallucination checks against retrieved records, and report structured uncertainty for unsupported, conflicting, or missing evidence.
22. **Central Precision Grounding report pattern**: Use Precision Grounding as the central pattern for variant summarization by retrieving evidence-based database records before drafting; ranking ClinVar, gnomAD, and literature sources by relevance and evidence role; preserving claim-level provenance; handling source conflicts explicitly; rejecting hallucinated or unsupported assertions; and producing review-ready variant report templates for qualified human review.
23. **Evidence-database augmented variant summaries**: Apply Precision Grounding as an evidence-database augmentation workflow for variant summaries; rank sources by relevance and evidence role; handle database and literature conflicts explicitly; preserve provenance citations for each claim; run hallucination checks against retrieved records; and keep retrieved evidence separate from interpretive synthesis.
24. **ClinVar/gnomAD/dbSNP/COSMIC Precision Grounding augmentation**: Augment genetic variant summaries with evidence-based database retrieval from ClinVar, gnomAD, dbSNP, and COSMIC when relevant; record source provenance, accession or identifier, assertion or retrieval date, and database freshness; preserve conflicting records without forced consensus; validate generated claims against retrieved evidence to control hallucinations; and present transparent evidence tables before narrative synthesis.
25. **Precision Grounding evidence routing and clinician-review outputs**: Route variant questions to evidence databases by evidence role, including ClinVar classifications, gnomAD population-frequency evidence, and literature-style reports; preserve provenance through synthesis; detect conflicts across sources; label uncertainty for missing, limited, or discordant evidence; check generated statements against retrieved records for hallucinations; and return structured clinician-review outputs with evidence, conflicts, limitations, and verification steps.
26. **Precision Grounding variant summarization pattern**: Retrieve evidence from evidence-based databases before drafting; link each claim to source provenance; preserve and explain conflicts across ClinVar, gnomAD, and literature; apply hallucination controls to database-unsupported assertions; and report uncertainty in structured categories for unsupported, conflicting, limited, or missing evidence.
27. **Evidence-backed Precision Grounding validation**: Apply Precision Grounding as an evidence-based database augmentation pattern for variant summarization by grounding generated summaries in trusted clinical genetics sources, carrying provenance with each claim, detecting and disclosing source conflicts, checking for hallucinated or unsupported assertions, and validating the final variant summary against retrieved database evidence before clinical review.
28. **Precision Grounding clinical handoff pattern**: Retrieve variant evidence from evidence-based databases before generation; preserve provenance for each generated claim; expose source conflicts and uncertainty; constrain narrative statements to cited facts or explicitly labeled inference; run hallucination checks for uncited or unsupported claims; and require qualified review before clinical handoff.
29. **Precision Grounding named evidence-database workflow**: Use Precision Grounding as the named workflow for evidence-database augmentation of variant summaries; select databases by variant context and evidence role; capture claim-level provenance; reconcile database and literature conflicts; check generated statements for hallucinated or unsupported claims; and report uncertainty for missing, limited, discordant, or inference-only evidence.
30. **PubMed 41950627 Precision Grounding augmentation**: Apply Precision Grounding as an evidence-database augmentation pattern for trustworthy variant summarization; retain source provenance for each database, literature, and generated-summary claim; handle conflicts across evidence databases without forcing consensus; remove, qualify, or explicitly label hallucinated or unsupported statements; and require qualified human review before clinical interpretation.
31. **Precision Grounding variant summarization control pattern**: Use evidence-database retrieval before LLM drafting; rank sources by relevance and evidence role; detect conflicts across database and literature records; write provenance-linked statements; run hallucination checks against retrieved evidence; and explicitly separate database facts from LLM interpretation.
32. **Precision Grounding fail-closed variant-summary workflow**: Bind every summary claim to ClinVar, gnomAD, disease, and literature evidence; surface source conflicts and review status; and fail closed by withholding or marking claims unsupported when database support is absent or stale.
33. **Precision Grounding uncertainty practice**: Retrieve evidence from evidence-based databases before summarizing; attach provenance links to database and literature claims; preserve disagreements as explicit conflicts; check generated claims against retrieved records for hallucination; and state uncertainty when databases disagree or evidence is sparse.
34. **Precision Grounding signoff workflow**: Select evidence databases based on variant context and evidence role; preserve provenance for every retrieved and generated-summary claim; handle database, literature, and assertion conflicts explicitly; run hallucination checks against retrieved evidence; return structured variant-summary sections with evidence, limitations, and verification steps; and require clinician or geneticist signoff before clinical use.
35. **Precision Grounding clinical summary gate**: Route each variant question to evidence databases by evidence role, require provenance on every claim, detect conflicts across source records, use controlled uncertainty language for missing, limited, or discordant evidence, and run hallucination checks before returning any clinical genetics summary.
36. **Primary evidence-grounded Precision Grounding pattern**: Treat Precision Grounding as a primary pattern for trustworthy genetic variant summarization by augmenting LLM drafting with evidence-based database retrieval, preserving provenance for database-backed and generated-summary claims, handling conflicts across retrieved sources, applying hallucination checks against retrieved evidence, and producing clinician-reviewable variant summaries for qualified review.
37. **Precision Grounding variant summarization pattern**: For clinical genetics use, ground summaries in evidence-based databases, preserve source provenance in each summary claim, handle conflicts across retrieved sources, check for hallucinated or unsupported statements, and label uncertainty clearly when evidence is missing, limited, or discordant.
38. **Core Precision Grounding variant-summarization pattern**: Use database-backed retrieval as the starting point for variant summaries; preserve source provenance; detect conflicts across clinical databases; apply uncertainty labels for missing, limited, or discordant evidence; enforce hallucination controls against unsupported assertions; and produce final summaries with evidence-linked claims.
39. **Precision Grounding clinical-style summary pattern**: Retrieve from evidence databases before generation; preserve provenance for each claim; handle conflicting classifications explicitly; separate observed evidence from interpretation; and run hallucination checks before returning clinical-style variant summaries.
40. **Precision Grounding audit-output pattern**: Ground variant summaries in evidence-based databases; make each clinically relevant statement provenance-linked; surface database, literature, and assertion conflicts; apply hallucination controls that remove, qualify, or label unsupported claims; and produce variant-summary audit outputs listing evidence records, claim provenance, conflicts, unsupported or missing evidence, and verification steps.
41. **Precision Grounding evidence-database variant-summarization pattern**: Use Precision Grounding as a named pattern for trustworthy genetics reports by augmenting LLM summaries with evidence-based databases, provenance links, conflict reconciliation, source-freshness checks, and hallucination controls for unsupported or uncited statements.
42. **Precision Grounding source-priority and contradiction checks**: Prioritize evidence databases by evidence role before drafting, using ClinVar clinical assertions and review status, gnomAD population-frequency context, ACMG-style evidence provenance when supplied by curation sources, and literature records for study support; attach source, identifier, assertion or retrieval date, and review or evidence status to each claim; flag contradictions across databases, submitters, phenotypes, transcripts, genome builds, or literature; and remove, qualify, or explicitly label any hallucinated or unsupported statement after checking it against retrieved evidence.
43. **Precision Grounding expert-review summary templates**: Retrieve variant evidence from evidence-based databases before drafting; preserve provenance for each source-backed statement; handle conflicts across ClinVar and related clinical genetics resources explicitly; run hallucination checks against retrieved records; and use variant-level summary templates that expose evidence, conflicts, unsupported claims, and review needs for expert evaluation.
44. **Precision Grounding auditable assertion summaries**: Retrieve evidence-database records before drafting, preserve source provenance for each claim, handle conflicting assertions explicitly, apply hallucination controls to unsupported statements, represent ClinVar-style assertions with condition, review status, and date when available, and generate auditable variant summaries that expose evidence, conflicts, limitations, and verification needs.
45. **Precision Grounding clinical uncertainty checks**: For clinical variant summaries, retrieve database-backed evidence before drafting; link each assertion to source provenance; detect conflicts across ClinVar and other evidence sources; check generated statements for hallucinated, uncited, or unsupported claims; and use explicit uncertainty language when evidence is limited, missing, discordant, or inference-only.
46. **Precision Grounding reviewer workflow**: Build trustworthy genetic variant summaries by retrieving evidence from ClinVar and related evidence databases before drafting; preserving source provenance for every clinical claim; exposing conflicts across records, submitters, conditions, and supporting literature; removing or labeling hallucinated and unsupported assertions; and returning structured summaries with reviewer-facing uncertainty statements for missing, limited, conflicting, or inference-only evidence.
47. **Precision Grounding pre-handoff controls**: Before clinical interpretation handoff, retrieve database-backed evidence; preserve ClinVar and other source provenance with citation-linked claims; run recency checks on source records; expose conflicts without forcing consensus; label uncertainty for missing, limited, stale, or discordant evidence; and remove, qualify, or mark hallucinated or unsupported statements.
48. **Publication-backed Precision Grounding summary requirements**: For clinical genetics outputs, use database-backed evidence retrieval before generation; preserve provenance through summary generation; report conflicts across evidence sources; require variant-level citations for each clinical claim; and apply hallucination controls to remove, qualify, or mark unsupported statements.
49. **Precision Grounding implementation architecture**: Normalize variants, retrieve matching records from authoritative databases, preserve assertion-level provenance and review status, reconcile conflicting classifications without hiding disagreement, generate summaries constrained to retrieved evidence, and verify every material claim against that evidence before finalizing.

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

- Du X, Nagy A, Oates MF, Wang Y, Wang X. Precision Grounding: augmenting large language models with evidence-based databases for trustworthy genetic variant summarization. Int J Med Inform. 2026 Jul 1. PubMed: https://pubmed.ncbi.nlm.nih.gov/41950627/
- Source finding: https://pubmed.ncbi.nlm.nih.gov/41950627/
- Richards S, Aziz N, Bale S, et al. Standards and guidelines for the interpretation of sequence variants. PubMed: https://pubmed.ncbi.nlm.nih.gov/25741868/
- ClinVar public variant archive: https://www.ncbi.nlm.nih.gov/clinvar/
- ClinGen Variant Curation Interface and Sequence Variant Interpretation resources: https://clinicalgenome.org/
