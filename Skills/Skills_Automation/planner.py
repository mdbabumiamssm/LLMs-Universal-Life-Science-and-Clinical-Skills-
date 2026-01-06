import os
import re

class SkillsPlanner:
    def __init__(self, plan_path="SKILLS_GAP_ANALYSIS_AND_IMPROVEMENT_PLAN_2026.md"):
        self.plan_path = plan_path

    def analyze_gap(self, inventory):
        """
        Reads the plan and compares with inventory to generate a task list.
        """
        tasks = []
        
        try:
            with open(self.plan_path, 'r', encoding='utf-8') as f:
                plan_content = f.read()
        except FileNotFoundError:
            print(f"Plan file {self.plan_path} not found.")
            return []

        # Heuristic parsing of the plan to find "Gap:" or "Action:" keywords
        # In a real rigorous system, we'd use an LLM to parse this. 
        # Here we use regex for the standalone script.
        
        lines = plan_content.split('\n')
        current_section = "General"
        
        for line in lines:
            if line.startswith('##'):
                current_section = line.strip('# ').strip()
            
            if "**Gap:**" in line or "**Missing:**" in line or "*Action:*" in line or "*Upgrade:*" in line:
                task_desc = line.split(':', 1)[1].strip()
                tasks.append({
                    'section': current_section,
                    'action': task_desc,
                    'priority': 'High'
                })

        return tasks

if __name__ == "__main__":
    # Mock inventory for testing
    planner = SkillsPlanner()
    tasks = planner.analyze_gap({})
    for t in tasks:
        print(f"[{t['priority']}] {t['section']}: {t['action']}")
