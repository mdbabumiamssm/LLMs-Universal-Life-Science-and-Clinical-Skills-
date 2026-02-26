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

# Data Visualization Skills

Publication-quality visualization skills for biological data.

## Sub-categories

| Category | Description | Skills |
|----------|-------------|--------|
| **data-visualization** | Comprehensive plotting | Heatmaps, volcano, circos, genome tracks |

## Key Capabilities

- **Heatmaps** - Gene expression, correlation matrices
- **Volcano Plots** - Differential expression visualization
- **Circos Plots** - Circular genome visualization
- **Genome Tracks** - IGV-style genomic data tracks
- **Interactive Plots** - Plotly, Bokeh integration
- **Multi-panel Figures** - Publication-ready layouts

## Key Tools

- **matplotlib/seaborn** - Static plots
- **plotly** - Interactive visualization
- **ComplexHeatmap** - R heatmap package
- **pyGenomeTracks** - Genome browser tracks
- **circlize** - Circos plots in R

## Example Volcano Plot

```python
import matplotlib.pyplot as plt
import numpy as np

def volcano_plot(results, fc_thresh=1, pval_thresh=0.05):
    plt.figure(figsize=(10, 8))

    # Color by significance
    colors = np.where(
        (abs(results['log2FC']) > fc_thresh) &
        (results['pvalue'] < pval_thresh),
        'red', 'gray'
    )

    plt.scatter(results['log2FC'], -np.log10(results['pvalue']),
                c=colors, alpha=0.5, s=10)
    plt.xlabel('log2 Fold Change')
    plt.ylabel('-log10(p-value)')
    plt.axhline(-np.log10(pval_thresh), linestyle='--', color='k')
    plt.axvline(-fc_thresh, linestyle='--', color='k')
    plt.axvline(fc_thresh, linestyle='--', color='k')
```

## Related Skills
- **[R Programming](../Software_Engineering/R_Programming/SKILL.md)**: Master the foundational language for `ggplot2`, `ComplexHeatmap`, and Bioconductor visualizations.

---
*Source: bioSkills collection - integrated into BioMedical Skills Library*


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->