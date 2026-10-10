# MedSAM2 Operations

## Installation

The official setup uses Python 3.12 and a CUDA-enabled PyTorch environment:

```bash
conda create -n medsam2 python=3.12 -y
conda activate medsam2
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu124
git clone https://github.com/bowang-lab/MedSAM2.git
cd MedSAM2
pip install -e ".[dev]"
bash download.sh
```

Pin the repository commit and checkpoint hash for reproducible evaluation.

## Inference

### 3D CT

```bash
python medsam2_infer_3D_CT.py -i CT_DeepLesion/images -o CT_DeepLesion/segmentation
```

### Medical video

```bash
python medsam2_infer_video.py -i input_video_path -m input_mask_path -o output_video_path
```

The project also provides RECIST-to-3D and Efficient MedSAM2 workflows. Retain prompt masks or RECIST markers with each output.

## Training

The official example uses the FLARE25 pan-cancer CT data and SAM2.1 Hiera Tiny. Set batch size from measured GPU memory and keep validation patients, sites, and time points independent from training.

## Provenance

Verified 2026-06-18:

- Official repository: https://github.com/bowang-lab/MedSAM2
- Project page: https://medsam2.github.io/
- Model weights: https://huggingface.co/wanglab/MedSAM2
- Repository license: Apache-2.0
- Latest repository commit observed: 2025-07-11
- Paper: https://arxiv.org/abs/2504.03600
- 3D Slicer integration: https://github.com/bowang-lab/MedSAMSlicer/tree/MedSAM2
