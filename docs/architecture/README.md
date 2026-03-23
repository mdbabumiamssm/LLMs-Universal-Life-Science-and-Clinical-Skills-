# Repository Architecture Map

```
repo/
├── Skills/                 # Domain-specific skills + agents
│   ├── AI_Providers/       # Cloud/provider operations skills
│   ├── Agentic_AI/         # Multi-agent orchestrators and runtimes
│   ├── Clinical/           # EHR, imaging, and oncology skills
│   ├── Data_Visualization/ # Plotting, dashboards, figure export
│   ├── Research_Tools/     # Literature, reporting, dispatch flows
│   └── …                   # (see Skills/README.md for the full list)
├── docs/                   # (You are here) domain documentation
├── platform/               # BioOS runtime + CLI entrypoints
├── src/                    # Shared Python packages/utilities
├── tests/, test_demonstration/  # Regression and tutorial suites
└── skills_catalog.json     # Machine-generated index of SKILL metadata
```

### How to add a new skill
1. Pick or create the domain folder under `Skills/`.
2. Follow `TUTORIAL_ADDING_NEW_SKILLS.md` and drop a `SKILL.md`.
3. Add any helper code/scripts inside the skill folder.
4. Reference the skill from the relevant docs page plus
   `skills_catalog.json` (via the generator).

### Operational stacks (2026 refresh)

| Stack | Components | Notes |
|-------|------------|-------|
| **MedgeClaw Ops** | `Research_Tools/General_Agent/biomed-dispatch`, `Reporting/dashboard`, `Reporting/feishu-rich-card`, `Reporting/svg-ui-templates`, `Data_Visualization/cjk-viz` | Turn-key workflow for dispatching biomedical analyses with live dashboards + Feishu briefings. |
| **Single-Cell QC** | `External_Collections/*/single-cell-rna-qc`, `tests/qc_*` | Shared code between notebooks, tests, and CLI demos. |
| **Provider Reliability** | `AI_Providers/*` | Tracks release cadence + operational status per vendor. |

Keep this file updated whenever large directory moves happen so downstream
contributors do not have to rediscover the structure.
