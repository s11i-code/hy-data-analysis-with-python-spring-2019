#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def municipalities_of_finland():
    df = pd.read_csv(get_path('municipal.tsv'), sep='\t', index_col='Region 2018')
    return df['Akaa':'Äänekoski']

def growing_municipalities(df):
    population_change_col = df.columns[1]
    growing_count = df[df[population_change_col] > 0].shape[0]
    proportion = growing_count/df.shape[0]
    return proportion

def main():
    df = municipalities_of_finland()
    print("Proportion of growing municipalities: {:.1f}%".format(growing_municipalities(df)*100))

if __name__ == "__main__":
    main()
