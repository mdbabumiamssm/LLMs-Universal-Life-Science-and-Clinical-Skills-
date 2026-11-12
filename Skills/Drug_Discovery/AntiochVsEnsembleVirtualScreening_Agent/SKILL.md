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
name: 'antioch-vs-ensemble-virtual-screening'
description: 'Plan and run ANTIOCH-VS ensemble virtual screening from protein sequence or receptor structures through conformational selection, docking, consensus ranking, and physics-based hit triage.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# ANTIOCH-VS Ensemble Virtual Screening

## Overview

Use ANTIOCH-VS to connect protein sequence or supplied receptor structures to conformational ensemble selection, pocket detection, ligand preparation, docking, and a reproducible candidate shortlist. Ensemble screening addresses sensitivity to receptor conformation, while AF2RAVE state selection and subsequent CTMD triage provide complementary physical information. Treat ranked compounds as computational hypotheses requiring experimental validation.

The 15-minute outcome applies to a documented preflight and execution plan, or a tiny docking smoke test with dependencies and prepared inputs already available. It is not a runtime claim for sequence prediction, MD, library-scale screening, or CTMD; report exactly which stages completed.

## When to Use This Skill

- Start a screening campaign from a protein sequence without a ligand-bound crystal structure.
- Screen a ligand library against multiple supplied or predicted receptor conformations.
- Compare single-structure and ensemble rankings under matched docking conditions.
- Prepare a reproducible workstation or HPC workflow using DOCK6 or AutoDock Vina.
- Select receptor–ligand pairs for physics-based triage and experimental follow-up.

## Core Capabilities

1. **Verify interfaces and define the campaign.** Record the repository commit, target construct, ligand-library identity, intended binding site, selected modules, and compute budget. Read the relevant module guide, configuration template, and executable argument parser at that commit before constructing commands. The interfaces below were checked against repository documentation on 2026-11-11; recheck installed versions. The supplied arXiv abstract could not be independently retrieved during authoring, so its scientific claims remain attributed to the supplied finding.

   The repository advertises an `antioch-vs` launcher and supplies `full_pipeline/`, but do not infer a sequence-to-hits command or flags from that name. Inspect the launcher and orchestration script before use. Prefer verified standalone modules if orchestration is unavailable. Documentation conflicts should be resolved against executable code and a small test, not silently treated as implemented functionality.

2. **Validate inputs and plan dependencies.** Confirm the sequence, chain/domain boundaries, mutations, disulfides, cofactors, and membrane versus soluble context. Preserve stable parent-compound identifiers through stereoisomer, tautomer, protonation, and conformer generation; record exclusions and failed preparations. Choose protonation and charge treatment appropriate to the planned assay conditions.

   Install only the dependencies required by selected modules, following their environment files. Check ColabFold/AF2RAVE requirements for ensemble generation; DOCK6 and UCSF Chimera for the DOCK6 route; Vina or Vina-GPU and the specified preparation environment for Vina; P2Rank with Java or GrASP for pocket detection; and AmberTools plus the required simulation engine for MD/CTMD. Confirm CPU/GPU availability, RAM, scratch space, container binds, scheduler limits, and executable paths. Estimate production resources from a small pilot; a complete campaign is not a 15-minute job.

3. **Generate and select receptor states.** For sequence input, follow `structure_prediction_module/README.md` to generate reduced-MSA ColabFold ensembles, select features, cluster conformations, run unbiased MD, and apply SPIB within AF2RAVE. Record MSA settings, seeds, simulation conditions, state assignments, sampling diagnostics, and the origin of state populations. Inspect binding-site geometry and missing residues before accepting representatives. Supplied structures may enter downstream directly, but must not be described as AF2RAVE-derived or Boltzmann-weighted without the corresponding analysis.

4. **Prepare comparable binding sites and docking inputs.** Use a justified known site or review P2Rank/GrASP predictions; the highest-ranked predicted pocket is a candidate site, not proof of the biological site. Map chains and residues across the ensemble and confirm each box covers the same intended pocket in that receptor's coordinate frame. Preserve relevant cofactors and document deletions, capping, and loop truncation.

   DOCK6 uses receptor preparation outputs including MOL2 and DMS, a MOL2 ligand library, and a reference ligand or pocket-definition YAML. Vina uses a receptor PDB/PDBQT and a directory of ligand PDBQT files. In Vina configuration, `paths.pocket_definition` can supply a detected pocket; automatic box settings otherwise require the documented residue CSV. Check atom-type compatibility before routing ligands to Vina-GPU; do not change chemistry merely to make an unsupported input parse.

5. **Run a bounded test, then ensemble docking.** Make run-specific copies of the upstream configuration templates and replace installation paths, receptor/library paths, box settings, resource allocations, seeds where supported, and output directories. From the repository root, the documented standalone CPU Vina command has this form:

   ```bash
   python docking_module/vina_pipeline/vina_cpu_pipeline.py \
     --config /absolute/path/to/run/vina_cpu_config.yaml
   ```

   The alternative DOCK6 route has two documented stages:

   ```bash
   python docking_module/dock6_pipeline/chimera_pipeline.py \
     --config /absolute/path/to/run/chimera_config.yaml
   python docking_module/dock6_pipeline/dock6_pipeline.py \
     --config /absolute/path/to/run/dock6_config.yaml
   ```

   These paths are templates to replace, not ready-to-run local files. Start with one prepared receptor and a few ligands. Accept the smoke test only if outputs contain parseable poses, finite scores, matching ligand IDs, and poses in the intended box; inspect logs and account for failures. For production, repeat across the selected receptors with comparable settings and separate output directories. Use fresh directories rather than automatically passing destructive overwrite options. Stop expansion when systematic preparation or docking failures appear, identify the first failed stage, and resume only after fixing its cause.

