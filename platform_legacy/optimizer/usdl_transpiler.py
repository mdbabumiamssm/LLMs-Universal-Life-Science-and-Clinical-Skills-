# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
USDL (Universal Skill Description Language) Transpiler.

Transforms a canonical skill specification into provider-specific
payloads so a single skill can run across Anthropic, OpenAI, Gemini,
and local models.

The USDL spec is the bridge between declarative skill definitions
(SKILL.md) and executable LLM prompts + tool schemas.
"""

from __future__ import annotations

import json
import re
import yaml
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Data Model
# ---------------------------------------------------------------------------

@dataclass
class FieldSpec:
    """Describes an input or output field."""
    name: str
    description: str
    type: str
    required: bool = True
    default: Optional[Any] = None


@dataclass
class USDLSpec:
    """
    Canonical representation of a biomedical skill.

    This is the intermediate representation that the transpiler converts
    into provider-specific formats.
    """
    name: str
    description: str
    inputs: List[FieldSpec] = field(default_factory=list)
    outputs: List[FieldSpec] = field(default_factory=list)
    safety_checks: List[str] = field(default_factory=list)
    audit_policy: str = "Log all decisions to BioKernel event bus."
    instructions_body: str = ""
    version: str = "1.0.0"
    category: str = "general"

    @classmethod
    def from_dict(cls, payload: Dict[str, Any]) -> USDLSpec:
        """Deserialize from a JSON/YAML dictionary."""
        return cls(
            name=payload["name"],
            description=payload["description"],
            inputs=[FieldSpec(**f) for f in payload.get("inputs", [])],
            outputs=[FieldSpec(**f) for f in payload.get("outputs", [])],
            safety_checks=payload.get("safety_checks", []),
            audit_policy=payload.get("audit_policy", "Log decisions to event bus."),
            instructions_body=payload.get("instructions_body", ""),
            version=payload.get("version", "1.0.0"),
            category=payload.get("category", "general"),
        )

    @classmethod
    def from_skill_md(cls, content: str) -> USDLSpec:
        """
        Parse a SKILL.md file into a USDLSpec.

        Uses PyYAML for robust frontmatter parsing.
        """
        name = "Unknown Skill"
        description = "No description provided."
        body = content

        if content.startswith("---"):
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
            if match:
                try:
                    fm = yaml.safe_load(match.group(1))
                    if isinstance(fm, dict):
                        name = fm.get("name", name)
                        description = fm.get("description", description)
                    body = match.group(2).strip()
                except yaml.YAMLError:
                    pass

        # Infer safety checks from body content
        safety_checks = []
        safety_keywords = ["safety", "risk", "contraindication", "warning", "caution"]
        if any(kw in body.lower() for kw in safety_keywords):
            safety_checks.append("Review skill instructions for safety guidelines.")

        return cls(
            name=name,
            description=description if isinstance(description, str) else str(description),
            safety_checks=safety_checks,
            audit_policy="Log execution of SKILL.md-based agent.",
            instructions_body=body,
        )

    @classmethod
    def from_yaml_file(cls, path: str) -> USDLSpec:
        """Load a USDL spec from a YAML file."""
        with open(path) as f:
            data = yaml.safe_load(f)
        skill = data.get("skill", data)
        return cls.from_dict(skill)


# ---------------------------------------------------------------------------
# Provider Enum
# ---------------------------------------------------------------------------

class Provider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"


# ---------------------------------------------------------------------------
# Transpiler
# ---------------------------------------------------------------------------

class USDLTranspiler:
    """
    Converts USDL specs into provider-specific prompt + schema bundles.

    Each provider gets an optimized output format:
    - **Anthropic**: XML-structured prompts with thinking blocks
    - **OpenAI**: System/user messages with function schemas
    - **Gemini**: Role cards with structured context
    """

    def compile(self, spec: USDLSpec, provider: Provider) -> Dict[str, Any]:
        """Compile a USDL spec for a specific provider."""
        compilers = {
            Provider.OPENAI: self._compile_openai,
            Provider.ANTHROPIC: self._compile_anthropic,
            Provider.GEMINI: self._compile_gemini,
        }
        compiler = compilers.get(provider)
        if compiler is None:
            raise ValueError(f"Unsupported provider: {provider}")
        return compiler(spec)

    def compile_all(self, spec: USDLSpec) -> Dict[str, Dict[str, Any]]:
        """Compile for all providers at once."""
        return {p.value: self.compile(spec, p) for p in Provider}

    # -- Provider implementations --------------------------------------------

    def _compile_openai(self, spec: USDLSpec) -> Dict[str, Any]:
        system = (
            f"You are the '{spec.name}' biomedical agent. "
            f"{spec.description}\n\n"
            "### Instructions\n"
            f"{spec.instructions_body}\n\n"
            "Emit structured JSON when a schema is provided. "
            "Cite relevant clinical policies and literature."
        )
        if spec.safety_checks:
            system += "\n\n### Safety\n" + "\n".join(f"- {s}" for s in spec.safety_checks)

        return {
            "provider": "openai",
            "system_message": system,
            "function_schemas": self._openai_functions(spec) if spec.inputs else [],
            "output_schema": self._json_schema(spec.outputs) if spec.outputs else {},
            "safety_checks": spec.safety_checks,
            "audit_policy": spec.audit_policy,
        }

    def _compile_anthropic(self, spec: USDLSpec) -> Dict[str, Any]:
        prompt = self._render_xml_prompt(spec)
        return {
            "provider": "anthropic",
            "system_prompt": prompt,
            "tool_definitions": self._anthropic_tools(spec) if spec.inputs else [],
            "safety_checks": spec.safety_checks,
            "audit_policy": spec.audit_policy,
        }

    def _compile_gemini(self, spec: USDLSpec) -> Dict[str, Any]:
        parts = [
            f"Role: {spec.name}",
            f"Objective: {spec.description}",
            "--- INSTRUCTIONS ---",
            spec.instructions_body,
            "---",
        ]
        if spec.inputs:
            parts.append("Inputs:\n" + "\n".join(
                f"- {f.name} ({f.type}): {f.description}" for f in spec.inputs
            ))
        if spec.outputs:
            parts.append("Expected Outputs:\n" + "\n".join(
                f"- {f.name} ({f.type}): {f.description}" for f in spec.outputs
            ))
        if spec.safety_checks:
            parts.append("Safety:\n" + "\n".join(f"- {s}" for s in spec.safety_checks))

        return {
            "provider": "gemini",
            "prompt": "\n".join(parts),
            "output_constraints": [f.name for f in spec.outputs],
            "audit_policy": spec.audit_policy,
        }

    # -- Schema helpers -------------------------------------------------------

    @staticmethod
    def _json_schema(fields: List[FieldSpec]) -> Dict[str, Any]:
        props = {
            f.name: {"type": f.type, "description": f.description}
            for f in fields
        }
        required = [f.name for f in fields if f.required]
        return {"type": "object", "properties": props, "required": required}

    def _openai_functions(self, spec: USDLSpec) -> List[Dict[str, Any]]:
        return [{
            "name": spec.name.lower().replace(" ", "_"),
            "description": spec.description,
            "parameters": self._json_schema(spec.inputs),
        }]

    def _anthropic_tools(self, spec: USDLSpec) -> List[Dict[str, Any]]:
        return [{
            "name": spec.name.lower().replace(" ", "_"),
            "description": spec.description,
            "input_schema": self._json_schema(spec.inputs),
        }]

    def _render_xml_prompt(self, spec: USDLSpec) -> str:
        """Render Claude-optimized XML prompt."""
        input_xml = "\n".join(
            f"  <input name='{f.name}' type='{f.type}' required='{f.required}'>"
            f"{f.description}</input>"
            for f in spec.inputs
        )
        output_xml = "\n".join(
            f"  <output name='{f.name}' type='{f.type}'>{f.description}</output>"
            for f in spec.outputs
        )
        safety_xml = "\n".join(
            f"  <policy>{p}</policy>" for p in spec.safety_checks
        )

        return f"""<system>
  <role>{spec.name}</role>
  <description>{spec.description}</description>
  <version>{spec.version}</version>

  <instructions>
{spec.instructions_body}
  </instructions>

  <inputs>
{input_xml}
  </inputs>

  <outputs>
{output_xml}
  </outputs>

  <safety>
{safety_xml}
  </safety>

  <audit>{spec.audit_policy}</audit>
