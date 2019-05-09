#!/usr/bin/python3

import unittest


from tmc import points

from tmc.utils import load, get_out

context_probabilities = load('src.pseudocounts', 'context_probabilities')

@points('p07-13.1')
class TestPseudoCounts(unittest.TestCase):


    def test_first(self):
        k=2
        s="ATGATATCATCGACGATGTAG"
        d = context_probabilities(s, k)
        self.assertEqual(len(d), 16)      # Number of 2-mers
        for context, d2 in d.items():
            self.assertEqual(len(d2), 4)  # Number of nucleotides per context
        places=3
        self.assertAlmostEqual(d["CT"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["CT"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["TC"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TC"]['T'], 0.166667, places=places)
        self.assertAlmostEqual(d["TC"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["TC"]['A'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['T'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TA"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["TA"]['A'], 0.166667, places=places)
        self.assertAlmostEqual(d["AA"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["AA"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["AT"]['C'], 0.333333, places=places)
        self.assertAlmostEqual(d["AT"]['T'], 0.111111, places=places)
        self.assertAlmostEqual(d["AT"]['G'], 0.333333, places=places)
        self.assertAlmostEqual(d["AT"]['A'], 0.222222, places=places)
        self.assertAlmostEqual(d["TG"]['T'], 0.333333, places=places)
        self.assertAlmostEqual(d["TG"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["TG"]['G'], 0.166667, places=places)
        self.assertAlmostEqual(d["TG"]['A'], 0.333333, places=places)
        self.assertAlmostEqual(d["CG"]['C'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['T'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['G'], 0.166667, places=places)
        self.assertAlmostEqual(d["CG"]['A'], 0.500000, places=places)
        self.assertAlmostEqual(d["GG"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["GG"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["AC"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["AC"]['T'], 0.200000, places=places)
        self.assertAlmostEqual(d["AC"]['G'], 0.400000, places=places)
        self.assertAlmostEqual(d["AC"]['A'], 0.200000, places=places)
        self.assertAlmostEqual(d["GC"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["GC"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["GT"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['T'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['G'], 0.200000, places=places)
        self.assertAlmostEqual(d["GT"]['A'], 0.400000, places=places)
        self.assertAlmostEqual(d["CA"]['T'], 0.400000, places=places)
        self.assertAlmostEqual(d["CA"]['C'], 0.200000, places=places)
        self.assertAlmostEqual(d["CA"]['G'], 0.200000, places=places)
        self.assertAlmostEqual(d["CA"]['A'], 0.200000, places=places)
        self.assertAlmostEqual(d["AG"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["AG"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["GA"]['T'], 0.428571, places=places)
        self.assertAlmostEqual(d["GA"]['C'], 0.285714, places=places)
        self.assertAlmostEqual(d["GA"]['G'], 0.142857, places=places)
        self.assertAlmostEqual(d["GA"]['A'], 0.142857, places=places)
        self.assertAlmostEqual(d["TT"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["TT"]['A'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['C'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['T'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['G'], 0.250000, places=places)
        self.assertAlmostEqual(d["CC"]['A'], 0.250000, places=places)


if __name__ == '__main__':
    unittest.main()

