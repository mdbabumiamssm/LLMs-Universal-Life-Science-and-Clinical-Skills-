# MedgeClaw Stack Runbook

This guide ties together the dispatch + reporting skills that were imported
from the MedgeClaw project so you can run the workflow without bouncing across
multiple directories.

## Skill Components

| Layer | Path | Purpose |
|-------|------|---------|
| Dispatch | `Skills/Research_Tools/General_Agent/biomed-dispatch` | CLI + prompt scaffolding for scientific tasks (dashboard setup, task splitting). |
| Dashboards | `Skills/Research_Tools/Reporting/dashboard` | Local HTML dashboard + tiny server for progress/state tracking. |
| Messaging | `Skills/Research_Tools/Reporting/feishu-rich-card` | Helpers for Feishu interactive cards and template upload. |
| Visuals | `Skills/Research_Tools/Reporting/svg-ui-templates` | SVG templates to turn outputs into polished status tiles. |
| Font sanity | `Skills/Data_Visualization/data-visualization/cjk-viz` | Ensures Chinese labels render before exporting plots. |
| Repro playbooks | `Skills/Research_Tools/Data_Analysis/paper-reproduce` & `charls-reproduce` | Standard operating procedures for paper replication + CHARLS-specific mappings. |

## Typical Flow
1. Create a task dir under `data/<task>/`.
2. Copy dashboard templates (`dashboard.html`, `dashboard_serve.py`) and start the server.
3. Run `biomed-dispatch` to send the scoped prompt to Claude Code or similar.
4. Feed outputs into Feishu reports using `feishu-rich-card` + `svg-ui-templates`.
5. For CHARLS or other reproduction exercises, load the relevant playbook before analysis.

## Checklists
- [ ] Dashboard launched with state.json + port recorded.
- [ ] Each Claude Code phase limited to a single concern (search, drafting, plotting).
- [ ] Chinese labels tested via `cjk-viz/scripts/setup_cjk_font.py`.
- [ ] Final deliverable shared via Feishu card (link + hero image).
- [ ] Outputs archived under `data/<task>/output/` with README.

> Keep this runbook updated whenever we add/rename core workflow skills so
> operators have a single source of truth.
