#!/usr/bin/python3

import unittest
import random

from tmc import points

from tmc.utils import load, get_out

MarkovChain = load('src.markov_chain_log_probability', 'MarkovChain')
get_example_model = load('src.markov_chain_log_probability', 'get_example_model')

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

@points('p07-15.1')
class TestMarkovChainLogProbability(unittest.TestCase):

    
    def test_first(self):
        mc = get_example_model()
        prob = mc.log_probability("ATGATATCATCGACGATGTAG")
        self.assertAlmostEqual(prob, -3.171783e+01, places=5)

    def test_random(self):
        mc = get_example_model()
        for _ in range(100):
            s=random_nucleotide_sequence(20)
            prob = mc.log_probability(s)
            self.assertLessEqual(prob, 0.0)

    def test_uniform(self):
        u = dict.fromkeys("ACGT", 0.25)
        kth={}
        k = 2
        for context in all_kmers(k):
            kth[context] = u
#        try:
        mc = MarkovChain(k, u, kth)
#        except ValueError:
#            print(k, u, kth)
#            raise
        n=4
        for kmer in all_kmers(n):
            self.assertAlmostEqual(mc.log_probability(kmer), -2*n)
            
if __name__ == '__main__':
    unittest.main()
    
