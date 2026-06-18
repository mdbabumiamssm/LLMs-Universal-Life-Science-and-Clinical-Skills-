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
name: bio-proteomics-enrichment
description: Pathway, network, and functional enrichment for proteomics using STRING,
  DAVID, or g:Profiler.
tool_type: mixed
primary_tool: proteomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# 🗺️ Proteomics Enrichment

Pathway, network, and Gene Ontology enrichment analysis for proteomics data.

## CLI Reference

```bash
python omicsclaw.py run prot-enrichment --demo
python omicsclaw.py run prot-enrichment --input <proteins.csv> --output <dir>
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--method` | `ora` | ora or gsea |
| `--species` | `human` | Species |

## Why This Exists

- **Without it**: A list of 500 significant proteins is biologically impossible to interpret
- **With it**: Algorithms collapse hundreds of targets into 5 or 10 meaningful biological pathways
- **Why OmicsClaw**: Runs fast local enrichment caches utilizing multiple ontologies simultaneously

## Workflow

1. **Calculate**: Map Uniprot IDs to Gene Symbols or Entrez.
2. **Execute**: Hypergeometric tests over known Kegg/GO definitions.
3. **Assess**: Perform FDR multiple testing adjustments.
4. **Generate**: Output structural network graphs.
5. **Report**: Tabulate key functionally enriched terms.

## Example Queries

- "Perform GO enrichment on these significant proteins using STRING"
- "Run g:Profiler on this list of genes"

## Output Structure

```
output_directory/
├── report.md
├── result.json
├── pathways.csv
├── figures/
│   └── enrichment_dotplot.png
├── tables/
│   └── top_pathways.csv
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
- `differential-abundance` — Upstream source of significant proteins

## Citations

- [STRING](https://string-db.org/) — protein interaction network
- [g:Profiler](https://doi.org/10.1093/nar/gkz369) — functional enrichment

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->