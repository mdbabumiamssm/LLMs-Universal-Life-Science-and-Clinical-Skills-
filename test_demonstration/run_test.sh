#!/bin/bash

# Exit on error
set -e

echo "Starting Single-Cell QC Skill Demonstration..."

# 0. Setup Environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies (this may take a few minutes)..."
pip install -r requirements.txt --quiet

# 1. Generate Dummy Data
echo "Generating dummy .h5ad file..."
python3 generate_dummy_data.py

# 2. Run QC Analysis
echo "Running QC Analysis..."
python3 qc_analysis.py test_input.h5ad --output-dir ./qc_results

# 3. Verify Output
echo "Analysis Complete."
echo "Results are in ./qc_results:"
ls -F ./qc_results

echo "Demonstration finished successfully."