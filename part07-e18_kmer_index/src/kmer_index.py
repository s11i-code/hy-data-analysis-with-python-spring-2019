#!/usr/bin/env python3

import sys
from collections import defaultdict

def kmer_index(s, k):
    return {}

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
