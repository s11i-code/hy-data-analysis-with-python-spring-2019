#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)


def best_record_company():
    top40 = pd.read_csv(get_path('UK-top40-1964-1-2.tsv'), sep='\t')
    grouped = top40.groupby('Publisher').sum()
    best = grouped.sort_values('WoC', ascending = False).index[0]
    return top40.loc[top40['Publisher']==best, :]

def main():
    print(best_record_company().head(30))
    return


if __name__ == "__main__":
    main()
