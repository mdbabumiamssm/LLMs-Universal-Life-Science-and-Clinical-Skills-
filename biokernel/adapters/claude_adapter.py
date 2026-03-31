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
Claude Platform Adapter for Universal Skill Definition Language (USDL)

Converts USDL skill definitions to:
1. MCP Server packages
2. Claude Code SKILL.md files
3. Claude API tool_use schemas
"""

import yaml
import json
from pathlib import Path
from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ClaudeSkillOutput:
    """Output container for Claude-specific skill formats"""
    skill_md: str
    mcp_server_config: Dict[str, Any]
    tool_use_schema: Dict[str, Any]
    hooks_config: Dict[str, Any]


class ClaudeAdapter:
    """
    Adapter to convert USDL skill definitions to Claude-compatible formats.

    Supports:
    - MCP (Model Context Protocol) Servers
    - Claude Code Skills (SKILL.md)
    - Claude API tool_use format
    - Claude Hooks
    """

    def __init__(self, usdl_path: str):
        """
        Initialize adapter with a USDL skill definition.

        Args:
            usdl_path: Path to USDL YAML file
        """
        self.usdl_path = Path(usdl_path)
        with open(self.usdl_path, 'r') as f:
            self.usdl = yaml.safe_load(f)
        self.skill = self.usdl['skill']

    def convert(self) -> ClaudeSkillOutput:
        """Convert USDL to all Claude formats."""
        return ClaudeSkillOutput(
            skill_md=self.generate_skill_md(),
            mcp_server_config=self.generate_mcp_server(),
            tool_use_schema=self.generate_tool_use_schema(),
            hooks_config=self.generate_hooks_config()
        )

    def generate_skill_md(self) -> str:
        """
        Generate Claude Code SKILL.md format.

        Returns:
            String content for SKILL.md file
        """
        skill = self.skill

        # Build the SKILL.md content
        md_content = f"""# {skill['name']}

{skill['description']['long']}

## Capabilities

"""
        # Add capabilities
        for cap in skill['capabilities']:
            md_content += f"### {cap['name']}\n\n"
            md_content += f"{cap['description']}\n\n"

            if cap.get('inputs'):
                md_content += "**Inputs:**\n"
                for inp in cap['inputs']:
                    required = "(required)" if inp.get('required', True) else "(optional)"
                    default = f" [default: {inp['default']}]" if 'default' in inp else ""
                    md_content += f"- `{inp['name']}` ({inp['type']}) {required}: {inp.get('description', '')}{default}\n"
                md_content += "\n"

            if cap.get('outputs'):
                md_content += "**Outputs:**\n"
                for out in cap['outputs']:
                    md_content += f"- `{out['name']}` ({out['type']}): {out.get('description', '')}\n"
                md_content += "\n"

        # Add prompts section
        if skill.get('prompts'):
            md_content += "## System Prompt\n\n"
            md_content += f"```\n{skill['prompts'].get('system', '')}\n```\n\n"

            if skill['prompts'].get('examples'):
                md_content += "## Examples\n\n"
                for i, example in enumerate(skill['prompts']['examples'], 1):
                    md_content += f"### Example {i}\n\n"
                    md_content += f"**User:** {example['user']}\n\n"
                    md_content += f"**Assistant:** {example['assistant']}\n\n"

        # Add dependencies
        if skill.get('dependencies'):
            md_content += "## Dependencies\n\n"
            if skill['dependencies'].get('python'):
                md_content += "### Python Packages\n"
                md_content += "```\n"
                md_content += "\n".join(skill['dependencies']['python'])
                md_content += "\n```\n\n"

        # Add metadata footer
        md_content += f"""---

