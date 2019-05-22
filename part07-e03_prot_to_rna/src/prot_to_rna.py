#!/usr/bin/env python3
import re
from collections import defaultdict
from bs4 import BeautifulSoup

CODON_REGEX = r'([A-Z]{3})\s+'
AA_REGEX = r'\s+([A-Z*]{1})\s+'

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def get_dict():
    html = open(get_path("Codon_usage_table.html")).read()
    parsed = BeautifulSoup(html, 'html.parser').pre.text
    codons = re.findall(CODON_REGEX, parsed)
    aminoacids = re.findall(AA_REGEX, parsed)

    aa_to_codon_dict = defaultdict(list)
    for index, aa in enumerate(aminoacids):
        aa_to_codon_dict[aa].append(codons[index])

    return dict(aa_to_codon_dict)

if __name__ == '__main__':
    aa_to_codons = get_dict()
    from pprint import PrettyPrinter
    PrettyPrinter().pprint(aa_to_codons)
