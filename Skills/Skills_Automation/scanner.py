# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

import os
import json
from pathlib import Path

class SkillsScanner:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.ignore_dirs = {'.git', '__pycache__', 'Skills_Automation', '.gemini'}

    def scan(self):
        inventory = {}
        for root, dirs, files in os.walk(self.root_dir):
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
            
            rel_path = os.path.relpath(root, self.root_dir)
            if rel_path == '.':
                continue

            category = rel_path.split(os.sep)[0]
            if category not in inventory:
                inventory[category] = []

            # Check for README
            readme_content = ""
            if 'README.md' in files:
                try:
                    with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
                        readme_content = f.read(1000) # Read first 1000 chars for context
                except Exception:
                    pass

            item = {
                'path': rel_path,
                'files': files,
                'description': self._extract_description(readme_content)
            }
            inventory[category].append(item)
        
        return inventory

    def _extract_description(self, content):
        if not content:
            return "No description available."
        # Simple extraction of the first paragraph or header
        lines = content.split('\n')
        for line in lines:
            if line.strip() and not line.startswith('#'):
                return line.strip()
        return "Description not found."

if __name__ == "__main__":
    scanner = SkillsScanner(".")
    inventory = scanner.scan()
    print(json.dumps(inventory, indent=2))

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
