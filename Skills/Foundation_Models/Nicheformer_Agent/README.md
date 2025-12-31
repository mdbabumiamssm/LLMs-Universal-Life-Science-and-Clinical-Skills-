# Nicheformer Agent

## Overview
**Nicheformer** is a foundation model specifically designed for **spatial transcriptomics**. Unlike single-cell models that treat cells in isolation, Nicheformer encodes the spatial context and cellular neighborhood ("niche"), enabling it to predict cell-cell communication and tissue organization.

## Applications
- **Niche Reconstruction**: Imputing missing spatial information from dissociated single-cell data.
- **Cell-Cell Interaction**: Predicting ligand-receptor activity based on spatial proximity.
- **Tissue Architecture**: Segmenting tissue domains (e.g., tumor core vs. invasive margin).
- **Perturbation Analysis**: Predicting how the tissue niche changes under drug treatment.

## Model Architecture
- **Input**: Spatial graph or coordinate-tagged gene expression matrices.
- **Backbone**: Graph Transformer or Spatial-Aware Transformer.
- **Training Data**: SpatialCorpus-110M (110 million spatial spots).

## Reference
- *Nicheformer: A foundation model for spatial omics (Nature Methods 2025)*