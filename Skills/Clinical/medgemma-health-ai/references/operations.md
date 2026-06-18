# MedGemma Operations

## Current Model

MedGemma 1.5 is available as a 4B multimodal instruction-tuned model:

```text
google/medgemma-1.5-4b-it
```

The official model card describes 128K total input context, text and image inputs, and text output. CT, MRI, and whole-slide pathology require dedicated preprocessing.

## Local Inference

```bash
pip install -U transformers accelerate
```

```python
import torch
from transformers import pipeline

pipe = pipeline(
    "image-text-to-text",
    model="google/medgemma-1.5-4b-it",
    torch_dtype=torch.bfloat16,
    device="cuda",
)
```

Use the official notebooks for message formatting and modality-specific preprocessing. Pin `transformers`, model revision, and container digest for controlled evaluations.

## Deployment Paths

| Need | Path |
|---|---|
| Experimentation and sensitive local data | Local Hugging Face inference |
| Scalable online HTTPS endpoint | Vertex AI Model Garden |
| Large offline dataset | Vertex AI batch prediction |
| Domain adaptation | Official fine-tuning notebook plus local validation |

## Evaluation Minimums

- expert-reviewed task accuracy;
- sensitivity and specificity at a prespecified operating point;
- calibration and abstention behavior;
- subgroup and site-level performance;
- hallucination and unsupported-claim rate;
- PHI leakage and prompt-injection tests;
- workflow time, override rate, and user acceptance.

## Provenance

Verified 2026-06-18:

- Official repository: https://github.com/Google-Health/medgemma
- Get started: https://developers.google.com/health-ai-developer-foundations/medgemma/get-started
- MedGemma 1.5 model card: https://developers.google.com/health-ai-developer-foundations/medgemma/model-card
- Official documentation last updated: 2026-06-05 UTC
- Model version in model card: `1.5.0`
- Model terms: https://developers.google.com/health-ai-developer-foundations/terms
- Technical report: https://arxiv.org/abs/2604.05081
