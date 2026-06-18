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
name: bio-combined-database-lookup
description: Unified interface to query multiple biomedical databases (NCBI Entrez, Ensembl, UniProt, ChEMBL, PubChem) in a single workflow.
tool_type: mixed
primary_tool: Entrez
measurable_outcome: Retrieve cross-referenced data from at least 3 databases for a single query within 60 seconds.
allowed-tools:
  - run_shell_command
  - read_file
---

# bio-combined-database-lookup: Multi-Omics Database Query

Unified agent capability for cross-database exploration and data retrieval.

## Core Capabilities

1.  **Cross-Reference Search**: Use a single ID (Gene Symbol, RSID, SMILES) to fetch data from Ensembl (Genomics), UniProt (Proteomics), and ChEMBL (Pharmacology).
2.  **NCBI Entrez Integration**: Query PubMed, Gene, and Protein databases.
3.  **Chemical-Gene Interaction**: Map small molecules from PubChem to their targets in UniProt.
4.  **Batch Retrieval**: Download structured metadata for a list of entities.

## Workflow

1.  **Identify Entity**: Determine if the input is a Gene, Protein, Variant, or Molecule.
2.  **Dispatch Queries**:
    *   For Genes: `GET /ensembl/lookup/symbol`, `GET /entrez/gene/summary`.
    *   For Proteins: `GET /uniprot/search`.
    *   For Molecules: `GET /pubchem/cid/property`.
3.  **Harmonize Results**: Join the metadata by common keys (e.g., HGNC symbol).
4.  **Present Summary**: Provide a comprehensive "Biomedical Identity Card" for the entity.

## Example Usage

**User**: "Find everything about the gene JAK2."

**Agent Action**:
1. Search Ensembl for genomic coordinates and transcripts.
2. Search UniProt for protein domains and PTMs.
3. Search ChEMBL for known inhibitors (e.g., Ruxolitinib).
4. Search PubMed for recent high-impact publications.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->