6. **Extract scores and assess receptor-state sensitivity.** Use `docking_module/post_docking_analysis/extract_docking_results.py` with the verified engine selector, for example:

   ```bash
   python docking_module/post_docking_analysis/extract_docking_results.py \
     --software vina \
     -i /absolute/path/to/run/vina_output \
     --out_dir /absolute/path/to/run/vina_summary \
     --out_parquet vina_summary.parquet \
     --out_csv top_hits.csv
   ```

   Confirm extraction dependencies and argument support in the checkout. Collapse poses and enumerated chemical variants consistently to the intended compound unit before comparing hit counts. Preserve per-receptor ranks, raw scores, source poses, missing results, and failure counts. Do not average DOCK6 and Vina raw scores as though they shared a scale.

   The repository describes unweighted reciprocal-rank fusion across receptors. Verify the implementation's rank offset, tie handling, and treatment of missing ligands before applying it. Boltzmann-informed receptor selection does not imply Boltzmann-weighted consensus scoring. Compare the consensus shortlist with individual-state rankings and a leave-one-state-out analysis; flag candidates supported by only one conformation or unstable under reasonable state choices. Report docking coverage alongside rank changes.

7. **Stage physics-based triage without overstating completion.** Select the actual receptor and pose associated with each shortlisted compound. The CTMD guide requires one project per selected receptor–ligand pairing, with `rec_prepped.pdb` and docked MOL2 input under `molecules/`. Run its preparation script from that project directory only after checking environment and resource requirements:

   ```bash
   bash /absolute/path/to/antioch-vs/ctmd_module/prepare_ctmd.sh ./rec_prepped.pdb
   ```

   Verify `system.prmtop`, `system.inpcrd`, `system.pdb`, charge treatment, and setup logs. The root README and CTMD guide document preparation, while the docking guide contains an older placeholder statement. Neither preparation output nor successful topology generation proves completed CTMD. Production protocols remain user supplied: establish force fields, equilibration, membrane treatment when applicable, collective variables, bias parameters, replicates, and convergence criteria before simulations. Keep CTMD results separate from docking scores and avoid claiming validated affinity from either alone.

8. **Deliver a traceable shortlist and validation plan.** Record input checksums, repository commit, software/container versions, commands, configurations, seeds, resource use, logs, failures, and stage status. For retrospective evaluation, keep known binder/decoy labels out of tuning and report the precise library denominator, top-k precision, and enrichment relative to its active fraction. The supplied finding reports DUD-E results for JAK2 and ADRB2; those target-specific retrospective outcomes do not establish prospective hit rates for another target.

   Prioritize chemically diverse, inspectable candidates and identify assay-relevant liabilities. Require experimental confirmation through suitable binding or functional assays, concentration-response measurements, orthogonal confirmation, and relevant interference/selectivity controls before calling candidates confirmed binders. Computational rankings alone do not demonstrate efficacy or safety.

## Inputs / Outputs

**Inputs**

- Protein sequence with construct details, or receptor structures/ensemble with chain and residue mappings.
- Ligand library with stable IDs and chemical structures; optional known binders and decoy labels for retrospective evaluation.
- Known-site evidence or permission to predict pockets; preparation choices and intended assay conditions.
- ANTIOCH-VS checkout, module configuration templates, installed external tools, and workstation/HPC resource limits.
- For MD/CTMD execution, a scientifically specified production protocol and suitable simulation environment.

**Outputs**

- Within the bounded initial workflow: a preflight report listing validated inputs, dependency status, selected stages, resource estimate, exact next commands, and unresolved blockers; optionally a verified smoke-test result.
- After ensemble preparation: receptor-state manifest, structures, pocket definitions, and documented selection evidence.
- After docking: prepared-input provenance, poses, per-receptor score/rank tables, coverage and failure accounting, and consensus shortlist with receptor-state sensitivity notes.
- After CTMD setup or execution: clearly labeled preparation artifacts or completed simulation analyses, with their diagnostics and limitations.
- A reproducibility manifest and experimental follow-up plan. Explicitly label skipped, blocked, staged, running, and completed stages; a launch or prepared configuration is not a completed screen.

## References

- [ANTIOCH-VS: From Sequence to Hits with Modular, Open-Source Ensemble Virtual Screening — supplied source finding, arXiv:2611.14287v1](http://arxiv.org/abs/2611.14287v1).
- [ANTIOCH-VS repository and overview](https://github.com/tiwarylab/antioch-vs).
- [Structure prediction and ensemble generation guide](https://github.com/tiwarylab/antioch-vs/blob/main/structure_prediction_module/README.md).
- [Docking interfaces, configurations, and result extraction guide](https://github.com/tiwarylab/antioch-vs/blob/main/docking_module/README.md).
- [CTMD and AMBER preparation guide](https://github.com/tiwarylab/antioch-vs/blob/main/ctmd_module/README.md).
