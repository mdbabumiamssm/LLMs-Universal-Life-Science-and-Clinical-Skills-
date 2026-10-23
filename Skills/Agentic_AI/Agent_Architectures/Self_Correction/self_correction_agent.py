# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

import sys
import os
import json
from typing import Dict, Any, List

# Adjust path to find platform module
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../../../"))
platform_dir = os.path.join(project_root, "platform")

if platform_dir not in sys.path:
    sys.path.append(platform_dir)

# Import directly from adapters to avoid 'import platform' conflict
try:
    from adapters.runtime_adapter import llm
except ImportError:
    # Fallback if path resolution fails
    print("Warning: Could not import runtime_adapter. Using mock.")
    class MockLLM:
        def complete(self, s, p): return " [Mock LLM Output] "
    llm = MockLLM()

try:
    from optimizer.meta_prompter import PromptOptimizer, ModelTarget
except ImportError:
    # Fallback
    class PromptOptimizer:
        def optimize(self, p, t): return p
    class ModelTarget:
        OPENAI = "openai"

class SelfCorrectionAgent:
    """
    Implements a 'Reflexion' or 'Self-Correction' pattern using the RuntimeLLMAdapter.
    
    Workflow:
    1. Generator: Produces an initial draft based on a task.
    2. Critic: Reviews the draft against specific criteria or ground truth.
    3. Refiner: Updates the draft based on the critic's feedback.
    """

    def __init__(self, model_target: str = "openai"):
        self.optimizer = PromptOptimizer()
        self.model_target = model_target

    def run_cycle(self, task: str, criteria: List[str], max_iterations: int = 2) -> Dict[str, Any]:
        """
        Executes the self-correction cycle.
        """
        history = []
        
        # Step 1: Initial Draft
        draft_prompt = self._build_generator_prompt(task)
        current_draft = llm.complete("You are a helpful assistant.", draft_prompt)
        
        history.append({"step": "initial_draft", "content": current_draft})
        print(f"[{self.model_target}] generated initial draft.")

        for i in range(max_iterations):
            # Step 2: Critique
            critique_prompt = self._build_critic_prompt(task, current_draft, criteria)
            critique = llm.complete("You are a critical reviewer.", critique_prompt)
            history.append({"step": f"critique_{i+1}", "content": critique})
            
            if "NO_ISSUES" in critique:
                print(f"Critique passed at iteration {i+1}.")
                break
                
            # Step 3: Refine
            refine_prompt = self._build_refiner_prompt(task, current_draft, critique)
            current_draft = llm.complete("You are an expert editor.", refine_prompt)
            history.append({"step": f"refined_draft_{i+1}", "content": current_draft})
            print(f"Refined draft at iteration {i+1}.")

        return {
            "final_output": current_draft,
            "history": history,
            "iterations": i + 1
        }

    def _build_generator_prompt(self, task: str) -> str:
        # We can still use the optimizer if available
        return f"Task: {task}\nGenerate a comprehensive solution."

    def _build_critic_prompt(self, task: str, draft: str, criteria: List[str]) -> str:
        criteria_str = "\n- ".join(criteria)
        return f"""
        Task: {task}
        Current Draft: {draft}
        
        Critique this draft based on:
        - {criteria_str}
        
        If it meets all criteria, output 'NO_ISSUES'. Otherwise, list specific actionable improvements.
        """

    def _build_refiner_prompt(self, task: str, draft: str, critique: str) -> str:
        return f"""
        Task: {task}
        Draft: {draft}
        Critique: {critique}
        
        Rewrite the draft to address the critique.
        """

if __name__ == "__main__":
    agent = SelfCorrectionAgent()
    task = "Recommend treatment for 38C fever in adult."
    criteria = ["Include Dosage", "Check Contraindications (Liver)", "Specify Frequency"]
    
    result = agent.run_cycle(task, criteria)
    print(json.dumps(result, indent=2))

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
