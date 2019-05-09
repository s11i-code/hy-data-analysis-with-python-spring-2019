#!/usr/bin/python3

import unittest


from tmc import points

from tmc.utils import load, get_out

kmer_index = load('src.kmer_index', 'kmer_index')

@points('p07-18.1')
class TestKmerIndex(unittest.TestCase):

    
    def test_first(self):
        s = "ATGATATCATCGACGATGTAG"
        n = len(s)
        for k in range(4):
            index = kmer_index(s, k)
            positions = []
            for context, pos_lst in index.items():
                positions.extend(pos_lst)
            self.assertEqual(len(positions), n-k+1)
            positions.sort()
            self.assertSequenceEqual(positions, range(n-k+1))



if __name__ == '__main__':
    unittest.main()
    
