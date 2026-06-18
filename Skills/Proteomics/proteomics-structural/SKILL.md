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
name: bio-proteomics-structural
description: Structural proteomics and cross-linking MS analysis using XlinkX, pLink,
  or xiSEARCH.
tool_type: mixed
primary_tool: proteomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 🏗️ Structural Proteomics

Cross-linking mass spectrometry (XL-MS) analysis. Identifies protein-protein interaction interfaces and distance constraints.

## CLI Reference

```bash
python omicsclaw.py run struct-proteomics --demo
python omicsclaw.py run struct-proteomics --input <data.csv> --output <dir>
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--method` | `xlinkx` | xlinkx, plink, or xisearch |

## Why This Exists

- **Without it**: Identifying inter-linked peptides is a computational nightmare computationally mapping combinatorial massive search spaces
- **With it**: Efficiently deconvolutes cross-linker mass shifts to prove physical protein-protein interactions
- **Why OmicsClaw**: Standardizes structural XL-MS parsing which is traditionally highly vendor-locked

## Workflow

1. **Calculate**: Generate combinatorial databases based on cross-linker specificity.
2. **Execute**: Score intra- and inter-peptide linkages.
3. **Assess**: Estimate coordinate FDR constraints.
4. **Generate**: Output structural distance restraints.
5. **Report**: Synthesize 2D interaction network topologies.

## Example Queries

- "Analyze cross-linking MS data with XlinkX"
- "Find protein interactions from this pLink output"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── crosslinks.csv
├── figures/
│   └── interaction_network.png
├── tables/
│   └── specific_linkages.csv
└── reproducibility/
    ├── commands.sh
    ├── environment.yml
    └── checksums.sha256
```

## Safety

- **Local-first**: Strict offline processing without external upload.
- **Disclaimer**: Requires OmicsClaw reporting structures and disclaimers.
- **Audit trail**: Hyperparameters and operational flow states are logged fully.

## Integration with Orchestrator

**Trigger conditions**:
- Automatically invoked dynamically based on tool metadata and user intent matching.

**Chaining partners**:
- `data-import` — Upstream format parsing

## Citations

- [XlinkX](https://doi.org/10.1038/nmeth.3603)
- [pLink](https://doi.org/10.1038/nmeth.2099)

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->