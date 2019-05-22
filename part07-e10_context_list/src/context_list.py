#!/usr/bin/env python3

import sys
from collections import defaultdict

def kmer_gen(string, k):
    idx = 0
    while idx < len(string) - k:
        kmer = string[idx:idx+k]
        next_n = string[idx+k]
        idx += 1
        yield (kmer, next_n)

def context_list(s, k):
    contexts = defaultdict(str)
    for kmer, next_n in kmer_gen(s, k):
        contexts[kmer] = contexts[kmer] + next_n
    return dict(contexts)

if __name__ == '__main__':
    k=2
    if len(sys.argv) == 1:
        d=context_list("ATGATATCATCGACGATCTAG", k)
        print(d)
    else:
        for s in sys.argv[1:]:
            d=context_list(s, k)
            print(d)
