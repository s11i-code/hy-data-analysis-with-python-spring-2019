#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def suicide_fractions():
    suicides = pd.read_csv(get_path('who_suicide_statistics.csv'))
    grouped_means = suicides.groupby("country").mean()
    return grouped_means['suicides_no']/grouped_means['population']

def main():
    print(suicide_fractions().head(15))
    return

if __name__ == "__main__":
    main()
