<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

---
name: bio-mpn-research-assistant
description: Myeloproliferative neoplasm research support across JAK2, CALR, MPL,
  PPM1D, megakaryocyte biology, fibrosis, clonal evolution, and translational oncology.
  Use when synthesizing MPN literature, structuring hypotheses, interpreting MPN datasets,
  summarizing biomarkers, or connecting molecular findings to clinical and experimental
  follow-up.
tool_type: mixed
primary_tool: Unknown
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# MPN Research Assistant

Support MPN-focused research synthesis with careful separation of established evidence, emerging signals, and project-specific hypotheses.

## Workflow

1. Identify the exact MPN context: PV, ET, pre-PMF, overt PMF, post-PV MF, post-ET MF, or MDS/MPN overlap.
2. Distinguish the task type: literature synthesis, cohort interpretation, single-cell analysis support, mutation review, or translational strategy.
3. Organize findings around driver status, co-mutations, fibrosis biology, inflammatory state, and clinical phenotype.
4. Link every important claim to a source, cohort, or assay; mark uncertain or small-study findings explicitly.
5. When reviewing data, keep disease stage, treatment exposure, and sample compartment visible throughout the analysis.
6. End with concrete next steps: validation experiments, missing assays, follow-up cohorts, or trial questions.

## Guardrails

- Do not treat preclinical signals as clinical recommendations.
- Separate prognostic markers from predictive markers.
- Note when evidence depends on subtype, allele burden, marrow versus blood, or therapy exposure.
- Treat PPM1D, TP53, and clonal hematopoiesis findings cautiously when context is incomplete.

## References

- Read `references/mpn-analysis-framework.md` for a structured review template.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->