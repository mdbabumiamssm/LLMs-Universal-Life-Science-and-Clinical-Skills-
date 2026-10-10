# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

#!/usr/bin/env python3
"""
Create bone marrow reference marker file for CellIdentifierDX.
"""

import pandas as pd

# Bone marrow / hematopoietic cell type markers
BONE_MARROW_MARKERS = {
    'HSC': 'CD34,KIT,THY1,PROM1,CRHBP,HLF,AVP,MLLT3',
    'HSPC': 'CD34,CD38,FLT3,PTPRC,KIT,SPN',
    'MPP': 'CD34,FLT3,MPO,ELANE',
    'Erythroid_Early': 'GATA1,KLF1,TFRC,EPOR,CD36,GYPA',
    'Erythroid': 'HBB,HBA1,HBA2,GYPA,ALAS2,ANK1,SLC4A1',
    'Erythroid_Late': 'HBB,HBA1,HBA2,SPTA1,EPB42,RHAG',
    'GMP': 'CD34,MPO,ELANE,AZU1,PRTN3',
    'Neutrophil': 'ELANE,MPO,PRTN3,CTSG,AZU1,LCN2,S100A8,S100A9',
    'Monocyte': 'CD14,LYZ,CST3,VCAN,FCN1,S100A8,S100A9',
    'Macrophage': 'CD68,CD163,MRC1,MSR1,MARCO,C1QA,C1QB',
    'Dendritic': 'CD1C,FCER1A,CLEC10A,CD86,HLA-DRA,ITGAX',
    'pDC': 'IL3RA,CLEC4C,NRP1,TCF4,IRF7,IRF8',
    'Mast': 'TPSAB1,CPA3,KIT,MS4A2,HDC',
    'Basophil': 'CLC,HDC,GATA2,MS4A2',
    'Eosinophil': 'CLC,EPX,PRG2,RNASE2,RNASE3',
    'MEP': 'GATA1,ITGA2B,PF4,GP9',
    'Megakaryocyte': 'ITGA2B,GP9,PF4,PPBP,GP1BA,TUBB1,TREML1',
    'Platelet': 'PF4,PPBP,GP9,ITGA2B',
    'CLP': 'CD34,IL7R,FLT3,DNTT',
    'T_Cell': 'CD3D,CD3E,CD3G,TRAC,CD4,CD8A,CD8B',
    'CD4_T': 'CD3D,CD4,IL7R,TCF7,LEF1',
    'CD8_T': 'CD3D,CD8A,CD8B,GZMK,GZMB',
    'NK': 'NCAM1,NKG7,GNLY,KLRD1,KLRF1,KLRB1,PRF1',
    'B_Cell': 'CD79A,CD79B,MS4A1,CD19,PAX5,BANK1,IGHM',
    'Pro_B': 'CD34,CD79A,VPREB1,IGLL1,RAG1,RAG2,DNTT',
    'Pre_B': 'CD79A,VPREB1,IGLL1,CD19,PAX5',
    'Plasma': 'JCHAIN,MZB1,SDC1,TNFRSF17,XBP1,PRDM1',
    'MSC': 'CXCL12,LEPR,KITLG,VCAM1,PDGFRA,THY1',
    'Stromal': 'COL1A1,COL1A2,DCN,LUM,PDGFRA,PDGFRB',
    'Endothelial': 'PECAM1,VWF,CDH5,KDR,FLT1,EMCN',
    'Adipocyte': 'ADIPOQ,PPARG,LEP,FABP4,PLIN1',
}

# Create DataFrame
df = pd.DataFrame({
    'CELL TYPES': list(BONE_MARROW_MARKERS.keys()),
    'Markers': list(BONE_MARROW_MARKERS.values())
})

# Save to Excel with sheet name
output_path = '/media/drdx/mystorage/ARTIFICIALINTELLIGENCEGROUP/skills/tests/results_BM_vs_BT_analysis/bone_marrow_reference.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Bone_Marrow', index=False)

print(f"Created reference file: {output_path}")
print(f"Contains {len(df)} cell types")

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
