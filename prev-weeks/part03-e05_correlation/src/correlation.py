#!/usr/bin/env python3

import seaborn as sns
import scipy.stats
import numpy as np

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def load():
    import pandas as pd
    return pd.read_csv(get_path("iris.csv")).drop('species', axis=1).values

def lengths():
    iris_data = load()
    sepal_length = iris_data[:, 0]
    petal_length = iris_data[:, 2]
    corr = scipy.stats.pearsonr(sepal_length, petal_length)[0]
    return corr

def correlations():
    iris_data = load()
    return np.corrcoef(iris_data, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
