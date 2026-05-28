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
name: bio-machine-learning-survival-analysis
description: Analyzes time-to-event data using Kaplan-Meier curves, log-rank tests, and Cox proportional hazards regression with lifelines. Builds survival models from clinical and omics features. Use when predicting patient survival or modeling time-to-event outcomes.
tool_type: python
primary_tool: lifelines
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
  - read_file
  - run_shell_command
---

# Survival Prediction with lifelines

## Core Capabilities

- Use PROMISE-AD as a reference design for leakage-safe, multi-horizon survival modeling from irregular longitudinal clinical histories: tokenize pre-index visits with standardized measurements, missingness masks, longitudinal changes, time-normalized slopes, visit timing, and non-diagnostic categorical attributes; estimate latent discrete-time mixture hazards with censoring-aware likelihoods and horizon-specific risk losses; calibrate 1-, 2-, 3-, and 5-year risks on validation data; and report dynamic horizon risks as histories update.
- For survival prediction from initial oncology consultation documents, extract text-derived predictors only from information present at the initial consultation, compare zero-shot general-LLM extraction or risk scoring with fine-tuned document models on identical consult-time inputs, calibrate risk outputs on held-out data, validate fixed-horizon or time-to-event endpoints with censoring-aware patient-level splits and metrics, and block leakage from labels, survival time, censoring status, follow-up language, later notes, or post-consultation facts.
- For survival prediction from oncology consultation documents, compare zero-shot LLM extraction, fine-tuned text models, and structured clinical covariate baselines on the same initial-consultation cohort; define time origin, endpoint, censoring, and temporal train/validation/test splits before modeling; calibrate predicted risks; and run leakage checks for outcome labels, survival time, censoring status, follow-up language, later notes, and post-consultation facts.
- For initial oncology consultation document survival prediction, compare zero-shot LLM extraction or risk scoring, fine-tuned document models, and conventional survival models on the same consult-time cohort; define the index consultation, fixed-horizon or time-to-event endpoint, and censoring rules before modeling; block leakage from survival labels, survival duration, censoring status, follow-up language, later notes, and post-consultation facts; calibrate risk estimates; and report clinician-facing uncertainty as reviewed risk ranges, confidence intervals, or caveated risk strata rather than standalone deterministic predictions.
- For cancer survival models using LLM-derived features from initial oncology consultation documents, compare fine-tuned models with zero-shot prediction or extraction on identical consult-time inputs; enforce leakage controls for survival labels, survival time, censoring status, follow-up text, later notes, and post-consultation facts; calibrate predicted risks; and require external validation before clinical interpretation.
- For LLM-based survival prediction from initial oncology consultation documents, compare LLM-derived feature pipelines and fine-tuned document models against zero-shot baselines on the same consult-time inputs; check for leakage from labels, survival time, censoring status, follow-up, later notes, and post-consultation facts; validate with censoring-aware splits and metrics, calibrate predicted risks, and report clinically usable uncertainty around survival probabilities or risk strata.
- For LLM-derived feature extraction from initial oncology consultation documents, compare zero-shot and fine-tuned pipelines on identical consult-time text, block leakage from labels, survival time, censoring status, follow-up, later notes, and post-consultation facts, calibrate downstream survival predictions, and retain clinician-reviewable feature provenance linking extracted variables back to source evidence.
- When applying general LLMs to cancer survival prediction from initial oncology consultation documents, compare zero-shot extraction or prediction with fine-tuned text models on the same consult-time notes; lock inputs to information available at the initial consultation; screen prompts, tuning data, and features for leakage from labels, survival duration, censoring status, follow-up, later notes, or post-consultation treatment facts; and check calibration before using risk estimates.
- For cancer survival prediction directly from initial oncology consultation documents, compare zero-shot general-LLM extraction or risk scoring against fine-tuned models on identical consult-time text; lock the index time to the initial consultation; exclude survival labels, event or censoring status, follow-up duration, later notes, and post-consultation treatment facts from prompts, fine-tuning data, and predictors; and validate with calibration plus censoring-aware time-to-event metrics such as C-index, time-dependent AUC, or Brier score.
- For oncology consultation-document survival prediction, evaluate zero-shot general-LLM extraction or scoring and fine-tuned document models on the same initial-consultation cohort; define whether the endpoint is fixed-horizon survival or censoring-aware time-to-event before modeling; keep labels, survival times, censoring status, follow-up language, later documents, and post-index treatment details out of document-derived features; calibrate risk outputs on held-out data; and govern extracted variables with versioned prompts or checkpoints, feature dictionaries, data-lineage records, access controls, and clinician-reviewable audit trails before downstream use.
- For survival prediction from initial oncology consultation notes, compare zero-shot prompting against fine-tuning on the same consult-time inputs; prevent temporal and label leakage by excluding outcome labels, survival duration, follow-up, later notes, and post-consultation treatment details; evaluate calibration and concordance/C-index; and require external validation before clinical interpretation.
- For general-LLM survival prediction from initial oncology consultation documents, structure comparisons as zero-shot versus fine-tuned approaches on identical prediction-time notes; keep labels, survival duration, censoring indicators, follow-up, later notes, and post-consultation treatment information out of prompts and predictor inputs; evaluate with calibration plus censoring-aware time-to-event or fixed-horizon metrics; and treat model rationales or extracted evidence as clinician-review aids rather than standalone clinical explanations.
- For text-derived oncology survival modeling from initial consultation documents, evaluate zero-shot general-LLM extraction against fine-tuned models on the same consult-time corpus; block leakage from survival labels, outcome descriptions, follow-up duration, later notes, and post-consultation treatment data; calibrate predicted risks, require external validation before deployment, and present clinically interpretable extracted features or rationale for clinician review.
- For oncology consult-note survival modeling, compare three pathways on identical initial-consultation inputs: zero-shot LLM extraction feeding survival models, fine-tuned document models, and conventional clinical feature models; define prediction time at consultation, handle censoring explicitly, check leakage from outcomes, survival duration, follow-up, future notes, and post-consultation treatments, evaluate calibration before prognostic output, and require clinician validation before prognostic use.
- For oncology consultation-document survival prediction, frame zero-shot general-LLM extraction or prediction, fine-tuned text models, and conventional survival models as separate comparison arms on the same initial-consultation cohort; lock the time origin to the consultation, prevent leakage from labels, survival duration, censoring indicators, follow-up language, later notes, and post-consultation treatment facts; use censoring-aware metrics with calibration checks; and require external validation before clinical interpretation.
- When deriving features from initial oncology consultation documents for survival prediction, compare zero-shot LLM extraction against fine-tuned models on the same consult-time inputs, run explicit leakage checks for future notes, outcomes, survival duration, follow-up, and post-consultation treatments, validate with censoring-aware metrics and calibration, and audit extracted features in a clinician-readable form before using them downstream.
- For cancer survival prediction from initial oncology consultation documents, compare zero-shot and fine-tuned LLM feature extraction with traditional clinical covariate models without assuming one is superior: define the survival time origin from the initial consultation, prevent leakage from future notes, follow-up duration, outcomes, or treatment facts unavailable at prediction time, encode censoring explicitly, report censoring-aware discrimination and calibration metrics, and keep outputs within clinical decision-support boundaries until externally and prospectively validated.
- For an oncology consultation-note survival prediction workflow, run zero-shot general LLM extraction or prediction against fine-tuned model variants on the same consult-time inputs; evaluate calibration and censoring-aware performance, document censoring handling, audit leakage from outcomes, survival duration, follow-up, future notes, or post-consultation treatments, and require external validation before clinical use.
- For oncology-consult-note survival prediction with general LLMs, compare zero-shot extraction/prediction against fine-tuned models using patient-level train/test separation, no prompt examples or tuning data from the test set, and no access to post-consultation information; evaluate calibration and censoring-aware metrics, require external validation, and route high-risk predictions through clinician review with reviewable feature attribution before acting on them.
- For general-LLM cancer survival prediction from initial oncology consultation notes, compare zero-shot prompting with supervised fine-tuning on identical consult-time documents; keep survival labels, survival duration, censoring indicators, follow-up, later notes, and post-consultation treatments out of prompts and predictor inputs; define censoring-aware time-to-event or fixed-horizon endpoints; check calibration before reporting risk; and provide clinician-readable feature attribution or extracted evidence for review.
- Build an LLM-derived feature pipeline for initial oncology consultation documents by comparing zero-shot structured extraction with fine-tuned model outputs, locking the prediction timestamp to the consultation and excluding future notes, follow-up duration, outcomes, and post-consultation treatment details; validate downstream survival models with calibration, C-index, and time-dependent AUC, and label survival predictions as review-only for clinician interpretation.
- When predicting cancer survival from initial oncology consultation documents, benchmark zero-shot general LLM extraction against fine-tuned models for the same predefined clinical features, then link those extracted features to calibrated time-to-event models with explicit checks that labels, survival duration, censoring status, future encounters, and post-consultation treatment information were not exposed during extraction or prediction.
- For an initial-oncology-consultation survival prediction protocol, predefine the index date, endpoint, censoring rules, and clinical predictor dictionary; compare zero-shot LLM extraction of structured predictors with fine-tuned document models using patient-level nested validation; keep survival labels, event or censoring status, follow-up duration, later notes, and post-consultation treatment facts out of prompts, tuning data, and features; evaluate with censoring-aware validation plus calibration; and require clinician review of extracted predictors before modeling outputs are used for clinical interpretation.
- For initial oncology consult-note survival modeling, compare zero-shot LLM extraction, fine-tuned text models, and structured survival models on the same consult-time cohort; audit leakage from outcomes, survival duration, censoring labels, follow-up, future notes, and post-consultation treatments; handle censoring explicitly, calibrate horizon-specific risk estimates, and return clinically interpretable time-to-event outputs such as survival probabilities at fixed time horizons or risk strata with clear review context.
- For oncology-consultation-document survival modeling informed by PubMed 42004490, evaluate zero-shot LLM extraction or prediction against fine-tuned models on identical initial-consultation text; predefine the time origin and whether the endpoint is fixed-horizon survival or censoring-aware time-to-event risk; check leakage from labels, survival duration, censoring status, follow-up, later notes, and post-consultation treatment details; report calibration with censoring-aware metrics; and expose clinician-readable feature attribution or extracted evidence for review.
- For text-derived oncology survival prediction from initial consultation notes, compare zero-shot general-LLM outputs, fine-tuned text models, and feature-based clinical baselines on the same consult-time cohort; lock prediction inputs to information available at the initial consultation, run leakage checks for labels, survival time, censoring status, follow-up, future notes, and post-consultation treatment facts; evaluate censoring-aware discrimination and calibration; and require clinician review of extracted evidence, features, and intended use before acting on predictions.
- For oncology-consult-note survival prediction informed by PubMed 42004490, compare zero-shot LLM extraction, fine-tuned document models, and classical survival models built from consult-time clinical features; handle censoring explicitly, check leakage from labels, survival duration, censoring status, follow-up, later notes, and post-consultation treatment facts, calibrate risk estimates, require external validation, and make text-derived features explainable enough for clinician review.
- For cancer survival prediction from initial oncology consultation documents, compare zero-shot LLM extraction, fine-tuned document models, and classical survival models using the same consult-time cohort; enforce leakage controls for labels, survival duration, censoring status, follow-up language, later documents, and post-consultation treatment facts; calibrate risk estimates; and validate fixed-horizon or censoring-aware time-to-event outputs before clinical interpretation.
- For survival prediction from oncology consultation notes, compare zero-shot LLM feature extraction against fine-tuned text models on the same consult-time documents; use leakage-safe train/test splits that keep patients, prompts, tuning examples, labels, survival duration, censoring status, follow-up, later notes, and post-consultation facts out of the test prediction context; assess calibration and censoring-aware metrics; and require clinician review of extracted predictors before using them in downstream survival models.

