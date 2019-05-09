#!/usr/bin/env python3

import sys
from math import log2


class MarkovChain(object):

    def __init__(self, k, zeroth, kth):
        self.k = k
        self.zeroth = { nuc : log2(p) for nuc, p in zeroth.items() }
        self.kth = { context : { nuc : log2(p) for nuc,p in d2.items() } for context, d2 in kth.items() }
        
    def log_probability(self, s):
        return 0.0
    
def get_example_model():
    return MarkovChain(2, {}, {})  # Modify this line
    
if __name__ == '__main__':
    mc = get_example_model()
    if len(sys.argv) == 1:
        s="ATGATATCATCGACGATGTAG"
        print("Probability of sequence %s is %e" % (s, mc.log_probability(s)))
    else:
        for s in sys.argv[1:]:
            print("Probability of sequence %s is %e" % (s, mc.log_probability(s)))
