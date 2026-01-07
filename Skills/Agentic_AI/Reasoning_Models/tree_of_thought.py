"""
Tree of Thought (ToT) Reasoning Engine

A production-grade implementation of the Tree of Thought reasoning framework.
Enables LLMs to perform deliberate problem solving by exploring multiple
reasoning paths, evaluating intermediate steps, and backtracking when necessary.

Features:
- Generic state representation for any problem domain
- Pluggable search strategies (BFS, DFS)
- LLM-based state evaluation (self-reflection)
- Decomposition of complex problems into steps
- Structured prompt management

References:
- Tree of Thoughts: Deliberate Problem Solving with Large Language Models
  (https://arxiv.org/abs/2305.10601)

Version: 2.0.0
Date: January 2026
"""

from typing import List, Dict, Any, Optional, Callable, Tuple, Union
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import heapq
import json
import time


# --- Interfaces ---

class Evaluator(ABC):
    """Abstract base class for state evaluators."""
    
    @abstractmethod
    def evaluate(self, state: str, problem_description: str) -> float:
        """
        Evaluate the promise of a state.
        Returns score between 0.0 (failure) and 1.0 (success/highly promising).
        """
        pass

class Generator(ABC):
    """Abstract base class for thought generators."""
    
    @abstractmethod
    def generate_thoughts(self, state: str, problem_description: str, n: int) -> List[str]:
        """Generate n possible next steps (thoughts) from the current state."""
        pass


# --- LLM Adapter ---

class LLMAdapter(ABC):
    """Interface for LLM interaction."""
    
    @abstractmethod
    def generate(self, prompt: str, temperature: float = 0.7) -> str:
        pass


class MockLLM(LLMAdapter):
    """Mock LLM for testing without API costs."""
    
    def generate(self, prompt: str, temperature: float = 0.7) -> str:
        # Simple heuristic response generation for demo purposes
        if "evaluate" in prompt.lower():
            return "0.8"  # High confidence mock
        if "generate" in prompt.lower():
            return "Step 1\nStep 2\nStep 3"
        return "Generic thought"


# --- Core ToT Components ---

@dataclass
class SearchNode:
    """A node in the reasoning tree."""
    state: str
    parent: Optional['SearchNode']
    score: float
    depth: int
    path_history: List[str] = field(default_factory=list)
    
    def __lt__(self, other):
        # For priority queue (max-heap behavior needs negative score if using min-heap)
        return self.score > other.score

    def get_full_path(self) -> str:
        """Reconstruct the full reasoning chain."""
        return "\n".join(self.path_history + [self.state])


class LLMEvaluator(Evaluator):
    """Uses an LLM to evaluate state promise."""
    
    def __init__(self, llm: LLMAdapter):
        self.llm = llm

    def evaluate(self, state: str, problem_description: str) -> float:
        prompt = f"""
        Evaluate the following reasoning step towards solving the problem. 
        
        Problem: {problem_description}
        
        Current Reasoning State:
        {state}
        
        Assess whether this step is:
        - Impossible/Wrong (0.1)
        - Unlikely to work (0.3)
        - Plausible (0.5)
        - Promising (0.7)
        - Correct/Solved (1.0)
        
        Return ONLY the numeric score (0.0 to 1.0).
        """
        
        try:
            response = self.llm.generate(prompt, temperature=0.1).strip()
            # Extract float from response
            import re
            match = re.search(r"0\.\d+|1\.0|1", response)
            if match:
                return float(match.group(0))
            return 0.5 # Default fallback
        except Exception:
            return 0.5


class LLMGenerator(Generator):
    """Uses an LLM to generate next thoughts."""
    
    def __init__(self, llm: LLMAdapter):
        self.llm = llm

    def generate_thoughts(self, state: str, problem_description: str, n: int) -> List[str]:
        prompt = f"""
        You are an intelligent problem solver. 
        
        Problem: {problem_description}
        
        Current State:
        {state}
        
        Generate {n} distinct, valid next steps (thoughts) to move closer to the solution.
        Provide each thought on a new line.
        """
        
        response = self.llm.generate(prompt, temperature=0.7)
        thoughts = [line.strip() for line in response.split('\n') if line.strip()]
        return thoughts[:n]


# --- Search Algorithms ---

