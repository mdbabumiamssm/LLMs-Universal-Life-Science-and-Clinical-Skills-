#!/bin/bash
#===============================================================================
# Universal Biomedical Skills - Demo Commands Script
#
# This script contains all commands used in the video tutorial series.
# Run individual sections or use as a reference during recording.
#
# Usage:
#   - Source this file: source demo_commands.sh
#   - Or run individual functions
#===============================================================================

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Base paths
SKILLS_ROOT="/home/drdx/ARTIFICIALINTELLIGENCEGROUP/skills"
REPO_PATH="$SKILLS_ROOT/Universal-Life-Science-and-Clinical-Skills-"
DEMO_PATH="$SKILLS_ROOT/test_demonstration"
PROTOTYPE_PATH="$SKILLS_ROOT/platform_prototype"

#-------------------------------------------------------------------------------
# Helper Functions
#-------------------------------------------------------------------------------

print_header() {
    echo ""
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo ""
}

print_step() {
    echo -e "${GREEN}▶ $1${NC}"
}

wait_for_enter() {
    echo ""
    echo -e "${YELLOW}Press Enter to continue...${NC}"
    read
}

#-------------------------------------------------------------------------------
# VIDEO 2: GitHub Repository Tour
#-------------------------------------------------------------------------------

demo_repo_tour() {
    print_header "VIDEO 2: Repository Tour"

    print_step "Navigating to repository..."
    cd "$REPO_PATH"
    pwd

    wait_for_enter

    print_step "Showing repository structure..."
    ls -la

    wait_for_enter

    print_step "Showing Skills folder..."
    ls Skills/

    wait_for_enter

    print_step "Showing Clinical skills..."
    ls Skills/Clinical/

    wait_for_enter

    print_step "Showing Genomics skills..."
    ls Skills/Genomics/

    wait_for_enter

    print_step "Showing a skill's contents..."
    ls -la Skills/Genomics/single_cell_qc/ 2>/dev/null || ls -la Skills/Genomics/

    wait_for_enter

    print_step "Showing test demonstration folder..."
    ls test_demonstration/

    wait_for_enter

    print_step "Showing scRNA-seq data samples..."
    ls test_demonstration/scRNAsedata/

    print_header "Repository Tour Complete!"
}

#-------------------------------------------------------------------------------
# VIDEO 3: Live Demo - scRNA-seq QC
#-------------------------------------------------------------------------------

demo_scrna_qc() {
    print_header "VIDEO 3: Live Demo - scRNA-seq QC"

    print_step "Navigating to test demonstration folder..."
    cd "$DEMO_PATH"
    pwd

    wait_for_enter

    print_step "Showing scRNA-seq data folder..."
    ls -la scRNAsedata/

    wait_for_enter

    print_step "Showing sample 1 contents..."
    ls -la scRNAsedata/GSM3901485_BM1/

    wait_for_enter

    print_step "Activating Python environment..."
    source venv/bin/activate
    echo "Environment activated!"

    wait_for_enter

    print_step "Quick data check - loading sample..."
    python3 << 'EOF'
import scanpy as sc
print("Loading 10X data...")
adata = sc.read_10x_mtx('scRNAsedata/GSM3901485_BM1/')
print(f"Loaded successfully!")
print(f"  Cells: {adata.n_obs:,}")
print(f"  Genes: {adata.n_vars:,}")
EOF

    wait_for_enter

    print_step "Showing pre-generated QC results..."
    ls -la qc_results/

    wait_for_enter

    print_step "QC Results Summary:"
    echo "  - qc_metrics_before_filtering.png  (visualization before QC)"
    echo "  - qc_metrics_after_filtering.png   (visualization after QC)"
    echo "  - qc_filtering_thresholds.png      (threshold visualization)"
    echo "  - test_input_filtered.h5ad         (filtered dataset)"

    print_header "Demo Complete!"
}

demo_run_qc_analysis() {
    print_header "Running Full QC Analysis"

    cd "$DEMO_PATH"
    source venv/bin/activate

    print_step "Running QC analysis on test data..."
    python3 qc_analysis.py test_input.h5ad

    print_step "Analysis complete! Check qc_results/ for outputs."
}

#-------------------------------------------------------------------------------
# VIDEO 4: USDL & Adapters
#-------------------------------------------------------------------------------

demo_usdl_adapters() {
    print_header "VIDEO 4: USDL & Adapters"

    print_step "Navigating to platform prototype..."
    cd "$PROTOTYPE_PATH"
    pwd

    wait_for_enter

    print_step "Showing USDL example file..."
    echo "File: examples/single_cell_qc.yaml"
    echo ""
    if [ -f "examples/single_cell_qc.yaml" ]; then
        head -60 examples/single_cell_qc.yaml
    else
        echo "(File would be shown here)"
    fi

    wait_for_enter

    print_step "Showing adapters folder..."
    ls adapters/ 2>/dev/null || echo "adapters/"

    wait_for_enter

    print_step "Validating skill definition..."
    if [ -f "cli.py" ]; then
        python3 cli.py validate examples/single_cell_qc.yaml 2>/dev/null || echo "Validation command would run here"
    else
        echo "python cli.py validate examples/single_cell_qc.yaml"
    fi

    wait_for_enter

    print_step "Building for Claude..."
    echo "python cli.py build --platform claude examples/single_cell_qc.yaml"

    wait_for_enter

    print_step "Building for OpenAI..."
    echo "python cli.py build --platform openai examples/single_cell_qc.yaml"

    print_header "USDL Demo Complete!"
}

