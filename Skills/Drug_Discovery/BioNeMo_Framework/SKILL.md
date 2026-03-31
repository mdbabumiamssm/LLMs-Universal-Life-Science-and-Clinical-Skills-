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

---
name: nvidia-bionemo-framework
description: Stand up NVIDIA BioNeMo Framework + NIM microservices to train, fine-tune, and deploy generative biomolecular models for drug discovery.
keywords:
  - generative-ai
  - drug-discovery
  - protein-design
  - nvidia
  - bionemo
measurable_outcome: Launch BioNeMo Framework from NGC, run one inference (NIM) and one fine-tuning recipe on DGX Cloud or on-prem GPUs within a single working day.
license: Apache-2.0 (framework) / NVIDIA AI Enterprise (enterprise support)
metadata:
  author: Computational Pharmacology Guild
  version: "2026.03"
compatibility:
  - system: NVIDIA GPU Compute Capability >= 8.0
  - system: DGX Cloud or on-prem DGX/HGX clusters
allowed-tools:
  - docker
  - run_shell_command
  - web_fetch
---

# NVIDIA BioNeMo Framework Skill

Use BioNeMo when you need enterprise-ready generative AI tooling for omics, protein, and small-molecule pipelines without assembling dozens of bespoke repos.

## Core Components
1. **BioNeMo Framework** – OSS toolkit (Apache 2.0) with training recipes, dataloaders, and model zoo (Evo2, DiffDock, MolMIM, AlphaBind). Downloaded as NGC containers (Refs. 1–3).
2. **BioNeMo NIMs** – Optimized inference microservices (Docker) that expose REST/gRPC endpoints to deploy models in under five minutes (Ref. 1).
3. **DGX Cloud / NVIDIA AI Enterprise** – Managed supercomputing tier for multi-node training with enterprise support; optional, framework also runs on self-managed clusters (Refs. 1,4).

## Setup Checklist
1. **Create/verify NGC account** and request access to `bionemo-framework` org.
2. **Pull the framework container**:
   ```bash
   docker login nvcr.io
   docker pull nvcr.io/nvidia/clara/bionemo-framework:2.2
   ```
3. **Launch training workspace** (single node):
   ```bash
   docker run --gpus all -it --rm \
     -v $PWD:/workspace \
     -e WANDB_API_KEY=$WANDB_API_KEY \
     nvcr.io/nvidia/clara/bionemo-framework:2.2 /bin/bash
   ```
4. **Set up DGX Cloud (optional)** using `dgxcloud cluster create` for multi-node jobs; attach encrypted NVMe scratch per recipe.
5. **Install CLI helpers** if you plan to run OSS repo directly:
   ```bash
   git clone https://github.com/NVIDIA/bionemo-framework.git
   cd bionemo-framework
   uv sync
   pre-commit install
   ```

## Standard Workflow
1. **Data staging** – Convert PDB/FASTA/SMILES to BioNeMo dataloaders using `recipes/*/prepare_data.py`.
2. **Fine-tune** (example: DiffDock):
   ```bash
   cd recipes/diffdock
   bash scripts/train.sh config/train.yaml
   ```
3. **Package inference microservice** via NIM:
   ```bash
   docker pull nvcr.io/nim/bionemo/diffdock:latest
   docker run --gpus all -p 8000:8000 nvcr.io/nim/bionemo/diffdock:latest
   ```
4. **Integrate with BioNeMo Blueprints** for turnkey workflows (virtual screening, protein design) when you need reference pipelines instead of bespoke notebooks (Ref. 4).
5. **Monitor + trace** using NVIDIA Base Command, Weights & Biases, or your own MLFlow deployment.

## Governance & Contribution Notes
- BioNeMo Framework is OSS (Apache 2.0). Follow CONTRIBUTING guidelines for CI labels (`ciflow:*`) before submitting PRs (Refs. 2,5).
- Enterprise deployments fall under NVIDIA AI Enterprise license; coordinate with legal before shipping regulated workloads (Refs. 1,4).
- Hardware baseline: Hopper/Blackwell class GPUs with ≥80 GB HBM for full-recipe throughput; smaller GPUs supported for inference only (Ref. 3).

## References
1. NVIDIA, *BioNeMo – Generative AI Platform* (product overview, framework vs. NIM breakdown). https://www.nvidia.com/en-us/clara/bionemo/
2. NVIDIA Docs, *BioNeMo Framework FAQ & User Guide*. https://docs.nvidia.com/bionemo-framework/2.2
3. NVIDIA Docs, *DiffDock recipe* (model details + scripts). https://docs.nvidia.com/bionemo-framework/1.10/models/diffdock.html
4. NVIDIA, *BioNeMo for Biopharma* (Blueprint workflows + DGX Cloud guidance). https://www.nvidia.com/en-au/clara/drug-discovery/
5. NVIDIA Docs, *Contributing to BioNeMo Framework*. https://docs.nvidia.com/bionemo-framework/2.5/user-guide/contributing
