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

# reporting

## Overview

Reproducible report generation for bioinformatics analyses using literate programming frameworks and QC aggregation.

**Tool type:** mixed | **Primary tools:** RMarkdown, Quarto, Jupyter, MultiQC, matplotlib

## Skills

| Skill | Description |
|-------|-------------|
| rmarkdown-reports | Create reproducible analysis reports with R Markdown |
| quarto-reports | Build multi-format documents and presentations with Quarto |
| jupyter-reports | Parameterized Jupyter notebooks with papermill |
| automated-qc-reports | Aggregate QC metrics with MultiQC |
| figure-export | Publication-ready figure formatting and export |
| dashboard | Bootstrap local research dashboards with live progress panels |
| feishu-rich-card | Send Feishu interactive cards with text + image summaries |
| svg-ui-templates | Generate SVG/PNG UI layouts for cards and executive briefs |

## Example Prompts

- "Create an RMarkdown report for my RNA-seq analysis"
- "Set up a Quarto document with code and results"
- "Generate a parameterized report for multiple samples"
- "Export my analysis to HTML and PDF"
- "Run my analysis notebook on all samples with papermill"
- "Generate a MultiQC report from my pipeline outputs"
- "Export my figure at 300 DPI for journal submission"

## Requirements

```bash
# R packages
install.packages(c('rmarkdown', 'knitr'))

# Quarto
# Download from https://quarto.org/docs/download/

# Python
pip install jupyter papermill nbconvert multiqc matplotlib

# Optional
pip install seaborn plotly
```

## Related Skills

- **differential-expression** - Analysis to report
- **pathway-analysis** - Enrichment results
- **data-visualization** - Publication figures
- **read-qc** - QC outputs for MultiQC


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
