# BioEmu Operations

## Installation

BioEmu is a Linux package for Python 3.10+:

```bash
pip install bioemu
pip install "bioemu[cuda]"
```

The first run downloads bundled AlphaFold2-related weights and model assets. Plan cache and network access accordingly.

## Pilot Sampling

```bash
python -m bioemu.sample \
  --sequence GYDPETGTWG \
  --num_samples 10 \
  --output_dir bioemu-pilot
```

BioEmu filters structures with clashes or chain discontinuities by default, so retained samples can be substantially fewer than requested.

## Physical Steering

```bash
python -m bioemu.sample \
  --sequence GYDPETGTWG \
  --num_samples 100 \
  --output_dir bioemu-steered \
  --denoiser_config src/bioemu/config/steering/physical_steering.yaml
```

The official implementation supports Sequential Monte Carlo and Feynman-Kac Corrector steering. Compare ensemble statistics before and after steering to detect distortion.

## Side Chains and Relaxation

```bash
pip install "bioemu[md]"
python -m bioemu.sidechain_relax \
  --pdb-path topology.pdb \
  --xtc-path samples.xtc
```

Run this on selected representatives. Side-chain reconstruction and MD relaxation have additional CUDA and conda dependencies.

## Provenance

Verified 2026-06-18:

- Official repository: https://github.com/microsoft/bioemu
- Latest GitHub release observed: `v1.3.1`, published 2026-04-15
- Repository pushed: 2026-06-12
- License: MIT
- Model weights: https://huggingface.co/microsoft/bioemu
- Benchmark repository: https://github.com/microsoft/bioemu-benchmarks
- Paper: https://www.science.org/doi/10.1126/science.adv9817
