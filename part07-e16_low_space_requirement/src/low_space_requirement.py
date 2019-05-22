#!/usr/bin/env python3

import sys
from collections import defaultdict
import regex as re #use regex (not re) to support overlapping matches TA

NUCLEOTIDES = 'ATGC'

#assign prob 0.25 to each nucleotide. this is used when preceding kmer is not found.
MISSING_KMER_PROB = dict(zip(NUCLEOTIDES, [1/len(NUCLEOTIDES)]*len(NUCLEOTIDES)))

def all_kmers(k):
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

def get_pseudo_probs(context):
    """
    returns a dict with nucleotides as keys. The value is the
    pseudo probability of that nucleotide where 1 is added to the
    frequency. Nucleotides which are not found get a frequency of 1.
    """
    pseudo_total = len(context) + len(NUCLEOTIDES)
    return {str(nuc): (context.count(nuc) + 1)/pseudo_total for nuc in list(NUCLEOTIDES)}

def context_probabilities(s, k):
    kmers = {}
    if(k == 0):
        return get_pseudo_probs(s)
    for kmer in all_kmers(k):
        if(kmer in s):
            next_nucs_after_kmer = "%s([%s]{1})" % (kmer, NUCLEOTIDES)
            context = re.findall(next_nucs_after_kmer, s, overlapped=True)
            kmers[kmer] = get_pseudo_probs(context)
        else:
            kmers[kmer] = MISSING_KMER_PROB
    return kmers

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


