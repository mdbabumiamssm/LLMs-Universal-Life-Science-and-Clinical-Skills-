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
name: 'bidirectional-drug-target-screening-audit'
description: 'Audit drug-to-target and target-to-drug rankings for model disagreement, recurring candidate preferences, correspondence, and selectivity before allocating experimental screening capacity.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Bidirectional Drug-Target Screening Audit

## Overview

Audit drug-target interaction recommendations in both directions to distinguish model agreement, recurring candidate preferences, and evidence of pair-specific discrimination. The source study reports substantial disagreement among released systems and shows why benchmark performance and hit enrichment alone may not establish useful screening recommendations. Produce a traceable shortlist and an experimental follow-up plan while treating every ranking score as an unvalidated prediction.

## When to Use This Skill

- Compare models that rank molecules for a target or targets for a drug.
- Decide how to distribute a limited assay budget across consensus and disputed candidates.
- Investigate whether recommendations reflect broadly favored molecules or proteins rather than the intended pairing.
- Assess selectivity using comparable experimental measurements across multiple drugs and targets.
- Compare screening recommendations across training seeds despite similar held-out performance.

## Core Capabilities

1. **Define a bounded audit.** Record the screening catalogue, model versions, ranking direction, experimental budget, requested list lengths, and available measurements. Use Top-10 as a descriptive default only when appropriate to the budget; also examine nearby cutoffs. The 15-minute deliverable is an audit of supplied prediction tables or a clearly labeled partial report with missing inputs and next steps, not model retraining, catalogue-scale inference, or experimental validation. Set a runtime limit and report which analyses completed.

2. **Harmonize identifiers without erasing biological distinctions.** Map molecules using structures and stable identifiers, preserving stereochemistry and recording salt, tautomer, and parent-compound normalization decisions. Map proteins to species, accession, isoform, sequence or construct, and mutations when available; gene symbols alone are insufficient. Retain original IDs and a reversible crosswalk. Quarantine ambiguous mappings, conflicting duplicate predictions, and unresolved structures rather than guessing; document any replicate aggregation.

3. **Construct comparable bidirectional rankings.** Require one score per model/run and canonical drug-target pair, with documented score meaning and whether higher or lower is better. For each target rank eligible drugs; for each drug rank eligible targets. Preserve raw scores, missingness, and eligibility exclusions. Compare models on an explicitly shared candidate universe, and report original coverage separately. Do not treat absent predictions as low scores or average incomparable raw score scales. Resolve ties deterministically with canonical IDs and report cutoff ties; show sensitivity when ties materially change inclusion.

4. **Quantify recommendation agreement and stability.** For each query and model pair, report intersection count, overlap fraction, Jaccard similarity, and whether the lists are disjoint. For equal-length lists A and B of length k, overlap fraction is |A ∩ B|/k and Jaccard is |A ∩ B|/|A ∪ B|. If fewer than k shared candidates exist, use and disclose the effective k; exclude empty lists from ratios. Summarize each direction separately with query counts, distributions, and macro averages. Apply the same procedure across supplied training seeds while holding architecture, data, and objective fixed; do not attribute changes to seeds if these also differ.

5. **Separate recurring preference from query correspondence.** Count how often each candidate appears across queries, divided by the number of queries for which it was eligible. Inspect whether shared recommendations are dominated by these frequent candidates. With suitable activity labels, compare correctly matched recommendation lists against lists reassigned among queries: shuffle target labels for molecule lists and drug labels for target lists, preserving list size and candidate preferences. Use a complete measured submatrix when possible; otherwise restrict permutations to compatible eligibility and measurement coverage, documenting the rule. Recompute hit yield under each seeded permutation and report the observed yield, null distribution, and absolute loss after reassignment. A small loss is a warning about query specificity, not proof that a model ignores its query. Without labels, report preference and overlap only; mark correspondence in activity recovery unassessed.

