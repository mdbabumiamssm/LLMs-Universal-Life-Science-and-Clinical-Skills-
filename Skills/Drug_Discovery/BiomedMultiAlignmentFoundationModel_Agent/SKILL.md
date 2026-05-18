<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'biomed-multi-alignment-foundation-model'
description: 'Use IBM biomed.omics.bl.sm.ma-ted-458m workflows to connect proteins, small molecules, and single-cell gene data for biomedical discovery.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Biomedical Multi-Alignment Foundation Model

## Overview

This skill guides use of the BiomedSciAI biomed-multi-alignment repository and IBM `biomed.omics.bl.sm.ma-ted-458m`, a biomedical foundation model trained across proteins, small molecules, and single-cell gene data. Use it to plan or execute multimodal biomedical discovery workflows where cross-modal alignment can help compare, retrieve, or organize biological entities. It emphasizes reproducible environment setup, input validation, and conservative interpretation of model outputs.

## When to Use This Skill

- A user asks to work with `BiomedSciAI/biomed-multi-alignment` or `ibm/biomed.omics.bl.sm.ma-ted-458m`.
- A workflow needs embeddings or aligned representations across proteins, small molecules, and single-cell gene profiles.
- A biomedical discovery task involves cross-modal retrieval, clustering, candidate prioritization, or representation analysis.
- A user wants to inspect, run, adapt, or troubleshoot notebooks from the biomed-multi-alignment repository.
- A project needs a concise workflow for validating multimodal biomedical model inputs and outputs without inventing performance claims.

## Core Capabilities

1. Repository orientation: Locate notebooks, dependency files, model-loading code, and example data paths in the upstream repository before running or modifying anything.
2. Environment setup: Create or verify the Python/Jupyter environment needed for repository notebooks, preferring pinned project instructions when available.
3. Modality preparation: Check that protein sequences, small-molecule representations, and single-cell gene data match the expected formats before inference.
4. Representation generation: Run model or notebook workflows to produce embeddings or aligned representations when the required model weights and dependencies are available.
5. Cross-modal analysis: Use generated representations for retrieval, similarity search, clustering, visualization, or candidate ranking while reporting assumptions and limitations.
6. Output validation: Confirm file existence, schema shape, modality labels, sample counts, and basic sanity checks before treating results as usable.
7. Reproducible reporting: Record repository commit, model identifier, environment details, input sources, commands run, and generated artifacts.
8. Repository-grounded `ibm/biomed.omics.bl.sm.ma-ted-458m` usage: prepare proteins as amino acid sequences in AA tokenizer prompts, small molecules as SMILES in SMILES tokenizer prompts, and single-cell inputs as repository-compatible AnnData `.h5ad` or ranked gene-expression sequences; load both `Mammal.from_pretrained(...)` and `ModularTokenizerOp.from_pretrained(...)`, tokenize prompts with attention masks, then use documented `generate`, encoder-only, fine-tuning, or inference paths before exporting embeddings, hidden states, or aligned representations for retrieval. Validate cross-modal work against repository examples such as protein-protein interaction, drug-target interaction, cell-line drug response, and scRNA cell type workflows; preserve sample IDs and modality labels, check SMILES validity, protein sequence bounds, gene ordering/truncation, and train/test splits, and treat upstream performance statements or experimental biological claims as unverified unless reproduced on the user's data.
9. IBM release context checks: Treat `ibm/biomed.omics.bl.sm.ma-ted-458m` as a 458M-parameter biomedical foundation model reported as trained over 2B+ biological samples across proteins, small molecules, and single-cell gene data. For cross-modal drug discovery use, verify that each modality is explicitly labeled, paired or compared entities remain traceable, and retrieval, similarity, or candidate-prioritization outputs are validated against the user's intended drug discovery question before reporting conclusions.

## Inputs / Outputs

Inputs this skill may consume:

- A local clone or GitHub URL for `BiomedSciAI/biomed-multi-alignment`.
- Protein sequences or protein identifiers, depending on the repository workflow.
- Small-molecule strings, structures, or identifiers, such as SMILES when supported by the workflow.
- Single-cell gene expression data or derived sample matrices in repository-compatible form.
- User goals such as embedding generation, similarity search, cross-modal comparison, or notebook troubleshooting.

Outputs this skill should produce:

- A short execution plan tied to the requested modalities and available files.
- Validated environment and dependency notes.
- Generated embeddings, tables, plots, notebooks, or analysis summaries when requested and supported.
- A reproducibility note with commands, paths, model identifier, and any known limitations.
- Clear error reports when data, dependencies, weights, or credentials are missing.

## References

- Source finding: https://github.com/BiomedSciAI/biomed-multi-alignment
