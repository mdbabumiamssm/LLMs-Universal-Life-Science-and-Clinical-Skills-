#!/usr/bin/env python3
# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
BioKernel CLI — Interactive command-line interface for the biomedical skills platform.

Supports both autonomous execution and manual interactive mode,
with rich terminal output for a publication-quality user experience.

Usage::

    biokernel serve                      # Start API server
    biokernel run "analyze BRCA1 variants"  # Execute a query
    biokernel skills                     # List all skills
    biokernel eval tests/eval.yaml       # Run evaluation suite
    biokernel interactive                # Interactive chat mode
    biokernel mcp                        # Start MCP server
"""

from __future__ import annotations

import asyncio
import sys
import os

# Ensure platform package is importable
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

try:
    import click
    HAS_CLICK = True
except ImportError:
    HAS_CLICK = False

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.live import Live
    HAS_RICH = True
except ImportError:
    HAS_RICH = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _console():
    if HAS_RICH:
        return Console(stderr=True)
    return None


def _print(msg: str, style: str = ""):
    c = _console()
    if c:
        c.print(msg, style=style)
    else:
        print(msg)


def _get_kernel():
    from platform.biokernel.server import BioKernel
    return BioKernel()


# ---------------------------------------------------------------------------
# CLI (click-based if available, argparse fallback)
# ---------------------------------------------------------------------------

if HAS_CLICK:

    @click.group()
    @click.version_option("2026.4.0", prog_name="biokernel")
    def cli():
        """BioKernel — Autonomous Biomedical AI Skills Platform."""
        pass

    @cli.command()
    @click.option("--port", default=8000, help="Server port")
    @click.option("--host", default="0.0.0.0", help="Server host")
    @click.option("--reload", is_flag=True, help="Enable auto-reload")
    def serve(port, host, reload):
        """Start the BioKernel API server."""
        import uvicorn
        _print(f"Starting BioKernel on {host}:{port}...", "bold green")
        uvicorn.run(
            "platform.biokernel.server:app",
            host=host,
            port=port,
            reload=reload,
        )

    @cli.command()
    @click.argument("query")
    @click.option("--provider", "-p", default="anthropic",
                  type=click.Choice(["anthropic", "openai", "gemini", "local"]))
    @click.option("--skill", "-s", default=None, help="Force specific skill ID")
    def run(query, provider, skill):
        """Execute a query through the BioKernel."""
        kernel = _get_kernel()

        from platform.schema.io_types import AgentRequest, ProviderName
        request = AgentRequest(
            query=query,
            provider_preference=ProviderName(provider),
            skill_id=skill,
        )

        result = asyncio.run(kernel.execute(request))

        if HAS_RICH:
            console = Console()
            console.print(Panel(
                Markdown(result.response),
                title=f"[bold]{result.skill_used}[/bold]",
                subtitle=f"{result.provider_used}/{result.model_used} | {result.execution_time_ms:.0f}ms",
                border_style="blue",
            ))
            if result.safety_flags:
                console.print(f"[yellow]Safety flags: {', '.join(result.safety_flags)}[/yellow]")
        else:
            print(f"\n{'='*60}")
            print(f"Skill: {result.skill_used}")
            print(f"Provider: {result.provider_used}/{result.model_used}")
            print(f"Time: {result.execution_time_ms:.0f}ms")
            print(f"{'='*60}")
            print(result.response)

    @cli.command()
    @click.option("--category", "-c", default=None, help="Filter by category")
    def skills(category):
        """List all registered skills."""
        kernel = _get_kernel()
        all_skills = kernel.list_skills()

        if category:
            all_skills = [
                s for s in all_skills
                if category.lower() in (s.get("category") or "").lower()
                or category.lower() in " ".join(s.get("tags", [])).lower()
            ]

        if HAS_RICH:
            console = Console()
            table = Table(title=f"BioKernel Skills ({len(all_skills)} registered)")
            table.add_column("ID", style="cyan", no_wrap=True)
            table.add_column("Type", style="magenta")
            table.add_column("Description", max_width=60)
            table.add_column("Tags")

            for s in sorted(all_skills, key=lambda x: x["skill_id"]):
                table.add_row(
                    s["skill_id"],
                    s["type"],
                    s["description"][:60],
                    ", ".join(s.get("tags", [])[:3]),
                )
            console.print(table)
        else:
            print(f"\nRegistered Skills ({len(all_skills)}):")
            for s in sorted(all_skills, key=lambda x: x["skill_id"]):
                print(f"  {s['skill_id']:40s} [{s['type']}] {s['description'][:50]}")

    @cli.command()
    @click.argument("eval_file")
    @click.option("--platform", "-p", default="all")
    @click.option("--html", is_flag=True, help="Generate HTML report")
    def eval(eval_file, platform, html):
        """Run evaluation suite on a skill."""
        from platform.evaluator.eval_engine import EvaluationEngine

        engine = EvaluationEngine()

        if platform == "all":
            reports = engine.compare_platforms(eval_file)
            _print("\n=== Cross-Platform Comparison ===\n", "bold")
            for plat, report in reports.items():
                status = "[green]PASS[/green]" if report.overall_score >= 0.8 else "[red]FAIL[/red]"
                _print(f"  {plat.upper()}: {report.overall_score:.0%} {status}")
                if html:
                    path = engine.generate_html_report(report, f"./reports/{plat}_report.html")
                    _print(f"    Report: {path}", "dim")
        else:
            report = engine.evaluate_skill(eval_file, platform)
            _print(f"\nScore: {report.overall_score:.0%} | Passed: {report.passed_cases}/{report.total_cases}", "bold")
            for rec in report.recommendations:
                _print(f"  - {rec}")

    @cli.command()
    @click.option("--provider", "-p", default="anthropic")
    def interactive(provider):
        """Start an interactive chat session with BioKernel."""
        kernel = _get_kernel()
        from platform.schema.io_types import AgentRequest, ProviderName

        _print("\nBioKernel Interactive Mode", "bold blue")
        _print("Type 'quit' to exit, 'skills' to list skills, 'help' for commands.\n")

        while True:
            try:
                query = input("You > ").strip()
            except (EOFError, KeyboardInterrupt):
                _print("\nGoodbye!", "bold")
                break

            if not query:
                continue
            if query.lower() in ("quit", "exit", "q"):
                _print("Goodbye!", "bold")
                break
            if query.lower() == "skills":
                for s in kernel.list_skills():
                    _print(f"  {s['skill_id']}: {s['description'][:60]}")
                continue
            if query.lower() == "help":
                _print("Commands: skills, providers, quit")
                continue
            if query.lower() == "providers":
                for name, avail in kernel.list_providers().items():
                    status = "available" if avail else "unavailable"
                    _print(f"  {name}: {status}")
                continue

            request = AgentRequest(
                query=query,
                provider_preference=ProviderName(provider),
            )
            result = asyncio.run(kernel.execute(request))

            if HAS_RICH:
                Console().print(Panel(
                    Markdown(result.response),
                    title=f"[bold]{result.skill_used}[/bold]",
                    subtitle=f"{result.execution_time_ms:.0f}ms",
                    border_style="green",
                ))
            else:
                print(f"\n[{result.skill_used}] ({result.execution_time_ms:.0f}ms)")
                print(result.response)
                print()

    @cli.command()
    def mcp():
        """Start the MCP (Model Context Protocol) server on stdio."""
        from platform.biokernel.mcp_server import MCPServer
        server = MCPServer()
        asyncio.run(server.run())

    @cli.command()
    @click.argument("text")
    @click.option("--target", "-t", required=True,
                  type=click.Choice(["claude", "openai", "gemini"]))
    @click.option("--output", "-o", default=None)
    def optimize(text, target, output):
        """Optimize a prompt for a specific LLM provider."""
        from platform.optimizer.meta_prompter import PromptOptimizer, ModelTarget

        optimizer = PromptOptimizer()
        result = optimizer.optimize(text, ModelTarget(target))

        if output:
            with open(output, "w") as f:
                f.write(result)
            _print(f"Saved to {output}")
        else:
            print(result)

    @cli.command()
    def catalog():
        """Scan and catalog all SKILL.md files."""
        from platform.skills_catalog import scan_skills, SKILLS_ROOT
        catalog_data, errors = scan_skills(str(SKILLS_ROOT))
        _print(f"\nSkills found: {len(catalog_data)}", "bold green")
        if errors:
            _print(f"Errors: {len(errors)}", "bold yellow")
            for err in errors[:10]:
                _print(f"  - {err}", "dim")

else:
    # Argparse fallback
    import argparse

    def cli():
        parser = argparse.ArgumentParser(prog="biokernel", description="BioKernel CLI")
        sub = parser.add_subparsers(dest="command")

        sub.add_parser("serve").add_argument("--port", default=8000, type=int)

        run_p = sub.add_parser("run")
        run_p.add_argument("query")
        run_p.add_argument("--provider", default="anthropic")

        sub.add_parser("skills")
        sub.add_parser("interactive")
        sub.add_parser("mcp")

        eval_p = sub.add_parser("eval")
        eval_p.add_argument("eval_file")
        eval_p.add_argument("--platform", default="all")

        args = parser.parse_args()

        if args.command == "serve":
            import uvicorn
            uvicorn.run("platform.biokernel.server:app", host="0.0.0.0", port=args.port)
        elif args.command == "run":
            kernel = _get_kernel()
            from platform.schema.io_types import AgentRequest, ProviderName
            req = AgentRequest(query=args.query, provider_preference=ProviderName(args.provider))
            result = asyncio.run(kernel.execute(req))
            print(result.response)
        elif args.command == "skills":
            kernel = _get_kernel()
            for s in kernel.list_skills():
                print(f"  {s['skill_id']:40s} {s['description'][:50]}")
        elif args.command == "mcp":
            from platform.biokernel.mcp_server import MCPServer
            asyncio.run(MCPServer().run())
        else:
            parser.print_help()


def main():
    """Entry point for the biokernel CLI."""
    cli()


if __name__ == "__main__":
    main()
