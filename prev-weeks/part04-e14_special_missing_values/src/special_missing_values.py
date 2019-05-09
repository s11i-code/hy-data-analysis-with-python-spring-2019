#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

SPECIAL_VALUES = ['New', 'Re']

def special_missing_values():
    df = pd.read_csv(get_path('UK-top40-1964-1-2.tsv'), sep='\t')
    df.loc[df.LW.isin(SPECIAL_VALUES), 'LW'] = None
    df.loc[df.Pos.isin(SPECIAL_VALUES), 'Pos'] = None
    df.Pos = pd.to_numeric(df.Pos)
    df.LW = pd.to_numeric(df.LW)
    declining = df[df.LW < df.Pos]
    return declining

def main():
    print(special_missing_values())
    return

if __name__ == "__main__":
    main()
