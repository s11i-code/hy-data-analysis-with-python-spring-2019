#!/usr/bin/env python3

import sys
from math import log2

kth = {'AA': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'AC': {'A': 0.2, 'C': 0.2, 'G': 0.4, 'T': 0.2},
 'AG': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'AT': {'A': 0.2222222222222222,
        'C': 0.3333333333333333,
        'G': 0.3333333333333333,
        'T': 0.1111111111111111},
 'CA': {'A': 0.2, 'C': 0.2, 'G': 0.2, 'T': 0.4},
 'CC': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'CG': {'A': 0.5,
        'C': 0.16666666666666666,
        'G': 0.16666666666666666,
        'T': 0.16666666666666666},
 'CT': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'GA': {'A': 0.14285714285714285,
        'C': 0.2857142857142857,
        'G': 0.14285714285714285,
        'T': 0.42857142857142855},
 'GC': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'GG': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'GT': {'A': 0.4, 'C': 0.2, 'G': 0.2, 'T': 0.2},
 'TA': {'A': 0.16666666666666666,
        'C': 0.16666666666666666,
        'G': 0.3333333333333333,
        'T': 0.3333333333333333},
 'TC': {'A': 0.3333333333333333,
        'C': 0.16666666666666666,
        'G': 0.3333333333333333,
        'T': 0.16666666666666666},
 'TG': {'A': 0.3333333333333333,
        'C': 0.16666666666666666,
        'G': 0.16666666666666666,
        'T': 0.3333333333333333},
 'TT': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}}

zeroth = {'A': 0.32, 'C': 0.16, 'G': 0.24, 'T': 0.28}


class MarkovChain(object):

    def __init__(self, k, zeroth, kth):
        self.k = k
        self.zeroth = { nuc : log2(p) for nuc, p in zeroth.items() }
        self.kth = { context : { nuc : log2(p) for nuc,p in d2.items() } for context, d2 in kth.items() }

    def __kmers_with_next_nucs(self, s):
        idx = 0
        while idx < len(s) - self.k:
            kmer = s[idx:idx+self.k]
            next_n = s[idx + self.k]
            idx += 1
            yield (kmer, next_n)

    def log_probability(self, s):
        if(len(s) == 0):
            return {}

        log_prob = sum([self.zeroth[nuc] for nuc in s[0:self.k]])

        for kmer, next_n in self.__kmers_with_next_nucs(s):
            next_prob = self.kth[kmer][next_n]
            log_prob = log_prob + next_prob

        return log_prob

def get_example_model():
    return MarkovChain(2, zeroth, kth)  # Modify this line

if __name__ == '__main__':
    mc = get_example_model()
    if len(sys.argv) == 1:
        s="ATGATATCATCGACGATGTAG"
        print("Log probability of sequence %s is %e" % (s, mc.log_probability(s)))
    else:
        for s in sys.argv[1:]:
            print("Log probability of sequence %s is %e" % (s, mc.log_probability(s)))
