#!/usr/bin/env python3

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

if __name__ == '__main__':
    print(dna_to_rna("ATCCCGTAGGCTCAT"))