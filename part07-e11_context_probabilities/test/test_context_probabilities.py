#!/usr/bin/python3

import unittest
import random
from collections import Counter

from tmc import points

from tmc.utils import load, get_out

context_probabilities = load('src.context_probabilities', 'context_probabilities')

def random_nucleotide_sequence(length):
    nucs="ACGT"
    result = [random.choice(nucs) for _ in range(length)]
    return "".join(result)

@points('p07-11.1')
class TestContextProbabilities(unittest.TestCase):

    
    def test_first(self):
        k=2
        s="ATGATATCATCGACGATGTAG"
        d = context_probabilities(s, k)
        places=3
        self.assertAlmostEqual(d["TA"]['G'], 0.500000, places=places)
        self.assertAlmostEqual(d["TA"]['T'], 0.500000, places=places)
        self.assertAlmostEqual(d["TA"]['A'], 0.000000, places=places)
        self.assertAlmostEqual(d["TA"]['C'], 0.000000, places=places)
        self.assertAlmostEqual(d["TC"]['G'], 0.500000, places=places)
        self.assertAlmostEqual(d["TC"]['T'], 0.000000, places=places)
        self.assertAlmostEqual(d["TC"]['A'], 0.500000, places=places)
        self.assertAlmostEqual(d["TC"]['C'], 0.000000, places=places)
        self.assertAlmostEqual(d["AT"]['G'], 0.400000, places=places)
        self.assertAlmostEqual(d["AT"]['T'], 0.000000, places=places)
        self.assertAlmostEqual(d["AT"]['A'], 0.200000, places=places)
        self.assertAlmostEqual(d["AT"]['C'], 0.400000, places=places)
        self.assertAlmostEqual(d["CG"]['G'], 0.000000, places=places)
        self.assertAlmostEqual(d["CG"]['T'], 0.000000, places=places)
        self.assertAlmostEqual(d["CG"]['A'], 1.000000, places=places)
        self.assertAlmostEqual(d["CG"]['C'], 0.000000, places=places)
        self.assertAlmostEqual(d["GA"]['G'], 0.000000, places=places)
        self.assertAlmostEqual(d["GA"]['T'], 0.666667, places=places)
        self.assertAlmostEqual(d["GA"]['A'], 0.000000, places=places)
        self.assertAlmostEqual(d["GA"]['C'], 0.333333, places=places)
        self.assertAlmostEqual(d["TG"]['G'], 0.000000, places=places)
        self.assertAlmostEqual(d["TG"]['T'], 0.500000, places=places)
        self.assertAlmostEqual(d["TG"]['A'], 0.500000, places=places)
        self.assertAlmostEqual(d["TG"]['C'], 0.000000, places=places)
        self.assertAlmostEqual(d["GT"]['G'], 0.000000, places=places)
        self.assertAlmostEqual(d["GT"]['T'], 0.000000, places=places)
        self.assertAlmostEqual(d["GT"]['A'], 1.000000, places=places)
        self.assertAlmostEqual(d["GT"]['C'], 0.000000, places=places)
        self.assertAlmostEqual(d["CA"]['G'], 0.000000, places=places)
        self.assertAlmostEqual(d["CA"]['T'], 1.000000, places=places)
        self.assertAlmostEqual(d["CA"]['A'], 0.000000, places=places)
        self.assertAlmostEqual(d["CA"]['C'], 0.000000, places=places)
        self.assertAlmostEqual(d["AC"]['G'], 1.000000, places=places)
        self.assertAlmostEqual(d["AC"]['T'], 0.000000, places=places)
        self.assertAlmostEqual(d["AC"]['A'], 0.000000, places=places)
        self.assertAlmostEqual(d["AC"]['C'], 0.000000, places=places)

    def test_random(self):
        n=100
        for k in range(5):
            s=random_nucleotide_sequence(n)
            d = context_probabilities(s, k)
            for context, d2 in d.items():
                self.assertAlmostEqual(sum(d2.values()), 1.0)

    def test_empty_context(self):
        k=0
        n=100
        s=random_nucleotide_sequence(n)
        d = context_probabilities(s, k)
        c=Counter(s)
        c = { nuc : count/n for nuc, count in c.items()} # Dictionary comprehension
        self.assertEqual(d[""], c)
        
if __name__ == '__main__':
    unittest.main()
    
