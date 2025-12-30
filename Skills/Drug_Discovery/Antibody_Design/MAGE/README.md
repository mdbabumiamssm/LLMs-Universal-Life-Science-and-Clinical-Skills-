# MAGE: Monoclonal Antibody Generator

**Source:** [IGlab-VUMC/MAGE_ab_generation](https://github.com/IGlab-VUMC/MAGE_ab_generation)
**Local Repository:** `./repo`
**Status:** Integrated & Downloaded

## Overview
MAGE is a cutting-edge protein language model designed to accelerate the development of monoclonal antibodies, specifically targeting novel viral strains. It represents a significant leap from screening-based discovery to generative design.

## Key Features
- **Generative Design:** Creates antibody sequences that do not exist in nature.
- **Viral Targeting:** Fine-tuned for rapid response to emerging viral threats.
- **Speed:** Reduces timeline from months to days.

## Quick Start
1.  **Environment:**
    See `repo/README.md` (root) for dependencies. Usually requires PyTorch and transformers.
2.  **Generation:**
    The core script is `repo/generate_antibodies.py`.
    ```bash
    python repo/generate_antibodies.py --antigen_sequence "YOUR_ANTIGEN_SEQ" --output_dir ./results
    ```
3.  **Data:**
    Training data and examples are in `repo/MAGE_annotated_training_data.zip`.

## Funding & Support
Supported by a **$30M ARPA-H award**.

## Integration
MAGE outputs amino acid sequences (FASTA) which should be validated using structural tools like AlphaFold 3.