# Pheno-Genotype Matcher

## Overview
This agent acts as a "computational geneticist," bridging the gap between clinical phenotypes and genomic data. It uses Large Language Models (LLMs) to extract phenotypes from clinical notes and matches them against candidate variants using algorithms like Exomiser and AMIE-inspired reasoning.

## Workflow
1.  **Phenotype Extraction**: NLP parsing of clinical notes to HPO terms.
2.  **Variant Filtering**: Hard filtering based on inheritance models (dominant/recessive).
3.  **Semantic Similarity**: Calculating vector similarity between patient phenotype and gene-disease profiles.
4.  **Ranking**: Prioritizing genes based on combined phenotypic and genotypic scores.

## Key Integration
- **AMIE (Artificially Intelligent Medical Epidemiology)**: Diagnostic reasoning logic.
- **PhenoDB / OMIM**: Knowledge base connectivity.
