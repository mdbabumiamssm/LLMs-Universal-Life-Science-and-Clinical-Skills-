<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'deepsems-ocean-biosynthetic-llm-agent'
description: 'Agentic workflow that applies a DeepSeMS-style large language model to mine biosynthetic gene clusters and secondary metabolite potential from global ocean microbiome metagenomes.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# DeepSeMS Marine Microbiome Biosynthetic LLM Agent

## Overview

This skill operationalizes a DeepSeMS-style large language model workflow for revealing the hidden biosynthetic potential of the global ocean microbiome. It treats protein and gene-context sequences as a "language" so an LLM can detect biosynthetic gene clusters (BGCs) and predict the secondary metabolites they may produce, including cryptic clusters that traditional rule-based tools (e.g., antiSMASH) often miss. The agent automates ingestion of marine metagenomes, BGC inference, candidate ranking, and downstream chemistry/drug-discovery follow-up.

## When to Use This Skill

- Mining BGCs from marine metagenomic assemblies (e.g., Tara Oceans, Bio-GO-SHIP, OceanDNA).
- Prioritizing novel natural product (NP) leads from uncultivated ocean microbes for drug discovery.
- Comparing LLM-based BGC predictions against rule-based baselines (antiSMASH, DeepBGC, GECCO).
- Annotating cryptic or fragmented clusters where homology-only methods fail.
- Building chemistry-informed shortlists of putative polyketides, NRPs, RiPPs, terpenes, and hybrids.
- Linking predicted BGCs to taxonomy and biogeography across ocean depth and latitude.

## Core Capabilities

1. **Metagenome ingestion** — Accepts assembled contigs or MAGs (FASTA), gene calls (Prodigal/Pyrodigal), and per-contig taxonomy; normalizes inputs for LLM tokenization.
2. **LLM-based BGC detection** — Runs a DeepSeMS-style sequence LLM over protein/gene-context tokens to score BGC likelihood per ORF window and stitch contiguous high-scoring regions into candidate clusters.
3. **Cluster typing & metabolite prediction** — Classifies clusters by NP class (PKS, NRPS, RiPP, terpene, hybrid) and proposes putative chemical scaffolds or SMILES sketches for chemistry-aware triage.
4. **Cross-tool reconciliation** — Optionally cross-checks predictions against antiSMASH, DeepBGC, and GECCO; flags LLM-only ("dark") clusters as novelty candidates.
5. **Novelty & dereplication** — Compares against MIBiG and BiG-FAM/BiG-SLiCE GCFs to estimate novelty and avoid known-compound rediscovery.
6. **Biogeographic mapping** — Joins clusters with sample metadata (depth, temperature, latitude) to produce ecological context for hits.
7. **Drug-discovery shortlist** — Ranks candidates by novelty, completeness, predicted bioactivity class, and host phylogeny; emits a prioritized table for wet-lab follow-up.
8. **Provenance & reproducibility** — Captures model version, prompts, thresholds, and seeds so every prediction is traceable.

## Inputs / Outputs

**Inputs**
- Assembled metagenomic contigs or MAGs (`.fasta`/`.fa`) from ocean samples.
- Optional: precomputed ORFs (`.faa`), GFF gene coordinates, taxonomy (GTDB-Tk), and sample metadata (CSV/TSV).
- Configuration: model checkpoint, score threshold, minimum cluster length, NP-class filter.

**Outputs**
- BGC table (TSV/Parquet): contig, coordinates, predicted NP class, LLM score, novelty score, host taxonomy.
- Per-cluster GenBank/JSON records with annotated ORFs and predicted product class.
- Optional putative SMILES / scaffold sketches for chemistry triage.
- Comparison report vs. antiSMASH/DeepBGC/GECCO with overlap and LLM-only sets.
- Ranked drug-discovery shortlist (CSV) with biogeographic context and reproducibility manifest (model, version, parameters).

## References

- Source paper: Xu T, Yang Y, Zhu R, Lin W, Li J. *DeepSeMS: revealing the hidden biosynthetic potential of the global ocean microbiome with a large language model.* Nat Comput Sci, 2026 Apr 30. https://pubmed.ncbi.nlm.nih.gov/42062603/
- antiSMASH (rule-based BGC detection): https://antismash.secondarymetabolites.org/
- DeepBGC (deep learning BGC detection): https://github.com/Merck/deepbgc
- GECCO (BGC detection with conditional random fields): https://github.com/zellerlab/GECCO
- MIBiG (curated BGC reference database): https://mibig.secondarymetabolites.org/
- BiG-SLiCE / BiG-FAM (BGC family clustering at scale): https://github.com/medema-group/bigslice
- Tara Oceans expedition data portal: https://fondationtaraocean.org/en/expedition/tara-oceans/
- OceanDNA MAG catalog: https://doi.org/10.1038/s41597-022-01392-5
