# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

"""Swarm orchestrator entrypoint for Agentic AI skills."""
from __future__ import annotations

import argparse
import asyncio
import os
import subprocess
import sys
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

AGENTIC_ROOT = Path(__file__).resolve().parents[1]
AUTOGEN_RUNTIME_SCRIPT = AGENTIC_ROOT / "AutoGen_Runtime" / "autogen_runtime.py"
RESPONSES_AGENTOPS_SCRIPT = AGENTIC_ROOT / "OpenAI_Responses_AgentOps" / "responses_agentops.py"
OPENHANDS_RUNNER = AGENTIC_ROOT / "OpenHands_Coding_Agent" / "openhands_runner.py"
AGENTSCOPE_RUNNER = AGENTIC_ROOT / "AgentScope_Runtime" / "agentscope_runner.py"

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class AgentMessage:
    sender: str
    recipient: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class Task:
    id: str
    description: str
    status: str = "pending"
    assigned_to: Optional[str] = None
    result: Optional[str] = None


# ---------------------------------------------------------------------------
# Local swarm agents
# ---------------------------------------------------------------------------


class BaseAgent:
    def __init__(self, name: str, role: str, capabilities: List[str]):
        self.name = name
        self.role = role
        self.capabilities = capabilities

    async def process(self, message: AgentMessage) -> AgentMessage:
        raise NotImplementedError


class ResearchAgent(BaseAgent):
    async def process(self, message: AgentMessage) -> AgentMessage:
        await asyncio.sleep(0.4)
        print(f"  [{self.name}] 🔍 Searching for: '{message.content}'")
        return AgentMessage(
            sender=self.name,
            recipient=message.sender,
            content=f"Top finding for '{message.content}': Protein X interacts with Drug Y via Mechanism Z.",
            metadata={"source": "PubMed_Mock", "confidence": 0.94},
        )


class ReviewAgent(BaseAgent):
    async def process(self, message: AgentMessage) -> AgentMessage:
        await asyncio.sleep(0.3)
        print(f"  [{self.name}] 🧐 Reviewing: '{message.content[:48]}...' ")
        verdict = "APPROVED" if "Mechanism Z" in message.content else "REJECTED"
        return AgentMessage(
            sender=self.name,
            recipient=message.sender,
            content=f"Verdict: {verdict}. Findings align with known pathways.",
            metadata={"verdict": verdict},
        )


class SafetyAgent(BaseAgent):
    async def process(self, message: AgentMessage) -> AgentMessage:
        await asyncio.sleep(0.2)
        print(f"  [{self.name}] 🛡️ Running compliance scan...")
        return AgentMessage(
            sender=self.name,
            recipient=message.sender,
            content="No PHI/biohazards detected.",
            metadata={"cleared": True},
        )


# ---------------------------------------------------------------------------
# Swarm brain
# ---------------------------------------------------------------------------


class SwarmOrchestrator:
    def __init__(self, name: str = "Overmind"):
        self.name = name
        self.agents: Dict[str, BaseAgent] = {}
        self.history: List[AgentMessage] = []

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.name] = agent
        print(f"[{self.name}] Registered {agent.name} ({agent.role})")

    async def _route_task(self, task: Task) -> List[str]:
        desc = task.description.lower()
        selected: List[str] = []
        if any(word in desc for word in ("search", "find", "investigate")):
            selected.append("Researcher")
        if any(word in desc for word in ("verify", "review", "check")):
            selected.append("Reviewer")
        if "safety" in desc or "compliance" in desc:
            selected.append("SafetyOfficer")
        if not selected:
            selected.append("Researcher")
        return selected

    async def run_mission(self, mission: str):
        print(f"\n=== 🚀 Starting Mission: {mission} ===")
        task = Task(id=str(uuid.uuid4())[:8], description=mission)
        agent_names = await self._route_task(task)
        print(f"[{self.name}] Assigned to: {', '.join(agent_names)}")
        coros = []
        for name in agent_names:
            agent = self.agents.get(name)
            if not agent:
                print(f"[{self.name}] ⚠️ Agent '{name}' not registered.")
                continue
            coros.append(agent.process(AgentMessage(sender=self.name, recipient=name, content=mission)))
        results = await asyncio.gather(*coros)
        print("\n=== 🏁 Mission Report ===")
        for res in results:
            print(f"From {res.sender}: {res.content}")
            self.history.append(res)
        return results


