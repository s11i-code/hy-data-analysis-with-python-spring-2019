#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def subsetting_by_positions():
    df = pd.read_csv(get_path('UK-top40-1964-1-2.tsv'), sep='\t')
    return df.iloc[1:11, 2:4]

def main():
    print(subsetting_by_positions().head(4))
    return

if __name__ == "__main__":
    main()
