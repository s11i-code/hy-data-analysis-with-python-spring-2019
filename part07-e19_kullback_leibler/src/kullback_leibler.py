#!/usr/bin/env python3

from collections import defaultdict
from math import log2
import random

aas="*ACDEFGHIKLMNPQRSTVWY"


def random_event(dist):
    """Takes as input a dictionary from events to their probabilities.
Return a random event sampled according to the given distribution.
The probabilities must sum to 1.0"""
    # Copy the solution from the previous exercise here
    return event


# def grouped_codon_probabilities(s):
#     d=defaultdict(lambda : defaultdict(float))
#     assert len(s) % 3 == 0
#     n = len(s) // 3
#     for i in range(n):
#         codon = s[3*i:3*(i+1)]
#         aa=codon2aa[codon]
#         d[aa][codon] += 1
#     #add_pseudo_counts(d)
#     #n += 64  # Total 64 pseudocounts added
#     for aa in d:
#         d2 = d[aa]
#         n = sum(d2.values())
#         for codon in d2:
#             d2[codon] /= n
#     return d

def random_nucleotide_sequence(length):
    nucs="ACGU"
    result = [random.choice(nucs) for _ in range(length)]
    return "".join(result)

def random_amino_acid_sequence(length):
    result = [random.choice(aas) for _ in range(length)]
    return "".join(result)


# def print_in_order(d):
#     i=0
#     for key in sorted(d):
#         print("%s: %f" % (key, d[key]), end="")
#         i += 1
#         if i==6:
#             i=0
#             print()
#         else:
#             print("\t", end="")
#     if i != 0:
#         print()
            
# def pio(d):
#     for aa in sorted(d):
#         print(aa, end="\t")
#         print_in_order(d[aa])

# For double checking        
def rna_to_protein(s):
    assert len(s) % 3 == 0
    ncodons=len(s) // 3
    result=[]
    for i in range(ncodons):
        result.append(codon2aa[s[3*i:3*(i+1)]])
    return "".join(result)


def kullback_leibler(p, q):
    """Computes Kullback-Leibler divergence between two distributions.
Both p and q must be dictionaries from events to probabilities.
The divergence is defined only when q[event] == 0 implies p[event] == 0.
"""
    return 0.0

if __name__ == '__main__':
    n=10000
    protein=random_amino_acid_sequence(n)
    
    p=ProteinToRandomCodons()
    rna = p.convert(protein)
    protein2=rna_to_protein(rna)
    assert protein == protein2
    cp_predicted=codon_probabilities(rna)
    
    temp = sum(c2p.values())
    cp_orig = { codon : freq / temp for codon, freq in c2p.items() }
    
    uniform_random_rna = random_nucleotide_sequence(3*n)
    cp_uniform=codon_probabilities(uniform_random_rna)
    
    print("d(original|predicted)=", kullback_leibler(cp_orig, cp_predicted))
    print("d(predicted|original)=", kullback_leibler(cp_predicted, cp_orig))
    print()
    print("d(original|uniform)=", kullback_leibler(cp_orig, cp_uniform))
    print("d(uniform|original)=", kullback_leibler(cp_uniform, cp_orig))
    print()
    print("d(predicted|uniform)=", kullback_leibler(cp_predicted, cp_uniform))
    print("d(uniform|predicted)=", kullback_leibler(cp_uniform, cp_predicted))

