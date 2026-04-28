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
name: bio-proteomics-data-import
description: Import and convert proteomics data formats between MaxQuant, DIA-NN,
  Spectronaut, and standard CSV.
tool_type: mixed
primary_tool: proteomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 📥 Proteomics Data Import

Import and convert proteomics data from various formats (MaxQuant, DIA-NN, Spectronaut output) into standardised tables.

## CLI Reference

```bash
python omicsclaw.py run proteomics-data-import --demo
python omicsclaw.py run proteomics-data-import --input <proteinGroups.txt> --output <dir>
```

## Why This Exists

- **Without it**: Each search engine (MaxQuant, DIA-NN, FragPipe) outputs completely different table structures
- **With it**: Raw vendor and search outputs are unified into a standard long-format intensity matrix
- **Why OmicsClaw**: Provides a single universal ingestion point before statistical testing

## Workflow

1. **Calculate**: Parse header shapes and metadata dictionaries.
2. **Execute**: Melt and reshape raw search engine text files.
3. **Assess**: Perform basic missing value logic checks.
4. **Generate**: Output normalized H5AD or standard CSV objects.
5. **Report**: Tabulate key protein/peptide groups parsed.

## Example Queries

- "Convert my MaxQuant proteinGroups.txt into a standard format"
- "Import DIA-NN evidence tables"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── processed.csv
├── figures/
│   └── intensity_distribution.png
├── tables/
│   └── import_summary.csv
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
- `ms-qc` — Downstream quality profiling
- `differential-abundance` — Downstream statistical execution

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->