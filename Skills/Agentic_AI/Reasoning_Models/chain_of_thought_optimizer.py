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

# Adjust path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../../"))
platform_dir = os.path.join(project_root, "platform")

if platform_dir not in sys.path:
    sys.path.append(platform_dir)

from adapters.runtime_adapter import llm

class ChainOfThoughtOptimizer:
    """
    Optimizes simple prompts into 'Chain of Thought' (CoT) prompts 
    to improve reasoning performance.
    """
    
    def __init__(self):
        pass

    def optimize_prompt(self, original_prompt: str) -> str:
        """
        Rewrites a prompt to force step-by-step reasoning.
        """
        meta_prompt = f"""
        You are a Prompt Engineer.
        
        Original Prompt: "{original_prompt}"
        
        Task: Rewrite this prompt to include instructions for "Chain of Thought" reasoning. 
        Add instructions like "Think step by step" and "Explain your logic before answering".
        
        Return ONLY the rewritten prompt.
        """
        
        optimized = llm.complete("You are an expert prompt engineer.", meta_prompt)
        
        # Fallback if mock returns generic text
        if "step by step" not in optimized.lower():
             return f"{original_prompt}\n\nPlease think step by step. First explain your reasoning, then provide the final answer."
             
        return optimized

    def run_with_cot(self, prompt: str) -> str:
        """
        Optimizes the prompt and then executes it.
        """
        cot_prompt = self.optimize_prompt(prompt)
        print(f"✨ [CoT Optimizer] Rewrote prompt to:\n{cot_prompt}\n")
        
        return llm.complete("You are a reasoning engine.", cot_prompt)

if __name__ == "__main__":
    optimizer = ChainOfThoughtOptimizer()
    
    query = "If I have 3 apples and eat one, then buy two more, how many do I have?"
    result = optimizer.run_with_cot(query)
    
    print(f"💡 Result: {result}")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
