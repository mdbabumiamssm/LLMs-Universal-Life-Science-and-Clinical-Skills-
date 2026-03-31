# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
BioKernel MCP (Model Context Protocol) Server.

Exposes BioKernel skills as MCP tools, allowing any MCP-compatible client
(Claude Desktop, Claude Code, Cursor, etc.) to discover and invoke
biomedical AI skills seamlessly.

Protocol: JSON-RPC 2.0 over stdio (MCP spec 2024-11-05).

Tools exposed:
- ``run_bio_agent``: Execute any registered biomedical skill
- ``list_skills``: Discover available skills with descriptions
- ``run_workflow``: Execute a multi-step DAG workflow
- ``route_query``: Preview skill routing without execution
"""

from __future__ import annotations

import asyncio
import json
import logging
import sys
from typing import Any, Dict, Optional

from biokernel.biokernel.server import BioKernel, load_config
from biokernel.schema.io_types import AgentRequest, WorkflowDefinition

# Logging to stderr to avoid corrupting JSON-RPC stdout
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr,
    format="[MCP:BioKernel] %(levelname)s %(message)s",
)
logger = logging.getLogger("mcp_server")


# ---------------------------------------------------------------------------
# MCP Tool Definitions
# ---------------------------------------------------------------------------

MCP_TOOLS = [
    {
        "name": "run_bio_agent",
        "description": (
            "Execute a biomedical AI skill. Supports 59+ domains including "
            "genomics, clinical decision support, drug discovery, single-cell "
            "analysis, and more. If skill_id is omitted, the system routes "
            "automatically based on query content."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Natural language request for the biomedical agent.",
                },
                "skill_id": {
                    "type": "string",
                    "description": "Optional: specific skill ID to invoke (e.g., 'bioinformatics-singlecell').",
                },
                "provider": {
                    "type": "string",
                    "enum": ["anthropic", "openai", "gemini", "local"],
                    "description": "Optional: preferred LLM provider.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "list_skills",
        "description": "List all available biomedical skills with their descriptions and categories.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Optional: filter by category (e.g., 'genomics', 'clinical').",
                },
            },
        },
    },
    {
        "name": "route_query",
        "description": (
            "Preview which skills would match a query without executing. "
            "Returns ranked matches with similarity scores."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to route.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "run_workflow",
        "description": (
            "Execute a multi-step biomedical workflow (e.g., "
            "literature mining → molecule design → safety review). "
            "Steps run as a DAG with automatic parallelization."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Workflow name.",
                },
                "steps": {
                    "type": "array",
                    "description": "Array of workflow steps.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "step_id": {"type": "string"},
                            "skill_id": {"type": "string"},
                            "depends_on": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "query": {"type": "string"},
                        },
                        "required": ["step_id", "skill_id"],
                    },
                },
            },
            "required": ["name", "steps"],
        },
    },
]


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

class MCPServer:
    """
    JSON-RPC 2.0 server implementing the Model Context Protocol.

    Communicates over stdio (stdin/stdout) and delegates biomedical
    queries to the BioKernel.
    """

    def __init__(self) -> None:
        self.kernel = BioKernel(config=load_config())
        self.name = "biokernel-mcp"
        self.version = "2026.4.0"

    async def handle_message(self, message: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Dispatch a JSON-RPC message to the appropriate handler."""
        method = message.get("method", "")
        msg_id = message.get("id")
        params = message.get("params", {})

        handlers = {
            "initialize": self._handle_initialize,
            "notifications/initialized": self._handle_notification,
            "tools/list": self._handle_tools_list,
            "tools/call": self._handle_tools_call,
            "prompts/list": self._handle_prompts_list,
            "prompts/get": self._handle_prompts_get,
        }

        handler = handlers.get(method)
        if handler is None:
            if msg_id is not None:
                return self._error(msg_id, -32601, f"Method not found: {method}")
            return None

        try:
            result = await handler(params)
            if msg_id is None:
                return None  # Notification, no response needed
            return {"jsonrpc": "2.0", "id": msg_id, "result": result}
        except Exception as exc:
            logger.error("Handler error: %s", exc)
            if msg_id is not None:
                return self._error(msg_id, -32000, str(exc))
            return None

    # -- Protocol handlers ---------------------------------------------------

    async def _handle_initialize(self, params: Dict) -> Dict:
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}, "prompts": {}},
            "serverInfo": {"name": self.name, "version": self.version},
        }

    async def _handle_notification(self, params: Dict) -> None:
        logger.info("Client initialized successfully")

    async def _handle_tools_list(self, params: Dict) -> Dict:
        return {"tools": MCP_TOOLS}

    async def _handle_tools_call(self, params: Dict) -> Dict:
        name = params.get("name", "")
        args = params.get("arguments", {})

        if name == "run_bio_agent":
            return await self._tool_run_agent(args)
        elif name == "list_skills":
            return await self._tool_list_skills(args)
        elif name == "route_query":
            return await self._tool_route_query(args)
        elif name == "run_workflow":
            return await self._tool_run_workflow(args)
        else:
            raise ValueError(f"Unknown tool: {name}")

    async def _handle_prompts_list(self, params: Dict) -> Dict:
        prompts = []
        for skill in self.kernel.router.skills.values():
            if skill.skill_type.value == "skill_md":
                prompts.append({
                    "name": skill.skill_id,
                    "description": skill.description,
                    "arguments": [],
                })
        return {"prompts": prompts}

    async def _handle_prompts_get(self, params: Dict) -> Dict:
        name = params.get("name", "")
        skill = self.kernel.router.skills.get(name)
        if not skill:
            raise ValueError(f"Prompt/skill not found: {name}")
        return {
            "messages": [
                {
                    "role": "user",
                    "content": {"type": "text", "text": skill.instructions_body},
                }
            ]
        }

    # -- Tool implementations ------------------------------------------------

    async def _tool_run_agent(self, args: Dict) -> Dict:
        request = AgentRequest(
            query=args["query"],
            skill_id=args.get("skill_id"),
        )
        if args.get("provider"):
            request.provider_preference = ProviderName(args["provider"])

        result = await self.kernel.execute(request)
        return {
            "content": [
                {"type": "text", "text": result.response},
            ],
            "metadata": {
                "skill_used": result.skill_used,
                "provider": result.provider_used,
                "model": result.model_used,
                "execution_time_ms": result.execution_time_ms,
                "safety_flags": result.safety_flags,
            },
        }

    async def _tool_list_skills(self, args: Dict) -> Dict:
        skills = self.kernel.list_skills()
        category = args.get("category", "").lower()
        if category:
            skills = [
                s for s in skills
                if category in (s.get("category") or "").lower()
                or category in " ".join(s.get("tags", [])).lower()
            ]
        formatted = "\n".join(
            f"- **{s['skill_id']}**: {s['description']}" for s in skills
        )
        return {
            "content": [
                {"type": "text", "text": f"## Available Skills ({len(skills)})\n\n{formatted}"},
            ]
        }

    async def _tool_route_query(self, args: Dict) -> Dict:
        matches = self.kernel.router.route(args["query"], top_k=5)
        if not matches:
            return {
                "content": [{"type": "text", "text": "No matching skills found."}]
            }
        lines = []
        for sid, score in matches:
            skill = self.kernel.router.skills[sid]
            lines.append(f"- **{sid}** (score: {score:.3f}): {skill.description}")
        return {
            "content": [{"type": "text", "text": "\n".join(lines)}]
        }

    async def _tool_run_workflow(self, args: Dict) -> Dict:
        from biokernel.schema.io_types import WorkflowStep as WS

        steps = []
        for s in args["steps"]:
            steps.append(WS(
                step_id=s["step_id"],
                skill_id=s["skill_id"],
                depends_on=s.get("depends_on", []),
                parameters={"query": s.get("query", f"Execute {s['skill_id']}")},
            ))

        workflow = WorkflowDefinition(
            name=args["name"],
            steps=steps,
        )

        result = await self.kernel.execute_workflow(workflow)

        summary_lines = [f"## Workflow: {result.name}", f"Status: {result.status.value}\n"]
        for step in result.steps:
            status_icon = "✓" if step.status.value == "completed" else "✗"
            summary_lines.append(
                f"{status_icon} **{step.step_id}** ({step.skill_id}): "
                f"{step.result[:200] if step.result else step.error or 'No output'}"
            )
        summary_lines.append(f"\nTotal time: {result.total_latency_ms:.0f}ms")

        return {
            "content": [{"type": "text", "text": "\n".join(summary_lines)}]
        }

    # -- Helpers -------------------------------------------------------------

    @staticmethod
    def _error(msg_id: Any, code: int, message: str) -> Dict:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": code, "message": message},
        }

    # -- Main loop -----------------------------------------------------------

    async def run(self) -> None:
        """Run the MCP server on stdio."""
        reader = asyncio.StreamReader()
        protocol = asyncio.StreamReaderProtocol(reader)
        await asyncio.get_running_loop().connect_read_pipe(lambda: protocol, sys.stdin)
        w_transport, _ = await asyncio.get_running_loop().connect_write_pipe(
            asyncio.BaseProtocol, sys.stdout
        )

        logger.info("BioKernel MCP Server running on stdio...")
        logger.info("Skills loaded: %d", len(self.kernel.router.skills))

        while True:
            try:
                line = await reader.readline()
                if not line:
                    break

                msg = json.loads(line)
                response = await self.handle_message(msg)

                if response:
                    output = json.dumps(response) + "\n"
                    sys.stdout.write(output)
                    sys.stdout.flush()

            except json.JSONDecodeError as exc:
                logger.error("Invalid JSON: %s", exc)
            except Exception as exc:
                logger.error("Server error: %s", exc)


# Need this import for the tool handler
from biokernel.schema.io_types import ProviderName


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    server = MCPServer()
    try:
        asyncio.run(server.run())
    except KeyboardInterrupt:
        logger.info("MCP server shutting down")
