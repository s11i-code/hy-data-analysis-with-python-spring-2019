#!/usr/bin/env python3
import pandas as pd
import numpy as np
def powers_of_series(s, k):
    powers = np.arange(1, k+1)
    array = np.transpose(s.values ** powers[:, np.newaxis])
    df = pd.DataFrame(array, index=s.index, columns=powers)
    return df

def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    return

if __name__ == "__main__":
    main()
