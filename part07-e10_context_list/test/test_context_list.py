#!/usr/bin/python3

import unittest
import random

from tmc import points

from tmc.utils import load, get_out

context_list = load('src.context_list', 'context_list')

def random_nucleotide_sequence(length):
    nucs="ACGT"
    result = [random.choice(nucs) for _ in range(length)]
    return "".join(result)

@points('p07-10.1')
class TestContextList(unittest.TestCase):

    
    def test_first(self):
        k=2
        s="ATGATATCATCGACGATCTAG"
        d = context_list(s, k)
        
        self.assertEqual(len(d), 9)

        self.assertEqual(d["TC"], "AGT")
        self.assertEqual(d["CT"], "A")
        self.assertEqual(d["GA"], "TCT")
        self.assertEqual(d["TG"], "A")
        self.assertEqual(d["AC"], "G")
        self.assertEqual(d["TA"], "TG")
        self.assertEqual(d["CA"], "T")
        self.assertEqual(d["AT"], "GACCC")
        self.assertEqual(d["CG"], "AA")

    def test_random(self):
        n=100
        for k in range(2, 5):
            s=random_nucleotide_sequence(n)
            d = context_list(s, k)
            self.assertLessEqual(len(d), n-k)
            self.assertEqual(sum([len(val) for key,val in d.items()]), n-k)

if __name__ == '__main__':
    unittest.main()
    
