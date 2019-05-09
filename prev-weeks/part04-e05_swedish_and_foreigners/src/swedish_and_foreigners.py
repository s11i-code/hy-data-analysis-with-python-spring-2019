#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def municipalities_of_finland():
    df = pd.read_csv(get_path('municipal.tsv'), sep='\t', index_col='Region 2018')
    return df['Akaa':'Äänekoski']

def swedish_and_foreigners():
    df = municipalities_of_finland()
    swedish_col = df.columns[2]
    foreigner_col = df.columns[3]
    df = df[(df[swedish_col] > 5.0) & (df[foreigner_col] > 5.0)]
    return df[df.columns[[0, 2, 3]]]

def main():
    print(swedish_and_foreigners())
    return

if __name__ == "__main__":
    main()
