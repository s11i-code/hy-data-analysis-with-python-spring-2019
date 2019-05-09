#!/usr/bin/python3

import unittest

from tmc import points

from tmc.utils import load, get_out

#dna_to_rna = load('src.dna_to_rna', 'dna_to_rna')
get_dict = load('src.rna_to_prot', 'get_dict')

@points('p07-02.1')
class TestRnaToProt(unittest.TestCase):

 
    def test_size(self):
        d = get_dict()
        self.assertEqual(len(d), 64, msg="Incorrect number of elements in the returned dict!")
        
    def test_content(self):
        d = get_dict()
        
        self.assertIn("UUU", d, msg="The dict did not contain key UUU")
        self.assertEqual(d["UUU"], "F", msg="Incorrect amino acid for codon UUU")

        self.assertIn("UCU", d, msg="The dict did not contain key UCU")
        self.assertEqual(d["UCU"], "S", msg="Incorrect amino acid for codon UCU")

        self.assertIn("UAU", d, msg="The dict did not contain key UAU")
        self.assertEqual(d["UAU"], "Y", msg="Incorrect amino acid for codon UAU")

        self.assertIn("UGU", d, msg="The dict did not contain key UGU")
        self.assertEqual(d["UGU"], "C", msg="Incorrect amino acid for codon UGU")

        self.assertIn("UUC", d, msg="The dict did not contain key UUC")
        self.assertEqual(d["UUC"], "F", msg="Incorrect amino acid for codon UUC")

        self.assertIn("UCC", d, msg="The dict did not contain key UCC")
        self.assertEqual(d["UCC"], "S", msg="Incorrect amino acid for codon UCC")

        self.assertIn("UAC", d, msg="The dict did not contain key UAC")
        self.assertEqual(d["UAC"], "Y", msg="Incorrect amino acid for codon UAC")

        self.assertIn("UGC", d, msg="The dict did not contain key UGC")
        self.assertEqual(d["UGC"], "C", msg="Incorrect amino acid for codon UGC")

        self.assertIn("UUA", d, msg="The dict did not contain key UUA")
        self.assertEqual(d["UUA"], "L", msg="Incorrect amino acid for codon UUA")

        self.assertIn("UCA", d, msg="The dict did not contain key UCA")
        self.assertEqual(d["UCA"], "S", msg="Incorrect amino acid for codon UCA")

        self.assertIn("UAA", d, msg="The dict did not contain key UAA")
        self.assertEqual(d["UAA"], "*", msg="Incorrect amino acid for codon UAA")

        self.assertIn("UGA", d, msg="The dict did not contain key UGA")
        self.assertEqual(d["UGA"], "*", msg="Incorrect amino acid for codon UGA")

        self.assertIn("UUG", d, msg="The dict did not contain key UUG")
        self.assertEqual(d["UUG"], "L", msg="Incorrect amino acid for codon UUG")

        self.assertIn("UCG", d, msg="The dict did not contain key UCG")
        self.assertEqual(d["UCG"], "S", msg="Incorrect amino acid for codon UCG")

        self.assertIn("UAG", d, msg="The dict did not contain key UAG")
        self.assertEqual(d["UAG"], "*", msg="Incorrect amino acid for codon UAG")

        self.assertIn("UGG", d, msg="The dict did not contain key UGG")
        self.assertEqual(d["UGG"], "W", msg="Incorrect amino acid for codon UGG")

        self.assertIn("CUU", d, msg="The dict did not contain key CUU")
        self.assertEqual(d["CUU"], "L", msg="Incorrect amino acid for codon CUU")

        self.assertIn("CCU", d, msg="The dict did not contain key CCU")
        self.assertEqual(d["CCU"], "P", msg="Incorrect amino acid for codon CCU")

        self.assertIn("CAU", d, msg="The dict did not contain key CAU")
        self.assertEqual(d["CAU"], "H", msg="Incorrect amino acid for codon CAU")

        self.assertIn("CGU", d, msg="The dict did not contain key CGU")
        self.assertEqual(d["CGU"], "R", msg="Incorrect amino acid for codon CGU")

        self.assertIn("CUC", d, msg="The dict did not contain key CUC")
        self.assertEqual(d["CUC"], "L", msg="Incorrect amino acid for codon CUC")

        self.assertIn("CCC", d, msg="The dict did not contain key CCC")
        self.assertEqual(d["CCC"], "P", msg="Incorrect amino acid for codon CCC")

        self.assertIn("CAC", d, msg="The dict did not contain key CAC")
        self.assertEqual(d["CAC"], "H", msg="Incorrect amino acid for codon CAC")

        self.assertIn("CGC", d, msg="The dict did not contain key CGC")
        self.assertEqual(d["CGC"], "R", msg="Incorrect amino acid for codon CGC")

        self.assertIn("CUA", d, msg="The dict did not contain key CUA")
        self.assertEqual(d["CUA"], "L", msg="Incorrect amino acid for codon CUA")

        self.assertIn("CCA", d, msg="The dict did not contain key CCA")
        self.assertEqual(d["CCA"], "P", msg="Incorrect amino acid for codon CCA")

        self.assertIn("CAA", d, msg="The dict did not contain key CAA")
        self.assertEqual(d["CAA"], "Q", msg="Incorrect amino acid for codon CAA")

        self.assertIn("CGA", d, msg="The dict did not contain key CGA")
        self.assertEqual(d["CGA"], "R", msg="Incorrect amino acid for codon CGA")

        self.assertIn("CUG", d, msg="The dict did not contain key CUG")
        self.assertEqual(d["CUG"], "L", msg="Incorrect amino acid for codon CUG")

        self.assertIn("CCG", d, msg="The dict did not contain key CCG")
        self.assertEqual(d["CCG"], "P", msg="Incorrect amino acid for codon CCG")

        self.assertIn("CAG", d, msg="The dict did not contain key CAG")
        self.assertEqual(d["CAG"], "Q", msg="Incorrect amino acid for codon CAG")

        self.assertIn("CGG", d, msg="The dict did not contain key CGG")
        self.assertEqual(d["CGG"], "R", msg="Incorrect amino acid for codon CGG")

        self.assertIn("AUU", d, msg="The dict did not contain key AUU")
        self.assertEqual(d["AUU"], "I", msg="Incorrect amino acid for codon AUU")

        self.assertIn("ACU", d, msg="The dict did not contain key ACU")
        self.assertEqual(d["ACU"], "T", msg="Incorrect amino acid for codon ACU")

        self.assertIn("AAU", d, msg="The dict did not contain key AAU")
        self.assertEqual(d["AAU"], "N", msg="Incorrect amino acid for codon AAU")

        self.assertIn("AGU", d, msg="The dict did not contain key AGU")
        self.assertEqual(d["AGU"], "S", msg="Incorrect amino acid for codon AGU")

        self.assertIn("AUC", d, msg="The dict did not contain key AUC")
        self.assertEqual(d["AUC"], "I", msg="Incorrect amino acid for codon AUC")

        self.assertIn("ACC", d, msg="The dict did not contain key ACC")
        self.assertEqual(d["ACC"], "T", msg="Incorrect amino acid for codon ACC")

        self.assertIn("AAC", d, msg="The dict did not contain key AAC")
        self.assertEqual(d["AAC"], "N", msg="Incorrect amino acid for codon AAC")

        self.assertIn("AGC", d, msg="The dict did not contain key AGC")
        self.assertEqual(d["AGC"], "S", msg="Incorrect amino acid for codon AGC")

        self.assertIn("AUA", d, msg="The dict did not contain key AUA")
        self.assertEqual(d["AUA"], "I", msg="Incorrect amino acid for codon AUA")

        self.assertIn("ACA", d, msg="The dict did not contain key ACA")
        self.assertEqual(d["ACA"], "T", msg="Incorrect amino acid for codon ACA")

        self.assertIn("AAA", d, msg="The dict did not contain key AAA")
        self.assertEqual(d["AAA"], "K", msg="Incorrect amino acid for codon AAA")

        self.assertIn("AGA", d, msg="The dict did not contain key AGA")
        self.assertEqual(d["AGA"], "R", msg="Incorrect amino acid for codon AGA")

        self.assertIn("AUG", d, msg="The dict did not contain key AUG")
        self.assertEqual(d["AUG"], "M", msg="Incorrect amino acid for codon AUG")

        self.assertIn("ACG", d, msg="The dict did not contain key ACG")
        self.assertEqual(d["ACG"], "T", msg="Incorrect amino acid for codon ACG")

        self.assertIn("AAG", d, msg="The dict did not contain key AAG")
        self.assertEqual(d["AAG"], "K", msg="Incorrect amino acid for codon AAG")

        self.assertIn("AGG", d, msg="The dict did not contain key AGG")
        self.assertEqual(d["AGG"], "R", msg="Incorrect amino acid for codon AGG")

        self.assertIn("GUU", d, msg="The dict did not contain key GUU")
        self.assertEqual(d["GUU"], "V", msg="Incorrect amino acid for codon GUU")

        self.assertIn("GCU", d, msg="The dict did not contain key GCU")
        self.assertEqual(d["GCU"], "A", msg="Incorrect amino acid for codon GCU")

        self.assertIn("GAU", d, msg="The dict did not contain key GAU")
        self.assertEqual(d["GAU"], "D", msg="Incorrect amino acid for codon GAU")

        self.assertIn("GGU", d, msg="The dict did not contain key GGU")
        self.assertEqual(d["GGU"], "G", msg="Incorrect amino acid for codon GGU")

        self.assertIn("GUC", d, msg="The dict did not contain key GUC")
        self.assertEqual(d["GUC"], "V", msg="Incorrect amino acid for codon GUC")

        self.assertIn("GCC", d, msg="The dict did not contain key GCC")
        self.assertEqual(d["GCC"], "A", msg="Incorrect amino acid for codon GCC")

        self.assertIn("GAC", d, msg="The dict did not contain key GAC")
        self.assertEqual(d["GAC"], "D", msg="Incorrect amino acid for codon GAC")

        self.assertIn("GGC", d, msg="The dict did not contain key GGC")
        self.assertEqual(d["GGC"], "G", msg="Incorrect amino acid for codon GGC")

        self.assertIn("GUA", d, msg="The dict did not contain key GUA")
        self.assertEqual(d["GUA"], "V", msg="Incorrect amino acid for codon GUA")

        self.assertIn("GCA", d, msg="The dict did not contain key GCA")
        self.assertEqual(d["GCA"], "A", msg="Incorrect amino acid for codon GCA")

        self.assertIn("GAA", d, msg="The dict did not contain key GAA")
        self.assertEqual(d["GAA"], "E", msg="Incorrect amino acid for codon GAA")

        self.assertIn("GGA", d, msg="The dict did not contain key GGA")
        self.assertEqual(d["GGA"], "G", msg="Incorrect amino acid for codon GGA")

        self.assertIn("GUG", d, msg="The dict did not contain key GUG")
        self.assertEqual(d["GUG"], "V", msg="Incorrect amino acid for codon GUG")

        self.assertIn("GCG", d, msg="The dict did not contain key GCG")
        self.assertEqual(d["GCG"], "A", msg="Incorrect amino acid for codon GCG")

        self.assertIn("GAG", d, msg="The dict did not contain key GAG")
        self.assertEqual(d["GAG"], "E", msg="Incorrect amino acid for codon GAG")

        self.assertIn("GGG", d, msg="The dict did not contain key GGG")
        self.assertEqual(d["GGG"], "G", msg="Incorrect amino acid for codon GGG")

        
        

if __name__ == '__main__':
    unittest.main()
    
