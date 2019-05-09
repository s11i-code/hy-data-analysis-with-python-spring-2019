#!/usr/bin/python3

import unittest


from tmc import points

from tmc.utils import load, get_out

ProteinToMaxRNA = load('src.protein_to_max_rna', 'ProteinToMaxRNA')

@points('p07-06.1')
class TestProteinToMaxRNA(unittest.TestCase):

    def setUp(self):
        self.protein_to_max_rna = ProteinToMaxRNA()
        
    def test_first(self):
        self.assertEqual(self.protein_to_max_rna.convert("LTPIQNRA"), "CUGACCCCCAUCCAGAACAGAGCC")

    def test_second(self):
        self.assertEqual(self.protein_to_max_rna.convert("ARNQIPTL"), "GCCAGAAACCAGAUCCCCACCCUG")

    def test_empty(self):
        self.assertEqual(self.protein_to_max_rna.convert(""), "")


if __name__ == '__main__':
    unittest.main()
    
