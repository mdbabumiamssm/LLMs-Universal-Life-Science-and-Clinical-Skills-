---
name: bioemu-protein-ensembles
description: Operate Microsoft BioEmu to sample approximate equilibrium conformational ensembles for protein monomers from amino-acid sequences or supplied MSAs. Use when studying protein flexibility, alternative conformations, free-energy landscapes, disorder, ensemble generation, physical steering, or downstream side-chain reconstruction and MD relaxation.
---

# BioEmu Protein Ensembles

Use BioEmu when a single static structure is insufficient. It samples monomer ensembles and does not replace molecular dynamics, multimer modeling, or experimental biophysics.

## Workflow

1. Confirm that the target is a protein monomer. Route multimers or ligand complexes to a complex-prediction workflow.
2. Validate the amino-acid sequence, residue numbering, construct boundaries, mutations, tags, and disordered regions.
3. Decide whether to use automatic ColabFold MSA retrieval or a supplied A3M file. Record the MSA source and date.
4. Estimate sample count from protein length, available GPU memory, and the downstream analysis. Start with a small pilot before requesting thousands of conformations.
5. Run default sampling, then inspect the fraction removed for clashes or chain discontinuities.
6. If physical failure rates are high, enable the official steering configuration and compare steered versus unsteered distributions.
7. Cluster the retained ensemble and quantify structural diversity with RMSD, radius of gyration, contacts, secondary structure, or task-specific collective variables.
8. Reconstruct side chains and perform optional short relaxation only for representative structures, not blindly for the entire ensemble.
9. Compare ensemble observables with experimental data or independent simulations when available.

## Guardrails

- Do not interpret sampling frequency as a calibrated experimental population without validation.
- Do not use the linker trick as a validated multimer workflow.
- Report filtered sample counts; never analyze only the requested count.
- Preserve checkpoint, seed, MSA, steering configuration, and filtering settings.
- Treat large disordered regions and long proteins as higher-risk for clashes, chain breaks, and prohibitive runtime.
- Separate generated backbone ensembles from reconstructed or MD-relaxed all-atom structures.

## Output Contract

Return the input construct, MSA provenance, checkpoint, sampling and steering parameters, requested and retained counts, QC failure rates, ensemble summary, representative structures, and limitations.

Read `references/operations.md` for installation, CLI examples, steering, post-processing, and canonical sources.
