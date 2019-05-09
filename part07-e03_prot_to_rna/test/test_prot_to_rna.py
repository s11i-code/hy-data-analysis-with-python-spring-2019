#!/usr/bin/python3

import unittest

#from p01_dna_to_rna import dna_to_rna

from tmc import points

from tmc.utils import load, get_out

get_dict = load('src.prot_to_rna', 'get_dict')

@points('p07-03.1')
class TestProtToRna(unittest.TestCase):
        
    def test_content(self):
        d = get_dict()
        self.assertIn("F", d, msg="amino acid F not found in dictionary!")
        self.assertEqual(set(d["F"]), set(['UUU', 'UUC']), msg="Invalid codons for amino acid F!")
        self.assertIn("S", d, msg="amino acid S not found in dictionary!")
        self.assertEqual(set(d["S"]), set(['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']), msg="Invalid codons for amino acid S!")
        self.assertIn("Y", d, msg="amino acid Y not found in dictionary!")
        self.assertEqual(set(d["Y"]), set(['UAU', 'UAC']), msg="Invalid codons for amino acid Y!")
        self.assertIn("C", d, msg="amino acid C not found in dictionary!")
        self.assertEqual(set(d["C"]), set(['UGU', 'UGC']), msg="Invalid codons for amino acid C!")
        self.assertIn("L", d, msg="amino acid L not found in dictionary!")
        self.assertEqual(set(d["L"]), set(['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']), msg="Invalid codons for amino acid L!")
        self.assertIn("*", d, msg="amino acid * not found in dictionary!")
        self.assertEqual(set(d["*"]), set(['UAA', 'UGA', 'UAG']), msg="Invalid codons for amino acid *!")
        self.assertIn("W", d, msg="amino acid W not found in dictionary!")
        self.assertEqual(set(d["W"]), set(['UGG']), msg="Invalid codons for amino acid W!")
        self.assertIn("P", d, msg="amino acid P not found in dictionary!")
        self.assertEqual(set(d["P"]), set(['CCU', 'CCC', 'CCA', 'CCG']), msg="Invalid codons for amino acid P!")
        self.assertIn("H", d, msg="amino acid H not found in dictionary!")
        self.assertEqual(set(d["H"]), set(['CAU', 'CAC']), msg="Invalid codons for amino acid H!")
        self.assertIn("R", d, msg="amino acid R not found in dictionary!")
        self.assertEqual(set(d["R"]), set(['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']), msg="Invalid codons for amino acid R!")
        self.assertIn("Q", d, msg="amino acid Q not found in dictionary!")
        self.assertEqual(set(d["Q"]), set(['CAA', 'CAG']), msg="Invalid codons for amino acid Q!")
        self.assertIn("I", d, msg="amino acid I not found in dictionary!")
        self.assertEqual(set(d["I"]), set(['AUU', 'AUC', 'AUA']), msg="Invalid codons for amino acid I!")
        self.assertIn("T", d, msg="amino acid T not found in dictionary!")
        self.assertEqual(set(d["T"]), set(['ACU', 'ACC', 'ACA', 'ACG']), msg="Invalid codons for amino acid T!")
        self.assertIn("N", d, msg="amino acid N not found in dictionary!")
        self.assertEqual(set(d["N"]), set(['AAU', 'AAC']), msg="Invalid codons for amino acid N!")
        self.assertIn("K", d, msg="amino acid K not found in dictionary!")
        self.assertEqual(set(d["K"]), set(['AAA', 'AAG']), msg="Invalid codons for amino acid K!")
        self.assertIn("M", d, msg="amino acid M not found in dictionary!")
        self.assertEqual(set(d["M"]), set(['AUG']), msg="Invalid codons for amino acid M!")
        self.assertIn("V", d, msg="amino acid V not found in dictionary!")
        self.assertEqual(set(d["V"]), set(['GUU', 'GUC', 'GUA', 'GUG']), msg="Invalid codons for amino acid V!")
        self.assertIn("A", d, msg="amino acid A not found in dictionary!")
        self.assertEqual(set(d["A"]), set(['GCU', 'GCC', 'GCA', 'GCG']), msg="Invalid codons for amino acid A!")
        self.assertIn("D", d, msg="amino acid D not found in dictionary!")
        self.assertEqual(set(d["D"]), set(['GAU', 'GAC']), msg="Invalid codons for amino acid D!")
        self.assertIn("G", d, msg="amino acid G not found in dictionary!")
        self.assertEqual(set(d["G"]), set(['GGU', 'GGC', 'GGA', 'GGG']), msg="Invalid codons for amino acid G!")
        self.assertIn("E", d, msg="amino acid E not found in dictionary!")
        self.assertEqual(set(d["E"]), set(['GAA', 'GAG']), msg="Invalid codons for amino acid E!")
 
    def test_size(self):
        d = get_dict()
        self.assertEqual(len(d), 21)
        
if __name__ == '__main__':
    unittest.main()
    
