#!/usr/bin/env python3
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import pandas as pd
CODON_REGEX = r'([A-Z]{3})\s+'
AA_REGEX = r'\s+([A-Z*]{1})\s+'
FREQ_REGEX = r'(\d+.\d)\s{1}\('

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def get_synonomous_freqs_sum(aa, df):
    synonymous_codons = df[df.aa == aa]
    return synonymous_codons.freqs_per_1000.sum()

def get_dict():
    html = open(get_path("Codon_usage_table.html")).read()
    codon_html = BeautifulSoup(html, 'html.parser').pre.text

    df = pd.DataFrame()
    df['codon'] = re.findall(CODON_REGEX,  codon_html)
    df['freqs_per_1000'] = list(map(float, re.findall(FREQ_REGEX, codon_html)))
    df['aa'] = re.findall(AA_REGEX, codon_html)
    df['syn_sum'] = df.aa.map(lambda aa: get_synonomous_freqs_sum(aa, df))
    df['freq_frac'] = round(df.freqs_per_1000 / df.syn_sum, 3)
    return dict(zip(df.codon, df.freq_frac))

if __name__ == '__main__':
    codon_to_prob = get_dict()
    print(codon_to_prob)

