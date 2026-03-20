# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
BioKernel Server — The core orchestration engine.

A FastAPI application that:
1. Discovers and indexes biomedical skills from the filesystem
2. Routes user queries to the best-matching skill via semantic similarity
3. Executes skills through a unified LLM provider abstraction
4. Supports autonomous, interactive, and manual execution modes
5. Orchestrates multi-step DAG workflows
6. Exposes a RESTful API and health endpoints

This is the central runtime of the Universal Biomedical Skills Platform.
"""

from __future__ import annotations

import os
import re
import time
import yaml
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from platform.adapters.factory import LLMFactory
from platform.biokernel.router import SkillRouter
from platform.biokernel.workflow_engine import WorkflowEngine
from platform.interface.llm_provider import LLMProvider
from platform.observability import configure_logging, get_logger
from platform.schema.io_types import (
    AgentRequest,
    AgentResponse,
    AgentStep,
    ExecutionMode,
    LLMRequest,
    ProviderName,
    SkillMetadata,
    SkillType,
    WorkflowDefinition,
    WorkflowStep,
    WorkflowStatus,
)


# ---------------------------------------------------------------------------
# Configuration loader
# ---------------------------------------------------------------------------

def load_config(config_path: str | None = None) -> Dict[str, Any]:
    """Load YAML configuration, falling back to defaults."""
    paths_to_try = [
        config_path,
        os.getenv("BIOKERNEL_CONFIG"),
        "platform/config.yaml",
        "config.yaml",
    ]
    for p in paths_to_try:
        if p and Path(p).exists():
            with open(p) as f:
                return yaml.safe_load(f)
    return {}


# ---------------------------------------------------------------------------
# BioKernel Core
# ---------------------------------------------------------------------------

class BioKernel:
    """
    The BioKernel orchestrates skill discovery, routing, and execution.

    This class is independent of FastAPI and can be used programmatically
    in scripts, notebooks, or embedded in other applications.
    """

    def __init__(self, config: Dict[str, Any] | None = None) -> None:
        self.config = config or load_config()
        self.logger = get_logger("biokernel")

        # Configure logging
        sys_cfg = self.config.get("system", {})
        configure_logging(
            level=sys_cfg.get("log_level", "INFO"),
            json_output=sys_cfg.get("log_json", False),
        )

        # Initialize components
        routing_cfg = self.config.get("routing", {})
        self.router = SkillRouter(
            similarity_threshold=routing_cfg.get("similarity_threshold", 0.35)
        )
        self.workflow_engine = WorkflowEngine(
            max_retries=self.config.get("workflow", {}).get("retry_count", 2),
            retry_delay=self.config.get("workflow", {}).get("retry_delay_seconds", 5),
            step_timeout=self.config.get("workflow", {}).get("step_timeout_seconds", 120),
        )

        # Initialize LLM providers
        self.providers: Dict[str, LLMProvider] = {}
        self._init_providers()

        # Discover skills
        self._discover_skills()

        self.logger.info(
            "BioKernel initialized",
            skills_count=len(self.router.skills),
            providers=list(self.providers.keys()),
        )

    # -- Provider initialization ----------------------------------------------

    def _init_providers(self) -> None:
        """Initialize configured LLM providers."""
        LLMFactory.register_defaults()
        providers_cfg = self.config.get("providers", {})

        for name, cfg in providers_cfg.items():
            try:
                provider = LLMFactory.create_provider(name, cfg)
                if provider.is_available:
                    self.providers[name] = provider
            except Exception as exc:
                self.logger.warning(
                    "Failed to initialize provider",
                    provider=name,
                    error=str(exc),
                )

    def get_provider(self, preference: ProviderName | str = "anthropic") -> LLMProvider:
        """Get a provider by name, with fallback chain."""
        name = preference.value if isinstance(preference, ProviderName) else preference

        if name in self.providers:
            return self.providers[name]

        # Fallback chain
        for fallback in ["anthropic", "openai", "gemini", "local"]:
            if fallback in self.providers:
                self.logger.info(
                    "Provider fallback",
                    requested=name,
                    using=fallback,
                )
                return self.providers[fallback]

        raise RuntimeError("No LLM providers available. Configure at least one API key.")

    # -- Skill discovery ------------------------------------------------------

    def _discover_skills(self) -> None:
        """Scan configured directories for SKILL.md and Python agent files."""
        skill_paths = self.config.get("skill_paths", ["Skills"])

        for base_path in skill_paths:
            if not Path(base_path).exists():
                continue
            self._scan_skill_md(base_path)
            self._scan_python_agents(base_path)

    def _scan_skill_md(self, base_dir: str) -> None:
        """Discover SKILL.md files and register them."""
        for skill_path in Path(base_dir).rglob("SKILL.md"):
            try:
                content = skill_path.read_text(encoding="utf-8")
                metadata = self._parse_skill_md(content, str(skill_path))
                if metadata:
                    self.router.register_skill(metadata)
            except Exception as exc:
                self.logger.warning(
                    "Failed to parse SKILL.md",
                    path=str(skill_path),
                    error=str(exc),
                )

    def _scan_python_agents(self, base_dir: str) -> None:
        """Discover Python agent files and register them."""
        for agent_path in Path(base_dir).rglob("*_agent.py"):
            rel = agent_path.relative_to(base_dir)
            skill_id = str(rel).replace("/", "_").replace(".py", "").lower()
            skill_id = re.sub(r"[^a-z0-9_-]", "-", skill_id)

            metadata = SkillMetadata(
                skill_id=skill_id,
                name=skill_id.replace("_", " ").replace("-", " ").title(),
                description=f"Python agent: {agent_path.stem}",
                skill_type=SkillType.PYTHON_AGENT,
                file_path=str(agent_path),
                tags=["python", "agent"],
            )
            self.router.register_skill(metadata)

    @staticmethod
    def _parse_skill_md(content: str, file_path: str) -> Optional[SkillMetadata]:
        """Parse a SKILL.md file into SkillMetadata."""
        if not content.startswith("---"):
            return None

        parts = content.split("---", 2)
        if len(parts) < 3:
            return None

        frontmatter_raw = parts[1]
        body = parts[2].strip()

        # Parse YAML frontmatter
        try:
            frontmatter = yaml.safe_load(frontmatter_raw)
        except yaml.YAMLError:
            frontmatter = {}

        if not isinstance(frontmatter, dict):
            return None

        name = frontmatter.get("name", "")
        if not name:
            return None

        description = frontmatter.get("description", "No description")
        if isinstance(description, str):
            desc_text = description
        else:
            desc_text = str(description)

        # Extract tags from frontmatter or body
        tags = frontmatter.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]

        # Extract capabilities from body headings
        capabilities = re.findall(r"^#+\s+(.+)$", body, re.MULTILINE)

        return SkillMetadata(
            skill_id=name,
            name=name.replace("-", " ").title(),
            description=desc_text,
            skill_type=SkillType.SKILL_MD,
            file_path=file_path,
            tags=tags,
            capabilities=capabilities,
            instructions_body=body,
            version=frontmatter.get("version", "1.0.0"),
            author=frontmatter.get("author", None),
        )

    # -- Execution ------------------------------------------------------------

    async def execute(self, request: AgentRequest) -> AgentResponse:
        """
        Execute a user request through the BioKernel pipeline.

        1. Route to best skill
        2. Build context-aware prompt
        3. Execute via selected LLM provider
        4. Return structured response
        """
        start = time.perf_counter()
        steps: List[AgentStep] = []

        # Step 1: Route
        skill_id = self.router.get_best_match(request.query, request.skill_id)
        skill_meta = self.router.skills.get(skill_id or "")

        steps.append(AgentStep(
            step_number=1,
            action="routing",
            content=f"Routed to skill: {skill_id or 'general-assistant'}",
        ))

        # Step 2: Build prompt
        system_prompt = self._build_system_prompt(skill_meta)
        user_query = request.query

        # Step 3: Execute
        provider = self.get_provider(request.provider_preference)
        llm_request = LLMRequest(
            query=user_query,
            system_instruction=system_prompt,
            temperature=0.3,
            max_tokens=4096,
        )

        llm_response = await provider.generate(llm_request)

        steps.append(AgentStep(
            step_number=2,
            action="generation",
            content=f"Generated response via {provider.provider_name}",
            latency_ms=llm_response.latency_ms,
        ))

        # Safety check
        safety_flags = self._check_safety(llm_response.text)

        total_ms = (time.perf_counter() - start) * 1000

        return AgentResponse(
            response=llm_response.text,
            skill_used=skill_id or "general-assistant",
            provider_used=provider.provider_name,
            model_used=llm_response.model,
            steps=steps,
            tools_used=[],
            execution_time_ms=total_ms,
            token_usage=llm_response.usage,
            session_id=request.session_id,
            safety_flags=safety_flags,
        )

    async def execute_workflow(
        self,
        workflow: WorkflowDefinition,
    ) -> WorkflowDefinition:
        """
        Execute a multi-step workflow through the DAG engine.

        Each step is executed as a separate skill invocation, with results
        from upstream steps available as context.
        """
        async def step_executor(
            step: WorkflowStep, upstream: Dict[str, str]
        ) -> str:
            context_text = "\n".join(
                f"[{k}]: {v}" for k, v in upstream.items() if v
            )
            query = step.parameters.get("query", f"Execute skill: {step.skill_id}")
            if context_text:
                query = f"Context from previous steps:\n{context_text}\n\nTask: {query}"

            request = AgentRequest(
                query=query,
                skill_id=step.skill_id,
                context=step.parameters,
            )
            response = await self.execute(request)
            return response.response

        return await self.workflow_engine.execute(workflow, step_executor)

    def _build_system_prompt(self, skill_meta: Optional[SkillMetadata]) -> str:
        """Build a context-aware system prompt from skill metadata."""
        base = (
            "You are BioKernel, an expert biomedical AI assistant developed at "
            "the Icahn School of Medicine at Mount Sinai. You provide scientifically "
            "accurate, clinically safe, and evidence-based responses.\n\n"
            "SAFETY: Always include appropriate disclaimers for clinical content. "
            "Never provide definitive diagnoses. Recommend professional consultation "
            "for clinical decisions.\n"
        )

        if not skill_meta:
            return base

        prompt = base + f"\n## Active Skill: {skill_meta.name}\n"
        prompt += f"{skill_meta.description}\n"

        if skill_meta.instructions_body:
            prompt += f"\n## Detailed Instructions\n{skill_meta.instructions_body}\n"

        if skill_meta.safety_checks:
            prompt += "\n## Safety Requirements\n"
            for check in skill_meta.safety_checks:
                prompt += f"- {check}\n"

        return prompt

    @staticmethod
    def _check_safety(text: str) -> List[str]:
        """Run basic safety checks on generated output."""
        flags = []
        text_lower = text.lower()

        # Check for potentially dangerous content
        danger_terms = [
            "synthesize", "manufacture", "produce at home",
            "without prescription", "self-medicate",
        ]
        for term in danger_terms:
            if term in text_lower:
                flags.append(f"safety:potential_risk:{term}")

        # Check for missing disclaimers on clinical content
        clinical_terms = ["diagnosis", "treatment", "prescribe", "medication", "dosage"]
        has_clinical = any(t in text_lower for t in clinical_terms)
        disclaimer_terms = ["consult", "healthcare", "physician", "professional", "medical advice"]
        has_disclaimer = any(t in text_lower for t in disclaimer_terms)

        if has_clinical and not has_disclaimer:
            flags.append("safety:missing_clinical_disclaimer")

        return flags

    # -- Introspection --------------------------------------------------------

    def list_skills(self) -> List[Dict[str, Any]]:
        """Return all registered skills as serializable dicts."""
        return [
            {
                "skill_id": s.skill_id,
                "name": s.name,
                "description": s.description,
                "type": s.skill_type.value,
                "category": s.category,
                "tags": s.tags,
            }
            for s in self.router.skills.values()
        ]

    def list_providers(self) -> Dict[str, bool]:
        """Return available providers."""
        return {name: p.is_available for name, p in self.providers.items()}


# ---------------------------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------------------------

kernel: Optional[BioKernel] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize BioKernel on startup."""
    global kernel
    kernel = BioKernel()
    yield
    kernel = None


