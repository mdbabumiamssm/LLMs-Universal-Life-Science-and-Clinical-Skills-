# CRISPR Guide Design Agent

**ID:** `biomedical.genomics.crispr_design`
**Version:** 1.0.0
**Status:** Production
**Category:** Genomics / Gene Editing

---

## Overview

The **CRISPR Guide Design Agent** automates the design of CRISPR guide RNAs (sgRNAs) for gene-editing experiments. It assists researchers in identifying optimal genomic targets, predicting off-target effects, and generating complete experimental protocols.

This skill bridges the gap between computational biology expertise and wet-lab execution, enabling AI agents to design publication-quality CRISPR experiments.

---

## Key Capabilities

### 1. Target Selection

- Identifies optimal genomic loci for CRISPR-Cas9 targeting
- Prioritizes exons based on functional domain disruption
- Considers transcript variants and protein isoforms

### 2. Guide RNA Design

- Generates sgRNA sequences based on PAM constraints (NGG for SpCas9)
- Supports multiple Cas variants: SpCas9, SaCas9, Cas12a (Cpf1), base editors
- Optimizes for on-target efficiency using validated scoring algorithms:
  - **Doench 2016:** Rule Set 2 for SpCas9
  - **DeepCRISPR:** Deep learning-based scoring
  - **CFD Score:** Cutting Frequency Determination

### 3. Off-Target Analysis

- Predicts potential off-target cleavage sites genome-wide
- Supports human (hg38), mouse (mm10), and other reference genomes
- Integrates with Cas-OFFinder for comprehensive off-target prediction

### 4. Protocol Generation

- Creates step-by-step experimental procedures
- Supports common vector systems: pX458, pX459, LentiCRISPRv2
- Generates oligonucleotide sequences for cloning

---

## Usage

### Example Prompt

```text
Design 3 optimal sgRNAs for TP53 gene knockout in human cells using CRISPR-Cas9.
Target the first coding exon.
Check for off-target effects in the human genome (hg38).
Generate a cloning protocol for the pX458 vector (GFP reporter).
```

### Expected Output

The agent will return:

1. **Ranked sgRNA sequences** with efficiency scores
2. **Off-target analysis** showing potential mismatches
3. **Oligonucleotide sequences** ready for ordering
4. **Cloning protocol** with annealing and ligation steps

### LLM Agent Integration

```python
@tool
def design_crispr_guides(
    gene_symbol: str,
    organism: str = "human",
    cas_variant: str = "SpCas9",
    num_guides: int = 3,
    target_region: str = "first_exon"
) -> str:
    """
    Designs optimal CRISPR guide RNAs for gene knockout.

    Args:
        gene_symbol: Official gene symbol (e.g., TP53, BRCA1)
        organism: Target organism (human, mouse)
        cas_variant: CRISPR enzyme (SpCas9, SaCas9, Cas12a)
        num_guides: Number of guides to design
        target_region: Region to target (first_exon, all_exons, specific_domain)

    Returns:
        Formatted guide designs with sequences and protocols
    """
    # Implementation calls genomic APIs and scoring algorithms
    pass
```

---

## Prerequisites

### Required APIs/Databases

| Resource | Purpose | Access |
|----------|---------|--------|
| **NCBI/Ensembl** | Genomic sequences | Public API |
| **Cas-OFFinder** | Off-target prediction | Web service or local |
| **CRISPOR** | Guide scoring | Web API |

### Dependencies

```
biopython>=1.80
requests>=2.28
pandas>=1.5
```

---

## Methodology

This implementation incorporates validated scoring methods:

1. **Doench et al. (2016):** "Optimized sgRNA design to maximize activity and minimize off-target effects of CRISPR-Cas9." *Nature Biotechnology*
2. **Hsu et al. (2013):** "DNA targeting specificity of RNA-guided Cas9 nucleases." *Nature Biotechnology*

### Design Principles

- **Exon targeting:** Focus on early exons for complete knockout
- **Domain disruption:** Prioritize functional domains when known
- **GC content:** Optimal range 40-70% for efficient loading
- **Poly-T avoidance:** Exclude sequences with >4 consecutive T's (Pol III terminator)

---

## Related Skills

- **Single-Cell RNA-seq QC:** Validate knockout efficiency at single-cell resolution
- **Variant Interpretation:** Assess pathogenicity of introduced mutations
- **AgentD Drug Discovery:** Target validation for therapeutic targets

---

## References

- Based on concepts from **CRISPR-GPT** (Huang et al.)
- Validated against CRISPOR and Benchling design tools
- [CRISPR-GPT Repository](https://github.com/UEA-Cancer-Genetics-Lab/CRISPR-GPT)

---

## Author

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu
