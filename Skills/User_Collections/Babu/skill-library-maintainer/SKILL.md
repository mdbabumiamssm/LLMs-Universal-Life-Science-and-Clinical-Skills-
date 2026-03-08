---
name: skill-library-maintainer
description: Maintain and improve large skill repositories with consistent metadata, lean SKILL.md bodies, reusable references, and validation discipline. Use when auditing skill collections, normalizing frontmatter, splitting oversized skills into references, adding new skills, updating agents/openai.yaml, or preparing a curated skills repo for release.
---

# Skill Library Maintainer

Maintain skill repositories as a product, not a dump of markdown files.

## Workflow

1. Audit the collection structure before editing: identify priority folders, malformed metadata, duplicate coverage, and user-specific collections.
2. Fix high-value skills first; do not churn hundreds of files without a reason.
3. Keep `SKILL.md` lean and trigger-oriented: frontmatter should help discovery, body should explain workflow, and bulky details should move into `references/`.
4. Add `agents/openai.yaml` for curated skills that should surface cleanly in UI-driven environments.
5. Validate every touched skill after editing and record any repo-wide issues left unresolved.
6. Commit only the intentional paths and avoid sweeping unrelated repo cleanup.

## Guardrails

- Do not preserve invalid frontmatter just because it already exists.
- Avoid redundant skills with nearly identical triggers unless they target distinct user groups.
- Prefer a few well-maintained flagship skills over many thin placeholders.
- Treat imported external collections as reference material until curated locally.

## References

- Read `references/audit-checklist.md` before a broad update.
- Read `references/curation-rules.md` when deciding whether to rewrite, split, merge, or add a skill.
