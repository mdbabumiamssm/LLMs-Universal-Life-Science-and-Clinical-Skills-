<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

# Universal Skill Description Layer (USDL)

USDL is the canonical, model-agnostic schema for defining a biomedical agent. A USDL spec describes **what** a skill does (inputs, outputs, safety, audit rules). The `platform/optimizer/usdl_transpiler.py` module then compiles that spec into provider-specific artifacts:

| Provider | Artifact |
| --- | --- |
| OpenAI | System prompt + JSON schema bundle for ChatGPT Health / OpenAI for Healthcare endpoints. |
| Anthropic | Claude coworker transcript template with `<thinking>/<analysis>/<decision>` tags plus XML field definitions. |
| Gemini | Role card + output constraints tuned for long-context reasoning. |

## Workflow

1. Write a USDL JSON (example: `Skills/USDL_SPEC_PRIOR_AUTH.json`).
2. Load it into `USDLTranspiler` and emit the provider artifacts:
   ```python
   from platform.optimizer.usdl_transpiler import USDLTranspiler, USDLSpec, Provider
   import json

   spec = USDLSpec.from_dict(json.load(open("Skills/USDL_SPEC_PRIOR_AUTH.json")))
   bridge = USDLTranspiler()
   openai_payload = bridge.compile(spec, Provider.OPENAI)
   anthropic_payload = bridge.compile(spec, Provider.ANTHROPIC)
   ```
3. Wire the provider payloads into BioKernel router profiles so the same skill runs on any LLM.

## Benefits

* **Single Source of Truth:** Define skill logic once; auto-generate prompts and schemas.
* **Stack Alignment:** Ensures OpenAI and Anthropic stacks stay in sync.
* **Auditability:** Safety + audit policies travel with each compiled artifact.


<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->