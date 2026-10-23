# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

'''Check sequence compatibility for Golden Gate cloning'''

from Bio import SeqIO
from Bio.Restriction import BsaI, BsmBI, BbsI, SapI

record = SeqIO.read('insert.fasta', 'fasta')
seq = record.seq

print(f'Checking Golden Gate compatibility for: {record.id}')
print(f'Sequence length: {len(seq)} bp')
print('=' * 50)

golden_gate_enzymes = [
    (BsaI, 'Standard Golden Gate'),
    (BsmBI, 'MoClo / Golden Gate'),
    (BbsI, 'Golden Gate alternative'),
    (SapI, 'Golden Braid'),
]

compatible_with = []

for enzyme, system in golden_gate_enzymes:
    sites = enzyme.search(seq)
    if sites:
        print(f'\n{enzyme} ({system}):')
        print(f'  INCOMPATIBLE - {len(sites)} site(s) found at: {sites}')
        print(f'  Recognition site: {enzyme.site}')
    else:
        print(f'\n{enzyme} ({system}):')
        print(f'  COMPATIBLE - no sites found')
        compatible_with.append((enzyme, system))

print('\n' + '=' * 50)
print('Summary:')
if compatible_with:
    print('Sequence is compatible with:')
    for enzyme, system in compatible_with:
        print(f'  - {enzyme} ({system})')
else:
    print('Sequence contains sites for all common Golden Gate enzymes.')
    print('Consider domestication (removing internal sites) before cloning.')

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
