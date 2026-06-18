# TxGemma Operations

## Current Model Family

TxGemma version 1.0.0 is based on Gemma 2 and is released in 2B, 9B, and 27B sizes.

| Variant | Intended use |
|---|---|
| `google/txgemma-2b-predict` | Lower-resource predictive baselines |
| `google/txgemma-9b-predict` | Mid-sized therapeutic prediction |
| `google/txgemma-27b-predict` | Highest-capacity released prediction model |
| `google/txgemma-9b-chat` | Conversational therapeutic workflows |
| `google/txgemma-27b-chat` | Highest-capacity conversational workflow |

The official model card states that chat variants are available for 9B and 27B and may trade raw predictive performance for conversational flexibility.

## TDC Prompt Formatting

```python
import json
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="google/txgemma-27b-predict",
    filename="tdc_prompts.json",
)
with open(path) as handle:
    templates = json.load(handle)

prompt = templates["BBB_Martins"].replace(
    "{Drug SMILES}",
    "CN1C(=O)CN=C(C2=CCCCC2)c2cc(Cl)ccc21",
)
```

## Local Prediction

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "google/txgemma-27b-predict"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=8)
```

Use `tokenizer.apply_chat_template` with a `chat` model. For high-throughput production, Google recommends Model Garden.

## Validation Notes

The released models were benchmarked on 66 Therapeutics Data Commons tasks. Reproduce the split type and metric for each endpoint; aggregate benchmark claims do not establish performance on a new use case.

## Provenance

Verified 2026-06-18:

- Official model card: https://developers.google.com/health-ai-developer-foundations/txgemma/model-card
- Official get-started guide: https://developers.google.com/health-ai-developer-foundations/txgemma/get-started
- Official cookbook: https://github.com/google-gemini/gemma-cookbook/tree/main/TxGemma
- Hugging Face collection: https://huggingface.co/collections/google/txgemma-release-67dd92e931c857d15e4d1e87
- Model version: `1.0.0`
- Model terms: https://developers.google.com/health-ai-developer-foundations/terms
- Paper: https://arxiv.org/abs/2504.06196
