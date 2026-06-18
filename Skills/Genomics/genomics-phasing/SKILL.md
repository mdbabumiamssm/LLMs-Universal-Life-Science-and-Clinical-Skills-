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
name: bio-genomics-phasing
description: 'Haplotype phasing analysis: phase block N50, phased fraction, PS (Phase
  Set) field parsing, pipe-delimited genotype detection. Wraps WhatsHap, SHAPEIT5,
  Eagle2.'
tool_type: mixed
primary_tool: genomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 🔀 Haplotype Phasing

Haplotype phasing for variant data. Wraps WhatsHap, SHAPEIT, and Eagle.

## CLI Reference

```bash
python omicsclaw.py run genomics-phasing --demo
python omicsclaw.py run genomics-phasing --input <data.vcf> --output <dir>
```

## Why This Exists

- **Without it**: Variants remain independent loci without knowledge of allelic connectivity
- **With it**: Haplotypes are formed spanning genes, essential for compound heterozygote analysis
- **Why OmicsClaw**: Standardizes input and output across read-backed and population-backed phasing tools

## Workflow

1. **Calculate**: Prepare VCF indices and sequence mappings.
2. **Execute**: Run haplotype graph resolution algorithms.
3. **Assess**: Perform switch error evaluation and quality flagging.
4. **Generate**: Output structured phased VCF representation.
5. **Report**: Synthesize N50 phase block stats into tables.

## Example Queries

- "Phase this vcf file using WhatsHap"
- "Use SHAPEIT for population phasing of variants"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── phased.vcf.gz
├── figures/
│   └── phase_block_distribution.png
├── tables/
│   └── phasing_metrics.csv
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
- `variant-call` — Upstream generation of raw VCFs
- `annotation` — Downstream annotation of phased haplotypes

## Citations

- [WhatsHap](https://doi.org/10.1089/cmb.2014.0157)
- [SHAPEIT](https://doi.org/10.1038/nmeth.4507)

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->