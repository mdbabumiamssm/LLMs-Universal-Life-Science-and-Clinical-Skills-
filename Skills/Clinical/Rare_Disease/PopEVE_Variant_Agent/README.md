# PopEVE Variant Agent

## Overview
The **PopEVE Variant Agent** is a specialized clinical AI for prioritizing rare disease variants. It builds upon the **EVE (Evolutionary Model of Variant Effect)** and 2025's **PopEVE** architecture, which integrates population genetics with deep generative models to predict pathogenicity with high precision.

## Capabilities
- **Evolutionary Conservation**: Analyzes MSA (Multiple Sequence Alignments) to determine residue criticality.
- **Population Awareness**: Filters standing variation using gnomAD and All of Us datasets.
- **Pathogenicity Scoring**: Outputs a continuous score (0-1) for variant deleterious effects.
- **Clinical Reporting**: Generates ACMG-style automated draft reports for geneticists.

## Inputs
- VCF (Variant Call Format) files.
- Patient phenotype terms (HPO IDs).

## References
- *PopEVE: Evolutionary deep learning for rare disease diagnosis (2025)*.
