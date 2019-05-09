#!/usr/bin/python3

import unittest

from tmc import points

from tmc.utils import load, get_out

dna_to_prot = load('src.dna_to_prot', 'dna_to_prot')

@points('p07-04.1')
class TestDnaToProt(unittest.TestCase):

    def test_first(self):
        self.assertEqual(dna_to_prot("ATGATATCATCGACGATGTAG"), "MISSTM*")

    def test_empty(self):
        self.assertEqual(dna_to_prot(""), "")
        
        

if __name__ == '__main__':
    unittest.main()
    
