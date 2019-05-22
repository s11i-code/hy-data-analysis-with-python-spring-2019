#!/usr/bin/env python3

import sys
from collections import defaultdict


def sliding_window(s, k):
    """This function returns a generator that can be iterated over all
starting position of a k-window in the sequence."""
    idx = 0
    while(idx+k <= len(s)):
        kmer = s[idx:idx+k]
        yield(kmer, idx)
        idx = idx + 1

def kmer_index(s, k):
    indices = defaultdict(list)
    for kmer, idx in sliding_window(s, k):
        indices[kmer].append(idx)
    return indices

if __name__ == '__main__':
    k=2
    try:
        s = sys.argv[1]
    except IndexError:
        s = "ATGATATCATCGACGATGTAG"
    try:
        k = int(sys.argv[2])
    except (IndexError, ValueError):
        k = 2
    print("Using string:")
    print(s)
    print("".join(["%i" % (i%10) for i in range(len(s))]))
    print("%i-mer index is:" % k)
    d=kmer_index(s, k)
    print(dict(d))
