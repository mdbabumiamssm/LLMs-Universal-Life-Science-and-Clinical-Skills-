---
name: 'agentscope-runtime'
description: 'Deploy AgentScope + AgentScope Runtime for secure sandboxed multi-agent services inside BioKernel.'
keywords:
  - agentscope
  - runtime
  - sandbox
  - fastapi
  - deployment
metadata:
  upstream_repo: https://github.com/agentscope-ai/agentscope-runtime
  version: '2026-04-02'
allowed-tools:
  - python3
  - run_shell_command
  - read_file
---

# AgentScope Runtime Skill

AgentScope is a production-ready multi-agent framework with ReAct agents, memory, human-in-the-loop steering, MCP/A2A integrations, and voice support, while AgentScope Runtime adds hardened sandboxes, Agent-as-a-Service APIs, and FastAPI-native deployment adapters.¹ ² Use this skill when you want BioKernel missions to tap into AgentScope’s ecosystem or when you must expose an agent over HTTP with observability and sandbox isolation baked in.

## When to Use

* You need asynchronous sandboxes (GUI, browser, filesystem, mobile) with isolation guarantees before executing untrusted tool calls.²
* You want to host an AgentScope ReAct or planning workflow behind a FastAPI endpoint and call it from other agents.
* You must integrate with MCP/A2A compatible tools or run K8s/Function Compute deployments without rewriting orchestration.

## Setup

1. Install both framework + runtime (Python 3.10+):
   ```bash
   uv pip install "agentscope>=0.10" "agentscope-runtime>=1.1"
   # or pip install agentscope agentscope-runtime
   ```
2. Export provider keys (DashScope, OpenAI, Gemini, etc.) plus sandbox registry settings if you want non-default Docker images:
   ```bash
   export DASHSCOPE_API_KEY=sk-...
   export RUNTIME_SANDBOX_REGISTRY="agentscope-registry.ap-southeast-1.cr.aliyuncs.com"
   ```

## Workflow (Agent-as-a-Service)

1. Create `agent_app.py` based on the runtime quickstart:
   ```python
   import os
   from contextlib import asynccontextmanager
   from agentscope.agent import ReActAgent
   from agentscope.model import DashScopeChatModel
   from agentscope.tool import Toolkit, execute_python_code
   from agentscope_runtime.engine import AgentApp
   from agentscope_runtime.sandbox import BaseSandboxAsync

   @asynccontextmanager
   async def lifespan(app):
       async with BaseSandboxAsync() as box:
           app.state.sandbox = box
           yield

   agent_app = AgentApp(app_name="Friday", lifespan=lifespan)

   @agent_app.query(framework="agentscope")
   async def query(messages, **kwargs):
       toolkit = Toolkit()
       toolkit.register_tool_function(execute_python_code)
       agent = ReActAgent(
           name="Friday",
           sys_prompt="Reason carefully about biomedical code changes.",
           model=DashScopeChatModel("qwen-max", api_key=os.environ["DASHSCOPE_API_KEY"], stream=True),
           toolkit=toolkit,
       )
       async for msg, last in agent.stream_chat(messages):
           yield msg, last

   if __name__ == "__main__":
       agent_app.run(port=8090)
   ```
2. Launch the service:
   ```bash
   python agent_app.py
   # or use the helper runner (handles env injection + cwd)
   python Skills/Agentic_AI/AgentScope_Runtime/agentscope_runner.py \
     agent_app.py --workdir Skills/Agentic_AI/AgentScope_Runtime/examples \
     --env DASHSCOPE_API_KEY=sk-...
   ```
   Runtime exposes `POST /process` with SSE streaming just like the README example.
3. From BioKernel, call the endpoint via `platform/adapters/runtime_adapter.py` and treat it like any other remote agent. Attach mission metadata so Reviewer/SafetyOfficer agents can audit the AgentScope trace.

## Sandbox-First Tooling

* Switch between synchronous/asynchronous sandboxes depending on mission latency requirements.
* Use `BrowserSandboxAsync` for GUI Operator-like actions, `FilesystemSandboxAsync` for editing patient files, and `MobileSandboxAsync` for validating digital therapeutics.
* Configure Docker/tag fields with `RUNTIME_SANDBOX_IMAGE_NAMESPACE`/`RUNTIME_SANDBOX_IMAGE_TAG` to pull gVisor, BoxLite, or custom hardened images before handing control to the runtime.

## Integration Notes

* Keep mission templates under `Skills/Agentic_AI/AgentScope_Runtime/examples/` so other contributors can spin up the same AgentApp quickly. Ship ready-made `agent_app.py` samples plus `.env.example` for provider keys.
* Use AgentScope’s `MsgHub` if you want to route sub-agents locally inside the runtime and only send summarized responses back to the swarm.
* Stream the SSE trace plus sandbox logs into `platform/compliance/agent_logs/` for after-action audits.

## References

1. GitHub – agentscope-ai/agentscope (`README` details ReAct agents, MCP/A2A, memory, realtime voice, roadmap). <https://github.com/agentscope-ai/agentscope>
2. GitHub – agentscope-ai/agentscope-runtime (`README` covers AgentApp, asynchronous sandboxes, deployment, and async tool execution). <https://github.com/agentscope-ai/agentscope-runtime>
