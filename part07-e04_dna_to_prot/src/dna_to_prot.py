#!/usr/bin/env python3
import re
RNA_TO_PROT = {'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C', 'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C', 'UUA': 'L', 'UCA': 'S', 'UAA': '*', 'UGA': '*', 'UUG': 'L', 'UCG': 'S', 'UAG': '*', 'UGG': 'W', 'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R', 'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', 'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R', 'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S', 'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', 'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', 'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', 'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', 'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', 'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}

DNA_TO_RNA = {
    "C": "C",
    "G": "G",
    "A": "A",
    "T": "U"
}

def dna_to_rna(s):
    as_rna = s
    for dna_base, rna_base in DNA_TO_RNA.items():
        as_rna = as_rna.replace(dna_base, rna_base)
    return as_rna

def rna_to_prot(s):
    rna = dna_to_rna(s)
    codons = re.findall(r'...', rna)
    amino_acids = [RNA_TO_PROT.get(codon) for codon in codons]
    return "".join(amino_acids)

def dna_to_prot(s):
    return rna_to_prot(dna_to_rna(s))

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print(dna_to_prot("ATGATATCATCGACGATGTAG"))
    else:
        for s in sys.argv[1:]:
            print(dna_to_prot(s))
