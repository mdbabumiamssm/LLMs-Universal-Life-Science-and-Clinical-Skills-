# AIMarkerFinder Agent

## Overview
**AIMarkerFinder Agent** is a specialized tool for discovery of metabolic biomarkers in high-dimensional datasets. It addresses the "small n, large p" problem common in metabolomics by using ensemble feature selection and stable AI algorithms.

## Features
- **Ensemble Feature Selection**: Combines LASSO, Random Forest, and SVM-RFE to identify robust markers.
- **Stability Analysis**: Bootstrapping methods to ensure selected biomarkers are reproducible.
- **Pathway Enrichment**: Automatically maps selected metabolites to KEGG/Reactome pathways.
- **Clinical Classifier**: Trains a final diagnostic model using the identified panel.

## References
- *AIMarkerFinder: A new AI-assisted method for biomarker discovery (2025)*
