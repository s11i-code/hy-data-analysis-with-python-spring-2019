#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def municipalities_of_finland():
    return pd.read_csv(get_path('municipal.tsv'), sep='\t', index_col='Region 2018')

def subsetting_with_loc():
    df = municipalities_of_finland()
    cols = df.columns[[0, 2, 3]]
    df = df.loc['Akaa':'Äänekoski', cols]
    return df

def main():
    print(subsetting_with_loc().head(3))

if __name__ == "__main__":
    main()
