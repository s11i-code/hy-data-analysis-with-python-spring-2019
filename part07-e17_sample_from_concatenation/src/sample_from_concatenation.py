#!/usr/bin/env python3

import sys
import random
from collections import defaultdict
import numpy as np
import regex as re #use regex (not re) to support overlapping matches TA

NUCLEOTIDES = "ACGT"
#assign prob 0.25 to each nucleotide. this is used when preceding kmer is not found.
MISSING_KMER_PROB = dict(zip(NUCLEOTIDES, [1/len(NUCLEOTIDES)]*len(NUCLEOTIDES)))

def all_kmers(k):
    """A generator that can be used to iterate through all k-mers.
Usage: for kmer in all_kmers(k):
           do_something(kmer)
"""
    if k==0:
        yield ""
    else:
        v=[0]*k
        v[-1]=-1
        limit=pow(4, k)
        for i in range(limit):
            i=k-1
            while v[i] == 3:
                v[i] = 0
                i -= 1
            v[i] += 1
            yield "".join([ NUCLEOTIDES[x] for x in v ])

class MarkovChain(object):

    def __init__(self, s, k):
        self.k = k
        self.s = s
        self.contexts = self.__get_contexts(s, k)

    def __get_contexts(self, s, k):
        kmers = {}
        for kmer in all_kmers(k):
            if(kmer in s) and not s.endswith(kmer):
                next_nuc_after_kmer = "%s([%s]{1})" % (kmer, NUCLEOTIDES)
                context = re.findall(next_nuc_after_kmer, s, overlapped=True)
                kmers[kmer] = "".join(context)
            else:
                kmers[kmer] = NUCLEOTIDES

        return kmers

    def generate(self, n, seed=None):
        if seed != None:
            print("Seed is", seed)
            random.seed(seed)
        if(n < self.k):
            return n*random.choice(list(NUCLEOTIDES))
        #sample the first k-mer:
        seq = random.choice(list(self.contexts.keys()))
        for idx in range(0, n - self.k):
            prev_kmer = seq[idx: idx + self.k]
            context = list(self.contexts[prev_kmer])
            sample_nuc = random.choice(context)
            seq = seq + sample_nuc
        return seq

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

    mc = MarkovChain(s, 3)
    print(mc.generate(10, 0))