## Kaplan-Meier Curves

```python
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

kmf = KaplanMeierFitter()

# T: time to event or censoring
# E: event indicator (1=event occurred, 0=censored)
kmf.fit(T, event_observed=E)

# Plot survival curve
kmf.plot_survival_function()
plt.xlabel('Time (months)')
plt.ylabel('Survival probability')
plt.savefig('km_curve.png', dpi=150)
```

## Compare Groups with Log-Rank Test

```python
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

for group, color in zip(['high', 'low'], ['red', 'blue']):
    mask = df['risk_group'] == group
    kmf = KaplanMeierFitter()
    kmf.fit(df.loc[mask, 'time'], event_observed=df.loc[mask, 'event'], label=group)
    kmf.plot_survival_function(ax=ax, color=color)

# Log-rank test
high = df[df['risk_group'] == 'high']
low = df[df['risk_group'] == 'low']
results = logrank_test(high['time'], low['time'], event_observed_A=high['event'], event_observed_B=low['event'])
print(f'Log-rank p-value: {results.p_value:.4e}')

ax.set_xlabel('Time (months)')
ax.set_ylabel('Survival probability')
ax.set_title(f'Log-rank p = {results.p_value:.4e}')
plt.savefig('km_comparison.png', dpi=150)
```

## Cox Proportional Hazards Regression

