# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

'''Build a Neighbor Joining tree from a multiple sequence alignment'''

from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

sequences = [
    SeqRecord(Seq('ATGCATGCATGC'), id='Human'),
    SeqRecord(Seq('ATGCATGCATGA'), id='Chimp'),
    SeqRecord(Seq('ATGCATGAATGC'), id='Gorilla'),
    SeqRecord(Seq('ATGAATGCATGC'), id='Mouse'),
    SeqRecord(Seq('ATGAATGAATGC'), id='Rat'),
]
alignment = MultipleSeqAlignment(sequences)

calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)

print('Distance Matrix:')
print(dm)

constructor = DistanceTreeConstructor(calculator, 'nj')
tree = constructor.build_tree(alignment)
tree.ladderize()

print('\nNeighbor Joining Tree:')
Phylo.draw_ascii(tree)

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
