# Single-Cell RNA-seq Quality Control Skill

This skill provides a standardized, automated workflow for performing Quality Control (QC) on single-cell RNA sequencing data. It follows `scverse` and `scanpy` best practices.

## Capabilities

- **Automated Metrics:** Calculates count depth, gene detection, mitochondrial %, ribosomal %, and hemoglobin %.
- **Outlier Detection:** Uses Median Absolute Deviation (MAD) for robust, data-driven filtering (instead of arbitrary hard thresholds).
- **Visualization:** Generates comprehensive "Before vs. After" QC plots.

## Components

This skill consists of three Python modules:
1. `qc_analysis.py`: The main entry point for running the full pipeline.
2. `qc_core.py`: Core functions for metric calculation and filtering.
3. `qc_plotting.py`: Visualization utilities.

## Usage

### 1. As a Standalone Script (CLI)

You can run the analysis directly from the command line:

```bash
python qc_analysis.py input.h5ad --output-dir ./results
```

**Arguments:**
- `input_file`: Path to `.h5ad` or `.h5` file.
- `--output-dir`: Where to save results (default: `<input>_qc_results`).
- `--mad-counts`: MAD threshold for counts (default: 5).
- `--mad-genes`: MAD threshold for genes (default: 5).
- `--mt-threshold`: Hard cutoff for Mitochondrial % (default: 15.0).

### 2. As a Python Library (for Agents)

LLM Agents (using LangChain, AutoGen, etc.) can use the `qc_core` functions as tools.

**Example Tool Definition (Python):**

```python
from qc_core import calculate_qc_metrics, detect_outliers_mad, filter_cells
import anndata as ad

def run_sc_qc(file_path: str, output_path: str):
    """
    Performs quality control on a single-cell RNA-seq file.
    """
    adata = ad.read_h5ad(file_path)
    
    # 1. Calculate Metrics
    calculate_qc_metrics(adata, inplace=True)
    
    # 2. Filter
    # ... logic to apply filters ...
    
    adata.write(output_path)
    return "QC Complete. Saved to " + output_path
```

## Requirements

- `anndata`
- `scanpy`
- `scipy`
- `matplotlib`
- `seaborn`
- `numpy`
