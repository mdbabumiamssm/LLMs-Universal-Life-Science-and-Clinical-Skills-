import os
import glob
import shutil
import json
import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def validate_skill_md(content):
    if not content: return False
    if "#" not in content: return False
    return True

def get_reliability_score(repo_name):
    # Basic reliability scoring based on github stars or predefined list
    if repo_name == "TianGzlab/OmicsClaw":
        return 0.95
    return 0.5

def sync_skills_from_dir(src_dir, dest_dir, repo_name):
    score = get_reliability_score(repo_name)
    if score < 0.8:
        print(f"Skipping {repo_name} due to low reliability score ({score})")
        return

    skill_files = glob.glob(os.path.join(src_dir, "**", "SKILL.md"), recursive=True)
    skill_files += glob.glob(os.path.join(src_dir, "**", "skill.md"), recursive=True)
    
    updated_count = 0
    new_count = 0

    for src_path in skill_files:
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        if not validate_skill_md(content):
            print(f"Skipping invalid SKILL.md: {src_path}")
            continue

        # Determine relative path from src_dir
        rel_path = os.path.relpath(src_path, src_dir)
        # Often it starts with "skills/" or "knowledge_base/"
        # Let's just put them inside dest_dir / repo_name / rel_path
        # But wait, OmicsClaw has `skills/` and `knowledge_base/`. We can put them in `Skills/OmicsClaw/...`
        # Actually, let's map `skills/` to `Skills/` if they overlap, but maybe better to put them all in `Skills/External_Collections/OmicsClaw/` to be safe and structured.
        
        target_path = os.path.join(dest_dir, "External_Collections", "OmicsClaw", rel_path)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        is_update = os.path.exists(target_path)
        if is_update:
            updated_count += 1
        else:
            new_count += 1

        shutil.copy2(src_path, target_path)

    print(f"Synced from {repo_name}: {new_count} new, {updated_count} updated.")

def main():
    base_skills_dir = os.path.abspath("Skills")
    if not os.path.exists(base_skills_dir):
        os.makedirs(base_skills_dir)
        
    print("1. Scanning 'Skills/' for existing SKILL.md files...")
    existing = glob.glob(os.path.join(base_skills_dir, "**", "SKILL.md"), recursive=True)
    print(f"Found {len(existing)} existing SKILL.md files.")

    print("2. Integrating new skills via SKILL.md format from OmicsClaw...")
    omicsclaw_dir = "/home/drdx/.gemini/tmp/4f5a8d6d80f9f1aabe508f3421ea3f1a737b5185f913f438fbdbf47933db7a29/OmicsClaw"
    if os.path.exists(omicsclaw_dir):
        sync_skills_from_dir(omicsclaw_dir, base_skills_dir, "TianGzlab/OmicsClaw")

    print("9. Querying GitHub for 'SKILL.md' or 'agent capability' repos...")
    # Example GitHub search using gh
    # gh search repos "topic:ai-skill" --limit 5 --json nameWithOwner,stargazersCount
    try:
        search_result = run_cmd('gh search repos "topic:ai-skill" --limit 2 --json nameWithOwner,stargazersCount')
        if search_result:
            repos = json.loads(search_result)
            for r in repos:
                repo_name = r.get("nameWithOwner")
                stars = r.get("stargazersCount", 0)
                print(f"Found related repo: {repo_name} (Stars: {stars})")
    except Exception as e:
        print("Could not query gh: ", e)

    print("13. Use git add . for staging.")
    run_cmd("git add Skills/")
    run_cmd("git add .")

    print("14. Craft commit message.")
    run_cmd('git commit -m "feat: Add/update skills from GitHub"')

    print("15. Execute git push origin main.")
    print("Push skipped in script, will be done via agent command.")

if __name__ == "__main__":
    main()
