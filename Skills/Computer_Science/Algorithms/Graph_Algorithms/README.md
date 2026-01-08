# Graph Algorithms for Biomedical AI

This module contains graph algorithms essential for analyzing biological networks (Protein-Protein Interactions, Knowledge Graphs, Metabolic Pathways).

## Contents

### `knowledge_graph.py`
A robust Knowledge Graph implementation supporting:
- **Entities & Relations:** Typed nodes (Drug, Gene) and weighted edges.
- **Pathfinding:** Shortest path algorithms to find connections between entities (e.g., Drug -> Disease).
- **Pathway Analysis:** DFS-based traversal to find all possible interaction chains.
- **Serialization:** Export to JSON for visualization.

## Usage
```python
from knowledge_graph import KnowledgeGraph

kg = KnowledgeGraph()
kg.add_node("DrugA", "Drug")
kg.add_node("GeneB", "Gene")
kg.add_edge("DrugA", "GeneB", "inhibits")

path = kg.find_shortest_path("DrugA", "GeneB")
```