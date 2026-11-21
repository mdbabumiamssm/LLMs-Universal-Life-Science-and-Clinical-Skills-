<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'open-science-research-workbench'
description: 'Configure Open-Science projects, model backends and research tools, run reproducible Python/R analyses, and export artifacts with traceable inputs and execution evidence.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Open Science Research Workbench

## Overview

Use Open-Science to organize a scientific question, input files, analysis code, and results in a local-first research project. Configure the available model backend, skills, connectors, and Python/R execution environment, then preserve enough evidence to inspect and repeat the analysis. Export artifacts through supported interfaces so results remain connected to their inputs and execution history.

## When to Use This Skill

- Set up or resume an Open-Science project for a defined research question.
- Configure a supported model provider, scientific skill, or MCP connector for a project.
- Run a bounded Python or R analysis and inspect its tables, figures, and execution records.
- Trace a generated artifact to the data, code, and environment that produced it.
- Export research results or a portable research record for review and reuse.

## Core Capabilities

1. **Discover the installed interfaces.** Read the repository documentation and the installed CLI help before choosing commands, flags, or tool names. Record the application version, operating system, active profile, and project identifier. Use the documented CLI through `run_shell_command`; if a required operation is desktop-only and no UI tool is available, provide the exact manual step and report it as pending. Do not edit internal application databases or invent an API.

2. **Configure a project and runtime.** Establish the research question, input locations, expected outputs, and acceptance checks. Reuse the intended project or create one through the supported interface. Follow the documented setup sequence for environment, data location, agent runtime, model provider, and Notebook runtime; Python/R Notebook setup is required for analyses that depend on it. Test the selected provider and runtime before submitting substantive work. Keep credentials out of prompts and exported records.

3. **Connect the required tools.** Inspect existing skills and connections, then enable only those needed for the task. Follow the version-matched MCP guide for transport, executable, profile, and permissions; a successful `list_projects` call verifies connectivity when the client exposes that tool. This skill's allowed tools do not themselves grant access to arbitrary MCP tools. Use documented CLI equivalents when available, or report the missing integration. Local-first storage does not mean provider requests or remote connectors stay on the computer.

4. **Execute a reproducible analysis.** Preserve original inputs and record their source, content hash or version, schema, and relevant units. Submit a scoped task specifying the analysis, output filenames, and validation criteria. Run Python or R with the actual input paths and retain the executed code, parameters, random seed where relevant, runtime/package versions, and execution status. Review errors and output content before interpreting a result; generated code without a completed execution is not an executed analysis.

5. **Validate and trace results.** Check expected rows, columns, units, missing values, and domain-specific invariants. Inspect the artifact's available Provenance evidence for input versions, producer code, and execution history. Rerun a small deterministic calculation when feasible, comparing numeric outputs with a stated tolerance. Mark missing evidence as unavailable; an artifact's existence or a recorded verification claim alone does not establish reproducibility.

6. **Export and hand off.** Use the documented artifact listing and download interfaces to select outputs from the correct session. For example, the README documents `open-science artifacts list <session-id> --json` and `open-science artifacts download <artifact-id> --output ./report.md`; substitute identifiers returned by the application and a filename appropriate to the artifact. Where supported, export a `.science` package with selected conversation branches, file versions, Notebook records, and verification evidence. Reopen the downloaded file or inspect the imported package, and report exported paths, checks performed, and remaining limitations. Exporting locally does not authorize publishing or sending results.

## Inputs / Outputs

**Inputs**

- Research question, analysis scope, acceptance criteria, and desired export format.
- Existing project/profile identifier or a requested new project name and local data location.
- Input datasets, papers, scripts, or notebooks with source references and usage constraints.
- Installed Open-Science version, configured model access, required connectors, and Python/R dependencies.

**Outputs**

- A configured or resumed project and a recorded task/session identifier.
- Executed analysis code and validated tables, figures, or reports, as requested.
- A provenance summary linking inputs and versions to code, parameters, environment, execution status, and output paths; explicitly identify missing records.
- Downloaded artifacts or a supported `.science` export, plus a concise rerun procedure and validation results.

**Completion check:** On an already configured installation with suitable small inputs, target one bounded workflow within 15 minutes: confirm project access, execute the requested analysis, validate at least one output, and reopen its export. Treat this as an operational target, not a performance benchmark or a promise for installations, downloads, or large analyses. If a dependency, authentication failure, or unavailable interface blocks completion, report the exact blocker and partial artifacts without claiming success.

## References

- [Open-Science source repository](https://github.com/aipoch/open-science) — source finding and upstream project.
- [Open-Science README](https://github.com/aipoch/open-science/blob/main/README.md) — setup, project workflow, Notebook execution, provenance, and artifact export examples.
- [CLI and MCP guide](https://github.com/aipoch/open-science/blob/main/packages/open-science/CLI.md) — consult for version-specific commands, profiles, permissions, and integrations.
- [Standalone runtime guide](https://github.com/aipoch/open-science/blob/main/docs/standalone-runtime.md) — consult when standalone installation or runtime setup is needed.
