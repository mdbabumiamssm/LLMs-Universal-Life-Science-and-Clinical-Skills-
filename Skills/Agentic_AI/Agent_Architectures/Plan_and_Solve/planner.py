"""
Plan-and-Solve Agent Architecture

This module implements the "Plan-and-Solve" prompting strategy (Wang et al., 2023).
Unlike ReAct (which interleaves thought/action), Plan-and-Solve:
1. Devises a complete plan first.
2. Executes the plan step-by-step.
3. Replans if a step fails (optional).

This is ideal for complex, multi-step tasks like "Design a protocol for X and then analyze Y".
"""

from typing import List, Dict, Any, Optional
import json
import re

# --- Interfaces ---

class LLMAdapter:
    """Interface for LLM interaction."""
    def generate(self, prompt: str) -> str:
        # Mock implementation
        if "Create a step-by-step plan" in prompt:
            return """
            1. Retrieve the DNA sequence for the target gene.
            2. Identify potential CRISPR off-target sites.
            3. Design gRNA sequences that minimize off-targets.
            4. Output the top 3 gRNA candidates.
            """
        return "Step executed successfully."

# --- Core Classes ---

class PlanAndSolveAgent:
    def __init__(self, llm: LLMAdapter, tools: Dict[str, Any] = None):
        self.llm = llm
        self.tools = tools or {}
        self.current_plan: List[str] = []
        self.memory: List[str] = []

    def plan(self, goal: str) -> List[str]:
        """
        Phase 1: Generate a plan to achieve the goal.
        """
        prompt = f"""
        Goal: {goal}
        
        Create a step-by-step plan to achieve this goal. 
        Each step should be a clear, executable action.
        Return the plan as a numbered list.
        """
        
        response = self.llm.generate(prompt)
        
        # Parse numbered list
        steps = []
        for line in response.split('\n'):
            line = line.strip()
            # Match "1. Step description"
            match = re.match(r'^\d+\.\s+(.*)', line)
            if match:
                steps.append(match.group(1))
                
        self.current_plan = steps
        return steps

    def execute(self, steps: List[str]) -> str:
        """
        Phase 2: Execute the plan step-by-step.
        """
        results = []
        
        print(f"--- Executing Plan ({len(steps)} steps) ---")
        
        for i, step in enumerate(steps):
            print(f"Step {i+1}: {step}")
            
            # Construct context from previous steps
            context = "\n".join(results[-3:]) # Keep last 3 results as context
            
            prompt = f"""
            Current Step: {step}
            
            Context from previous steps:
            {context}
            
            Execute this step and provide the result.
            """
            
            # In a real agent, this would involve tool selection/calling
            # Here we simulate the LLM doing the work or calling a tool
            result = self.llm.generate(prompt)
            
            print(f"  -> Result: {result[:50]}...")
            results.append(f"Step {i+1} Result: {result}")
            self.memory.append(f"Step {i+1}: {step} -> {result}")
            
        return "\n".join(results)

    def run(self, goal: str) -> str:
        """
        Main entry point: Plan then Execute.
        """
        print(f"Agent Goal: {goal}")
        
        # 1. Plan
        plan = self.plan(goal)
        if not plan:
            return "Failed to generate a plan."
            
        print(f"Generated Plan: {plan}")
        
        # 2. Execute
        final_report = self.execute(plan)
        
        return final_report

# --- Example Usage ---

if __name__ == "__main__":
    agent = PlanAndSolveAgent(LLMAdapter())
    
    goal = "Design a CRISPR experiment to knockout the PCSK9 gene."
    
    result = agent.run(goal)
    
    print("\n--- Final Report ---")
    print(result)