</system>"""


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _demo():
    """Run a transpilation demo."""
    spec = USDLSpec(
        name="Prior Authorization Agent",
        description="Review prior authorization requests against payer policy and emit determinations.",
        inputs=[
            FieldSpec(name="clinical_note", description="Unstructured clinical note", type="string"),
            FieldSpec(name="procedure_code", description="CPT/HCPCS code", type="string"),
        ],
        outputs=[
            FieldSpec(name="decision", description="APPROVED or DENIED", type="string"),
            FieldSpec(name="rationale", description="Clinical reasoning", type="string"),
        ],
        safety_checks=[
            "Never hallucinate policy references.",
            "Escalate unclear cases to human reviewers.",
            "Include relevant regulatory citations.",
        ],
        audit_policy="Post determination + trace to event bus topic prior_auth.decisions.",
    )

    transpiler = USDLTranspiler()
    for provider in Provider:
        artifact = transpiler.compile(spec, provider)
        print(f"\n{'='*60}")
        print(f"  {provider.value.upper()}")
        print(f"{'='*60}")
        print(json.dumps(artifact, indent=2))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--file":
        spec = USDLSpec.from_yaml_file(sys.argv[2])
        provider = Provider(sys.argv[3]) if len(sys.argv) > 3 else Provider.ANTHROPIC
        result = USDLTranspiler().compile(spec, provider)
        print(json.dumps(result, indent=2))
    else:
        _demo()
