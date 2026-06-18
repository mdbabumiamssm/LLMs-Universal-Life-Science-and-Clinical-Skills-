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
name: bio-proteomics-quantification
description: Protein/peptide quantification (LFQ, TMT, DIA) using MaxQuant LFQ, DIA-NN,
  or Skyline.
tool_type: mixed
primary_tool: proteomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 📏 Protein Quantification

Protein and peptide quantification for label-free (LFQ), isobaric labelling (TMT), and DIA workflows.

## CLI Reference

```bash
python omicsclaw.py run proteomics-quantification --demo
python omicsclaw.py run proteomics-quantification --input <data.csv> --output <dir>
```

## Why This Exists

- **Without it**: Peak heights vary wildly due to ion suppression, ionization efficiency, and LC drift
- **With it**: Powerful algorithms (MaxLFQ, DIA-NN) normalize intensities across large cohorts
- **Why OmicsClaw**: Provides a standard programmatic interface to multiple quantification paradigms (LFQ, TMT, DIA)

## Workflow

1. **Calculate**: Map identified sequences to MS1 or MS2 extraction windows.
2. **Execute**: Integrate peak areas and apply cross-run retention time alignment.
3. **Assess**: Perform global normalization (median centering, quantile).
4. **Generate**: Output structural intensity matrices.
5. **Report**: Tabulate key quantification yield metrics.

## Example Queries

- "Quantify proteins using MaxQuant LFQ"
- "Run DIA-NN on these wiff files"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── quantified.csv
├── figures/
│   └── normalization_boxplot.png
├── tables/
│   └── intensity_matrix.csv
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
- `peptide-id` — Upstream sequence identification
- `differential-abundance` — Downstream statistical execution

## Citations

- [MaxQuant LFQ](https://doi.org/10.1074/mcp.M113.031591)
- [DIA-NN](https://doi.org/10.1038/s41592-019-0638-x)

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->