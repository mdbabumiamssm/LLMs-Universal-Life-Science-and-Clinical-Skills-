# MONAI Operations

## Installation

```bash
pip install monai==1.6.0
```

Use a compatible PyTorch and CUDA combination. For containerized work, pin a release-tagged `projectmonai/monai` image rather than `latest`.

## Core Pipeline Pattern

```python
from monai.transforms import Compose, EnsureChannelFirstd, LoadImaged, Orientationd, Spacingd

transforms = Compose([
    LoadImaged(keys=["image", "label"]),
    EnsureChannelFirstd(keys=["image", "label"]),
    Orientationd(keys=["image", "label"], axcodes="RAS"),
    Spacingd(
        keys=["image", "label"],
        pixdim=(1.0, 1.0, 1.0),
        mode=("bilinear", "nearest"),
    ),
])
```

Validate orientation and spacing against known landmarks. Image and label interpolation modes must differ appropriately.

## Ecosystem Routing

| Need | Project |
|---|---|
| Core transforms, networks, losses, metrics | MONAI |
| Reusable packaged workflows | MONAI Bundle and Model Zoo |
| AI-assisted annotation | MONAI Label |
| Clinical application packaging | MONAI Deploy App SDK |
| DICOM workflow integration | MONAI Deploy Informatics Gateway |

## Evaluation Minimums

- patient-level independent test set;
- subgroup and site-level metrics;
- calibration for probabilistic outputs;
- lesion-wise and surface metrics for segmentation;
- empty-case handling;
- inference latency and memory;
- reproducible bundle execution in a clean environment.

## Provenance

Verified 2026-06-18:

- Official repository: https://github.com/Project-MONAI/MONAI
- Documentation: https://monai.readthedocs.io/
- Latest release observed: `1.6.0`, published 2026-06-11
- License: Apache-2.0
- Tutorials: https://github.com/Project-MONAI/tutorials
- Model Zoo: https://github.com/Project-MONAI/model-zoo
- MONAI Label: https://github.com/Project-MONAI/MONAILabel
- MONAI Deploy App SDK: https://github.com/Project-MONAI/monai-deploy-app-sdk
