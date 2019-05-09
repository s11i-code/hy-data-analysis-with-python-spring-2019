#!/usr/bin/python3

import unittest


from tmc import points

from tmc.utils import load, get_out

MarkovChain = load('src.sample_from_concatenation', 'MarkovChain')

def is_subset(set1, set2):
    for element in set1:
        if element not in set2:
            return False
    return True

@points('p07-17.1')
class TestSampleFromConcatenation(unittest.TestCase):

    
    # def test_first(self):
    #     k=2
    #     s="ATGATATCATCGACGATGTAG"
    #     seed=0
    #     mc = MarkovChain(s, k)
    #     s2 = mc.generate(40, seed)
    #     self.assertEqual(s2, "ATCACTTTGCGGCCGATAGGCGAGATACTAATAGCTTGAT")

    def test_length_one(self):
        k=2
        s="ATGATATCATCGACGATGTAG"
        seed=0
        mc = MarkovChain(s, k)
        t = mc.generate(1, seed)
        self.assertEqual(len(t), 1, msg="generate does not work if string of length one is requested!")
        
    def test_deterministic(self):
        k=2
        s="ATGATATCATCGACGATGTAG"
        seed=0
        mc = MarkovChain(s, k)
        s1 = mc.generate(40, seed)
        s2 = mc.generate(40, seed)
        self.assertEqual(s1, s2, msg="Generate method should always return the same result, if the same seed and length used!")
        
    def test_second(self):
        s="ATGATATCATCGACGATGTAG"
        seed=0
        for n in range(40):
            for k in range(4):
                mc = MarkovChain(s, k)
                s2 = mc.generate(n, seed)
                self.assertEqual(len(s2), n)
                self.assertTrue(is_subset(s2, "ACGT"))


if __name__ == '__main__':
    unittest.main()
    
