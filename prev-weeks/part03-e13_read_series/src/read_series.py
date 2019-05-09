#!/usr/bin/env python3
import pandas as pd
import re

def read_series():
    line = None
    items = {}
    while(True):
        line = input("Give index-value pairs (separated by whitespace)")
        if line == "":
            break
        key, val = re.split(r'\s+', line)
        items[key] = val
    keys = list(items.keys())
    values = list(items.values())
    return pd.Series(pd.Series(values, index=keys))

def main():
    read_series()

if __name__ == "__main__":
    main()
