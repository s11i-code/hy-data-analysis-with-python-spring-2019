#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    num_of_cols = np.shape(a[2])[0]
    assert num_of_cols % 2 == 0, "Uneven number of rows in parameter array"
    m = int(num_of_cols/2)
    split_sum1 = np.sum(a[:, 0:m], axis = 1)
    split_sum2 = np.sum(a[:, m:num_of_cols], axis = 1)
    mask = split_sum1 > split_sum2
    return np.array(a[mask])

def main():
    a = np.array(
        [[8, 9, 3, 8],
        [0, 5, 3, 9],
        [5, 7, 6, 0],
        [7, 8, 1, 6],
        [2, 1, 3, 5]]
    )
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
