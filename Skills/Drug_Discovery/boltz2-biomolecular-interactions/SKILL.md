---
name: boltz2-biomolecular-interactions
description: Run Boltz-2 biomolecular interaction predictions for protein, nucleic-acid, ligand, and complex structures with binding-affinity outputs. Use for hit discovery, binder-versus-decoy prioritization, hit-to-lead comparisons, lead optimization, complex modeling, or reproducible Boltz YAML and batch inference workflows.
---

# Boltz-2 Biomolecular Interactions

Use Boltz-2 when structure and affinity need to be modeled together. Treat predictions as prioritization evidence, not assay results.

## Workflow

1. Define the decision:
   - complex structure prediction;
   - binder-versus-decoy ranking for hit discovery;
   - relative affinity comparison for hit-to-lead or lead optimization.
2. Standardize every input:
   - verify polymer sequences and chain identities;
   - preserve ligand stereochemistry, protonation assumptions, and identifiers;
   - document covalent bonds, templates, restraints, and modified residues.
3. Create one Boltz YAML per complex or a directory for batch inference.
4. Pin the Boltz package or container version. Do not rely on the latest model changing silently.
5. Run prediction with an approved MSA path. Record whether the public MSA server, a private server, or precomputed MSAs were used.
6. Interpret affinity outputs according to their training objective:
   - use `affinity_probability_binary` to separate likely binders from decoys;
   - use `affinity_pred_value` to compare affinity among plausible binders and close analogs.
7. Inspect structural confidence, interface plausibility, ligand pose, clashes, chemistry, and agreement across replicates.
8. Compare with orthogonal docking, physics-based calculations, known SAR, and biochemical assays before advancing compounds.

## Affinity Semantics

The official repository states that `affinity_pred_value` is reported as `log10(IC50)` derived from IC50 measured in micromolar. Do not mix it with pKd, binding free energy, or untransformed IC50 values.

## Guardrails

- Do not compare affinity values across incompatible assay types or unrelated target systems without calibration.
- Do not rank molecules that differ because of unresolved protonation, tautomer, stereochemistry, or covalent-state errors.
- Do not use a high structural confidence score as proof of binding.
- Keep train/test leakage and benchmark overlap in mind when evaluating known complexes.
- Flag unsupported chemistry, missing atoms, low-complexity sequences, and MSA failures.
- Require experimental confirmation before medicinal-chemistry or clinical decisions.

## Output Contract

Return input provenance, Boltz version, YAML and MSA settings, structural confidence, affinity fields with units and semantics, QC findings, ranked candidates, and the experimental validation plan.

Read `references/operations.md` for installation, command patterns, affinity interpretation, and canonical sources.
