# Metabolite ID Agent

## Overview
The **Metabolite ID Agent** automates the identification of unknown metabolites from Mass Spectrometry (LC-MS/MS) data. It integrates spectral similarity scoring, fragmentation tree analysis, and machine learning to annotate features with high confidence.

## Core Capabilities
- **Spectral Matching**: Queries local and remote databases (GNPS, MassBank, HMDB).
- **In Silico Fragmentation**: Uses CSI:FingerID and SIRIUS-like logic to predict structures for unknowns.
- **Spec2Vec Integration**: Utilizes spectral embeddings for finding structurally related compounds.
- **Retention Time Prediction**: Validates candidates using deep learning-based RT prediction.

## Workflow
1.  **Input**: .mzML raw data or feature lists (mass/charge, retention time).
2.  **Preprocessing**: Peak picking and alignment (via mzmine or pyopenms).
3.  **Annotation**: AI-driven spectral matching and substructure prediction.
4.  **Output**: Annotated metabolite list with confidence scores.

## Dependencies
- `pyopenms`
- `matchms`
- `spec2vec`
- `pubchempy`
