---
name: evo2-genome-model
description: Operate Arc Institute Evo 2 for long-context DNA sequence scoring, zero-shot variant effect analysis, genomic embeddings, sequence generation, and model deployment. Use when a task explicitly needs Evo 2, million-base genomic context, DNA likelihood comparisons, genomic foundation-model embeddings, or generated DNA candidates across species.
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
---

# Evo 2 Genome Model

Use Evo 2 as a genomic foundation model, not as a substitute for experimental or clinical validation.

## Workflow

1. Define the task before choosing a checkpoint:
   - score reference and alternate sequences for zero-shot variant effects;
   - consider Evo2VED as a candidate source of precomputed variant scores alongside direct Evo 2 inference; before documenting retrieval examples, verify current database access, supported genome assemblies, coordinate and reference/alternate allele conventions, score definitions and direction, variant coverage, and database/model versioning against the database documentation. Record the release and retrieval date, and treat model-derived scores as supporting research evidence rather than standalone pathogenicity classifications;
   - extract embeddings for a downstream classifier or retrieval system;
   - generate sequence continuations or design candidates;
   - fine-tune on a documented task-specific dataset.
2. Record the reference assembly, strand, coordinate convention, species, sequence length, and any ambiguous bases.
3. Choose the smallest suitable deployment:
   - use a 7B checkpoint for routine local scoring or generation on supported GPUs;
   - use 20B or 40B only when the expected gain justifies Hopper-class FP8 hardware;
   - use NVIDIA hosted API or NIM when local hardware is unsuitable.
4. Keep reference and alternate alleles in identical sequence context. Normalize variants before scoring and test reverse-complement sensitivity when strand orientation is not biologically fixed.
5. For embeddings, compare candidate intermediate layers on a held-out validation set instead of assuming the final layer is optimal.
6. For generation, preserve prompts, model identifier, temperature, top-k, random seed, and every post-generation filter.
7. Validate outputs with task-relevant baselines, external annotations, and wet-lab evidence where decisions are consequential.

## Quality Controls

- Pin the checkpoint and package version; do not rely on a moving default.
- Run the upstream generation test after installation or hardware changes.
- Exclude sequence leakage between train, validation, and test splits.
- Report uncertainty from replicate prompts, seeds, or sequence windows.
- Screen generated DNA for biosafety, synthesis constraints, off-target homology, and unintended coding potential before any experimental use.
- Label zero-shot scores as model-derived evidence, not pathogenicity classifications.

## Output Contract

Return:

- model and access path;
- input sequence provenance and preprocessing;
- scoring, embedding, or generation parameters;
- quality-control results and failed samples;
- limitations and the next orthogonal validation step.

Read `references/operations.md` for setup, checkpoint selection, examples, and canonical sources.

## References

- [Evo2VED: a database of DNA large language model-derived scores for variant interpretation](https://pubmed.ncbi.nlm.nih.gov/43021690/). Nucleic Acids Research, 2026 Nov 13.
