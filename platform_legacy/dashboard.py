#!/usr/bin/env python3
# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
BioKernel Interactive Dashboard — Rich terminal UI for skill orchestration.

Provides a command-line dashboard for:
- Browsing and searching registered skills
- Running queries interactively with provider selection
- Executing multi-step workflows with live progress
- Viewing system health and provider status

Uses ``rich`` for publication-quality terminal rendering.
"""

from __future__ import annotations

import asyncio
import sys
import os

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.prompt import Prompt, IntPrompt
    from rich.columns import Columns
    from rich.text import Text
    HAS_RICH = True
except ImportError:
    HAS_RICH = False


console = Console() if HAS_RICH else None


def _print(msg: str, style: str = ""):
    if console:
        console.print(msg, style=style)
    else:
        print(msg)


def _get_kernel():
    from platform.biokernel.server import BioKernel
    return BioKernel()


# ---------------------------------------------------------------------------
# Dashboard Screens
# ---------------------------------------------------------------------------

def show_banner():
    """Display the BioKernel banner."""
    banner = """
[bold blue]╔══════════════════════════════════════════════════════════╗
║           BioKernel Interactive Dashboard                ║
║       Autonomous Biomedical AI Skills Platform            ║
║                    v2026.4.0                             ║
╚══════════════════════════════════════════════════════════╝[/bold blue]
"""
    if console:
        console.print(banner)
    else:
        print("=" * 58)
        print("  BioKernel Interactive Dashboard v2026.4.0")
        print("=" * 58)


def show_status(kernel):
    """Display system status overview."""
    skills = kernel.list_skills()
    providers = kernel.list_providers()

    if console:
        # Provider status cards
        cards = []
        for name, available in providers.items():
            status = "[green]ONLINE[/green]" if available else "[red]OFFLINE[/red]"
            cards.append(Panel(
                f"{status}\n[dim]{name}[/dim]",
                title=f"[bold]{name.upper()}[/bold]",
                width=20,
                border_style="green" if available else "red",
            ))
        console.print(Columns(cards, equal=True, expand=True))
        console.print(f"\n[bold]{len(skills)}[/bold] skills registered across "
                      f"[bold]{sum(1 for v in providers.values() if v)}[/bold] active providers\n")
    else:
        print(f"\nProviders: {providers}")
        print(f"Skills: {len(skills)}\n")


def show_skills_table(kernel, search: str = ""):
    """Display skills in a formatted table."""
    skills = kernel.list_skills()
    if search:
        search_lower = search.lower()
        skills = [
            s for s in skills
            if search_lower in s["skill_id"].lower()
            or search_lower in s["description"].lower()
            or search_lower in " ".join(s.get("tags", [])).lower()
        ]

    if console:
        table = Table(
            title=f"Registered Skills ({len(skills)})",
            show_lines=False,
            header_style="bold cyan",
        )
        table.add_column("#", style="dim", width=4)
        table.add_column("Skill ID", style="cyan", no_wrap=True, max_width=35)
        table.add_column("Type", style="magenta", width=12)
        table.add_column("Description", max_width=45)

        for i, s in enumerate(sorted(skills, key=lambda x: x["skill_id"]), 1):
            table.add_row(
                str(i),
                s["skill_id"],
                s["type"],
                s["description"][:45],
            )
        console.print(table)
    else:
        for i, s in enumerate(sorted(skills, key=lambda x: x["skill_id"]), 1):
            print(f"  {i:3d}. {s['skill_id']:35s} [{s['type']}] {s['description'][:45]}")


async def run_query(kernel, query: str, provider: str = "anthropic"):
    """Execute a query and display results."""
    from platform.schema.io_types import AgentRequest, ProviderName

    request = AgentRequest(
        query=query,
        provider_preference=ProviderName(provider),
    )

    _print(f"\n[dim]Routing query...[/dim]")

    result = await kernel.execute(request)

    if console:
        console.print(Panel(
            Markdown(result.response),
            title=f"[bold green]{result.skill_used}[/bold green]",
            subtitle=(
                f"[dim]{result.provider_used}/{result.model_used} | "
                f"{result.execution_time_ms:.0f}ms | "
                f"{result.token_usage.get('total_tokens', 0)} tokens[/dim]"
            ),
            border_style="green",
            padding=(1, 2),
        ))
        if result.safety_flags:
            console.print(
                f"[yellow bold]Safety flags:[/yellow bold] "
                f"{', '.join(result.safety_flags)}"
            )
    else:
        print(f"\n--- {result.skill_used} ---")
        print(f"Provider: {result.provider_used}/{result.model_used}")
        print(f"Time: {result.execution_time_ms:.0f}ms")
        print(f"\n{result.response}\n")


async def run_workflow_demo(kernel):
    """Run a predefined drug discovery workflow."""
    from platform.schema.io_types import WorkflowDefinition, WorkflowStep

    _print("\n[bold]Drug Discovery Workflow[/bold]", "blue")
    _print("Pipeline: Literature Mining → Molecule Design → Safety Review\n")

    workflow = WorkflowDefinition(
        name="Drug Discovery Pipeline",
        description="End-to-end therapeutic target discovery",
        steps=[
            WorkflowStep(
                step_id="mine",
                skill_id="literature-mining",
                parameters={"query": "Find novel therapeutic targets for resistant AML"},
            ),
            WorkflowStep(
                step_id="design",
                skill_id="molecule-designer",
                depends_on=["mine"],
                parameters={"query": "Design candidate molecules for the identified target"},
            ),
            WorkflowStep(
                step_id="safety",
                skill_id="safety-review",
                depends_on=["design"],
                parameters={"query": "Evaluate safety profile of the candidate molecule"},
            ),
        ],
    )

    result = await kernel.execute_workflow(workflow)

    _print(f"\n[bold]Workflow Status: {result.status.value.upper()}[/bold]")
    _print(f"Total time: {result.total_latency_ms:.0f}ms\n")

    for step in result.steps:
        icon = "[green]OK[/green]" if step.status.value == "completed" else "[red]FAIL[/red]"
        _print(f"  {icon} {step.step_id} ({step.skill_id}): {step.latency_ms:.0f}ms")
        if step.result:
            _print(f"     {step.result[:100]}...")
        if step.error:
            _print(f"     [red]Error: {step.error}[/red]")


# ---------------------------------------------------------------------------
# Main Menu
# ---------------------------------------------------------------------------

async def main_menu():
    """Interactive dashboard main loop."""
    kernel = _get_kernel()

    show_banner()
    show_status(kernel)

    providers = kernel.list_providers()
    active_provider = next(
        (name for name, avail in providers.items() if avail),
        "anthropic"
    )

    while True:
        _print("\n[bold]Commands:[/bold]")
        _print("  [cyan]1[/cyan] - Query BioKernel (ask anything)")
        _print("  [cyan]2[/cyan] - Browse skills")
        _print("  [cyan]3[/cyan] - Search skills")
        _print("  [cyan]4[/cyan] - Run drug discovery workflow")
        _print("  [cyan]5[/cyan] - System status")
        _print("  [cyan]6[/cyan] - Switch provider (current: {})".format(active_provider))
        _print("  [cyan]q[/cyan] - Quit")

        try:
            choice = input("\nSelect > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if choice == "1":
            query = input("Query > ").strip()
            if query:
                await run_query(kernel, query, active_provider)

        elif choice == "2":
            show_skills_table(kernel)

        elif choice == "3":
            search = input("Search term > ").strip()
            show_skills_table(kernel, search)

        elif choice == "4":
            await run_workflow_demo(kernel)

        elif choice == "5":
            show_status(kernel)

        elif choice == "6":
            _print(f"Available: {', '.join(providers.keys())}")
            new_provider = input("Provider > ").strip().lower()
            if new_provider in providers:
                active_provider = new_provider
                _print(f"[green]Switched to {active_provider}[/green]")
            else:
                _print("[red]Invalid provider[/red]")

        elif choice in ("q", "quit", "exit"):
            _print("[bold]Goodbye![/bold]")
            break

    return 0


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        asyncio.run(main_menu())
    except KeyboardInterrupt:
        _print("\nExiting.")
