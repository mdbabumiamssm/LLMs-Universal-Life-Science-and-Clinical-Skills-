---
name: literature
description: >-
  Parse scholarly articles (PDF, DOI, URL) to extract metadata, GEO accessions, and acquisition links
  using OpenAlex + GROBID pipelines.
version: 0.2.0
author: OmicsClaw
license: MIT
tags: [literature, metadata, openalex, grobid, text-mining]
metadata:
  omicsclaw:
    domain: literature
    emoji: "📚"
    trigger_keywords:
      - literature search
      - openalex
      - pdf parsing
      - grobid
      - accession mining
source_reliability:
  - source: https://github.com/ourresearch/OpenAlex
    description: Primary open-source stack powering the OpenAlex API plus CLI/tutorial repos for scholarly metadata retrieval.
    score: 0.88
    rationale: >
      Maintained by OurResearch with multiple active repositories (CLI, API, docs) and open governance for the scholarly graph.
  - source: https://github.com/kermitt2/grobid
    description: GROBID ML pipeline for PDF parsing and citation extraction; used for high-fidelity metadata recovery.
    score: 0.86
    rationale: >
      Long-lived, peer-reviewed project with automated PDF extraction benchmarks; aligns with OmicsClaw’s PDF parsing approach.
---

# Literature Parsing Skill

## Purpose

Parse scientific literature (PDFs, URLs, DOIs) to extract GEO accessions and metadata, then download datasets for downstream omics analysis.

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
