# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

'''Call chromatin loops from Hi-C data'''

import cooler
import cooltools
import bioframe

clr = cooler.Cooler('matrix.mcool::resolutions/10000')
print(f'Loaded at {clr.binsize}bp resolution')

view_df = bioframe.make_viewframe(clr.chromsizes)

print('Computing expected values...')
expected = cooltools.expected_cis(clr, view_df=view_df, ignore_diags=2)

print('Calling loops...')
dots = cooltools.dots(
    clr,
    expected=expected,
    view_df=view_df,
    max_loci_separation=2000000,
)

print(f'\nFound {len(dots)} loops')

if len(dots) > 0:
    dots['size'] = abs(dots['end2'] - dots['start1'])
    print(f'\nLoop size statistics:')
    print(f'  Mean: {dots["size"].mean()/1000:.0f} kb')
    print(f'  Median: {dots["size"].median()/1000:.0f} kb')

    dots.to_csv('loops.bedpe', sep='\t', index=False)
    print('\nSaved to loops.bedpe')
else:
    print('No loops found. Try adjusting parameters.')

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
