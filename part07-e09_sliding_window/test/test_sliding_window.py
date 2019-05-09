#!/usr/bin/python3

import unittest
import random

from tmc import points

from tmc.utils import load, get_out

sliding_window = load('src.sliding_window', 'sliding_window')

def random_nucleotide_sequence(length):
    nucs="ACGT"
    result = [random.choice(nucs) for _ in range(length)]
    return "".join(result)

def is_subset(set1, set2):
    for element in set1:
        if element not in set2:
            return False
    return True

@points('p07-09.1')
class TestSlidingWindow(unittest.TestCase):

    
    def test_first(self):
        dicts=[{'T': 1, 'C': 1, 'A': 1, 'G': 1},
               {'T': 2, 'C': 1, 'A': 0, 'G': 1},
               {'T': 2, 'C': 0, 'A': 0, 'G': 2},
               {'T': 2, 'C': 1, 'A': 0, 'G': 1},
               {'T': 1, 'C': 1, 'A': 1, 'G': 1}]

        for d1, d2 in zip(dicts, sliding_window("ACGTTGCA", 4)):
            self.assertEqual(d1, d2) 
        
    def test_random(self):
        for _ in range(10):
            s = random_nucleotide_sequence(100)
            for k in range(1, 20):
                for d in sliding_window(s, k):
                    self.assertEqual(sum(d.values()), k)
                    self.assertEqual(is_subset(d.keys(), "ACGT"), True)

    # def test_too_short(self):
    #     k=4
    #     s=random_nucleotide_sequence(3)
    #     with self.assertRaises(AssertionError):
    #         for d in sliding_window(s, k):
    #             pass


if __name__ == '__main__':
    unittest.main()
    
