#!/usr/bin/env python3

CODON_PROBS = {'UUU': 0.46, 'UCU': 0.19, 'UAU': 0.44, 'UGU': 0.46, 'UUC': 0.54, 'UCC': 0.22, 'UAC': 0.56, 'UGC': 0.54, 'UUA': 0.08, 'UCA': 0.15, 'UAA': 0.29, 'UGA': 0.47, 'UUG': 0.13, 'UCG': 0.05, 'UAG': 0.24, 'UGG': 1.0, 'CUU': 0.13, 'CCU': 0.29, 'CAU': 0.42, 'CGU': 0.08, 'CUC': 0.2, 'CCC': 0.32, 'CAC': 0.58, 'CGC': 0.18, 'CUA': 0.07, 'CCA': 0.28, 'CAA': 0.26, 'CGA': 0.11, 'CUG': 0.4, 'CCG': 0.11, 'CAG': 0.74, 'CGG': 0.2, 'AUU': 0.36, 'ACU': 0.25, 'AAU': 0.47, 'AGU': 0.15, 'AUC': 0.47, 'ACC': 0.36, 'AAC': 0.53, 'AGC': 0.24, 'AUA': 0.17, 'ACA': 0.28, 'AAA': 0.43, 'AGA': 0.22, 'AUG': 1.0, 'ACG': 0.11, 'AAG': 0.57, 'AGG': 0.21, 'GUU': 0.18, 'GCU': 0.27, 'GAU': 0.46, 'GGU': 0.16, 'GUC': 0.24, 'GCC': 0.4, 'GAC': 0.54, 'GGC': 0.34, 'GUA': 0.12, 'GCA': 0.23, 'GAA': 0.42, 'GGA': 0.25, 'GUG': 0.46, 'GCG': 0.11, 'GAG': 0.58, 'GGG': 0.25}
AA_TO_RNA = {'F': ['UUU', 'UUC'], 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'Y': ['UAU', 'UAC'], 'C': ['UGU', 'UGC'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], '*': ['UAA', 'UGA', 'UAG'], 'W': ['UGG'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'H': ['CAU', 'CAC'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Q': ['CAA', 'CAG'], 'I': ['AUU', 'AUC', 'AUA'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG'], 'M': ['AUG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'D': ['GAU', 'GAC'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'], 'E': ['GAA', 'GAG']}

class ProteinToMaxRNA(object):

    def __init__(self):
        self.codon_probs = CODON_PROBS
        self.aa_to_rna = AA_TO_RNA

    def __get_codon_with_max_prob(self, aa):
        candidate_codons = self.aa_to_rna[aa]
        candidate_codons = {key:self.codon_probs[key] for key in candidate_codons}
        return max(candidate_codons, key=candidate_codons.get)

    def convert(self, s):
        max_prob_rna = [self.__get_codon_with_max_prob(aa) for aa in list(s)]
        return "".join(max_prob_rna)

if __name__ == '__main__':
    import sys
    protein_to_rna = ProteinToMaxRNA()
    if len(sys.argv) == 1:
        print(protein_to_rna.convert("LTPIQNRA"))
    else:
        for s in sys.argv[1:]:
            print(protein_to_rna.convert(s))
