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
name: 'trigger-first-adverse-drug-reaction-surveillance'
description: 'Prepare trigger-based adverse drug reaction surveillance with provenance-linked medication and event extraction, temporal review, pharmacist adjudication, and stage-specific validation.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Trigger-First Adverse Drug Reaction Surveillance

## Overview

Organize retrospective adverse drug reaction (ADR) surveillance around electronic triggers, evidence-linked LLM assistance, and pharmacist review. Separate candidate detection from causal attribution, and evaluate missed events, false positives, and actual review workload. Study-specific screening remains blocked until the original trigger definitions and complete validation protocol are verified.

## When to Use This Skill

- Preparing a pharmacist-supervised retrospective surveillance cohort from medication exposures and clinical records.
- Building a review queue from verified electronic trigger rules.
- Linking suspected medication-related events to source evidence and exposure timelines.
- Auditing trigger misses, model errors, and pharmacist review burden.
- Assessing whether a locally adapted workflow reproduces the study design or requires separate validation.

## Core Capabilities

1. **Verify the study and resolve implementation prerequisites.**
   The [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/42959829/) describes a prespecified Chinese Hospital Pharmacovigilance System trigger, two pharmacists establishing a blinded reference standard across 7,950 exposure episodes from distinct inpatients, and exact McNemar comparisons of paired errors. It compares Qwen3-4B-Instruct with a LoRA-adapted model trained on 410 patient-disjoint cases involving other medicines.

   Evidence status at authoring: the abstract was accessible; PMC and publisher full text could not be retrieved. Exact trigger predicates, thresholds, time windows, medicine eligibility, and detailed adjudication rules were therefore not verified. Do not substitute generic laboratory, antidote, or discontinuation rules and attribute them to this study.

   Before implementing screening, retrieve the full text and relevant supplements through the References links or read supplied copies. Extract a trigger register containing `trigger_id`, source section/table, eligible exposure, required fields, logical predicate, units, threshold boundaries, temporal window, exclusions, and handling of missing data. Extract the episode definition, cohort criteria, reference-standard procedure, blinding, disagreement resolution, causality criteria, and statistical methods. Mark any unstated detail `not_reported`; do not infer it. Unresolved executable predicates require `blocked_missing_trigger_definition` and an explicit missing-evidence list.

2. **Define a reproducible cohort and candidate selection.**
   The following instructions are proposed operational safeguards, not additional methods verified from the paper. Freeze the observation period, exposure-episode definition, inclusion rules, trigger version, and evaluation unit before examining outcomes. Keep patient identifiers pseudonymous and preserve links between repeated episodes. Distinguish medication orders from documented administration.

   Once the evidence gate passes, apply the verified predicates deterministically and retain both matched and unmatched episodes. Record which facts satisfied each predicate, including source identifiers and timestamps. Represent unavailable inputs as `indeterminate`, not trigger-negative. Consolidate duplicate alerts without losing their individual trigger matches. Clearly label locally changed rules as adaptations requiring their own validation.

3. **Extract medications and events with provenance.**
   For each candidate, extract drug identity, dose, route, administration dates, changes, co-medications, event description, onset, relevant observations, and documented management. Attach a record identifier and field or text-span locator to every extracted fact. Preserve negation, historical mentions, uncertainty, conflicting records, and missing values. A model must abstain when evidence is absent; generated explanations are not evidence.

4. **Review temporal plausibility without asserting causality.**
   Build an exposure/event timeline using event time separately from documentation time. Flag events predating exposure, uncertain onset, alternative causes, and concomitant therapies. Summarize documented dechallenge or rechallenge without inferring either from silence. Keep `trigger_match`, `event_present`, `suspected_drug_relationship`, and `pharmacist_causality_assessment` as separate fields. Temporal sequence alone does not establish an ADR.

5. **Support pharmacist adjudication and preserve independent validation.**
   Present evidence packets for all flagged candidates, including model-negative and abstained cases; an LLM-negative result must not autonomously exclude a case. Record provisional model labels separately from signed pharmacist decisions and reasons. Do not assign a named causality scale to the study unless confirmed in its methods.

   For study replication, obtain blinded reference review of the entire exposed cohort, including trigger-negative episodes. Keep model outputs concealed during reference adjudication and document disagreement resolution according to the verified protocol. If only a sampled negative audit is feasible, prespecify sampling and weights, label this a modified design, and do not report unadjusted full-cohort sensitivity. Keep tuning and evaluation patients disjoint; freeze model, prompt, and rule versions before evaluation.