app = FastAPI(
    title="BioKernel",
    description=(
        "Autonomous Biomedical AI Skills Platform — "
        "Universal Skill Description Language (USDL) runtime"
    ),
    version="2026.4.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _get_kernel() -> BioKernel:
    if kernel is None:
        raise HTTPException(status_code=503, detail="BioKernel not initialized")
    return kernel


# -- API Endpoints -----------------------------------------------------------

@app.get("/")
async def health_check():
    """Health check endpoint."""
    k = _get_kernel()
    return {
        "status": "active",
        "system": "BioKernel",
        "version": "2026.4.0",
        "skills_registered": len(k.router.skills),
        "providers": k.list_providers(),
    }


@app.post("/v1/agent/run", response_model=AgentResponse)
async def run_agent(request: AgentRequest):
    """Execute a query through the BioKernel."""
    k = _get_kernel()
    return await k.execute(request)


@app.post("/v1/workflow/run")
async def run_workflow(workflow: WorkflowDefinition):
    """Execute a multi-step workflow."""
    k = _get_kernel()
    result = await k.execute_workflow(workflow)
    return {
        "workflow_id": result.workflow_id,
        "name": result.name,
        "status": result.status.value,
        "total_latency_ms": result.total_latency_ms,
        "steps": [
            {
                "step_id": s.step_id,
                "skill_id": s.skill_id,
                "status": s.status.value,
                "result": s.result[:500] if s.result else None,
                "error": s.error,
                "latency_ms": s.latency_ms,
            }
            for s in result.steps
        ],
    }


@app.get("/v1/skills")
async def list_skills():
    """List all registered skills."""
    k = _get_kernel()
    return {"skills": k.list_skills(), "total": len(k.router.skills)}


@app.get("/v1/providers")
async def list_providers():
    """List available LLM providers."""
    k = _get_kernel()
    return {"providers": k.list_providers()}


@app.post("/v1/route")
async def route_query(request: AgentRequest):
    """Route a query to skills without executing (preview mode)."""
    k = _get_kernel()
    matches = k.router.route(request.query, top_k=5)
    return {
        "query": request.query,
        "matches": [
            {
                "skill_id": sid,
                "score": round(score, 4),
                "name": k.router.skills[sid].name,
                "description": k.router.skills[sid].description,
            }
            for sid, score in matches
        ],
    }


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
