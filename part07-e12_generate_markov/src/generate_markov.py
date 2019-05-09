#!/usr/bin/env python3

import sys
import numpy as np
#from collections import OrderedDict

k=2

zeroth = {'A': 0.2, 'C': 0.19, 'T': 0.31, 'G': 0.3}

kth = {'GT': {'A': 1.0, 'C': 0.0, 'T': 0.0, 'G': 0.0},
       'CA': {'A': 0.0, 'C': 0.0, 'T': 1.0, 'G': 0.0},
       'TC': {'A': 0.5, 'C': 0.0, 'T': 0.0, 'G': 0.5},
       'GA': {'A': 0.0, 'C': 0.3333333333333333, 'T': 0.6666666666666666, 'G': 0.0},
       'TG': {'A': 0.5, 'C': 0.0, 'T': 0.5, 'G': 0.0},
       'AT': {'A': 0.2, 'C': 0.4, 'T': 0.0, 'G': 0.4},
       'TA': {'A': 0.0, 'C': 0.0, 'T': 0.5, 'G': 0.5},
       'AC': {'A': 0.0, 'C': 0.0, 'T': 0.0, 'G': 1.0},
       'CG': {'A': 1.0, 'C': 0.0, 'T': 0.0, 'G': 0.0}}


def random_event(dist):
    """Takes as input a dictionary from events to their probabilities.
Return a random event sampled according to the given distribution.
The probabilities must sum to 1.0"""
    #normalize because due to rounding,
    #probabilities do not sum to exactly 1
    #and numpy complains
    probs = np.array(list(dist.values()))
    normalized_probs = probs/probs.sum()
    return np.random.choice(list(dist.keys()), 1, p=list(normalized_probs))[0]

class MarkovChain(object):

    def __init__(self, k=k, zeroth=zeroth, kth=kth):
        self.k = k
        self.zeroth = zeroth
        self.kth = kth

    def generate(self, n, seed=None):
        np.random.seed(seed)   # Initialize random number generator
        if(n == 0):
            return ""
        elif(n == 1):
            return np.random.choice(['A', 'C', 'G', 'T'])
        #sample the first k-mer:
        seq = np.random.choice(list(self.kth.keys()))
        for idx in range(0, n - self.k):
            last_kmer = seq[idx: idx + self.k]
            event = random_event(self.kth[last_kmer])
            seq = seq + event
        return seq

if __name__ == '__main__':
    try:
        n=int(sys.argv[1])
    except IndexError:
        n=10

    try:
        seed=int(sys.argv[2])
    except IndexError:
        seed=None

    try:
        mc = MarkovChain(k, zeroth, kth)
        print('seq: ', mc.generate(n, seed))
    except KeyError as e:
        print(e)
