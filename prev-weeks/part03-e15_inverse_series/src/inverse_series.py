#!/usr/bin/env python3
import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, index=s.values)

def main():
    s = pd.Series(["Jack", "Jones", "James"], index=[1,2,3])
    print(inverse_series(s))
    s = pd.Series(["Jack", "Jack", "James"], index=[1,2,3])
    print(inverse_series(s))
    return

if __name__ == "__main__":
    main()
