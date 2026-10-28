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
name: 'amaro-biomolecular-complex-dynamics'
description: 'Prepare and assess AMARO v2.0 heavy-atom simulations of proteins, drug-like ligands, and biomolecular complexes, with protonation-aware mapping, reference comparisons, and explicit applicability limits.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# AMARO Biomolecular Complex Dynamics

## Overview

Use this skill to prepare, configure, and evaluate AMARO v2.0 simulations of biomolecular complexes using a shared heavy-atom neural potential with implicit solvent. Hydrogen-aware bead types and total-charge conditioning enable chemically specific treatment of proteins and drug-like ligands, including ternary complexes. Treat pose retention, binding-pose recovery, and thermodynamic accuracy as separate questions.

## When to Use This Skill

- Prepare a protein, ligand, or protein–ligand complex for AMARO v2.0.
- Compare explicitly chosen protonation states or assess sensitivity to system charge.
- Investigate bound-pose stability, unbound ligand exploration, or protein–protein interface retention.
- Compare AMARO trajectories with atomistic simulations or experimental structures.
- Assess whether available sampling supports a binding free-energy analysis.

## Core Capabilities

1. **Establish execution readiness.** Read the official repository, preparation guide, simulation guide, and model card linked below before selecting commands. As checked on 2026-10-28, the paper reports checkpoint availability, but the model card explicitly says the checkpoint files and `v2.0` tag are pending. Recheck actual availability; without a verified final checkpoint, return a preparation report with execution blocked rather than simulate with substituted weights. The final model is `amaro_v2.ckpt`; the small-molecule and protein-stage checkpoints are distinct models. Record repository commit, checkpoint revision and checksum, dependency versions, and hardware.

   The repository documents Linux, Python 3.13, PyTorch 2.8.0, CUDA 12.6, and a compatible NVIDIA GPU. Follow its constrained installation and recursive submodule instructions in an isolated environment. Check dependency consistency, OpenMM installation, availability of `PythonForce`, and CUDA visibility. Installation instructions are documented, not locally execution-tested by this skill. Do not invent package names or runner arguments if the guides cannot be retrieved.

2. **Prepare chemically consistent inputs.** Resolve alternate conformations, missing atoms, chain identities, ligand bond orders, stereochemistry, termini, and protonation before mapping. Preserve the biological assembly and reference atom correspondence. Enumerate uncertain protonation states as separate systems; regenerate both bead types and total solute charge for each state.

   Use the official v2 NOH mapping, whose species IDs encode heavy atoms and their associated hydrogen counts; ordinary atomic numbers and the v1 mapping are not interchangeable substitutes. Preserve bead ordering and the documented mass assignment. Verify total charge from all retained components. Remove explicit solvent and distinguish removable counterions from functionally retained ions; do not silently discard an essential cofactor to make a system run. Reject unmapped species and report unsupported chemistry.

3. **Configure a bounded pilot.** Use the official prepared example first when the environment is new, then apply the same checks to the requested system. The paper's default protocol uses OpenMM 8.5, minimization for at most 2,000 L-BFGS iterations, nonperiodic NVT at 300 K, Langevin-middle dynamics, friction 1 ps⁻¹, a 4 fs timestep, and output every 0.1 ns. Its optimized backend is Acellera-TensorNet; the public repository also documents PythonForce. Treat backend performance as implementation-specific. [Methods](https://arxiv.org/html/2610.37606v1)

   Confirm coordinate, force, and energy conversions at the model–engine boundary. Specify random seeds, duration, output interval, restraints, and stopping conditions. Use the documented restraint definitions and system-specific dimensions for reproductions of unbound-ligand experiments; do not transfer them to unconstrained stability studies without justification. Stop on nonfinite energies or forces, mapping failures, or visibly corrupted geometry. Save diagnostic evidence instead of extending a failed run.

