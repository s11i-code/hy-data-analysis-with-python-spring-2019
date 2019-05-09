#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def main():
    df = pd.read_csv(get_path('municipal.tsv'), sep='\t')
    print("Shape: %s, %s" % df.shape)
    print('Columns:')
    for col in df.columns:
        print(col)
    return


if __name__ == "__main__":
    main()