#-------------------------------------------------------------------------------
# VIDEO 5: Platform Prototype SDK
#-------------------------------------------------------------------------------

demo_sdk() {
    print_header "VIDEO 5: Platform Prototype SDK"

    print_step "Navigating to platform prototype..."
    cd "$PROTOTYPE_PATH"
    pwd

    wait_for_enter

    print_step "Showing SDK structure..."
    ls -la

    wait_for_enter

    print_step "CLI Commands Overview:"
    echo ""
    echo "  validate   - Check skill against USDL schema"
    echo "  build      - Generate platform-specific artifacts"
    echo "  optimize   - AI-tune prompts for platforms"
    echo "  test       - Run evaluation suite"
    echo "  serve      - Start BioKernel runtime"
    echo "  compare    - Cross-platform performance comparison"

    wait_for_enter

    print_step "BioKernel intelligent routing:"
    echo ""
    echo "  Simple tasks    →  Gemini Flash (fast/cheap)"
    echo "  Complex tasks   →  Claude Opus (best reasoning)"
    echo "  Privacy-first   →  Local models"

    print_header "SDK Demo Complete!"
}

#-------------------------------------------------------------------------------
# Quick Verification Commands
#-------------------------------------------------------------------------------

verify_environment() {
    print_header "Environment Verification"

    print_step "Checking repository exists..."
    if [ -d "$REPO_PATH" ]; then
        echo -e "${GREEN}✓ Repository found${NC}"
    else
        echo -e "${RED}✗ Repository not found${NC}"
    fi

    print_step "Checking test data exists..."
    if [ -d "$DEMO_PATH/scRNAsedata" ]; then
        echo -e "${GREEN}✓ Test data found${NC}"
        ls "$DEMO_PATH/scRNAsedata/"
    else
        echo -e "${RED}✗ Test data not found${NC}"
    fi

    print_step "Checking QC results exist..."
    if [ -d "$DEMO_PATH/qc_results" ]; then
        echo -e "${GREEN}✓ QC results found${NC}"
        ls "$DEMO_PATH/qc_results/"
    else
        echo -e "${RED}✗ QC results not found${NC}"
    fi

    print_step "Checking Python environment..."
    cd "$DEMO_PATH"
    if [ -d "venv" ]; then
        source venv/bin/activate
        python3 -c "import scanpy; print('✓ scanpy available')" 2>/dev/null || echo "✗ scanpy not available"
        python3 -c "import anndata; print('✓ anndata available')" 2>/dev/null || echo "✗ anndata not available"
        python3 -c "import matplotlib; print('✓ matplotlib available')" 2>/dev/null || echo "✗ matplotlib not available"
    else
        echo -e "${RED}✗ Virtual environment not found${NC}"
    fi

    print_header "Verification Complete!"
}

#-------------------------------------------------------------------------------
# Clone and Setup Commands
#-------------------------------------------------------------------------------

show_quick_start() {
    print_header "Quick Start Commands"

    echo "# Clone the repository"
    echo "git clone https://github.com/mdbabumiamssm/Universal-Life-Science-and-Clinical-Skills-.git"
    echo ""
    echo "# Navigate to the folder"
    echo "cd Universal-Life-Science-and-Clinical-Skills-"
    echo ""
    echo "# Install dependencies"
    echo "pip install -r test_demonstration/requirements.txt"
    echo ""
    echo "# Run the demo"
    echo "cd test_demonstration"
    echo "bash run_test.sh"

    print_header "Copy and paste these commands!"
}

#-------------------------------------------------------------------------------
# Main Menu
#-------------------------------------------------------------------------------

show_menu() {
    print_header "Demo Commands Menu"

    echo "Available demo functions:"
    echo ""
    echo "  1) verify_environment    - Check all prerequisites"
    echo "  2) show_quick_start      - Show clone/setup commands"
    echo "  3) demo_repo_tour        - VIDEO 2: Repository tour"
    echo "  4) demo_scrna_qc         - VIDEO 3: scRNA-seq QC demo"
    echo "  5) demo_run_qc_analysis  - Run full QC analysis"
    echo "  6) demo_usdl_adapters    - VIDEO 4: USDL demo"
    echo "  7) demo_sdk              - VIDEO 5: SDK demo"
    echo ""
    echo "Usage: Call any function by name, e.g.:"
    echo "  $ verify_environment"
    echo "  $ demo_scrna_qc"
    echo ""
}

#-------------------------------------------------------------------------------
# Auto-run menu if script is executed directly
#-------------------------------------------------------------------------------

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    show_menu
fi

echo ""
echo -e "${GREEN}Demo commands loaded! Type 'show_menu' to see available functions.${NC}"
echo ""
