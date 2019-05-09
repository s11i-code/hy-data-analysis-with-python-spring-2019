#!/usr/bin/env python3

import sys

kth = {'AA': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'AC': {'A': 0.2, 'C': 0.2, 'G': 0.4, 'T': 0.2},
 'AG': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'AT': {'A': 0.222, 'C': 0.333, 'G': 0.333, 'T': 0.111},
 'CA': {'A': 0.2, 'C': 0.2, 'G': 0.2, 'T': 0.4},
 'CC': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'CG': {'A': 0.5, 'C': 0.167, 'G': 0.167, 'T': 0.167},
 'CT': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'GA': {'A': 0.143, 'C': 0.286, 'G': 0.143, 'T': 0.429},
 'GC': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'GG': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25},
 'GT': {'A': 0.4, 'C': 0.2, 'G': 0.2, 'T': 0.2},
 'TA': {'A': 0.167, 'C': 0.167, 'G': 0.333, 'T': 0.333},
 'TC': {'A': 0.333, 'C': 0.167, 'G': 0.333, 'T': 0.167},
 'TG': {'A': 0.333, 'C': 0.167, 'G': 0.167, 'T': 0.333},
 'TT': {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}}

zeroth = {'A': 0.32, 'C': 0.16, 'T': 0.28, 'G': 0.24}

#NUCLEOTIDES = 'ACGT'

class MarkovChain(object):

    def __init__(self, k, zeroth, kth):
        self.k = k
        self.zeroth = zeroth
        self.kth = kth

    def __split_str_to_kmers(self, s):
        idx = 0
        while idx < len(s) - self.k:
            print('round: ', idx)
            kmer = s[idx:idx+self.k]
            print('kmer: ', kmer)
            next_n = s[idx + self.k]
            idx += 1
            yield (kmer, next_n)

    def probability(self, s):
        if(len(s) == 0):
            return {}

        probability = self.zeroth[list(s)[0]]
        for kmer, next_n in self.__split_str_to_kmers(s):
            next_prob = self.kth[kmer][next_n]
            probability = probability * next_prob
        return probability

def get_example_model():
    return MarkovChain(2, zeroth, kth)  # Modify this line

if __name__ == '__main__':
    mc = get_example_model()
    if len(sys.argv) == 1:
        s="ATGATATCATCGACGATGTAG"
        print("Probability of sequence %s is %e" % (s, mc.probability(s)))
    else:
        for s in sys.argv[1:]:
            print("Probability of sequence %s is %e" % (s, mc.probability(s)))