class TreeOfThoughtSolver:
    """
    Generic Tree of Thought solver.
    
    Example:
        >>> llm = MyLLM()
        >>> solver = TreeOfThoughtSolver(llm)
        >>> solution = solver.solve("Solve the 24 game with 4, 5, 8, 2")
    """
    
    def __init__(
        self, 
        llm: Optional[LLMAdapter] = None, 
        evaluator: Optional[Evaluator] = None,
        generator: Optional[Generator] = None,
        strategy: str = "bfs",
        max_depth: int = 5,
        branching_factor: int = 3
    ):
        self.llm = llm or MockLLM()
        self.evaluator = evaluator or LLMEvaluator(self.llm)
        self.generator = generator or LLMGenerator(self.llm)
        self.strategy = strategy
        self.max_depth = max_depth
        self.branching_factor = branching_factor
        self.nodes_explored = 0

    def solve(self, problem: str) -> Dict[str, Any]:
        """
        Run the ToT search to solve the problem.
        """
        self.nodes_explored = 0
        start_time = time.time()
        
        # Initial node
        root = SearchNode(
            state="Start",
            parent=None,
            score=0.5,
            depth=0,
            path_history=[]
        )
        
        if self.strategy == "bfs":
            result_node = self._bfs(root, problem)
        elif self.strategy == "dfs":
            result_node = self._dfs(root, problem)
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")
            
        duration = time.time() - start_time
        
        if result_node:
            return {
                "status": "solved",
                "solution": result_node.get_full_path(),
                "final_score": result_node.score,
                "depth": result_node.depth,
                "nodes_explored": self.nodes_explored,
                "duration": duration
            }
        else:
            return {
                "status": "failed",
                "reason": "Max depth or no solution found",
                "nodes_explored": self.nodes_explored,
                "duration": duration
            }

    def _bfs(self, root: SearchNode, problem: str) -> Optional[SearchNode]:
        """Breadth-First Search (Beam Search logic can be added here)."""
        queue = [root]
        best_solution = None
        
        # Level-wise iteration
        for depth in range(self.max_depth):
            print(f"ToT Depth {depth}: {len(queue)} candidates")
            next_queue = []
            
            for node in queue:
                if node.score >= 0.9: # Early exit for high confidence
                    return node
                
                # Generate thoughts
                thoughts = self.generator.generate_thoughts(
                    node.state if node.state != "Start" else "", 
                    problem, 
                    self.branching_factor
                )
                
                for thought in thoughts:
                    self.nodes_explored += 1
                    
                    # Evaluate
                    full_state = node.get_full_path() + "\n" + thought
                    score = self.evaluator.evaluate(full_state, problem)
                    
                    if score < 0.3: # Prune bad paths
                        continue
                        
                    child = SearchNode(
                        state=thought,
                        parent=node,
                        score=score,
                        depth=depth + 1,
                        path_history=node.path_history + [node.state]
                    )
                    
                    next_queue.append(child)
                    
                    if score >= 0.9: # Found a solution
                        return child

            # Beam Search: keep top K candidates per level
            next_queue.sort(key=lambda x: x.score, reverse=True)
            queue = next_queue[:5] # Beam width of 5
            
            if not queue:
                break
                
        return queue[0] if queue else None

    def _dfs(self, root: SearchNode, problem: str) -> Optional[SearchNode]:
        """Depth-First Search."""
        stack = [root]
        best_node = root
        
        while stack:
            node = stack.pop()
            
            if node.depth > self.max_depth:
                continue
                
            if node.score > best_node.score:
                best_node = node
            if node.score >= 0.9:
                return node
                
            thoughts = self.generator.generate_thoughts(
                node.state if node.state != "Start" else "", 
                problem, 
                self.branching_factor
            )
            
            # Add to stack (reverse to process first generated first)
            for thought in reversed(thoughts):
                self.nodes_explored += 1
                full_state = node.get_full_path() + "\n" + thought
                score = self.evaluator.evaluate(full_state, problem)
                
                if score < 0.3: continue
                
                child = SearchNode(
                    state=thought,
                    parent=node,
                    score=score,
                    depth=node.depth + 1,
                    path_history=node.path_history + [node.state]
                )
                stack.append(child)
                
        return best_node


# --- Example Usage ---

if __name__ == "__main__":
    # Example using Mock LLM
    print("=" * 60)
    print("Tree of Thought Solver (v2026)")
    print("=" * 60)
    
    solver = TreeOfThoughtSolver(
        strategy="bfs", 
        max_depth=3, 
        branching_factor=2
    )
    
    problem = "Plan a 3-step synthesis for Aspirin starting from Benzene."
    print(f"\nProblem: {problem}")
    
    result = solver.solve(problem)
    
    print("\nResult:")
    print(json.dumps(result, indent=2))