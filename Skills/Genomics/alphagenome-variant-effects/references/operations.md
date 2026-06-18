# AlphaGenome Operations

## Installation and Client

```bash
git clone https://github.com/google-deepmind/alphagenome.git
pip install ./alphagenome
```

Create the model client with an API key:

```python
from alphagenome.models import dna_client

model = dna_client.create("ALPHAGENOME_API_KEY")
```

Never commit API keys. Load them from a secret manager or environment variable.

## Minimal Variant Pattern

```python
from alphagenome.data import genome
from alphagenome.models import dna_client

interval = genome.Interval(
    chromosome="chr22",
    start=35677410,
    end=36725986,
)
variant = genome.Variant(
    chromosome="chr22",
    position=36201698,
    reference_bases="A",
    alternate_bases="C",
)

outputs = model.predict_variant(
    interval=interval,
    variant=variant,
    ontology_terms=["UBERON:0001157"],
    requested_outputs=[dna_client.OutputType.RNA_SEQ],
)
```

Use the official visualization package to overlay reference and alternate tracks and to annotate the variant.

## Interpretation Checklist

- Verify allele normalization and coordinate indexing.
- Confirm that tissue ontology terms match the disease mechanism.
- Inspect multiple output modalities when the mechanism is uncertain.
- Check whether the inferred target gene is supported by distance, contacts, QTLs, or perturbation data.
- Repeat with nearby intervals if boundary placement could affect context.
- Record API errors, unavailable tracks, and rate-limit retries.

## Provenance

Verified 2026-06-18:

- Official API repository: https://github.com/google-deepmind/alphagenome
- Official model-code repository: https://github.com/google-deepmind/alphagenome_research
- Documentation: https://www.alphagenomedocs.com/
- Latest GitHub release observed: `v0.6.1`, published 2026-03-03
- Client license: Apache-2.0
- API terms: https://deepmind.google.com/science/alphagenome/terms
- Paper: https://www.nature.com/articles/s41586-025-10014-0