4. **Compare appropriate observables.** Align the receptor before computing ligand heavy-atom RMSD; retain a consistent atom mapping and document symmetry handling. Report protein RMSD, ligand contacts, pose occupancy, and interchain contacts separately. Compare partner-chain self-alignment with receptor alignment to distinguish internal deformation from assembly reorientation.

   Use matched starting structures, protonation, reference poses, restraint conditions, and replicate counts for atomistic comparisons. Report both simulated duration and measured hardware time, including how throughput was obtained. The finding's 3.3-fold pose-recovery advantage concerns trypsin–benzamidine at a fixed estimated GPU-time budget; it is not a universal speedup or accuracy guarantee. Predefine recovery criteria and report uncertainty across independent trajectories.

5. **Assess thermodynamics and applicability.** For sufficiently sampled trajectories, define bound and bulk states, inspect transitions and convergence, and test sensitivity to state definitions. Binding free energies require population estimates plus an effective-volume/standard-state correction; raw potential energies or pose-retention fractions are not binding affinities. Report unavailable estimates when sampling cannot support them, and do not interpret coarse-grained trajectory time as validated physical kinetics without a reference comparison.

   The reported structural benchmark comprises 262 complexes across 11 targets; short bound-state retention does not establish general binding prediction. HIF2A shows assembly reorientation, SHP2 exposes pose-recovery limitations, and CDK8 exposes site-specificity limitations. Reported trypsin–benzamidine and TYK2–EJM31 binding free energies are more favorable than experimental references. [Source finding](http://arxiv.org/abs/2610.37606v1)

   The broader structural benchmark uses cofactor-free complexes, while the trypsin reconstruction includes calcium. These cases do not validate arbitrary metalloproteins. Treat nucleic acids, membranes, covalent reactions, unusual cofactors, and untested charge or element combinations as unverified unless additional evidence establishes support. A representable element is not proof of validated chemistry.

## Inputs / Outputs

**Inputs**

- Protein/complex coordinates and ligand chemical structures with atom identities, connectivity, and reference pose where available.
- Intended assembly, protonation assumptions, total charge, retained ions/cofactors, and scientific question.
- Verified AMARO v2 checkpoint, compatible environment, hardware budget, simulation protocol, and reference data.

**Outputs**

- Preparation assessment: retained components, atom-to-bead correspondence, protonation decisions, charge reconciliation, unsupported features, and missing prerequisites.
- Reproducible configuration: exact software/checkpoint identifiers, units, seeds, integration settings, restraints, and planned comparisons.
- When execution is possible: pilot logs and trajectory with finite-value and geometry checks, followed by requested structural summaries.
- Evidence-qualified analysis distinguishing observations, uncertainty, applicability limits, and unperformed work.

**Fifteen-minute completion criterion:** deliver a checked preparation/configuration report and, only if dependencies and weights are ready, a bounded smoke test. A missing checkpoint is a documented blocked simulation, not a successful dynamics result. Production sampling, installation, rare-event recovery, and converged free energies are not promised within this window; state the next required step and estimated resource needs.

## References

- [A unified coarse-grained neural network potential for the dynamics of biomolecular complexes, arXiv:2610.37606v1](http://arxiv.org/abs/2610.37606v1) — source finding; [full text and methods](https://arxiv.org/html/2610.37606v1).
- [Official AMARO code and installation documentation](https://github.com/compsciencelab/amaro) — implementation and environment prerequisites.
- [System preparation guide](https://github.com/compsciencelab/amaro/blob/main/system-prepare/README.md) — official mapping and preparation entry point; linked by the repository, but detailed contents were not retrievable during authoring.
- [OpenMM PythonForce guide](https://github.com/compsciencelab/amaro/blob/main/openmm-pythonforce/README.md) — official runner entry point; linked by the repository, but detailed contents were not retrievable during authoring.
- [AMARO2 model card and checkpoint availability](https://huggingface.co/compsciencelab/AMARO2) — release status and representation requirements; recheck before execution.
