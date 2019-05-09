#!/usr/bin/python3

import unittest
import random

from tmc import points

from tmc.utils import load, get_out

ProteinToRandomRNA = load('src.protein_to_random_rna', 'ProteinToRandomRNA')

aas="*ACDEFGHIKLMNPQRSTVWY"

def random_amino_acid_sequence(length):
    result=[]
    for _ in range(length):
        result.append(random.choice(aas))
    return "".join(result)

@points('p07-08.1')
class TestProteinToRandomRNA(unittest.TestCase):

    
    def test_first(self):
        p=ProteinToRandomRNA()
        result=p.convert("LTPIQNRA")
        self.assertEqual(len(p.convert("LTPIQNRA")), 24)

    def test_random(self):
        p=ProteinToRandomRNA()
        for length in range(100):
            s=random_amino_acid_sequence(length)
            rna=p.convert(s)
            self.assertEqual(length*3, len(rna))
            nucs=set(rna)
            for nuc in nucs:
                self.assertIn(nuc, "ACGU")
            
if __name__ == '__main__':
    unittest.main()
    
