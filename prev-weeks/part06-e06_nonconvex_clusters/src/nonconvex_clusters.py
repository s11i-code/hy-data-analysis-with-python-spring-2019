#!/usr/bin/env python3

import pandas as pd
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
#from collections import Counter


def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def nonconvex_clusters():
    return pd.DataFrame()

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
