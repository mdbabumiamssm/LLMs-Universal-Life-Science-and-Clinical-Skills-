# New Biomedical Skills Research — 2026-06-18

## Objective

Identify actively maintained biomedical AI projects that add a distinct, recurring workflow to the first-party `Skills/` catalog without duplicating imported external collections.

## Audit Method

1. Enumerated existing `SKILL.md` files and searched names and bodies for candidate technologies.
2. Reviewed recent repository commits to avoid duplicating newly added orchestration skills.
3. Preferred official GitHub repositories, official developer documentation, model cards, and primary papers.
4. Required a clear operational workflow, current upstream activity, usable documentation, and explicit licensing or access terms.
5. Rejected candidates whose workflow was already covered by a dedicated first-party skill or whose source of truth was unclear.

## Selected Skills

| Skill | Gap Filled | Upstream Status Observed |
|---|---|---|
| `evo2-genome-model` | Long-context genomic scoring, embeddings, and DNA generation | ArcInstitute/evo2; Apache-2.0; release v0.5.0 on 2026-02-28 |
| `alphagenome-variant-effects` | Tissue-aware multimodal regulatory variant prediction | google-deepmind/alphagenome; Apache-2.0 client; release v0.6.1 on 2026-03-03 |
| `medgemma-health-ai` | Current medical text and vision foundation-model operations | Google-Health/medgemma; docs updated 2026-06-05; MedGemma 1.5 model card |
| `bioemu-protein-ensembles` | Generative equilibrium ensembles for protein monomers | microsoft/bioemu; MIT; release v1.3.1 on 2026-04-15; pushed 2026-06-12 |
| `boltz2-biomolecular-interactions` | Joint complex-structure and binding-affinity prediction | jwohlwend/boltz; MIT; pushed 2026-05-29 |

## Existing Coverage Considered

- Evo 2 was mentioned inside the BioNeMo skill and had a non-skill README under `Foundation_Models`, but no dedicated operational skill.
- AlphaGenome existed as a backend inside the vendored BioMCP repository, but no direct first-party API and interpretation skill existed.
- Boltz-1 and Boltz-2 appeared in broad structure or cloud-chemistry skills, but affinity semantics and Boltz YAML operations were not covered directly.
- MedGemma and BioEmu had no dedicated first-party skills.

## Deferred Candidates

- TxGemma: authoritative Google documentation exists, but the current catalog already has broad therapeutic property and agentic drug-discovery skills. It can be added later if a dedicated, maintained operational source or local evaluation workflow is adopted.
- Additional generic agent frameworks: recent commits already expanded AgentScope, OpenHands, and orchestration runtimes.

## Canonical Sources

- https://github.com/ArcInstitute/evo2
- https://www.nature.com/articles/s41586-026-10176-5
- https://github.com/google-deepmind/alphagenome
- https://www.alphagenomedocs.com/
- https://github.com/Google-Health/medgemma
- https://developers.google.com/health-ai-developer-foundations/medgemma/model-card
- https://github.com/microsoft/bioemu
- https://www.science.org/doi/10.1126/science.adv9817
- https://github.com/jwohlwend/boltz
- https://doi.org/10.1101/2025.06.14.659707
