#!/usr/bin/env python3

import sys
from collections import defaultdict

NUCLEOTIDES = 'ACGT'
def sliding_window(s, k):
    """This function return a generator that can be iterated over all
starting position of a k-window in the sequence.
For each starting position the generator returns the nucleotide frequencies
in the window as a dictionary."""
    idx = 0
    while(idx+k <= len(s)):
        kmer = s[idx:idx+k]
        print('kmer:', kmer)
        letter_freqs = {str(nuc):kmer.count(nuc) for nuc in list(NUCLEOTIDES)}
        idx = idx + 1
        yield(letter_freqs)

if __name__ == '__main__':
    for d in sliding_window('GCGCTACGAT', 4):
        print(d)
    for s in sys.argv[1:]:
        for d in sliding_window(s, 4):
            print(d)
