#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def mystery_data():
    df = pd.read_csv(get_path('mystery_data.tsv'), sep='\t')
    fit = LinearRegression(fit_intercept=False).fit(df.iloc[:, 0:5], df.loc[:, 'Y'])
    return fit.coef_

def main():
    for idx, coef in enumerate(mystery_data()):
        print("Coefficient of X{} is {}".format(idx+1, coef))

if __name__ == "__main__":
    main()
