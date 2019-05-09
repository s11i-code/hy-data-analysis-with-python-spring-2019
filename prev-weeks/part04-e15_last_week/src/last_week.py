#!/usr/bin/env python3

import pandas as pd
import numpy as np

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

SPECIAL_VALUES = ['New', 'Re']
MAX_POS = 40
ALL_POSITIONS = pd.np.arange(1.0, MAX_POS + 1)

def last_week():
    curr = pd.read_csv(get_path('UK-top40-1964-1-2.tsv'), sep='\t')
    from_last_week = curr[~curr.LW.isin(SPECIAL_VALUES)]

    reconstructed = from_last_week.filter(['Title','Artist', 'Publisher'], axis=1)
    reconstructed['Pos'] = pd.to_numeric(from_last_week.LW, errors='coerce')
    reconstructed['WoC'] = from_last_week['WoC'] - 1

    missing_pos = np.setdiff1d(ALL_POSITIONS, reconstructed.Pos.values)
    missing = pd.DataFrame({'Pos': missing_pos})
    reconstructed = pd.concat([reconstructed, missing], sort=False)
    reconstructed = reconstructed.sort_values(by=['Pos'])
    return reconstructed

def main():
    df = last_week()
    print("Shape: %i,%i" % df.shape)
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
