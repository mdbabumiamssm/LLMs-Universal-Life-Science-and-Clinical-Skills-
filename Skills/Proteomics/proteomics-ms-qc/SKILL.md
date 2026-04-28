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
name: bio-proteomics-ms-qc
description: Mass spectrometry raw data quality control using PTXQC, rawTools, or
  MSstatsQC.
tool_type: mixed
primary_tool: proteomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 📊 Proteomics MS-QC

Mass spectrometry data quality control. Computes basic QC statistics for protein/peptide abundance tables.

## CLI Reference

```bash
python omicsclaw.py run proteomics-ms-qc --demo
python omicsclaw.py run proteomics-ms-qc --input <data.csv> --output <dir>
```

## Why This Exists

- **Without it**: Instrument drift, missed cleavages, or poor LC gradients ruin quantitative integrity
- **With it**: Identifies bad samples early before costly downstream statistical processing
- **Why OmicsClaw**: Provides a unified mass-spectrometer agnostic report dashboard

## Workflow

1. **Calculate**: Extract basic peptide features and contaminant ratios.
2. **Execute**: Run descriptive statistics across raw files.
3. **Assess**: Flag outliers outside expected robust median ranges.
4. **Generate**: Output normalized QC matrices.
5. **Report**: Synthesize multiple metric traces across runs.

## Example Queries

- "Run mass spec QC on this data using PTXQC"
- "Assess proteomics instrument performance"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── metrics.csv
├── figures/
│   └── qc_dashboard.pdf
├── tables/
│   └── qc_summary.csv
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
- `quantification` — Downstream normalized feature tables

## Citations

- [PTXQC](https://doi.org/10.1021/acs.jproteome.5b00780)

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->