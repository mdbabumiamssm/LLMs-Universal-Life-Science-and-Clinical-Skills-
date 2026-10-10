---
name: protenix-structure-prediction
description: Operate ByteDance Protenix-v2 for open biomolecular structure prediction of proteins, antibodies, nucleic acids, ligands, and complexes using JSON inputs, MSA and template features, constraints, and inference-time sampling. Use when running Protenix locally or through its server, comparing AlphaFold3-style open models, or building reproducible co-folding evaluations.
---

# Protenix Structure Prediction

Use Protenix for structural hypotheses and model comparison. Confidence and plausibility scores do not establish binding, function, or experimental correctness.

## Workflow

1. Define the biological assembly and decision: monomer fold, protein complex, antibody-antigen interface, protein-nucleic-acid complex, or protein-ligand pose.
2. Standardize the JSON input:
   - verify chain sequences, stoichiometry, residue modifications, ligand identity, stereochemistry, and covalent bonds;
   - document templates, MSA sources, atom-level contacts, pocket constraints, and any missing features.
3. Select the model deliberately:
   - use `protenix-v2` for current high-accuracy inference;
   - use the 2021-09-30 cutoff model for leakage-controlled comparison with AlphaFold3-era benchmarks;
   - use the later-cutoff applied model for practical targets when benchmark comparability is not the goal.
4. Pin the Protenix release, model identifier, input JSON, MSA pipeline, templates, seeds, and sampling budget.
5. Start with a small inference budget, then increase seeds or samples only when interface confidence and candidate diversity justify the cost.
6. Inspect chain geometry, clashes, ligand chemistry, interface contacts, model confidence, and agreement across samples.
7. Compare against an orthogonal predictor or experimental structure when available.
8. Use PXMeter or another leakage-aware benchmark for claims about comparative accuracy.

## Guardrails

- Do not treat a high confidence score as evidence of biochemical binding or affinity.
- Separate benchmark models by training-data cutoff.
- Do not ignore invalid ligands, protonation, tautomer, stereochemistry, metal coordination, or covalent state.
- Report MSA and template failures instead of silently falling back.
- Preserve all candidate structures; avoid reporting only the visually preferred pose.
- Require experimental validation for drug, antibody, or therapeutic decisions.

## Output Contract

Return the assembly definition, model and cutoff, JSON and feature provenance, sampling budget, confidence and QC findings, structural diversity, comparison baseline, and validation plan.

Read `references/operations.md` for installation, commands, model choices, and canonical sources.
