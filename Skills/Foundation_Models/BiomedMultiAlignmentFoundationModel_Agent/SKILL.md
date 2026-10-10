---
name: 'biomed-multi-alignment-foundation-model'
description: 'Use IBM biomed.omics.bl.sm.ma-ted-458m for setup, modality routing, embeddings, retrieval, and drug-discovery workflows across proteins, small molecules, and single-cell data.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

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

# Biomed Multi-Alignment Foundation Model

## Overview

Use this skill to work with `ibm/biomed.omics.bl.sm.ma-ted-458m`, a biomedical foundation model introduced by the `BiomedSciAI/biomed-multi-alignment` repository for aligned representation learning across proteins, small molecules, and single-cell gene data. The workflow emphasizes correct setup, modality-aware preprocessing, embedding extraction, cross-modal retrieval, and cautious interpretation for biomedical discovery tasks.

## When to Use This Skill

- Use when a task mentions `biomed-multi-alignment`, `ibm/biomed.omics.bl.sm.ma-ted-458m`, or the `BiomedSciAI/biomed-multi-alignment` GitHub repository.
- Use when routing protein sequences, small-molecule structures, or single-cell gene expression inputs into a shared biomedical embedding workflow.
- Use when building cross-modal retrieval, similarity search, candidate prioritization, or exploratory drug-discovery workflows that span biological modalities.
- Use when comparing this multi-alignment model against existing single-modality protein, molecule, or single-cell foundation-model skills.
- Use when validating whether a result is an embedding-level association, a retrieval hit, or a claim that requires external biological or experimental evidence.

## Core Capabilities