```python
from lifelines import CoxPHFitter

# Prepare data: must have 'time' and 'event' columns
# Include covariates as additional columns
cph = CoxPHFitter()
cph.fit(df, duration_col='time', event_col='event')

# Summary with hazard ratios
cph.print_summary()

# Get hazard ratios as DataFrame
hr = cph.summary[['exp(coef)', 'exp(coef) lower 95%', 'exp(coef) upper 95%', 'p']]
print(hr)

# Concordance index (c-index): 0.5=random, 1.0=perfect
print(f'C-index: {cph.concordance_index_:.3f}')
```

## Multivariate Cox Model

```python
from lifelines import CoxPHFitter
import pandas as pd

# Combine clinical and omics features
cox_df = pd.DataFrame({
    'time': meta['survival_months'],
    'event': meta['vital_status'],
    'age': meta['age'],
    'stage': meta['stage_numeric'],
    'GENE1': expr.loc['GENE1'],
    'GENE2': expr.loc['GENE2']
})

cph = CoxPHFitter(penalizer=0.1)  # L2 regularization for stability
cph.fit(cox_df, duration_col='time', event_col='event')
cph.print_summary()
```

## Predict Risk Scores

```python
# Partial hazard (risk score)
risk_scores = cph.predict_partial_hazard(cox_df)

# Median risk split for KM plot
df['risk_group'] = (risk_scores > risk_scores.median()).map({True: 'high', False: 'low'})
```