# ---------------------------------------------------------------------------
# Runtime delegation helpers
# ---------------------------------------------------------------------------


def _run_script(script: Path, script_args: List[str], env: Optional[Dict[str, str]] = None):
    if not script.exists():
        raise FileNotFoundError(f"Runtime script missing: {script}")
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    cmd = [sys.executable, str(script)] + script_args
    print(f"[SwarmOrchestrator] Delegating to {script.name}: {' '.join(cmd)}")
    subprocess.run(cmd, check=True, env=merged_env)


def _validate_pairs(pairs: List[str]) -> List[str]:
    for pair in pairs:
        if "=" not in pair:
            raise ValueError(f"Invalid KEY=VALUE assignment: '{pair}'")
    return pairs


def _delegate_to_autogen(args):
    script_args: List[str] = ["--mission", args.mission]
    if args.autogen_graph:
        script_args += ["--graph", args.autogen_graph]
    if args.autogen_background:
        script_args.append("--background")
    if args.autogen_dry_run:
        script_args.append("--dry-run")
    if args.autogen_env:
        script_args += ["--env", *_validate_pairs(args.autogen_env)]
    _run_script(AUTOGEN_RUNTIME_SCRIPT, script_args)


def _delegate_to_responses(args):
    script_args: List[str] = [
        args.mission,
        "--model",
        args.responses_model,
        "--effort",
        args.responses_effort,
        "--poll",
        str(args.responses_poll),
    ]
    if args.responses_vector_store:
        script_args += ["--vector-store", args.responses_vector_store]
    if args.responses_no_web:
        script_args.append("--no-web")
    if args.responses_operator:
        script_args.append("--operator")
    if args.responses_background:
        script_args.append("--background")
    _run_script(RESPONSES_AGENTOPS_SCRIPT, script_args)


def _delegate_to_openhands(args):
    script_args: List[str] = []
    if args.mission:
        script_args += ["--mission", args.mission]
    if args.openhands_task_file:
        script_args += ["--task-file", args.openhands_task_file]
    if args.openhands_json_out:
        script_args += ["--json-out", args.openhands_json_out]
    if args.openhands_json_stream:
        script_args.append("--json-stream")
    if args.openhands_no_headless:
        script_args.append("--no-headless")
    if args.openhands_workdir:
        script_args += ["--workdir", args.openhands_workdir]
    if args.openhands_env:
        script_args += ["--env", *_validate_pairs(args.openhands_env)]
    if args.openhands_dry_run:
        script_args.append("--dry-run")
    _run_script(OPENHANDS_RUNNER, script_args)


def _delegate_to_agentscope(args):
    script_args: List[str] = [args.agentscope_app]
    if args.agentscope_workdir:
        script_args += ["--workdir", args.agentscope_workdir]
    script_args += ["--port", str(args.agentscope_port)]
    if args.agentscope_env:
        script_args += ["--env", *_validate_pairs(args.agentscope_env)]
    if args.agentscope_dry_run:
        script_args.append("--dry-run")
    if args.agentscope_extra_args:
        script_args += ["--extra-args", *args.agentscope_extra_args]
    _run_script(AGENTSCOPE_RUNNER, script_args)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