6. **Evaluate activity recovery on comparable evidence.** Record endpoint, units, assay conditions, concentration, inequality qualifiers, source, and a prespecified activity threshold. Keep inhibition at a fixed concentration separate from IC50, Ki, and Kd unless a justified transformation is supplied. Unknown measurements are not inactive. Report selected, measured, active, and excluded counts; label precision among measured selections as conditional on assay coverage. Calculate enrichment only against the active fraction in the same eligible measured pool, with undefined results flagged when the baseline is zero. Describe coverage bias and possible training-data overlap before interpreting results as independent validation.

7. **Test reciprocal selectivity explicitly.** Use measured 2-by-2 panels with two drugs and two targets when all four measurements are comparable and support opposing preferences beyond a declared margin. Orient experimental values so higher means stronger activity. For a stringent audit-defined reciprocal criterion, require each diagonal pair to outperform both its row and column alternative experimentally; then count a prediction as jointly correct only if all four corresponding score inequalities hold. Report each inequality, joint success rate, eligible panel count, ties, and exclusions. This operational criterion is not claimed to reproduce the paper's exact statistic; consult its full methods for replication. Shared panels are dependent, so do not treat all panels as independent observations when estimating uncertainty. Selectivity on this panel does not establish proteome-wide selectivity.

8. **Allocate follow-up and deliver an auditable decision record.** Build a deduplicated list of drug-target pairs annotated with both directional ranks, model and seed support, candidate recurrence, measurement evidence, and uncertainty. Allocate the stated assay budget across consensus candidates, informative disagreements, and controls using a declared rule; account for replicates and dose points when the budget is measured in wells. If no budget is supplied, provide a prioritized queue without inventing capacity. Favor useful chemical and target diversity and explain each selection. Recommend appropriate concentration-response, orthogonal confirmation, and selectivity counter-screens as follow-up proposals. Agreement is not independent validation, especially when models share data or architectures; avoid claims of validated binding, efficacy, or safety.

## Inputs / Outputs

**Inputs**

- Prediction table: `model_id`, `run_id` or seed, `drug_id`, `target_id`, `score`, score orientation, and model/data version provenance.
- Molecule catalogue with structures and original identifiers; protein catalogue with accessions, species, and available sequence/construct information.
- Candidate eligibility rules, requested k values, intended screening direction, and assay budget with its unit.
- Optional activity table with pair identifiers, endpoint, value, units, qualifiers, assay context, replicate information, and source; optional fixed-configuration seed runs.

**Outputs**

- Identifier crosswalk and exclusion ledger, including unresolved mappings, duplicate handling, coverage, and missing predictions.
- Long-form bidirectional rankings and per-query overlap metrics with model pair, direction, k, effective k, denominator, and tie policy.
- Candidate recurrence summaries; activity recovery, reassignment-null results, and reciprocal selectivity results when evidence permits. Use `not assessed` with a reason for unavailable analyses rather than fabricated values.
- Budgeted candidate queue with canonical drug/target IDs, directional ranks, supporting models, seed variability, existing evidence, rationale, proposed assay, and unresolved uncertainty.
- Audit report and reproducibility manifest containing input hashes, software/model versions, thresholds, normalization choices, permutation seeds/counts, runtime, completed stages, and limitations.

**Completion checks:** Every ranked pair resolves through the crosswalk; each list contains unique eligible candidates; metric denominators reconcile with coverage; overlap statistics stay within their mathematical bounds; missing labels remain unknown; and the proposed assay allocation fits the stated budget. A partial report must identify blocked analyses and must not claim a completed scientific audit.

## References

- [From Benchmarks to the Bench: Preference, Correspondence and Selectivity in Bidirectional Drug-Target Screening, arXiv:2611.26369v1](http://arxiv.org/abs/2611.26369v1). Source finding motivating this workflow; the operational audit choices above are explicit recommendations, not a claim of exact method replication.
