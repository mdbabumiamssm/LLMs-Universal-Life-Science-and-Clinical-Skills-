---
name: txgemma-therapeutics
description: Operate Google TxGemma prediction and chat models for therapeutic property prediction across small molecules, proteins, nucleic acids, diseases, targets, and cell lines. Use when formatting Therapeutics Data Commons tasks, choosing TxGemma model size or variant, running local or Model Garden inference, fine-tuning on private therapeutic data, or evaluating TxGemma in drug-discovery workflows.
---

# TxGemma Therapeutics

Use TxGemma for research prioritization and model development. Predictions and conversational rationales are not experimental measurements or mechanistic proof.

## Model Selection

- Use a `predict` checkpoint when raw predictive performance on a supported therapeutic task is the priority.
- Use a 9B or 27B `chat` checkpoint for multi-turn explanation or agentic workflows, accepting that conversational flexibility can reduce predictive performance.
- Start with 2B for constrained hardware or screening prototypes, then benchmark 9B and 27B only when the expected gain justifies the compute.

## Workflow

1. Define the endpoint, unit, label space, intended population, and downstream decision before choosing a prompt.
2. Standardize biomedical inputs: canonicalize SMILES while preserving stereochemistry, verify protein or nucleotide sequence alphabet, and normalize entity identifiers.
3. Use the official TDC prompt template for supported tasks. Preserve instructions, context, question, answer choices, and any few-shot examples exactly.
4. Select a split that reflects deployment risk: scaffold or cold-start for novel chemistry, target holdout for new proteins, and temporal split for prospective claims.
5. Pin the model revision, tokenizer, prompt template, decoding settings, and software environment.
6. Evaluate against specialist baselines with endpoint-appropriate metrics, calibration, confidence intervals, and subgroup or chemical-space slices.
7. Fine-tune only after establishing a zero-shot baseline and documenting private-data rights, leakage controls, and an external test set.
8. Route top candidates to orthogonal computational methods and experimental assays.

## Guardrails

- Do not infer causal mechanisms from generated explanations.
- Do not compare outputs across prompt templates without recalibration.
- Do not use random splits alone for claims about novel scaffolds, targets, or future trials.
- Detect invalid molecules, unsupported sequence characters, truncated prompts, and answer-format violations.
- Review the Health AI Developer Foundations terms before deployment or redistribution.
- Require assay confirmation before medicinal-chemistry, toxicology, or clinical decisions.

## Output Contract

Return the endpoint definition, model and revision, prompt template, split strategy, preprocessing, metrics, calibration, failure analysis, uncertainty, and recommended experimental validation.

Read `references/operations.md` for model identifiers, prompt formatting, local inference, and canonical sources.