async def main():
    swarm = SwarmOrchestrator()
    swarm.register_agent(ResearchAgent("Researcher", "Literature Search", ["search_pubmed", "read_paper"]))
    swarm.register_agent(ReviewAgent("Reviewer", "Quality Control", ["verify_facts", "critique"]))
    swarm.register_agent(SafetyAgent("SafetyOfficer", "Compliance", ["check_phi", "hazmat_check"]))

    parser = argparse.ArgumentParser(description="Run a swarm mission or delegate to external runtimes.")
    parser.add_argument("--mission", help="Objective for the swarm or delegated runtime.")
    parser.add_argument(
        "--runtime",
        choices=["swarm", "autogen", "openai", "openhands", "agentscope"],
        default="swarm",
        help="Choose between local swarm, Microsoft AutoGen, OpenAI Responses, OpenHands CLI, or AgentScope Runtime.",
    )

    # AutoGen options
    parser.add_argument("--autogen-graph", help="Path to AutoGen mission graph YAML.")
    parser.add_argument("--autogen-background", action="store_true", help="Add --background to AutoGen CLI.")
    parser.add_argument("--autogen-dry-run", action="store_true", help="Print AutoGen command without running.")
    parser.add_argument("--autogen-env", nargs="*", metavar="KEY=VALUE", default=[], help="Env vars for AutoGen CLI.")

    # OpenAI Responses options
    parser.add_argument("--responses-model", default="gpt-4.1", help="Responses model (default: gpt-4.1).")
    parser.add_argument(
        "--responses-effort",
        choices=["low", "medium", "high"],
        default="high",
        help="Reasoning effort parameter for Responses API.",
    )
    parser.add_argument("--responses-vector-store", help="Vector store ID for file_search tool.")
    parser.add_argument("--responses-no-web", action="store_true", help="Disable web_search tool.")
    parser.add_argument("--responses-operator", action="store_true", help="Enable Operator computer-use tool.")
    parser.add_argument("--responses-background", action="store_true", help="Request background execution.")
    parser.add_argument("--responses-poll", type=float, default=2.0, help="Polling interval for background runs.")

    # OpenHands options
    parser.add_argument("--openhands-task-file", help="Path passed to OpenHands --file.")
    parser.add_argument("--openhands-json-out", help="JSONL capture path for OpenHands runs.")
    parser.add_argument("--openhands-json-stream", action="store_true", help="Add --json flag to OpenHands CLI.")
    parser.add_argument("--openhands-no-headless", action="store_true", help="Skip --headless when delegating to OpenHands.")
    parser.add_argument("--openhands-workdir", help="Working directory for OpenHands mission.")
    parser.add_argument("--openhands-env", nargs="*", metavar="KEY=VALUE", default=[], help="Env vars for OpenHands CLI.")
    parser.add_argument("--openhands-dry-run", action="store_true", help="Print OpenHands command without running.")

    # AgentScope options
    parser.add_argument("--agentscope-app", help="Path to agent_app.py for AgentScope runtime.")
    parser.add_argument("--agentscope-port", type=int, default=8090, help="Port for AgentScope AgentApp.")
    parser.add_argument("--agentscope-workdir", help="Working directory for AgentScope project.")
    parser.add_argument("--agentscope-env", nargs="*", metavar="KEY=VALUE", default=[], help="Env vars for AgentScope runtime.")
    parser.add_argument(
        "--agentscope-extra-args",
        nargs=argparse.REMAINDER,
        help="Additional args forwarded to AgentApp script.",
    )
    parser.add_argument("--agentscope-dry-run", action="store_true", help="Print AgentScope command without running.")

    args = parser.parse_args()

    if args.runtime in {"autogen", "openai"} and not args.mission:
        parser.error("--mission is required when using autogen or openai runtimes.")
    if args.runtime == "openhands" and not (args.mission or args.openhands_task_file):
        parser.error("Provide --mission or --openhands-task-file for OpenHands delegation.")
    if args.runtime == "agentscope" and not args.agentscope_app:
        parser.error("--agentscope-app is required when using the AgentScope runtime.")

    try:
        if args.runtime == "autogen":
            _delegate_to_autogen(args)
            return
        if args.runtime == "openai":
            _delegate_to_responses(args)
            return
        if args.runtime == "openhands":
            _delegate_to_openhands(args)
            return
        if args.runtime == "agentscope":
            _delegate_to_agentscope(args)
            return
    except (ValueError, FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"[SwarmOrchestrator] Runtime delegation failed: {exc}")
        return

    if args.mission:
        await swarm.run_mission(args.mission)
    else:
        await swarm.run_mission("Investigate usage of Imatinib in GIST and review for side effects.")
        await swarm.run_mission("Perform safety compliance check on the lab dataset.")


if __name__ == "__main__":
    asyncio.run(main())

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
