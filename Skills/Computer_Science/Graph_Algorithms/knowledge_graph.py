# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

import heapq
from typing import List, Dict, Optional, Any
from dataclasses import dataclass

@dataclass
class KnowledgeNode:
    id: str
    type: str  # e.g., "Protein", "Drug", "Pathway", "Disease"
    properties: Dict[str, Any]

@dataclass
class KnowledgeEdge:
    source: str
    target: str
    relation: str  # e.g., "binds_to", "upregulates", "associated_with"
    weight: float = 1.0

class BioKnowledgeGraph:
    """
    A specialized Graph data structure for representing biomedical knowledge.
    Implements core graph algorithms useful for RAG (Retrieval Augmented Generation)
    and Drug Discovery pathfinding.
    """

    def __init__(self):
        self.nodes: Dict[str, KnowledgeNode] = {}
        self.adjacency: Dict[str, List[KnowledgeEdge]] = {}

    def add_node(self, id: str, type: str, **kwargs):
        self.nodes[id] = KnowledgeNode(id, type, kwargs)
        if id not in self.adjacency:
            self.adjacency[id] = []

    def add_edge(self, source: str, target: str, relation: str, weight: float = 1.0):
        if source not in self.nodes or target not in self.nodes:
            raise ValueError("Source or Target node does not exist.")
        
        edge = KnowledgeEdge(source, target, relation, weight)
        self.adjacency[source].append(edge)
        # Assuming undirected for simplicity in some algos, but storing directed
        # For a truly undirected graph, uncomment below:
        # self.adjacency[target].append(KnowledgeEdge(target, source, relation, weight))

    def find_shortest_path(self, start_id: str, end_id: str) -> Optional[List[str]]:
        """
        Dijkstra's algorithm to find the shortest interaction path between two bio-entities.
        Useful for finding how a Drug might affect a distant Disease pathway.
        """
        if start_id not in self.nodes or end_id not in self.nodes:
            return None

        # Priority queue: (distance, current_node, path)
        pq = [(0, start_id, [])]
        visited = set()

        while pq:
            cost, current, path = heapq.heappop(pq)
            
            if current in visited:
                continue
            visited.add(current)
            
            path = path + [current]
            
            if current == end_id:
                return path

            for edge in self.adjacency[current]:
                if edge.target not in visited:
                    heapq.heappush(pq, (cost + edge.weight, edge.target, path))
        
        return None

    def get_subgraph_context(self, center_id: str, depth: int = 2) -> List[str]:
        """
        Retrieves the 'ego graph' or immediate context around a node.
        Essential for GraphRAG: "Tell me about Aspirin" -> gets targets, side effects, etc.
        """
        if center_id not in self.nodes:
            return []
            
        context = set()
        queue = [(center_id, 0)]
        visited = set()
        
        while queue:
            current, d = queue.pop(0)
            if d > depth:
                continue
            
            visited.add(current)
            
            # Format as natural language triple for LLM consumption
            if d > 0: # Don't add the node itself as a relation, just its edges
                pass 

            for edge in self.adjacency[current]:
                # Add the triple string
                context.add(f"({self.nodes[edge.source].id}) --[{edge.relation}]--> ({self.nodes[edge.target].id})")
                
                if edge.target not in visited:
                    queue.append((edge.target, d + 1))
                    
        return list(context)

    def calculate_centrality(self) -> Dict[str, float]:
        """
        Calculates Degree Centrality.
        Nodes with high centrality are potential 'Hubs' (e.g., critical proteins like P53).
        """
        centrality = {}
        for node in self.nodes:
            # Out-degree only for this simple implementation
            degree = len(self.adjacency[node])
            centrality[node] = degree
        
        # Normalize
        max_deg = max(centrality.values()) if centrality else 1
        for node in centrality:
            centrality[node] /= max_deg
            
        return centrality

# --- Example Usage ---
if __name__ == "__main__":
    kg = BioKnowledgeGraph()
    
    # Building a mini Drug-Target-Disease graph
    kg.add_node("Imatinib", "Drug")
    kg.add_node("BCR-ABL", "Protein")
    kg.add_node("CML", "Disease") # Chronic Myeloid Leukemia
    kg.add_node("ATP_Binding_Pocket", "Domain")
    kg.add_node("Cell_Proliferation", "Process")
    
    kg.add_edge("Imatinib", "BCR-ABL", "inhibits", weight=0.1) # Low weight = strong connection
    kg.add_edge("BCR-ABL", "ATP_Binding_Pocket", "contains", weight=0.1)
    kg.add_edge("BCR-ABL", "Cell_Proliferation", "upregulates", weight=0.5)
    kg.add_edge("Cell_Proliferation", "CML", "drivers", weight=0.5)
    
    # RAG Query: "How does Imatinib treat CML?"
    # The graph finds the path
    path = kg.find_shortest_path("Imatinib", "CML")
    print(f"Mechanism of Action Path: {path}")
    
    # Context Retrieval
    context = kg.get_subgraph_context("BCR-ABL", depth=1)
    print("\nKnowledge Context for BCR-ABL:")
    for triple in context:
        print(triple)

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
