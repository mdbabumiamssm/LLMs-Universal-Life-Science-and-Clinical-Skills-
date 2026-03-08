# Audit Checklist

## Repository-level checks

- Which folders are first-party, user collections, or external imports?
- Which SKILL files fail the expected frontmatter shape?
- Which skills have useful coverage but poor triggers?
- Which skills are duplicated under multiple names?
- Which skills reference files that do not exist?

## Per-skill checks

- `name` is hyphen-case.
- `description` clearly states when to use the skill.
- Body is concise and workflow-oriented.
- `references/` exists when detail would otherwise bloat the body.
- `agents/openai.yaml` matches the skill if present.
