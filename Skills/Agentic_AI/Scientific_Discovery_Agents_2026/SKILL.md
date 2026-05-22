---
name: scientific-discovery-agents-2026
description: Design, evaluate, and operate agentic systems for biomedical and scientific discovery. Use when building or selecting agents for hypothesis generation, experiment planning, autonomous notebook analysis, lab-in-the-loop validation, pathology concept discovery, or multi-agent research workflows.
keywords:
  - scientific-discovery
  - biomedical-agents
  - hypothesis-generation
  - lab-in-the-loop
  - multi-agent
  - evaluation
measurable_outcome: Produce an evidence-grounded scientific agent plan with autonomy class, data/tool boundary, human checkpoint, validation endpoint, and rollback criteria within 2 hours.
metadata:
  author: Biomedical OS Team
  version: "2026.05"
source_reliability:
  - source: primary_literature
    score: 1.0
    rationale: Workflow is grounded in Nature, Nature Methods, Nature Medicine, and Nature Biotechnology papers checked on 2026-05-22.
  - source: official_project_sources
    score: 0.97
    rationale: Operational framing is cross-checked against official Google DeepMind, FutureHouse, and Stanford Biomni project sources.
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# Scientific Discovery Agents (2026)

Use this skill when the task is not just literature summarization, but a research loop that may generate hypotheses, choose analyses, propose experiments, execute notebooks, or interpret experimental results.

## Workflow

1. Classify the autonomy level: literature-only copilot, notebook/data-analysis agent, hypothesis generator, experiment planner, lab-in-the-loop agent, or clinical/pathology review assistant.
2. Define the scientific claim boundary before execution: hypothesis, in silico result, in vitro result, external validation, or clinical-grade evidence.
3. Bind each agent role to explicit tools, datasets, and stopping rules. Do not let a general agent silently become an experimental decision-maker.
4. Require human checkpoints at transitions from literature to experiment, from analysis to biological interpretation, and from model output to any clinical or therapeutic claim.
5. Evaluate against a specialist baseline: human expert, published analysis, benchmark task, ablation, or wet-lab validation endpoint.
6. Preserve a reproducibility package: prompt/config, model, tool versions, data snapshot, generated code/notebooks, citations, failed attempts, and reviewer decisions.

## May 2026 Landscape Signals

- **Co-Scientist**: multi-agent hypothesis generation built with Gemini, with biomedical validations including AML drug repurposing, liver fibrosis targets, and antimicrobial resistance mechanisms.
- **Robin**: FutureHouse lab-in-the-loop multi-agent system that couples literature search, experimental planning, data analysis, and updated hypotheses for experimental biology.
- **CellVoyager**: single-cell analysis agent that autonomously proposes and implements scRNA-seq notebook analyses and is evaluated on CellBench.
- **SPARK**: pathology-agent framework that uses language-mediated agents to generate biologically meaningful tumor-analysis concepts without additional model training.
- **Biomni**: general-purpose biomedical agent pattern for broad tool ecosystems, useful as an orchestrator only when task boundaries and validation gates are explicit.

## Guardrails

- Separate "agent proposed" from "experimentally validated" in every report.
- Do not present AI-discovered therapeutic candidates as clinically actionable without preclinical and clinical validation.
- Treat wet-lab, clinical, and patient-facing outputs as human-reviewed workflows, not autonomous deployment targets.
- For notebook agents, log executed code, environment, data hashes, and failed cells; reject hidden analysis steps.
- For multi-agent systems, track agent roles, messages, tool calls, critique/ranking decisions, and cost.
- For pathology and biomedical imaging, require cohort, scanner/site, leakage, and external-validation checks before deployment claims.

## Output Requirements

- State the autonomy class and allowed tools.
- State the scientific claim boundary and validation endpoint.
- State the human checkpoint and rollback trigger.
- Include citations or source IDs for every current-system claim.
