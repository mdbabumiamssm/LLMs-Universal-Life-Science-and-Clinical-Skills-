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
name: bio-machine-learning-model-validation
description: Implements nested cross-validation and stratified splits for unbiased model evaluation on biomedical datasets. Prevents data leakage and overfitting in biomarker discovery. Use when validating classifiers or optimizing hyperparameters on omics data.
tool_type: python
primary_tool: sklearn
measurable_outcome: Execute skill workflow successfully with valid output within 15 minutes.
allowed-tools:
  - read_file
  - run_shell_command
---

# Cross-Validation for Biomedical Data

## Core Capabilities

- Compare numeric and embedding-based clinical risk-prediction pipelines with matched patient splits, leakage controls, comparable tuning budgets, discrimination, calibration, and computational cost assessment using the template below; do not assume either representation is superior.

## Clinical Risk-Prediction Comparison Template

The [reviewed study](https://academic.oup.com/jamiaopen/article/9/5/ooag199/8994315) compared 458 engineered numeric features with frozen embeddings of text-serialized versions of the same structured clinical variables, using XGBoost in both pipelines. Numeric inputs used category-specific summaries and imputation; semantic inputs omitted missing variables and used raw values (F1), qualitatively interpreted values (F2), or abnormal findings only (F3). Six encoders, three formats, and six prompt wrappers formed 108 semantic configurations per endpoint. Both pipelines used Optuna; the study's 30 trials per configuration did not constitute equal total search budgets.

For each comparison, complete and enforce this evaluation template (requirements below are evaluation controls, not claims about the paper's results):

| Field | Required specification |
|-------|------------------------|
| Clinical task | Cohort, endpoint, prediction time, observation window, horizon, exclusions, and identical source variables available to both representations. |
| Pipelines | Numeric feature definitions and missingness rules; semantic serialization, prompt, frozen encoder identifier/version, truncation, and embedding dimensions. Keep the downstream classifier matched; document deviations from the study. |
| Matched splits | Reuse identical patient-level training, tuning, calibration, and held-out test assignments across pipelines; keep repeated admissions together and apply temporal/site separation when required by deployment. |
| Leakage controls | Exclude post-prediction information; fit imputation, scaling, feature selection, and any learned representation only within training folds. Select configurations and thresholds without test access; reserve separate calibration data. Document possible encoder pretraining overlap. |
| Tuning budget | Prespecify comparable total trial or compute budgets, counting encoder/format/prompt selection as well as classifier tuning. Report search spaces, seeds, actual fits, and budget deviations; distinguish a broader search from a budget-matched comparison. |
| Discrimination and calibration | Evaluate once on the same held-out patients: AUROC and AUPRC, paired uncertainty estimates, calibration curves, calibration intercept/slope, and Brier score. Fit any recalibration without test data and report before/after results. Compare patient-level false-positive/false-negative overlap at prespecified thresholds. |
| Computational cost | Report feature/embedding generation, tuning, training, and inference time; hardware, peak memory, embedding/API charges, and storage. State cohort size, batch size, and caching assumptions. |
| Interpretation | Report endpoint-specific tradeoffs and uncertainty without presuming a winner or generalizing a single-cohort result to other settings. |

## Why Nested CV Matters

Simple train/test splits overestimate performance on small omics datasets. Nested CV provides unbiased estimates by separating hyperparameter tuning from performance evaluation.

## Nested Cross-Validation

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier(random_state=42))
])

param_grid = {
    'clf__n_estimators': [50, 100, 200],
    'clf__max_depth': [5, 10, None]
}

# Outer CV: performance estimation (5 folds)
# Inner CV: hyperparameter tuning (3 folds)
outer_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
inner_cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

nested_scores = []
for train_idx, test_idx in outer_cv.split(X, y):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    grid = GridSearchCV(pipe, param_grid, cv=inner_cv, scoring='roc_auc', n_jobs=-1)
    grid.fit(X_train, y_train)
    score = grid.score(X_test, y_test)
    nested_scores.append(score)

print(f'Nested CV AUC: {np.mean(nested_scores):.3f} +/- {np.std(nested_scores):.3f}')
```

## Stratified K-Fold

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Always stratify for class imbalance
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipe, X, y, cv=cv, scoring='roc_auc')
print(f'CV AUC: {scores.mean():.3f} +/- {scores.std():.3f}')
```

## Repeated Stratified K-Fold

```python
from sklearn.model_selection import RepeatedStratifiedKFold

# More robust estimate with multiple repeats
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=10, random_state=42)
scores = cross_val_score(pipe, X, y, cv=cv, scoring='roc_auc')
print(f'Repeated CV AUC: {scores.mean():.3f} +/- {scores.std():.3f}')
```

## Leave-One-Out (Small Datasets)

```python
from sklearn.model_selection import LeaveOneOut, cross_val_predict

# Use for very small datasets (n < 30)
loo = LeaveOneOut()
y_pred = cross_val_predict(pipe, X, y, cv=loo, method='predict_proba')[:, 1]
auc = roc_auc_score(y, y_pred)
print(f'LOO AUC: {auc:.3f}')
```

## Group-Aware Splits

```python
from sklearn.model_selection import GroupKFold, LeaveOneGroupOut

# When samples from same patient/batch must stay together
groups = meta['patient_id'].values
group_cv = GroupKFold(n_splits=5)
scores = cross_val_score(pipe, X, y, cv=group_cv, groups=groups, scoring='roc_auc')
```

## CV Strategy Selection

| Dataset Size | Strategy | Notes |
|--------------|----------|-------|
| n > 100 | StratifiedKFold(5) | Standard choice |
| n = 50-100 | StratifiedKFold(10) | More train data per fold |
| n < 30 | LeaveOneOut | Maximum train data |
| Repeated measures | GroupKFold | Keep patients together |
| High variance | RepeatedStratifiedKFold | More stable estimates |

## Avoiding Data Leakage

```python
# WRONG: Feature selection before CV
# selected = SelectKBest(k=100).fit_transform(X, y)  # Leaks info!
# scores = cross_val_score(clf, selected, y, cv=cv)

# CORRECT: Feature selection inside CV
from sklearn.feature_selection import SelectKBest

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('select', SelectKBest(k=100)),  # Done per fold
    ('clf', RandomForestClassifier())
])
scores = cross_val_score(pipe, X, y, cv=cv, scoring='roc_auc')
```

## Related Skills

- machine-learning/omics-classifiers - Model training
- experimental-design/multiple-testing - Multiple hypothesis correction
- machine-learning/biomarker-discovery - Feature selection within CV


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

## References

- [Numeric versus embedding pipelines for optimized clinical risk prediction. JAMIA Open (2026).](https://pubmed.ncbi.nlm.nih.gov/42921350/)
