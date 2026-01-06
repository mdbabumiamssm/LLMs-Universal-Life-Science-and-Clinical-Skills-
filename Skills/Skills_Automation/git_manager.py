import subprocess
from datetime import datetime

class GitManager:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path

    def run_git(self, args):
        result = subprocess.run(['git'] + args, cwd=self.repo_path, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Git Error ({args}): {result.stderr}")
        return result.stdout.strip()

    def status(self):
        return self.run_git(['status', '--short'])

    def add_all(self):
        print("Staging files...")
        return self.run_git(['add', '.'])

    def commit(self, message):
        print(f"Committing with message: {message}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"{message}\n\nAutomated update by Skills_Automation Agent at {timestamp}"
        return self.run_git(['commit', '-m', full_message])

    def push(self):
        print("Pushing to remote...")
        # Note: This requires credentials to be set up in the environment/git config
        return self.run_git(['push'])

if __name__ == "__main__":
    gm = GitManager()
    print(gm.status())