1. **Repository and model setup**: Fetch or read the upstream repository instructions, confirm dependency and checkpoint requirements, record the repository commit or model revision, and verify that example inference runs complete before using the model on user data.
2. **Primary implementation reference**: Use `BiomedSciAI/biomed-multi-alignment` as the implementation reference for IBM `biomed.omics.bl.sm.ma-ted-458m`, covering setup, modality routing across proteins, small molecules, and single-cell gene data, embedding extraction, retrieval use, and cross-modal drug-discovery validation.
3. **IBM multi-alignment implementation notes**: Treat `ibm/biomed.omics.bl.sm.ma-ted-458m` as a multi-modal embedding model introduced for more than 2 billion biological samples across proteins, small molecules, and single-cell gene data; keep modality routing explicit, extract embeddings through the repository-supported path, run only repository-documented example or benchmark sanity checks, use retrieval as hypothesis generation, require cross-modal hits to be checked against modality-specific metadata or external evidence, and avoid presenting drug-discovery rankings as binding, mechanism, safety, or efficacy claims.
4. **Finding-driven route-and-retrieve workflow**: For `ibm/biomed.omics.bl.sm.ma-ted-458m`, route proteins, small molecules, and single-cell inputs into their modality-specific preprocessing paths, extract comparable embeddings, run retrieval across the requested modality pairs, and validate any drug-discovery hypothesis with source metadata and external biological or experimental evidence.
5. **Implementation evidence from BiomedSciAI**: Use the `BiomedSciAI/biomed-multi-alignment` repository as implementation evidence for IBM `biomed.omics.bl.sm.ma-ted-458m` setup, checkpoint provenance review, modality routing across proteins, small molecules, and single-cell data, embedding retrieval workflow, and cross-modal validation checks.
6. **Input modality routing**: Classify each input as protein sequence, small molecule, or single-cell gene data, then apply the repository-supported tokenizer, featurizer, or preprocessing path for that modality.
7. **Protein workflow support**: Validate amino-acid sequences, preserve identifiers and species metadata when available, batch inputs by length where practical, and treat isoforms or truncated sequences as distinct records.
8. **Small-molecule workflow support**: Accept SMILES, InChI, or structure-derived records when supported by the local stack, canonicalize molecules with a chemistry toolkit when available, and keep salts, stereochemistry, and invalid structures visible in output metadata.
9. **Single-cell workflow support**: Preserve gene identifiers, cell labels, batch annotations, and normalization state, and align feature order to the model or repository configuration before embedding.
10. **Embedding extraction**: Generate per-record embeddings, save them with modality, source identifier, model revision, preprocessing notes, and dimensionality, and normalize vectors only when the retrieval or comparison method requires it.
11. **Cross-modal retrieval**: Build a similarity search table or vector index, compute nearest neighbors across selected modalities, and report scores as model-space similarity rather than direct evidence of binding, mechanism, safety, or efficacy.
12. **Drug-discovery use cases**: Support target-to-compound exploration, molecule-to-cell-state retrieval, perturbation hypothesis generation, and hit triage while requiring downstream chemistry, biology, and experimental validation.
13. **Validation limits**: Do not invent benchmark results, clinical claims, mechanism claims, or accuracy numbers; distinguish repository examples from validated performance and cite the source of any external comparison.
14. **Single-modality comparison**: When the user asks whether to use this model or a single-modality foundation model, compare input coverage, embedding alignment needs, available validation, interpretability, runtime constraints, and task-specific baselines.
15. **License and model-card checks**: Before using `BiomedSciAI/biomed-multi-alignment` or `ibm/biomed.omics.bl.sm.ma-ted-458m`, read the repository license, model card, checkpoint terms, and usage restrictions; record any access, redistribution, or data-use constraints alongside embedding and retrieval outputs.
16. **GitHub finding route for `ibm/biomed.omics.bl.sm.ma-ted-458m`**: Start from the `BiomedSciAI/biomed-multi-alignment` setup path, route proteins, small molecules, and single-cell gene data through their supported preprocessing paths, extract embeddings with revision and modality metadata, use cross-modal retrieval for candidate ranking or hypothesis generation, and limit drug-discovery conclusions to model-space associations unless external validation is supplied.
17. **2026 repository finding guidance**: Treat the GitHub finding as evidence that `ibm/biomed.omics.bl.sm.ma-ted-458m` was introduced as a biomedical foundation model trained over 2 billion biological samples across proteins, small molecules, and single-cell gene data; begin with repository setup and checkpoint review, route each modality through its supported preprocessing path, extract embeddings with modality metadata, use cross-modal retrieval for model-space hypotheses, avoid benchmark claims unless the repository documents them, use it for drug-discovery work when aligned target-compound, molecule-cell-state, or perturbation retrieval is needed, and use it for general omics representation learning when the task centers on embeddings, clustering, retrieval, or comparison rather than validated binding, mechanism, safety, or efficacy prediction.
18. **Setup-to-retrieval operating path for `ibm/biomed.omics.bl.sm.ma-ted-458m`**: Pin the repository or model revision, follow the upstream setup instructions, smoke-test a minimal example, route protein, small-molecule, and single-cell records through their modality-specific preprocessing paths, extract embeddings with record identifiers and modality metadata, build retrieval tables or vector indexes for the requested modality pairs, validate retrieved neighbors with input-quality checks and source metadata, and frame drug-discovery output as candidate prioritization or hypothesis generation rather than verified activity.
19. **Pre-drug-discovery readiness gate**: Before using `ibm/biomed.omics.bl.sm.ma-ted-458m` for drug-discovery candidate prioritization, verify setup against the upstream repository, check the model card and checkpoint terms, route proteins, small molecules, and single-cell gene data through their documented preprocessing paths, benchmark multi-modal embeddings and cross-modal retrieval only with repository-documented examples or user-provided baselines, and keep rankings framed as hypotheses until independent validation is supplied.
20. **Modality-pair retrieval planning**: For tasks using `ibm/biomed.omics.bl.sm.ma-ted-458m`, first identify the requested modality pair or trio among proteins, small molecules, and single-cell gene data; then use the repository setup path to extract embeddings for each routed input, run cross-modal retrieval or validation against user-provided labels or metadata, and apply drug-discovery use cases such as target-compound, molecule-cell-state, or perturbation prioritization only as model-space evidence.
21. **Repository-specific operational guidance from the 2026 GitHub finding**: Treat `BiomedSciAI/biomed-multi-alignment` as the source for setup and usage of `ibm/biomed.omics.bl.sm.ma-ted-458m`; inspect the README, notebooks, model card, license, checkpoint terms, dependency versions, and documented hardware expectations before inference; route proteins, small molecules, and single-cell gene data through their repository-supported preprocessing paths; extract embeddings with model revision, modality, and device metadata; use cross-modal retrieval for target-compound, molecule-cell-state, or perturbation hypothesis generation; and validate results with repository examples, user-provided baselines, input-quality checks, metadata review, and external biological or experimental evidence before making drug-discovery claims.

## Inputs / Outputs

**Inputs consumed by this skill**

- Repository URL, local checkout, notebook, script, or model identifier for `BiomedSciAI/biomed-multi-alignment` or `ibm/biomed.omics.bl.sm.ma-ted-458m`.
- Protein sequences with identifiers and optional organism, isoform, domain, or annotation metadata.
- Small-molecule records such as SMILES, InChI, SDF-derived tables, compound IDs, or assay-linked metadata.
- Single-cell gene expression inputs such as matrices, AnnData objects, gene lists, cell labels, or perturbation annotations.
- User objective, such as embedding extraction, cross-modal retrieval, candidate ranking, clustering, visualization, or model comparison.

**Outputs produced by this skill**

- A setup checklist or executable workflow based on the current repository instructions.
- Cleaned and routed modality-specific input tables with validation notes.
- Embedding files or in-memory arrays linked to record identifiers and model revision metadata.
- Cross-modal retrieval results with similarity scores, rank positions, modality labels, and caveats.
- Drug-discovery or biomedical interpretation notes that separate model-derived hypotheses from experimentally supported conclusions.
- Comparison guidance against relevant single-modality workflows in the local skill library.

## References

- Source finding and repository: https://github.com/BiomedSciAI/biomed-multi-alignment
- GitHub source for `ibm/biomed.omics.bl.sm.ma-ted-458m`: https://github.com/BiomedSciAI/biomed-multi-alignment
