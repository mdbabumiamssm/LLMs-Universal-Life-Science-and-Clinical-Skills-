"""
Knowledge Graph Implementation for Biomedical Relationships

This module provides a robust implementation of a Knowledge Graph (KG) data structure
optimized for representing biomedical entities (Drugs, Genes, Diseases) and their relationships.
It includes traversal algorithms (BFS, DFS) useful for finding pathways and connections.

Key Features:
- Typed Nodes (Entity Types)
- Weighted Edges (Relationship Strength/Confidence)
- Pathfinding (Shortest Path)
- Subgraph Extraction
"""

from typing import Dict, List, Set, Optional, Tuple, Any, Generator
from dataclasses import dataclass, field
import heapq
from collections import deque
import json

@dataclass
class Entity:
    """Represents a node in the Knowledge Graph."""
    id: str
    type: str  # e.g., "Drug", "Gene", "Disease"
    properties: Dict[str, Any] = field(default_factory=dict)

    def __hash__(self):
        return hash(self.id)

@dataclass
class Relation:
    """Represents an edge between two entities."""
    source_id: str
    target_id: str
    type: str  # e.g., "inhibits", "upregulates", "associated_with"
    weight: float = 1.0  # Confidence score or strength
    properties: Dict[str, Any] = field(default_factory=dict)

class KnowledgeGraph:
    def __init__(self):
        self.nodes: Dict[str, Entity] = {}
        self.adjacency: Dict[str, List[Relation]] = {}
    
    def add_node(self, id: str, type: str, **kwargs):
        """Add a node to the graph."""
        if id not in self.nodes:
            self.nodes[id] = Entity(id=id, type=type, properties=kwargs)
            self.adjacency[id] = []
    
    def add_edge(self, source: str, target: str, type: str, weight: float = 1.0, **kwargs):
        """Add a directed edge between two nodes."""
        # Ensure nodes exist
        if source not in self.nodes:
            self.add_node(source, "Unknown")
        if target not in self.nodes:
            self.add_node(target, "Unknown")
            
        relation = Relation(source, target, type, weight, kwargs)
        self.adjacency[source].append(relation)
        
        # For undirected graphs, you would uncomment:
        # self.adjacency[target].append(Relation(target, source, type, weight, kwargs))

    def get_neighbors(self, node_id: str) -> List[Tuple[Entity, Relation]]:
        """Get all directly connected nodes and the relations connecting them."""
        if node_id not in self.adjacency:
            return []
        
        results = []
        for rel in self.adjacency[node_id]:
            if rel.target_id in self.nodes:
                results.append((self.nodes[rel.target_id], rel))
        return results

    def bfs_traversal(self, start_id: str, max_depth: int = 3) -> Generator[Tuple[str, int], None, None]:
        """
        Perform Breadth-First Search to explore the neighborhood of a node.
        Yields (node_id, depth).
        """
        if start_id not in self.nodes:
            return
            
        visited = {start_id}
        queue = deque([(start_id, 0)])
        
        while queue:
            current_id, depth = queue.popleft()
            yield current_id, depth
            
            if depth < max_depth:
                for rel in self.adjacency.get(current_id, []):
                    if rel.target_id not in visited:
                        visited.add(rel.target_id)
                        queue.append((rel.target_id, depth + 1))

    def find_shortest_path(self, start_id: str, end_id: str) -> Optional[List[str]]:
        """
        Find shortest path (unweighted) between two entities using BFS.
        Returns list of node IDs or None if no path exists.
        """
        if start_id not in self.nodes or end_id not in self.nodes:
            return None
            
        queue = deque([(start_id, [start_id])])
        visited = {start_id}
        
        while queue:
            current_id, path = queue.popleft()
            
            if current_id == end_id:
                return path
            
            for rel in self.adjacency.get(current_id, []):
                if rel.target_id not in visited:
                    visited.add(rel.target_id)
                    new_path = list(path)
                    new_path.append(rel.target_id)
                    queue.append((rel.target_id, new_path))
                    
        return None

    def find_pathways(self, start_id: str, end_id: str, max_depth: int = 4) -> List[List[Tuple[str, str, str]]]:
        """
        Find all paths between two nodes up to max_depth.
        Returns list of paths, where each path is a list of (source, relation, target) tuples.
        """
        results = []
        
        def dfs(current_id: str, target_id: str, path: List[Tuple[str, str, str]], depth: int, visited: Set[str]):
            if current_id == target_id and path:
                results.append(list(path))
                return
            
            if depth >= max_depth:
                return
            
            visited.add(current_id)
            
            for rel in self.adjacency.get(current_id, []):
                if rel.target_id not in visited:
                    path.append((rel.source_id, rel.type, rel.target_id))
                    dfs(rel.target_id, target_id, path, depth + 1, visited)
                    path.pop()
            
            visited.remove(current_id)

        dfs(start_id, end_id, [], 0, set())
        return results

    def to_json(self) -> str:
        """Serialize graph to JSON."""
        return json.dumps({
            "nodes": [
                {"id": n.id, "type": n.type, "properties": n.properties}
                for n in self.nodes.values()
            ],
            "edges": [
                {
                    "source": rel.source_id,
                    "target": rel.target_id,
                    "type": rel.type,
                    "weight": rel.weight
                }
                for adj in self.adjacency.values() for rel in adj
            ]
        }, indent=2)

# --- Example Usage ---

if __name__ == "__main__":
    kg = KnowledgeGraph()
    
    # Add Biomedical Entities
    kg.add_node("Imatinib", "Drug", description="Tyrosine kinase inhibitor")
    kg.add_node("BCR-ABL", "Gene", description="Fusion gene")
    kg.add_node("CML", "Disease", description="Chronic Myeloid Leukemia")
    kg.add_node("KIT", "Gene", description="Proto-oncogene c-Kit")
    kg.add_node("GIST", "Disease", description="Gastrointestinal Stromal Tumor")
    
    # Add Relationships
    kg.add_edge("Imatinib", "BCR-ABL", "inhibits", weight=0.9)
    kg.add_edge("BCR-ABL", "CML", "causes", weight=1.0)
    kg.add_edge("Imatinib", "KIT", "inhibits", weight=0.8)
    kg.add_edge("KIT", "GIST", "associated_with", weight=0.9)
    
    print("--- Shortest Path: Imatinib -> CML ---")
    path = kg.find_shortest_path("Imatinib", "CML")
    print(" -> ".join(path) if path else "No path")
    
    print("\n--- All Pathways: Imatinib -> GIST ---")
    pathways = kg.find_pathways("Imatinib", "GIST")
    for i, p in enumerate(pathways):
        print(f"Path {i+1}:")
        for step in p:
            print(f"  {step[0]} --[{step[1]}]--> {step[2]}")

    print("\n--- Neighborhood (BFS Depth 2) ---")
    for node, depth in kg.bfs_traversal("Imatinib", max_depth=2):
        print(f"Depth {depth}: {node} ({kg.nodes[node].type})")
