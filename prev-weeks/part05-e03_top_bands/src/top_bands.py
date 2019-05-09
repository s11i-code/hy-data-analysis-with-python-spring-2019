#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)


def top_bands():
    top40 = pd.read_csv(get_path('UK-top40-1964-1-2.tsv'), sep='\t')
    bands = pd.read_csv(get_path('bands.tsv'), sep='\t')
    bands['Band'] = bands['Band'].str.upper()
    merged = pd.merge(bands, top40, left_on='Band', right_on='Artist')
    return merged

def main():
    top10 = top_bands()
    print(top10['Artist'])
    print(top10['Band'])

    return

if __name__ == "__main__":
    main()
