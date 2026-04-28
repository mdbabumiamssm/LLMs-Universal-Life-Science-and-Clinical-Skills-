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
name: bio-genomics-alignment
description: 'Alignment statistics from SAM/BAM files: mapping rate, MAPQ distribution,
  insert size, duplicate rate, proper pair rate. Mirrors samtools-flagstat.'
tool_type: mixed
primary_tool: genomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 🎯 Genomics Read Alignment

Short and long read alignment to reference genomes. Supports BWA-MEM, Bowtie2, and Minimap2.

## CLI Reference

```bash
python omicsclaw.py run genomics-alignment --demo
python omicsclaw.py run genomics-alignment --input <reads.fastq> --output <dir>
```

## Why This Exists

- **Without it**: Alignment is run with disparate tools and ad-hoc flags causing unrecoverable errors downstream
- **With it**: Unified syntax automatically scaling threads and standardizing BAM/CRAM outputs
- **Why OmicsClaw**: Provides a standard local-first interface with built-in QC logging.

## Workflow

1. **Calculate**: Prepare sequences and parameterize indexing.
2. **Execute**: Run primary alignment heuristics over genomes.
3. **Assess**: Perform mapping quality filtering and deduplication.
4. **Generate**: Output structural mappings or sorted BAMs.
5. **Report**: Synthesize alignment stats into tables.

## Example Queries

- "Run alignment on my fastq data using BWA"
- "Map long reads using Minimap2 to reference"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── processed.bam
├── figures/
│   └── mapping_stats.png
├── tables/
│   └── alignment_metrics.csv
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
- `genomics-qc` — Upstream quality checks
- `variant-call` — Downstream variant discovery

## Citations

- [BWA-MEM](https://doi.org/10.1093/bioinformatics/btp324)
- [Minimap2](https://doi.org/10.1093/bioinformatics/bty191)

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->