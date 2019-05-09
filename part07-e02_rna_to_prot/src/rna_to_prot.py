#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re

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

    return dict(zip(codons, aminoacids))

if __name__ == '__main__':
    codon_to_aa = get_dict()
    print(codon_to_aa)
