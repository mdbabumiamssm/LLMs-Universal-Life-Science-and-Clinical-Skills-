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
OpenAI Platform Adapter for Universal Skill Definition Language (USDL)

Converts USDL skill definitions to:
1. Custom GPT configurations (GPT Builder)
2. Assistants API format
3. Function calling schemas
4. OpenAPI specs for GPT Actions
"""

import yaml
import json
from pathlib import Path
from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class OpenAISkillOutput:
    """Output container for OpenAI-specific skill formats"""
    gpt_config: Dict[str, Any]
    assistant_config: Dict[str, Any]
    function_schemas: List[Dict[str, Any]]
    openapi_spec: Dict[str, Any]


class OpenAIAdapter:
    """
    Adapter to convert USDL skill definitions to OpenAI-compatible formats.

    Supports:
    - Custom GPTs (GPT Builder/GPT Store)
    - Assistants API
    - Function Calling
    - GPT Actions (OpenAPI)
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

    def convert(self) -> OpenAISkillOutput:
        """Convert USDL to all OpenAI formats."""
        return OpenAISkillOutput(
            gpt_config=self.generate_custom_gpt(),
            assistant_config=self.generate_assistant(),
            function_schemas=self.generate_function_schemas(),
            openapi_spec=self.generate_openapi_action()
        )

    def generate_custom_gpt(self) -> Dict[str, Any]:
        """
        Generate Custom GPT configuration for GPT Builder.

        Returns:
            Dictionary containing GPT configuration
        """
        skill = self.skill

        # Build instructions from system prompt and capabilities
        instructions = skill.get('prompts', {}).get('system', '')
        instructions += "\n\n## Your Capabilities:\n"
        for cap in skill['capabilities']:
            instructions += f"\n### {cap['name']}\n{cap['description']}\n"

        # Build conversation starters from examples
        starters = []
        for example in skill.get('prompts', {}).get('examples', [])[:4]:
            starters.append(example['user'][:100])  # Limit length

        if not starters:
            starters = [
                f"Help me with {skill['name'].lower()}",
                f"What can you do for {skill['category']}?",
                "Show me an example workflow",
                "What parameters can I configure?"
            ]

        gpt_config = {
            "name": skill['name'],
            "description": skill['description']['short'],
            "instructions": instructions,
            "conversation_starters": starters,
            "capabilities": {
                "web_browsing": False,
                "dalle_image_generation": False,
                "code_interpreter": True  # Usually needed for biomedical
            },
            "profile_picture": None,  # Would need to generate
            "actions": [],  # Populated separately if needed
            "knowledge_files": skill.get('dependencies', {}).get('data', [])
        }

        return gpt_config

    def generate_assistant(self) -> Dict[str, Any]:
        """
        Generate OpenAI Assistants API configuration.

        Returns:
            Dictionary for creating an Assistant
        """
        skill = self.skill

        # Build tools list
        tools = []

        # Add code interpreter if Python dependencies exist
        if skill.get('dependencies', {}).get('python'):
            tools.append({"type": "code_interpreter"})

        # Add function tools
        for cap in skill['capabilities']:
            tool = {
                "type": "function",
                "function": self._capability_to_function(cap)
            }
            tools.append(tool)

        assistant_config = {
            "name": skill['name'],
            "description": skill['description']['short'],
            "instructions": skill.get('prompts', {}).get('system', ''),
            "model": "gpt-4-turbo-preview",  # Default to latest
            "tools": tools,
            "metadata": {
                "usdl_id": skill['id'],
                "usdl_version": skill['version'],
                "category": skill['category']
            }
        }

        return assistant_config

    def generate_function_schemas(self) -> List[Dict[str, Any]]:
        """
        Generate function calling schemas.

        Returns:
            List of function definitions
        """
        skill = self.skill
        functions = []

        for cap in skill['capabilities']:
            functions.append(self._capability_to_function(cap))

        return functions

    def generate_openapi_action(self) -> Dict[str, Any]:
        """
        Generate OpenAPI 3.0 spec for GPT Actions.

        Returns:
            OpenAPI specification dictionary
        """
        skill = self.skill
        skill_id = skill['id'].replace('.', '-')

        # Build paths from capabilities
        paths = {}
        for cap in skill['capabilities']:
            path = f"/{cap['name']}"

            # Build request body schema
            request_schema = {
                "type": "object",
                "properties": {},
                "required": []
            }

            for inp in cap.get('inputs', []):
                request_schema['properties'][inp['name']] = {
                    "type": self._map_type_to_openapi(inp['type']),
                    "description": inp.get('description', '')
                }
                if inp.get('required', True):
                    request_schema['required'].append(inp['name'])

            # Build response schema
            response_schema = {
                "type": "object",
                "properties": {}
            }
            for out in cap.get('outputs', []):
                response_schema['properties'][out['name']] = {
                    "type": self._map_type_to_openapi(out['type']),
                    "description": out.get('description', '')
                }

            paths[path] = {
                "post": {
                    "operationId": cap['name'],
                    "summary": cap['description'],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": request_schema
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Successful operation",
                            "content": {
                                "application/json": {
                                    "schema": response_schema
                                }
                            }
                        }
                    }
                }
            }

        openapi_spec = {
            "openapi": "3.0.0",
            "info": {
                "title": skill['name'],
                "description": skill['description']['long'],
                "version": skill['version'],
                "contact": {
                    "name": skill['metadata'].get('author', 'Unknown')
                }
            },
            "servers": [
                {
                    "url": f"https://api.biomedical-skills.io/v1/{skill_id}",
                    "description": "Production server"
                }
            ],
            "paths": paths,
            "components": {
                "securitySchemes": {
                    "ApiKeyAuth": {
                        "type": "apiKey",
                        "in": "header",
                        "name": "X-API-Key"
                    }
                }
            },
            "security": [{"ApiKeyAuth": []}]
        }

        return openapi_spec

    def _capability_to_function(self, cap: Dict[str, Any]) -> Dict[str, Any]:
        """Convert a USDL capability to OpenAI function schema."""
        parameters = {
            "type": "object",
            "properties": {},
            "required": []
        }

        for inp in cap.get('inputs', []):
            param = {
                "type": self._map_type_to_openapi(inp['type']),
                "description": inp.get('description', '')
            }
            if 'default' in inp:
                param['default'] = inp['default']
            parameters['properties'][inp['name']] = param

            if inp.get('required', True):
                parameters['required'].append(inp['name'])

        return {
            "name": cap['name'],
            "description": cap['description'],
            "parameters": parameters
        }

    def _map_type_to_openapi(self, usdl_type: str) -> str:
        """Map USDL types to OpenAPI types."""
        type_mapping = {
            'string': 'string',
            'integer': 'integer',
            'float': 'number',
            'boolean': 'boolean',
            'list': 'array',
            'dict': 'object',
            'AnnData': 'string',
            'DataFrame': 'string',
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

        # Save GPT config
        gpt_path = output_path / "custom_gpt.json"
        with open(gpt_path, 'w') as f:
            json.dump(outputs.gpt_config, f, indent=2)
        saved_files['custom_gpt'] = str(gpt_path)

        # Save Assistant config
        assistant_path = output_path / "assistant.json"
        with open(assistant_path, 'w') as f:
            json.dump(outputs.assistant_config, f, indent=2)
        saved_files['assistant'] = str(assistant_path)

        # Save function schemas
        functions_path = output_path / "functions.json"
        with open(functions_path, 'w') as f:
            json.dump(outputs.function_schemas, f, indent=2)
        saved_files['functions'] = str(functions_path)

        # Save OpenAPI spec
        openapi_path = output_path / "openapi.yaml"
        with open(openapi_path, 'w') as f:
            yaml.dump(outputs.openapi_spec, f, default_flow_style=False)
        saved_files['openapi'] = str(openapi_path)

        return saved_files


# CLI interface
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python openai_adapter.py <usdl_file.yaml> [output_dir]")
        sys.exit(1)

    usdl_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./openai_output"

    adapter = OpenAIAdapter(usdl_file)
    saved = adapter.save_outputs(output_dir)

    print(f"Generated OpenAI skill files:")
    for output_type, path in saved.items():
        print(f"  - {output_type}: {path}")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
