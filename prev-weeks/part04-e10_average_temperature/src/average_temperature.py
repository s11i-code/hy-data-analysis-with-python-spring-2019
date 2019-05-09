#!/usr/bin/env python3
import pandas as pd

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

AIR_TEMP_COL= 'Air temperature (degC)'
def average_temperature():
    df = pd.read_csv(get_path('kumpula-weather-2017.csv'))
    df_july = df[df.m == 7]
    july_mean = df_july.describe().loc['mean', AIR_TEMP_COL]
    return july_mean

def main():
    print("Average temperature in July: {:.1f}".format(average_temperature()))

    return

if __name__ == "__main__":
    main()
