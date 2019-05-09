#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def municipalities_of_finland():
    df = pd.read_csv(get_path('municipal.tsv'), sep='\t', index_col='Region 2018')
    return df['Akaa':'Äänekoski']

def main():
    print(municipalities_of_finland())
    return

if __name__ == "__main__":
    main()