## Check Proportional Hazards Assumption

```python
# Test PH assumption
cph.check_assumptions(df, p_value_threshold=0.05, show_plots=True)
```

## Survival at Specific Time

```python
# Survival probability at specific times
survival_probs = kmf.survival_function_at_times([12, 24, 60])
print(survival_probs)

# Median survival
print(f'Median survival: {kmf.median_survival_time_:.1f}')
```

## Feature Selection for Survival

```python
from lifelines import CoxPHFitter
import pandas as pd

# Univariate screening
results = []
for gene in expr.index[:1000]:
    cox_df = pd.DataFrame({
        'time': meta['survival_months'],
        'event': meta['vital_status'],
        'gene': expr.loc[gene]
    })
    cph = CoxPHFitter()
    cph.fit(cox_df, duration_col='time', event_col='event')
    results.append({
        'gene': gene,
        'hr': cph.hazard_ratios_['gene'],
        'p': cph.summary.loc['gene', 'p']
    })

results_df = pd.DataFrame(results)
sig_genes = results_df[results_df['p'] < 0.05].sort_values('p')
```

## Related Skills

- clinical-databases/variant-prioritization - Clinical variant interpretation
- differential-expression/de-results - Find DE genes for survival model
- machine-learning/biomarker-discovery - Select predictive features

## References

- http://arxiv.org/abs/2604.28055v1
- https://pubmed.ncbi.nlm.nih.gov/42004490/


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
