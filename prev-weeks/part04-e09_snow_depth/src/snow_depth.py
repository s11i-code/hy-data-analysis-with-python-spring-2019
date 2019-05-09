#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def snow_depth():
    df = pd.read_csv(get_path('kumpula-weather-2017.csv'))
    max_snow_depth = df.describe().loc['max','Snow depth (cm)']
    return max_snow_depth

def main():
    print("Max snow depth: {:.1f}".format(snow_depth()))
    return

if __name__ == "__main__":
    main()

