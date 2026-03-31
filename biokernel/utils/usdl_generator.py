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
import ast
import yaml
import re
from typing import Dict, Any

class USDLGenerator:
    def __init__(self, schema_version="1.0.0"):
        self.schema_version = schema_version

    def generate_usdl_from_file(self, file_path: str) -> Dict[str, Any]:
        """
        Parses a Python agent file and generates a USDL dictionary.
        """
        with open(file_path, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        # 1. Basic Metadata Extraction
        agent_class = self._find_agent_class(tree)
        if not agent_class:
            return None

        description = ast.get_docstring(agent_class) or "No description provided."
        name = agent_class.name.replace("Agent", "").replace("_", " ")
        
        # 2. Extract Capabilities (Public Methods)
        capabilities = []
        for node in agent_class.body:
            if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
                capabilities.append(self._parse_method(node))

        # 3. Construct USDL ID
        # e.g., Skills/Clinical/Prior_Authorization/agent.py -> clinical.prior_authorization
        rel_path = os.path.relpath(file_path, "Skills")
        parts = rel_path.split("/")
        domain = parts[0].lower()
        category = parts[1].lower() if len(parts) > 1 else "general"
        skill_id = f"biomedical.{domain}.{category}"

        # 4. Build USDL Structure
        return {
            "skill": {
                "id": skill_id,
                "version": "1.0.0",
                "name": name,
                "category": f"{domain}/{category}",
                "description": {
                    "short": description.split("\n")[0][:200],
                    "long": description,
                    "use_cases": ["Auto-generated from source code"]
                },
                "capabilities": capabilities,
                "metadata": {
                    "created": "2026-01-12",
                    "author": "BioKernel Auto-Generator"
                }
            }
        }

    def _find_agent_class(self, tree):
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and "Agent" in node.name:
                return node
        return None

    def _parse_method(self, node: ast.FunctionDef):
        inputs = []
        for arg in node.args.args:
            if arg.arg != "self":
                # Try to get type hint
                type_hint = "string"
                if arg.annotation:
                    type_hint = self._get_annotation_str(arg.annotation)
                
                inputs.append({
                    "name": arg.arg,
                    "type": type_hint,
                    "description": f"Input parameter {arg.arg}",
                    "required": True
                })

        # Try to infer output from return annotation
        output_type = "object"
        if node.returns:
            output_type = self._get_annotation_str(node.returns)

        return {
            "name": node.name,
            "description": ast.get_docstring(node) or f"Execute {node.name}",
            "inputs": inputs,
            "outputs": [
                {
                    "name": "result",
                    "type": output_type,
                    "description": "Result of the operation"
                }
            ]
        }

    def _get_annotation_str(self, node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Subscript):
            # Handle List[str], Dict[str, Any]
            val = self._get_annotation_str(node.value)
            if hasattr(node.slice, 'id'): # python < 3.9
                 slice_val = node.slice.id
            elif hasattr(node.slice, 'value'): # python 3.9+
                 slice_val = self._get_annotation_str(node.slice.value)
            else:
                 slice_val = "Any"
            return f"{val}[{slice_val}]"
        return "Any"

def scan_and_generate(root_dir="Skills"):
    generator = USDLGenerator()
    
    print(f"🔍 Scanning {root_dir} for Wild West agents...")
    
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith("_agent.py") or file == "agent.py" or file == "health_copilot.py" or file == "submission_drafter.py":
                full_path = os.path.join(root, file)
                
                # Check if .yaml already exists
                yaml_path = os.path.join(root, "skill.yaml")
                if os.path.exists(yaml_path):
                    continue

                print(f"  + Generating USDL for {file}...")
                usdl = generator.generate_usdl_from_file(full_path)
                
                if usdl:
                    with open(yaml_path, 'w') as f:
                        yaml.dump(usdl, f, sort_keys=False, default_flow_style=False)
                    print(f"    ✅ Saved to {yaml_path}")

if __name__ == "__main__":
    scan_and_generate()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
