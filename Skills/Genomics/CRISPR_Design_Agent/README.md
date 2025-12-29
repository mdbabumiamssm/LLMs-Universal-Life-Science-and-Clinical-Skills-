# CRISPR Design Agent

## Description
This skill leverages Large Language Models (LLMs) to automate the design of CRISPR guide RNAs (sgRNAs) for gene-editing experiments. It assists researchers in selecting optimal targets, minimizing off-target effects, and designing experimental protocols.

## Capabilities
- **Target Selection**: Identification of optimal genomic loci for CRISPR-Cas9 targeting.
- **Guide Design**: Generation of sgRNA sequences based on specific PAM (Protospacer Adjacent Motif) constraints.
- **Off-Target Analysis**: Prediction of potential off-target cleavage sites to ensure specificity.
- **Protocol Generation**: Creation of step-by-step experimental procedures for cloning and transfection.

## Usage (Conceptual)

### Prerequisite
Access to a genomic database API (e.g., NCBI, Ensembl) and an off-target prediction tool (e.g., Cas-OFFinder) via MCP or API.

### Example Prompt
```text
I want to knockout the gene TP53 in human cells using CRISPR-Cas9.
Please design 3 optimal sgRNAs targeting the first exon.
Check for off-target effects in the human genome (hg38).
Generate a cloning protocol for the pX458 vector.
```

## References
- Based on concepts from **CRISPR-GPT**.
- Related tools: [CRISPR-GPT Paper/Repo](https://github.com/UEA-Cancer-Genetics-Lab/CRISPR-GPT) (Example link reference)
