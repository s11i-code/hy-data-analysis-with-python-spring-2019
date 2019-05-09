#!/usr/bin/python3

import unittest


from tmc import points

from tmc.utils import load, get_out

MarkovChain = load('src.generate_markov', 'MarkovChain')

def is_subset(set1, set2):
    for element in set1:
        if element not in set2:
            return False
    return True

@points('p07-12.1')
class TestGenerateMarkov(unittest.TestCase):


    def test_length(self):
        for n in range(100):
            try:
                mc = MarkovChain()
                s = mc.generate(n)
                self.assertEqual(len(s), n, msg="n: " + str(n))
            except KeyError:
                pass

    def test_content(self):
        for n in range(100):
            try:
                mc = MarkovChain()
                s = mc.generate(n)
                self.assertTrue(is_subset(s, "ACGT"))
            except KeyError:
                pass

    def test_deterministic(self):
        n=20
        seed=1
        mc = MarkovChain()
        try:
            s1 = mc.generate(n, seed)
            s2 = mc.generate(n, seed)
            self.assertEqual(s1, s2,
                             msg="Generate method should always "\
                             "return the same result, if the same seed and length used!")
        except KeyError:
            pass

if __name__ == '__main__':
    unittest.main()

