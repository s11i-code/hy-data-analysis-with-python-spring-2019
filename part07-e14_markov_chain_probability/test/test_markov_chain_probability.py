#!/usr/bin/python3

import unittest
import random

from tmc import points

from tmc.utils import load, get_out

MarkovChain = load('src.markov_chain_probability', 'MarkovChain')
get_example_model = load('src.markov_chain_probability', 'get_example_model')

def random_nucleotide_sequence(length):
    nucs="ACGT"
    result = [random.choice(nucs) for _ in range(length)]
    return "".join(result)

def all_kmers(k):
    """A generator that can be used to iterate through all k-mers.
Usage: for kmer in all_kmers(k):
           do_something(kmer)
"""
    if k==0:
        yield ""
    else:
        nucs="ACGT"
        v=[0]*k
        v[-1]=-1
        limit=pow(4, k)
        for i in range(limit):
            i=k-1
            while v[i] == 3:
                v[i] = 0
                i -= 1
            v[i] += 1
            yield "".join([ nucs[x] for x in v ])

@points('p07-14.1')
class TestMarkovChainProbability(unittest.TestCase):


    def test_length_one(self):
        mc = get_example_model()
        try:
            mc.probability("A")
        except Exception:
            self.assertTrue(False, msg="Method probability does not work "\
                            "for strings of length 1!")


        self.assertAlmostEqual(mc.probability("A"), 0.32, places=10,
                               msg="Incorrect probability for sequence 'A'!")
        self.assertAlmostEqual(mc.probability("C"), 0.16, places=10,
                               msg="Incorrect probability for sequence 'C'!")
        self.assertAlmostEqual(mc.probability("G"), 0.24, places=10,
                               msg="Incorrect probability for sequence 'G'!")
        self.assertAlmostEqual(mc.probability("T"), 0.28, places=10,
                               msg="Incorrect probability for sequence 'T'!")

    def test_first(self):
        mc = get_example_model()
        prob = mc.probability("ATGATATCATCGACGATGTAG")
        self.assertAlmostEqual(prob, 2.831270e-10, places=10)

    def test_random(self):
        mc = get_example_model()
        for _ in range(100):
            s=random_nucleotide_sequence(20)
            prob = mc.probability(s)
            self.assertGreater(prob, 0.0)

    def test_uniform(self):
        u = dict.fromkeys("ACGT", 0.25)
        kth={}
        k = 2
        for context in all_kmers(k):
            kth[context] = u
        mc = MarkovChain(k, u, kth)
        for kmer in all_kmers(4):
            self.assertAlmostEqual(mc.probability(kmer), pow(0.25, 4))

if __name__ == '__main__':
    unittest.main()

