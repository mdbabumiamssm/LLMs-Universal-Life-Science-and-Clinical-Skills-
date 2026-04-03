#!/usr/bin/env python3
"""Launch an AgentScope Runtime AgentApp service from a mission spec."""
import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable


def _parse_pairs(pairs: Iterable[str]) -> Dict[str, str]:
    parsed: Dict[str, str] = {}
    for pair in pairs:
        if "=" not in pair:
            raise argparse.ArgumentTypeError(f"Invalid KEY=VALUE assignment: '{pair}'")
        key, value = pair.split("=", 1)
        parsed[key] = value
    return parsed


def main():
    parser = argparse.ArgumentParser(description="Run an AgentScope Runtime AgentApp.")
    parser.add_argument("app", help="Path to the agent_app.py (or entry module) to launch.")
    parser.add_argument("--port", type=int, default=8090, help="Port to run AgentApp on (default: 8090).")
    parser.add_argument(
        "--workdir",
        default=".",
        help="Directory containing the AgentScope project (default: current directory).",
    )
    parser.add_argument(
        "--env",
        nargs="*",
        default=[],
        metavar="KEY=VALUE",
        help="Environment variables passed to the AgentScope Runtime process.",
    )
    parser.add_argument(
        "--extra-args",
        nargs=argparse.REMAINDER,
        help="Additional arguments forwarded to the AgentApp script.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the command and exit without running AgentScope Runtime.",
    )
    args = parser.parse_args()

    workdir = Path(args.workdir).expanduser().resolve()
    if not workdir.exists():
        parser.error(f"Workdir does not exist: {workdir}")

    app_path = Path(args.app)
    if not app_path.is_absolute():
        app_path = (workdir / app_path).resolve()
    if not app_path.exists():
        parser.error(f"AgentApp file not found: {app_path}")

    cmd = [sys.executable, str(app_path), "--port", str(args.port)]
    if args.extra_args:
        cmd.extend(args.extra_args)

    env = os.environ.copy()
    env.update(_parse_pairs(args.env))

    if args.dry_run:
        print(f"[AgentScopeRunner] Dry run: {' '.join(cmd)}")
        print(f"Working dir: {workdir}")
        return

    subprocess.run(cmd, cwd=workdir, env=env, check=True)


if __name__ == "__main__":
    main()
