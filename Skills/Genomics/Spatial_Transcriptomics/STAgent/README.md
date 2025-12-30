# STAgent: Spatial Transcriptomics Agent

**Source:** [LiuLab-Bioelectronics-Harvard/STAgent](https://github.com/LiuLab-Bioelectronics-Harvard/STAgent)
**Local Repository:** `./repo`
**Status:** Integrated & Downloaded

## Overview
STAgent is a multimodal LLM-based AI agent designed to automate spatial transcriptomics (ST) data analysis. It bridges the gap between raw ST data and biological insights by leveraging advanced vision-language models and dynamic code generation.

## Key Features
- **Multimodal Integration:** Processes both histology images and gene expression matrices.
- **Dynamic Code Generation:** Writes and executes Python code for analysis tasks (clustering, annotation, spatial plotting).
- **Visual Reasoning:** Interprets spatial patterns in tissue directly.
- **Literature Retrieval:** Contextualizes findings with existing biomedical literature.
- **Report Generation:** Synthesizes analysis into publication-style reports.

## System Architecture
The agent operates via a central orchestrator that manages sub-agents for:
1.  **Data Preprocessing**: QC and normalization.
2.  **Analysis**: Clustering, SVG identification, cell-cell communication.
3.  **Visualization**: Generating spatial plots and UMAPs.
4.  **Interpretation**: Biologically grounding the results.

## Quick Start
1.  **Environment Setup:**
    ```bash
    cd repo
    conda env create -f environment.yml
    conda activate STAgent
    ```
2.  **Configuration:**
    *   Edit `repo/config.yaml` to set your OpenAI API key and data paths.
3.  **Running the Agent:**
    See `repo/src` for the main execution scripts. Typically:
    ```bash
    python repo/src/main.py --data_path your_data.h5ad --task "cluster and annotate"
    ```

## Usage (Conceptual)
```python
from st_agent import STAgent

agent = STAgent(
    data_path="./data/sample_tissue",
    model="gpt-4-vision-preview"
)

# Natural language query
report = agent.run("Identify spatial domains in this tissue and characterize the immune infiltration.")
print(report)
```