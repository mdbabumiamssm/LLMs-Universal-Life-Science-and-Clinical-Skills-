# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

"""
GraphRAG Engine (2026 Skills)

A hybrid retrieval system combining:
1. Knowledge Graph (NetworkX) for structural reasoning.
2. Vector Similarity (Mocked) for entry point discovery.

Use Case: Answering "How is Drug A related to Disease B?" via multi-hop pathways.
"""

import networkx as nx

class GraphRAG:
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def ingest_knowledge(self, triples: list):
        """
        Builds the Knowledge Graph from (Subject, Predicate, Object) triples.
        In reality, an LLM extracts these from documents.
        """
        for subj, pred, obj in triples:
            self.graph.add_edge(subj, obj, relation=pred)
            # Add reverse mock for traversal if needed, or bidirectional
            
    def find_connection(self, entity_a: str, entity_b: str, max_hops=3):
        """
        Performs a graph traversal to find the 'Reasoning Path' between entities.
        """
        print(f"--- GraphRAG Query: Path from '{entity_a}' to '{entity_b}' ---")
        
        try:
            path = nx.shortest_path(self.graph, source=entity_a, target=entity_b)
            
            # Reconstruct narrative
            narrative = []
            for i in range(len(path)-1):
                u = path[i]
                v = path[i+1]
                edge_data = self.graph.get_edge_data(u, v)
                narrative.append(f"{u} --[{edge_data['relation']}]--> {v}")
            
            return narrative
        except nx.NetworkXNoPath:
            return ["No direct connection found in Knowledge Graph."]
        except nx.NodeNotFound as e:
            return [f"Entity missing from graph: {e}"]

    def get_subgraph_context(self, entity: str, radius=1):
        """
        Retrieves local context (neighbors) for an entity to augment an LLM prompt.
        """
        if entity not in self.graph:
            return ""
            
        neighbors = self.graph.neighbors(entity)
        facts = []
        for n in neighbors:
            rel = self.graph.get_edge_data(entity, n)['relation']
            facts.append(f"{entity} {rel} {n}")
        return "\n".join(facts)

if __name__ == "__main__":
    rag = GraphRAG()
    
    # 1. Ingest Biomedical Knowledge (Triples)
    # Scenario: Finding a repurposed drug for a disease.
    knowledge = [
        ("Metformin", "inhibits", "mTOR"),
        ("mTOR", "regulates", "Autophagy"),
        ("Autophagy", "affects", "Aging"),
        ("Rapamycin", "inhibits", "mTOR"),
        ("mTOR", "associated_with", "Cancer_Pathway")
    ]
    
    rag.ingest_knowledge(knowledge)
    
    # 2. Query: How does Metformin relate to Aging?
    # Vector Search alone might miss this if they aren't mentioned in the same sentence.
    # GraphRAG finds the multi-hop path.
    path = rag.find_connection("Metformin", "Aging")
    
    print("\n[Reasoning Chain]")
    for step in path:
        print(f"  {step}")
        
    # 3. Augment Prompt
    print("\n[LLM Context Augmentation]")
    context = rag.get_subgraph_context("mTOR")
    print(f"mTOR Local Knowledge:\n{context}")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
