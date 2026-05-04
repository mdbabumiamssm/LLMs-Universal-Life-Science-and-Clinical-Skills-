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
- For oncology consultation notes, compare zero-shot LLM extraction, fine-tuned clinical language models, and structured survival models without assuming one is superior: define the survival time origin from the initial consultation, prevent leakage from future notes, follow-up duration, outcomes, or treatment facts unavailable at prediction time, encode censoring explicitly, and evaluate calibration, discrimination, and clinically validated utility before deployment.

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