6. **Measure missed events and false positives at each stage.**
   Report separate confusion matrices for trigger selection across the reference-reviewed cohort, model classification within trigger-positive episodes, and the specified end-to-end decision pathway. Identify trigger misses, model misses among flagged cases, false alarms, abstentions, and unreviewed cases separately. Do not count unreviewed or indeterminate episodes as true negatives.

   For each applicable stage, report denominators and compute sensitivity `TP/(TP+FN)`, specificity `TN/(TN+FP)`, positive predictive value `TP/(TP+FP)`, and F1 `2TP/(2TP+FP+FN)`; use `not_estimable` for zero denominators. Report uncertainty with the stated interval method. For paired model comparisons, use exact McNemar tests on discordant pairs, separating reference-positive and reference-negative strata when comparing sensitivity and specificity. Keep conditional model performance distinct from cohort-wide detection. Observing no misses does not establish perfect sensitivity in future cohorts.

7. **Quantify review workload and deliver an auditable result.**
   Report eligible episodes, trigger-positive episodes, unique candidates, completed reviews, unresolved cases, and additional reviews of trigger-negative records. Measure pharmacist time, re-review time, and time per adjudicated ADR when available. Candidate fraction is a volume measure, not measured labor savings; compare time only against a defined baseline and disclose reference-review effort separately.

   Within the 15-minute execution target, produce a bounded evidence packet and status report for the supplied batch, or a blocked report specifying missing prerequisites. This target does not promise completion of cohort-wide pharmacist adjudication. Verify provenance coverage, unique episode identifiers, consistent counts, explicit missingness, and separation of provisional and final decisions before returning results.

## Inputs / Outputs

**Inputs**

- Accessible study methods and supplements, plus any explicitly identified local adaptations.
- Authorized, preferably de-identified exposure records, administration records, clinical notes, laboratory observations, and stable source locators.
- Cohort boundaries, episode definition, timestamp conventions, and verified trigger register.
- Model and prompt versions when LLM assistance is requested; pharmacist reference labels and review logs when validation is requested.

Use patient data only in the authorized processing environment. Fetch literature without transmitting clinical records to public services.

**Outputs**

- **Evidence status:** verified methods, source locations, unresolved definitions, local deviations, and `ready`, `partial`, or `blocked_missing_trigger_definition` status.
- **Trigger register and cohort ledger:** versioned rules, inclusion decisions, match evidence, and positive/negative/indeterminate status for each episode.
- **Candidate review table:** `episode_id`, `trigger_ids`, medication facts, event facts, timeline, source locators, uncertainties, provisional model assessment, pharmacist decision, causality assessment, rationale, and review status.
- **Validation report:** stage-specific counts, denominators, uncertainty, paired comparisons where applicable, false-positive and missed-event audits, and limitations from incomplete reference review.
- **Workload report:** candidate volume, review completion, measured review time, and clearly identified estimates or unavailable measurements.

A blocked report must contain the missing trigger or protocol fields and the sources attempted. It must not contain fabricated screening results. Surveillance output supports pharmacist review; it does not independently authorize medication changes or establish drug causation.

## References

- Liao C, Lai X, Chen W, He J, Yu X. *Trigger-first large language model-assisted adverse drug reaction surveillance: A pharmacist-supervised retrospective cohort study.* Explor Res Clin Soc Pharm. 2026;24:100866. [PubMed PMID 42959829](https://pubmed.ncbi.nlm.nih.gov/42959829/). Abstract verified; detailed trigger definitions require full-text verification.
- Same study: [PMC full-text location, PMC13718469](https://pmc.ncbi.nlm.nih.gov/articles/PMC13718469/) and [publisher DOI](https://doi.org/10.1016/j.rcsop.2026.100866). Retrieval targets for methods and supplements; their contents were not verified during authoring.