**Skill ID:** `{skill['id']}`
**Version:** {skill['version']}
**Category:** {skill['category']}
**License:** {skill['metadata'].get('license', 'MIT')}
**Generated:** {datetime.now().strftime('%Y-%m-%d')}
"""

        return md_content

    def generate_mcp_server(self) -> Dict[str, Any]:
        """
        Generate MCP Server configuration.

        Returns:
            Dictionary containing MCP server config
        """
        skill = self.skill

        # Generate tools for MCP
        mcp_tools = []
        for cap in skill['capabilities']:
            tool = {
                "name": cap['name'],
                "description": cap['description'],
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }

            for inp in cap.get('inputs', []):
                prop = {
                    "type": self._map_type_to_json_schema(inp['type']),
                    "description": inp.get('description', '')
                }
                if 'default' in inp:
                    prop['default'] = inp['default']
                tool['inputSchema']['properties'][inp['name']] = prop

                if inp.get('required', True):
                    tool['inputSchema']['required'].append(inp['name'])

            mcp_tools.append(tool)

        # MCP Server configuration
        mcp_config = {
            "name": skill['id'].replace('.', '-'),
            "version": skill['version'],
            "description": skill['description']['short'],
            "tools": mcp_tools,
            "resources": [],
            "prompts": [
                {
                    "name": f"{skill['id']}_system",
                    "description": f"System prompt for {skill['name']}",
                    "messages": [
                        {
                            "role": "system",
                            "content": skill.get('prompts', {}).get('system', '')
                        }
                    ]
                }
            ]
        }

        return mcp_config

    def generate_tool_use_schema(self) -> Dict[str, Any]:
        """
        Generate Claude API tool_use schema.

        Returns:
            Dictionary containing tool definitions for Claude API
        """
        skill = self.skill
        tools = []

        for cap in skill['capabilities']:
            tool = {
                "name": cap['name'],
                "description": cap['description'],
                "input_schema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }

            for inp in cap.get('inputs', []):
                prop = {
                    "type": self._map_type_to_json_schema(inp['type']),
                    "description": inp.get('description', '')
                }
                tool['input_schema']['properties'][inp['name']] = prop

                if inp.get('required', True):
                    tool['input_schema']['required'].append(inp['name'])

            tools.append(tool)

        return {"tools": tools}

    def generate_hooks_config(self) -> Dict[str, Any]:
        """
        Generate Claude Code hooks configuration.

        Returns:
            Dictionary containing hooks config
        """
        skill = self.skill
        hooks_config = skill.get('platform_configs', {}).get('claude', {}).get('hooks', [])

        hooks = {}
        if 'pre_execution_validation' in hooks_config:
            hooks['PreToolUse'] = [{
                "matcher": skill['id'],
                "hooks": ["validate_inputs"]
            }]

        return hooks

    def _map_type_to_json_schema(self, usdl_type: str) -> str:
        """Map USDL types to JSON Schema types."""
        type_mapping = {
            'string': 'string',
            'integer': 'integer',
            'float': 'number',
            'boolean': 'boolean',
            'list': 'array',
            'dict': 'object',
            'AnnData': 'string',  # File path
            'DataFrame': 'string',  # File path or JSON
        }
        return type_mapping.get(usdl_type, 'string')

    def save_outputs(self, output_dir: str) -> Dict[str, str]:
        """
        Save all generated outputs to directory.

        Args:
            output_dir: Directory to save outputs

        Returns:
            Dictionary mapping output type to file path
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        outputs = self.convert()
        saved_files = {}

        # Save SKILL.md
        skill_md_path = output_path / "SKILL.md"
        with open(skill_md_path, 'w') as f:
            f.write(outputs.skill_md)
        saved_files['skill_md'] = str(skill_md_path)

        # Save MCP server config
        mcp_path = output_path / "mcp_server.json"
        with open(mcp_path, 'w') as f:
            json.dump(outputs.mcp_server_config, f, indent=2)
        saved_files['mcp_server'] = str(mcp_path)

        # Save tool_use schema
        tools_path = output_path / "claude_tools.json"
        with open(tools_path, 'w') as f:
            json.dump(outputs.tool_use_schema, f, indent=2)
        saved_files['tool_use'] = str(tools_path)

        # Save hooks config
        hooks_path = output_path / "hooks.json"
        with open(hooks_path, 'w') as f:
            json.dump(outputs.hooks_config, f, indent=2)
        saved_files['hooks'] = str(hooks_path)

        return saved_files


# CLI interface
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python claude_adapter.py <usdl_file.yaml> [output_dir]")
        sys.exit(1)

    usdl_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./claude_output"

    adapter = ClaudeAdapter(usdl_file)
    saved = adapter.save_outputs(output_dir)

    print(f"Generated Claude skill files:")
    for output_type, path in saved.items():
        print(f"  - {output_type}: {path}")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
