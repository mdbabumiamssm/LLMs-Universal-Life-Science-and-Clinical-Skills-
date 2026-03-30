---
name: kragen-knowledge-graph
description: "Knowledge graph-enhanced Retrieval-Augmented Generation system that uses Graph-of-Thoughts reasoning over biomedical KGs (PrimeKG, SPOKE) to answer multi-hop questions with cited evidence paths."
compatibility: "Python 3.9+"
allowed-tools: "run_shell_command, web_fetch"
metadata:
  author: Bioinformatics Oxford
  version: "1.0.0"
  keywords: "knowledge-graph, RAG, reasoning, graph-of-thoughts, biomedical-qa"
  measurable_outcome: "Return a reasoning path and an answer supported by ≥3 knowledge graph nodes for complex biomedical questions with <5s latency."
  license: MIT
---

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

# KRAGEN (Knowledge Graph Enhanced RAG)

A knowledge graph-enhanced Retrieval-Augmented Generation system for biomedical problem solving, using Graph-of-Thoughts (GoT) reasoning over structured databases and unstructured text.

Use when answering complex biomedical questions that require multi-hop deduction across genes, proteins, diseases, and pathways — especially when citing structured evidence paths is important.

## When to Use

- **Multi-hop reasoning** — questions like "How does gene A influence disease B via protein C?" that require traversing multiple knowledge graph edges.
- **Hypothesis verification** — checking whether a proposed biological mechanism is supported by existing knowledge graphs (PrimeKG, SPOKE).
- **Literature synthesis** — combining facts from structured databases and unstructured text into a coherent, cited answer.

## Workflow

1. **Accept question** — receive a natural language biomedical question.
2. **Retrieve sub-graph** — fetch relevant nodes and edges from the knowledge graph, plus similar text chunks from the vector DB.
3. **Reason over graph** — LLM traverses the retrieved sub-graph using Graph-of-Thoughts to find connecting paths.
4. **Generate answer** — produce a response citing the specific graph nodes and edges that support the reasoning.

## Example

**Prompt**: "Explain the mechanism connecting BRCA1 mutations to ovarian cancer."

**Agent steps**:
```bash
python -m kragen.solve --question "BRCA1 mutations to ovarian cancer mechanism"
```

The agent retrieves BRCA1 → DNA repair pathway → homologous recombination deficiency → genomic instability → ovarian tumorigenesis nodes, then generates a cited explanation tracing the path.

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->