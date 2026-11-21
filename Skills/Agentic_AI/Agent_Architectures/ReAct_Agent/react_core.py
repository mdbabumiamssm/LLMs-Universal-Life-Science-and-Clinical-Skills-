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
ReAct Agent Core (2026 Update)

A standalone, functional implementation of the ReAct (Reasoning + Acting) pattern.
Includes a Mock LLM to demonstrate the "Thought -> Action -> Observation" loop.
"""

import re

class MockLLM:
    """Simulates an LLM that knows how to use a Calculator tool."""
    def generate(self, prompt: str) -> str:
        last_line = prompt.strip().split('\n')[-1]
        
        # Scenario: User asks "What is 15 * 7?"
        if "What is 15 * 7" in prompt and "Action:" not in prompt:
            return "Thought: I need to calculate 15 * 7.\nAction: Calculator[15 * 7]"
        
        elif "Observation: 105" in prompt:
            return "Thought: I have the result.\nFinal Answer: The answer is 105."
            
        return "Final Answer: I am not sure how to help with that."

class ReActAgent:
    def __init__(self, llm, tools: dict):
        self.llm = llm
        self.tools = tools
        self.max_steps = 5

    def run(self, question: str):
        print(f"--- ReAct Agent Query: {question} ---")
        history = f"Question: {question}\n"
        
        for i in range(self.max_steps):
            # 1. Think & Decide Action
            response = self.llm.generate(history)
            print(f"\n[Step {i+1} LLM Output]:\n{response}")
            
            history += response + "\n"
            
            if "Final Answer:" in response:
                return response.split("Final Answer:")[1].strip()
            
            # 2. Parse Action
            # Regex to capture: Action: ToolName[Args]
            match = re.search(r"Action: (\w+)\[(.*?)\]", response)
            if match:
                tool_name = match.group(1)
                args = match.group(2)
                
                # 3. Execute Tool
                if tool_name in self.tools:
                    print(f"[System] Executing {tool_name} with '{args}'...")
                    try:
                        result = self.tools[tool_name](args)
                        observation = f"Observation: {result}"
                    except Exception as e:
                        observation = f"Observation: Error - {e}"
                else:
                    observation = f"Observation: Tool {tool_name} not found."
                
                print(f"[System] {observation}")
                history += observation + "\n"
            else:
                # If no structured action found, stop to prevent infinite loops of nonsense
                print("[System] No valid action parsed.")
                break
                
        return "Agent timed out."

# --- Tools ---
def calculator(expression):
    # DANGEROUS in production (eval), but okay for pure python demo
    try:
        # whitelist chars
        if not re.match(r'^[\d\+\-\*\/\.\s]+$', expression):
            return "Invalid characters"
        return str(eval(expression))
    except:
        return "Error"

if __name__ == "__main__":
    # Setup
    llm = MockLLM()
    tools = {"Calculator": calculator}
    agent = ReActAgent(llm, tools)
    
    # Run
    final_answer = agent.run("What is 15 * 7?")
    print(f"\nResult: {final_answer}")
__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
