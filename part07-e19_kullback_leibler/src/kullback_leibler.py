#!/usr/bin/env python3

from collections import defaultdict
from math import log2
import random
aas="*ACDEFGHIKLMNPQRSTVWY"

aa_to_codons = {'*': ['UAA', 'UGA', 'UAG'],
 'A': ['GCU', 'GCC', 'GCA', 'GCG'],
 'C': ['UGU', 'UGC'],
 'D': ['GAU', 'GAC'],
 'E': ['GAA', 'GAG'],
 'F': ['UUU', 'UUC'],
 'G': ['GGU', 'GGC', 'GGA', 'GGG'],
 'H': ['CAU', 'CAC'],
 'I': ['AUU', 'AUC', 'AUA'],
 'K': ['AAA', 'AAG'],
 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
 'M': ['AUG'],
 'N': ['AAU', 'AAC'],
 'P': ['CCU', 'CCC', 'CCA', 'CCG'],
 'Q': ['CAA', 'CAG'],
 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
 'T': ['ACU', 'ACC', 'ACA', 'ACG'],
 'V': ['GUU', 'GUC', 'GUA', 'GUG'],
 'W': ['UGG'],
 'Y': ['UAU', 'UAC']}
codon_to_aa = {'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C', 'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C', 'UUA': 'L', 'UCA': 'S', 'UAA': '*', 'UGA': '*', 'UUG': 'L', 'UCG': 'S', 'UAG': '*', 'UGG': 'W', 'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R', 'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', 'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R', 'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S', 'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', 'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', 'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', 'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', 'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', 'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}

class ProteinToRandomCodons:

    def convert(self, protein):
        return [random.choice(aa_to_codons[aa]) for aa in protein ]


def random_event(dist):
    """Takes as input a dictionary from events to their probabilities.
Return a random event sampled according to the given distribution.
The probabilities must sum to 1.0"""
    probs = list(dist.values())
    #normalize because due to rounding,
    #probabilities do not sum to exactly 1
    #and numpy complains
    normalized_probs = probs/sum(probs)
    return random.choice(list(dist.keys()), 1, p=list(normalized_probs))


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

def log_of_division(numer, denom):
    try:
        return log2(numer/denom)
    except Exception as e:
        return 0

def kullback_leibler(p, q):
    """Computes Kullback-Leibler divergence between two distributions.
Both p and q must be dictionaries from events to probabilities.
The divergence is defined only when q[event] == 0 implies p[event] == 0.
"""
    return sum([val * log_of_division(val,q[key]) for key, val in p.items()])

if __name__ == '__main__':
    n=10000
    protein=random_amino_acid_sequence(n)

    p=ProteinToRandomCodons()
    rna = p.convert(protein)
    #cp_predicted=codon_probabilities(rna)

    #temp = sum(c2p.values())
    #cp_orig = { codon : freq / temp for codon, freq in c2p.items() }

    p = dict(zip("ACGT", [1.0, 0.0, 0.0, 0.0]))
    q = dict(zip("ACGT", [0.25]*4))
    print(kullback_leibler(p, q))
    #self.assertAlmostEqual(kullback_leibler(q, p), 2.0, places=3)

    uniform_random_rna = random_nucleotide_sequence(3*n)
    #cp_uniform=codon_probabilities(uniform_random_rna)

    #print("d(original|predicted)=", kullback_leibler(cp_orig, cp_predicted))
    #print("d(predicted|original)=", kullback_leibler(cp_predicted, cp_orig))
    print()
    #print("d(original|uniform)=", kullback_leibler(cp_orig, cp_uniform))
    #print("d(uniform|original)=", kullback_leibler(cp_uniform, cp_orig))
    print()
    #print("d(predicted|uniform)=", kullback_leibler(cp_predicted, cp_uniform))
    #print("d(uniform|predicted)=", kullback_leibler(cp_uniform, cp_predicted))

