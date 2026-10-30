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
from typing import Dict, Any, Optional

# Adjust path to find sibling modules
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

try:
    from Skills.Agentic_AI.Agent_Architectures.Self_Correction.self_correction_agent import SelfCorrectionAgent
except ImportError:
    # Fallback for relative imports
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Agentic_AI/Agent_Architectures/Self_Correction")))
    from self_correction_agent import SelfCorrectionAgent

class MultiModalSymptomChecker:
    """
    Symptom Checker that combines user-reported symptoms (text) 
    with wearable data (vitals) to provide a more accurate assessment.
    """

    def __init__(self):
        self.agent = SelfCorrectionAgent()

    def check_symptoms(self, 
                     user_text: str,
                     vitals: Dict[str, float], 
                     history: Optional[str] = None) -> Dict[str, Any]:
        """
        Analyzes symptoms and vitals.
        """
        
        # 1. Define the Task
        task = f"""
        Role: AI Triage Assistant.
        
        User Report: "{user_text}"
        
        Current Vitals:
        - Heart Rate: {vitals.get('heart_rate', 'N/A')} bpm
        - Temperature: {vitals.get('temperature', 'N/A')} F
        - O2 Saturation: {vitals.get('spO2', 'N/A')}%
        """
        
        if history:
            task += f"\nMedical History: {history}"
            
        task += """
        
        Task:
        1. Correlate the subjective report with the objective vitals.
        2. Identify potential causes (differential diagnosis).
        3. Recommend a triage level (Home Care, Urgent Care, ER).
        4. Ask 1-2 clarifying questions.
        """

        # 2. Define Success Criteria
        criteria = [
            "Explicitly reference the vital signs in the analysis.",
            "Do not give definitive medical advice (use hedging).",
            "Provide a clear triage recommendation.",
            "Identify if vitals are abnormal (e.g., HR > 100, Temp > 100.4)."
        ]
        
        # 3. Execute Agent Loop
        print(f"--- Symptom Checker: Analyzing '{user_text}' ---")
        result = self.agent.run_cycle(task, criteria, max_iterations=2)
        
        return {
            "status": "success",
            "triage_assessment": result["final_output"],
            "vitals_analyzed": vitals
        }

def _demo():
    checker = MultiModalSymptomChecker()
    
    # Case: Flu-like symptoms with fever
    text = "I feel really weak and have the chills. My head hurts."
    vitals = {
        "heart_rate": 105,
        "temperature": 102.1,
        "spO2": 96
    }
    
    response = checker.check_symptoms(text, vitals, history="No significant history.")
    
    print("=== TRIAGE ASSESSMENT ===")
    print(response["triage_assessment"])

if __name__ == "__main__":
    _demo()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
