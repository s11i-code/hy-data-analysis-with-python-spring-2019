#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

AIR_TEMP_COL= 'Air temperature (degC)'

def below_zero():

    df = pd.read_csv(get_path('kumpula-weather-2017.csv'))
    return df[df[AIR_TEMP_COL] < 0].shape[0]

def main():
    print("Number of days below zero: {}".format(below_zero()))

    return

if __name__ == "__main__":
    main()
