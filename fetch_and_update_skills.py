import os
import glob
import shutil
import subprocess

def run_cmd(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing {cmd}: {result.stderr}")
    return result.stdout.strip()

def validate_skill_md(content):
    if not content: return False
    if "#" not in content: return False
    return True

def sync_skills_from_repo(repo_full_name, tmp_dir, dest_dir):
    repo_owner, repo_name = repo_full_name.split("/")
    repo_url = f"https://github.com/{repo_full_name}.git"
    clone_dir = os.path.join(tmp_dir, repo_name)
    
    # Clone the repo
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    run_cmd(f"git clone --depth 1 {repo_url} {clone_dir}")
    
    if not os.path.exists(clone_dir):
        print(f"Failed to clone {repo_full_name}")
        return

    # Find SKILL.md or skill.md
    skill_files = glob.glob(os.path.join(clone_dir, "**", "SKILL.md"), recursive=True)
    skill_files += glob.glob(os.path.join(clone_dir, "**", "skill.md"), recursive=True)
    
    updated_count = 0
    new_count = 0

    for src_path in skill_files:
        try:
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Could not read {src_path}: {e}")
            continue

        if not validate_skill_md(content):
            continue

        # Determine relative path from clone_dir
        rel_path = os.path.relpath(src_path, clone_dir)
        
        target_path = os.path.join(dest_dir, "External_Collections", repo_name, rel_path)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        is_update = os.path.exists(target_path)
        if is_update:
            updated_count += 1
        else:
            new_count += 1

        shutil.copy2(src_path, target_path)

    print(f"Synced from {repo_full_name}: {new_count} new, {updated_count} updated.")
    
    # Cleanup
    shutil.rmtree(clone_dir, ignore_errors=True)

def main():
    base_skills_dir = os.path.abspath("Skills")
    tmp_dir = "/home/drdx/.gemini/tmp/4f5a8d6d80f9f1aabe508f3421ea3f1a737b5185f913f438fbdbf47933db7a29/repos"
    os.makedirs(tmp_dir, exist_ok=True)
    
    repos_to_check = [
        "anthropics/skills",
        "obra/superpowers",
        "vercel-labs/agent-skills",
        "agentskills/agentskills"
    ]

    for repo in repos_to_check:
        sync_skills_from_repo(repo, tmp_dir, base_skills_dir)

if __name__ == "__main__":
    main()
