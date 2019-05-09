#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    col = a[:, c]
    (values, counts) = np.unique(col,return_counts = True)
    count_dict = dict(zip(values, counts))
    val_counts = [count_dict[num] for num in col]
    order = np.argsort(np.negative(val_counts))
    return np.array([])

def main():
    a = np.random.randint(1, 10, (7, 7))
    print(a)
    print(most_frequent_first(a, 6))

if __name__ == "__main__":
    main()
