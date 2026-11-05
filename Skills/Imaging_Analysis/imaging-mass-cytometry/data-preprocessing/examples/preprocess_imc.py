# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

'''IMC data preprocessing'''
import numpy as np
import tifffile
from scipy import ndimage

def remove_hot_pixels(img, threshold=50):
    '''Remove hot pixels using median filter comparison'''
    filtered = ndimage.median_filter(img, size=3)
    diff = np.abs(img.astype(float) - filtered.astype(float))
    hot = diff > threshold
    result = img.copy()
    result[hot] = filtered[hot]
    return result

def percentile_normalize(img, low=1, high=99):
    '''Normalize to percentiles'''
    p_low = np.percentile(img, low)
    p_high = np.percentile(img, high)
    if p_high > p_low:
        return np.clip((img - p_low) / (p_high - p_low), 0, 1)
    return img * 0

# Load image
img = tifffile.imread('acquisition.tiff')
print(f'Image shape: {img.shape}')  # (C, H, W)

# Process each channel
processed = []
for c in range(img.shape[0]):
    channel = img[c]
    channel = remove_hot_pixels(channel)
    channel = percentile_normalize(channel)
    processed.append(channel)

processed = np.stack(processed).astype(np.float32)

# Save
tifffile.imwrite('processed.tiff', processed)
print('Saved processed image')

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
