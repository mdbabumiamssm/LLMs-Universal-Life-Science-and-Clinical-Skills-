from scanner import SkillsScanner
from planner import SkillsPlanner
from generator import SkillsGenerator
from git_manager import GitManager
import sys
import os

def main():
    print("=== Skills Maintenance Agent 2026 ===")
    
    # 1. Initialize Components
    root_dir = ".." # Since we are in Skills_Automation/
    if os.path.basename(os.getcwd()) != "Skills_Automation":
        root_dir = "." # Running from root
        
    scanner = SkillsScanner(root_dir)
    planner = SkillsPlanner(os.path.join(root_dir, "SKILLS_GAP_ANALYSIS_AND_IMPROVEMENT_PLAN_2026.md"))
    generator = SkillsGenerator(root_dir)
    git = GitManager(root_dir)

    # 2. Scan Inventory
    print("\n[Phase 1] Scanning Inventory...")
    inventory = scanner.scan()
    print(f"Found {sum(len(v) for v in inventory.values())} skill modules.")

    # 3. Analyze Gaps
    print("\n[Phase 2] Analyzing Gaps...")
    tasks = planner.analyze_gap(inventory)
    print(f"Identified {len(tasks)} improvement tasks.")
    
    if not tasks:
        print("No tasks found. Ensure the Plan file is correctly formatted.")
        sys.exit(0)

    # 4. Generate Content
    print("\n[Phase 3] Generating Content...")
    for task in tasks:
        print(f"Executing: {task['action']}")
        generator.generate_skill_content(task)

    # 5. Review & Commit
    print("\n[Phase 4] Git Operations...")
    print(git.status())
    
    # In a fully autonomous loop, we would commit. 
    # For safety in this demo, we stage and ask for confirmation or just commit if instructed.
    # The prompt asked to "commit", so we will.
    git.add_all()
    git.commit("Automated Skills Update: Orchestrator, ChemTools, MedPrompt")
    
    # We do NOT push by default to avoid auth errors in this script run, 
    # but the method is available in git_manager.py
    print("Changes committed locally. Run 'git push' to sync.")

if __name__ == "__main__":
    main()
