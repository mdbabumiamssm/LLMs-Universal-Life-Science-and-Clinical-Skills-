# Precision Oncology Agent

**Source:** [Nature Cancer 2025](https://www.nature.com/articles/s43018-025-00991-6)
**Status:** Integrated Skill Reference

## Overview
This agent represents a high-performance implementation of multimodal AI for precision oncology. It combines genomic data, pathology imaging, and clinical history to recommend personalized treatments.

## Architecture
- **Vision Module:** Analyzes H&E slides for tumor grade and immune infiltration.
- **Genomic Module:** Interprets VCF files for actionable mutations (BRAF, KRAS, MSI status).
- **Knowledge Module:** RAG system connected to OncoKB and NCCN guidelines.
- **Decision Engine:** Synthesizes inputs to propose drug combinations.

## Performance
- Achieved **87.2% accuracy** in treatment recommendations compared to a tumor board (vs 30.3% for base GPT-4).
- Demonstrates the necessity of *multimodal* context for clinical AI.
