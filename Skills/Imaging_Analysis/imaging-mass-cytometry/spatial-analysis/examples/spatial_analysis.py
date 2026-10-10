# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

'''Spatial analysis of IMC data'''
import squidpy as sq
import anndata as ad

# Load phenotyped data
adata = ad.read_h5ad('imc_phenotyped.h5ad')
print(f'Loaded {adata.n_obs} cells')

# Build spatial graph (Delaunay triangulation)
sq.gr.spatial_neighbors(adata, coord_type='generic', delaunay=True)
print(f'Built spatial graph with {adata.obsp["spatial_connectivities"].nnz} edges')

# Neighborhood enrichment analysis
print('\nRunning neighborhood enrichment...')
sq.gr.nhood_enrichment(adata, cluster_key='cell_type')

# Print top interactions
zscore = adata.uns['cell_type_nhood_enrichment']['zscore']
cell_types = list(adata.obs['cell_type'].cat.categories)

print('\nTop enriched interactions (z > 2):')
for i, ct1 in enumerate(cell_types):
    for j, ct2 in enumerate(cell_types):
        if i < j and zscore[i, j] > 2:
            print(f'  {ct1} - {ct2}: z = {zscore[i, j]:.2f}')

print('\nTop depleted interactions (z < -2):')
for i, ct1 in enumerate(cell_types):
    for j, ct2 in enumerate(cell_types):
        if i < j and zscore[i, j] < -2:
            print(f'  {ct1} - {ct2}: z = {zscore[i, j]:.2f}')

# Co-occurrence analysis
print('\nRunning co-occurrence analysis...')
sq.gr.co_occurrence(adata, cluster_key='cell_type')

# Save results
adata.write('imc_spatial_analyzed.h5ad')
print('\nSaved to imc_spatial_analyzed.h5ad')

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
