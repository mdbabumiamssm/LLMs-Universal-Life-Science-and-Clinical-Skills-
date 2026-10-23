# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

'''Analyze phosphorylation sites from MaxQuant output'''
import pandas as pd
import numpy as np

phospho = pd.read_csv('Phospho (STY)Sites.txt', sep='\t', low_memory=False)
print(f'Total sites: {len(phospho)}')

# Filter contaminants and decoys
phospho = phospho[
    (phospho['Reverse'] != '+') &
    (phospho['Potential contaminant'] != '+')
]
print(f'After filtering: {len(phospho)}')

# Site localization classes
phospho['loc_class'] = pd.cut(phospho['Localization prob'], bins=[0, 0.5, 0.75, 1.0],
                               labels=['III', 'II', 'I'], include_lowest=True)
print('\nLocalization class distribution:')
print(phospho['loc_class'].value_counts())

# Keep only confident sites
confident = phospho[phospho['Localization prob'] >= 0.75].copy()
print(f'\nClass I sites: {len(confident)}')

# Amino acid distribution
aa_counts = confident['Amino acid'].value_counts()
print('\nPhosphorylated residues:')
for aa, count in aa_counts.items():
    print(f'  {aa}: {count} ({100*count/len(confident):.1f}%)')

# Create site identifier
confident['site_id'] = confident.apply(
    lambda r: f"{r['Gene names'].split(';')[0] if pd.notna(r['Gene names']) else r['Protein']}_{r['Amino acid']}{int(r['Position'])}",
    axis=1
)

# Extract intensity columns
intensity_cols = [c for c in confident.columns if c.startswith('Intensity ') and not c.startswith('Intensity___')]
if intensity_cols:
    site_matrix = confident[['site_id', 'Protein', 'Gene names', 'Amino acid', 'Position', 'Localization prob'] + intensity_cols].copy()
    site_matrix[intensity_cols] = site_matrix[intensity_cols].replace(0, np.nan)
    site_matrix[intensity_cols] = np.log2(site_matrix[intensity_cols])
    site_matrix.to_csv('phospho_sites_matrix.csv', index=False)
    print(f'\nSaved {len(site_matrix)} phosphosites to phospho_sites_matrix.csv')

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
