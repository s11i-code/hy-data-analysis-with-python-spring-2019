#!/usr/bin/python3

import unittest

#from p01_dna_to_rna import dna_to_rna

from tmc import points

from tmc.utils import load, get_out

dna_to_rna = load('src.dna_to_rna', 'dna_to_rna')

@points('p07-01.1')
class TestDnaToRna(unittest.TestCase):

    def test_first(self):
        self.assertEqual(dna_to_rna("ACGT"), "ACGU")
        self.assertNotEqual(dna_to_rna("ACGT"), "ACGT")

    def test_second(self):
        self.assertEqual(dna_to_rna(""), "")
        
        

if __name__ == '__main__':
    unittest.main()
    
