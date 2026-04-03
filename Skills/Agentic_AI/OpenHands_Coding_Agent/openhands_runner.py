#!/usr/bin/env python3
"""Helper to launch OpenHands headless missions from BioKernel swarms."""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, Optional


def _parse_key_values(pairs: Iterable[str]) -> Dict[str, str]:
    parsed: Dict[str, str] = {}
    for pair in pairs:
        if "=" not in pair:
            raise argparse.ArgumentTypeError(f"Invalid KEY=VALUE assignment: '{pair}'")
        key, value = pair.split("=", 1)
        parsed[key] = value
    return parsed


def _stream_process(cmd, cwd: Path, env: Dict[str, str], output_path: Optional[Path]):
    tee_handle = None
    try:
        if output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            tee_handle = output_path.open("w", encoding="utf-8")
        with subprocess.Popen(
            cmd,
            cwd=cwd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        ) as proc:
            assert proc.stdout
            for line in proc.stdout:
                print(line, end="")
                if tee_handle:
                    tee_handle.write(line)
            return_code = proc.wait()
            if return_code != 0:
                raise subprocess.CalledProcessError(return_code, cmd)
    finally:
        if tee_handle:
            tee_handle.flush()
            tee_handle.close()


def main():
    parser = argparse.ArgumentParser(description="Run OpenHands headless missions.")
    parser.add_argument("--mission", help="Task description passed to OpenHands (-t).")
    parser.add_argument("--task-file", help="Path passed to OpenHands via -f/--file.")
    parser.add_argument(
        "--json-out",
        help="Optional JSONL capture file. When set we enable --json and tee stdout to this path.",
    )
    parser.add_argument(
        "--json-stream",
        action="store_true",
        help="Add --json so OpenHands emits JSONL to stdout (requires headless).",
    )
    parser.add_argument(
        "--no-headless",
        action="store_true",
        help="Skip --headless flag (defaults to headless mode).",
    )
    parser.add_argument(
        "--workdir",
        default=".",
        help="Directory to run OpenHands from (defaults to current working directory).",
    )
    parser.add_argument(
        "--env",
        nargs="*",
        default=[],
        metavar="KEY=VALUE",
        help="Environment variables forwarded to the OpenHands process.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the command and exit without running OpenHands.",
    )
    args = parser.parse_args()

    if not args.mission and not args.task_file:
        parser.error("Provide --mission or --task-file so OpenHands has a starting brief.")

    cli_path = shutil.which("openhands")
    if not cli_path:
        parser.error(
            "OpenHands CLI not found on PATH. Install it via 'uv tool install openhands --python 3.12' or pip."
        )

    cmd = [cli_path]
    if not args.no_headless:
        cmd.append("--headless")
    if args.mission:
        cmd += ["-t", args.mission]
    if args.task_file:
        cmd += ["-f", args.task_file]
    if args.json_stream or args.json_out:
        cmd.append("--json")

    workdir = Path(args.workdir).expanduser().resolve()
    if not workdir.exists():
        parser.error(f"Workdir does not exist: {workdir}")

    env = os.environ.copy()
    env.update(_parse_key_values(args.env))

    if args.dry_run:
        printable = " ".join(cmd)
        print(f"[OpenHandsRunner] Dry run: {printable}\nWorking dir: {workdir}")
        return

    try:
        _stream_process(cmd, workdir, env, Path(args.json_out).expanduser() if args.json_out else None)
    except subprocess.CalledProcessError as exc:
        sys.exit(exc.returncode)


if __name__ == "__main__":
    main()
