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

# data-visualization

## Overview

Publication-quality data visualization for bioinformatics using ggplot2 and matplotlib with best practices for scientific figures.

**Tool type:** mixed | **Primary tools:** ggplot2, matplotlib, plotly, ComplexHeatmap

## Skills

| Skill | Description |
|-------|-------------|
| ggplot2-fundamentals | Create publication-ready figures with ggplot2 |
| multipanel-figures | Multi-panel figures with patchwork, cowplot, GridSpec |
| heatmaps-clustering | Expression heatmaps with ComplexHeatmap and pheatmap |
| interactive-visualization | Interactive plots with plotly and bokeh |
| genome-tracks | Genome browser tracks with pyGenomeTracks and Gviz |
| specialized-omics-plots | Volcano, MA, PCA, and enrichment dotplots |
| color-palettes | Colorblind-friendly palettes and journal color schemes |
| cjk-viz | Configure CJK-safe fonts and sanity checks for Chinese figures |
| circos-plots | Circular genome visualizations with Circos, pyCircos, circlize |
| upset-plots | UpSet plots for set intersection visualization |
| volcano-customization | Customized volcano plots with labels and thresholds |
| genome-browser-tracks | Genome browser figures with pyGenomeTracks, IGV |

## Example Prompts

- "Create a publication-quality volcano plot"
- "Make a multi-panel figure with shared legends"
- "Set up a consistent color scheme for my figures"
- "Export figures at 300 DPI for publication"
- "Create an interactive heatmap for my expression data"
- "Plot genome tracks for my ChIP-seq regions"
- "Apply a colorblind-friendly palette"
- "Create an UpSet plot of my gene set overlaps"
- "Label the top 20 genes on my volcano plot"
- "Combine 4 plots into a 2x2 grid with panel labels"
- "Generate genome browser figures for my ChIP-seq peaks"

## Requirements

```r
# R packages
install.packages(c('ggplot2', 'patchwork', 'scales', 'ggrepel', 'pheatmap'))
BiocManager::install(c('ComplexHeatmap', 'Gviz'))
```

```bash
# Python packages
pip install matplotlib seaborn plotly bokeh pyGenomeTracks upsetplot adjustText
```

## Related Skills

- **differential-expression/de-visualization** - Expression-specific plots
- **pathway-analysis/enrichment-visualization** - Enrichment plots
- **reporting** - Figures in reports


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
