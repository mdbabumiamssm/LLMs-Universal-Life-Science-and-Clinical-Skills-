---
name: alphagenome-variant-effects
description: Use Google DeepMind AlphaGenome to predict tissue-aware regulatory effects of DNA sequence variants across expression, splicing, chromatin, and contact-map outputs. Use when prioritizing noncoding variants, comparing reference and alternate alleles, visualizing predicted regulatory changes, or designing focused AlphaGenome API analyses.
---

# AlphaGenome Variant Effects

Use AlphaGenome for mechanistic prioritization of regulatory variants. Do not convert its predictions directly into clinical classifications.

## Workflow

1. Confirm the biological question, supported species and reference assembly, coordinate convention, and normalized reference/alternate allele.
2. Select a sequence interval that contains the relevant regulatory context without exceeding the model limit of one million base pairs.
3. Select tissue or cell context with ontology terms. Document why each term is biologically relevant.
4. Request only the output modalities needed for the hypothesis, such as RNA expression, splicing, chromatin accessibility, histone marks, transcription-factor binding, or chromatin contacts.
5. Use `predict_variant` for reference-versus-alternate comparisons and preserve both outputs.
6. Derive interpretable summaries:
   - direction and magnitude of predicted change;
   - affected tracks, genes, splice junctions, or regulatory elements;
   - consistency across related tissues and nearby windows.
7. Visualize reference and alternate tracks on the same axes and annotate the variant position.
8. Compare predictions with population frequency, ClinVar or disease evidence, QTLs, epigenomic tracks, and functional assays.

## Scale and Access

- Obtain an AlphaGenome API key and install the official client.
- Use the API for focused small-to-medium analyses. The official documentation states it is not intended for analyses requiring more than roughly one million predictions.
- Check the current terms before commercial use. The public API is offered for non-commercial use subject to Google DeepMind terms.
- Use the repository's BioMCP integration only when MCP orchestration is useful; use the official client for direct control and reproducible notebooks.

## Guardrails

- Do not infer causality from a predicted track change alone.
- Do not treat absent predicted effects as proof of benignity.
- Separate model outputs from external annotations in reports.
- Preserve API/client version, interval, ontology terms, requested outputs, and visualization settings.
- Require orthogonal evidence for clinical, therapeutic, or genome-editing decisions.

## Output Contract

Return a variant-centered report containing normalized input, biological context, requested modalities, reference-versus-alternate effects, supporting and conflicting evidence, limitations, and recommended validation.

Read `references/operations.md` for installation, a minimal API pattern, interpretation guidance, and canonical sources.
