#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    mask =  a[:, 1] >  a[:, -2]
    return np.array(a[mask])

def main():
    arr = np.array(
        [[8, 9, 3, 8],
        [0, 5, 3, 9],
        [5, 7, 6, 0],
        [7, 8, 1, 6],
        [2, 1, 3, 5]]
    )
    print(column_comparison(arr))


if __name__ == "__main__":
    main()
