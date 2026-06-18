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
name: agentomics-ml
description: An autonomous agentic system for supervised machine learning model development, specifically tailored for biomedical data.
keywords:
  - agentomics
  - automl
  - biomedical-ml
  - supervised-learning
  - autonomous-agents
measurable_outcome: Autonomously train, evaluate, and validate a supervised machine learning model on a biomedical dataset (e.g., omics data) with a performance report in under 1 hour.
license: MIT
metadata:
  author: BioGeMT
  source: "https://github.com/BioGeMT/agentomics-ml"
  version: "2026.04"
compatibility:
  - system: Python 3.9+
allowed-tools:
  - run_shell_command
  - python_repl
  - read_file
---

# Agentomics ML

An autonomous agentic system built specifically for the unique challenges of biomedical machine learning. Traditional AutoML systems often struggle with domain-specific complexities like high-dimensional omics data, class imbalances, and complex feature relationships. Agentomics addresses this by leveraging LLM-driven agents to guide the ML lifecycle.

## When to Use This Skill
- You need to develop predictive models on structured biomedical data (transcriptomics, proteomics, clinical tables).
- You want an autonomous system to handle data preprocessing, feature selection, model tuning, and evaluation.
- You require interpretable machine learning pipelines that are tailored to the nuances of biological datasets.

## Core Capabilities
- **Domain-Aware Preprocessing:** Handles missing values, scaling, and feature encoding with an understanding of biological data types.
- **Intelligent Model Selection:** Agents reason about the dataset characteristics to select and tune the most appropriate algorithms (e.g., Random Forests, Gradient Boosting, SVMs).
- **Automated Evaluation:** Generates comprehensive performance reports including cross-validation metrics and feature importance.

## Example Workflow
1. Provide a labeled biomedical dataset (e.g., a CSV of gene expression data for cancer vs. normal samples).
2. Invoke `agentomics-ml` with the dataset and target variable.
3. The multi-agent system autonomously explores data processing strategies, trains multiple models, and optimizes hyperparameters.
4. Review the final generated model and performance report.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->