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
name: bio-literature
description: Parse scholarly articles (PDF, DOI, URL) to extract metadata, GEO accessions,
  and acquisition links using OpenAlex + GROBID pipelines.
tool_type: mixed
primary_tool: literature
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# Literature Parsing Skill

## Purpose

Parse scientific literature (PDFs, URLs, DOIs) to extract GEO accessions and metadata, then download datasets for downstream omics analysis.

## Core Capabilities

- **Medical Q&A dataset evaluation**: Build fine-grained review checklists and schemas for medical language model benchmarking that cover answer correctness, clinically relevant omissions, harm potential, item-level ambiguity, domain coverage, answer provenance, trustworthiness metrics, item-level error taxonomies, dataset quality checks before using benchmark results for medical LLM claims, domain-specific answer rubrics, dataset documentation, and benchmark reporting standards.

## Methodology

### 1. Input Processing

Accepts multiple input types:
- **URL**: PubMed, bioRxiv, journal article links
- **DOI**: Digital Object Identifier (e.g., 10.1038/s41586-021-03569-1)
- **PubMed ID**: PMID (e.g., 33234567)
- **PDF**: Uploaded scientific paper
- **Text**: Raw text containing GEO references

### 2. Metadata Extraction

Extracts structured information:
- **GEO Accessions**: GSE (study-level), GSM (sample-level)
- **Organism**: Species (e.g., Homo sapiens, Mus musculus)
- **Tissue**: Tissue type or organ
- **Cell Type**: Cell type if specified
- **Technology**: Sequencing platform (10x, Visium, etc.)

### 3. Data Download

Downloads datasets from GEO:
- Resolves GSE to find all associated GSM samples
- Downloads expression matrices (.h5ad, .mtx, .csv)
- Organizes files by accession: `data/GSE123456/`
- Generates metadata.json with extracted information

### 4. Error Handling

- **Retry with fallbacks**: PDF parsing → text extraction → manual patterns
- **Partial results**: Returns successfully extracted data even if some downloads fail
- **Logging**: Detailed logs for debugging

## Output

- **data/GSE*/**: Downloaded datasets organized by accession
- **output/literature-parse_*/report.md**: Extraction report
- **output/literature-parse_*/metadata.json**: Structured metadata

## Usage

```bash
# Parse from URL
python skills/literature/literature_parse.py \
  --input "https://pubmed.ncbi.nlm.nih.gov/12345" \
  --output output/literature_results

# Parse from DOI
python skills/literature/literature_parse.py \
  --input "10.1038/s41586-021-03569-1" \
  --input-type doi \
  --output output/literature_results

# Parse PDF
python skills/literature/literature_parse.py \
  --input paper.pdf \
  --input-type file \
  --output output/literature_results
```

## Integration

After extraction, the bot automatically suggests appropriate analysis skills based on:
- Data type (spatial, single-cell, bulk)
- Organism and tissue
- Available files

## Dependencies

- pypdf: PDF text extraction
- requests: HTTP requests
- beautifulsoup4: HTML parsing
- GEOparse: GEO data access (optional, fallback to direct API)

## References

- https://pubmed.ncbi.nlm.nih.gov/42039929/

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
