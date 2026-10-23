# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

'''Consensus hit calling from multiple methods'''
import pandas as pd

# Load results from different methods
mageck = pd.read_csv('mageck.gene_summary.txt', sep='\t')
bagel = pd.read_csv('bagel_bf.txt', sep='\t')

# Standardize column names
mageck = mageck[['id', 'neg|score', 'neg|fdr']].rename(columns={'id': 'gene'})
bagel = bagel[['Gene', 'BF']].rename(columns={'Gene': 'gene'})

# Merge
merged = mageck.merge(bagel, on='gene', how='outer')

# Call hits per method
merged['mageck_hit'] = merged['neg|fdr'] < 0.1
merged['bagel_hit'] = merged['BF'] > 5

# Consensus
merged['n_methods'] = merged['mageck_hit'].fillna(False).astype(int) + merged['bagel_hit'].fillna(False).astype(int)

# Results
print('=== Consensus Hit Calling ===')
print(f'MAGeCK hits (FDR<0.1): {merged["mageck_hit"].sum()}')
print(f'BAGEL2 hits (BF>5): {merged["bagel_hit"].sum()}')
print(f'Consensus hits (both): {(merged["n_methods"] == 2).sum()}')

# High confidence hits
high_conf = merged[merged['n_methods'] == 2].sort_values('neg|score')
print('\nTop consensus hits:')
print(high_conf[['gene', 'neg|score', 'neg|fdr', 'BF']].head(20).to_string(index=False))

# Save
high_conf.to_csv('consensus_hits.csv', index=False)

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
