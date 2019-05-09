#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)


def get_score(X, y):
    score = LinearRegression(fit_intercept=True).fit(X, y).score(X, y)
    print(X)
    return score

def coefficient_of_determination():
    df = pd.read_csv(get_path('mystery_data.tsv'), sep='\t')
    print(df)
    X = df.loc[:, 'X1':'X5']
    y = df.loc[:, 'Y']
    score_all = get_score(X, y)
    num_of_features = X.shape[1]
    single_feature_scores = [get_score(X.iloc[:, [i]], y) for i in range(0, num_of_features)]
    return [score_all] + single_feature_scores

def main():
    for idx, coef in enumerate(coefficient_of_determination()):
        idx = str(idx) if idx else ''
        print("R2-score with feature(s) X{} is: {}".format(idx, coef))

if __name__ == "__main__":
    main()
