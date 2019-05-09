#!/usr/bin/env python3

import sys
import random
from collections import defaultdict

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


class MarkovChain(object):

    def __init__(self, s, k):

    def generate(self, n, seed=None):
        if seed != None:
            print("Seed is", seed)
            random.seed(seed)    # Initialize the random number generator
        return ""
        
if __name__ == '__main__':
    k=2
    
    try:
        s = sys.argv[1]
    except IndexError:
        s = "ATGATATCATCGACGATGTAG"

    try:
        n = int(sys.argv[2])
    except IndexError:
        n = 10

    try:
        seed = int(sys.argv[3])
    except IndexError:
        seed = None
    
    mc = MarkovChain(s, k)
    print(mc.generate(n, seed))
