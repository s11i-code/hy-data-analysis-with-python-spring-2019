#!/usr/bin/env python3

import sys
from collections import defaultdict

def all_kmers(k):
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


def dhelper():              # This function can be given as parameter to defaultdict.
    return defaultdict(int) # Can be useful in solving the exercise.

def context_probabilities(s, k):
    return {}

        
    
if __name__ == '__main__':
    k=2
    if len(sys.argv) > 1:
        for s in sys.argv[1:]:
            d=context_probabilities(s, k)
            print(d)
    else:
        s="ATGATATCATCGACGATGTAG"
        d=context_probabilities(s, k)
        print(d)

    
