#!/usr/bin/env python3
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def explained_variance():
    data = pd.read_csv(get_path('data.tsv'), sep='\t')
    model = PCA()
    model.fit(data)
    variances = data.var(axis='index')
    explained_variances = model.explained_variance_
    return variances, explained_variances

def main():
    vs, evs = explained_variance()
    plt.plot(np.arange(1, len(evs)+1), np.cumsum(evs))
    plt.show()
    print("The variances are:", " ".join(["{:.3f}".format(v, 3) for v in vs]))
    print("The explained variances after PCA are:", " ".join(["{:.3f}".format(v, 3) for v in evs]))

if __name__ == "__main__":
    main()
