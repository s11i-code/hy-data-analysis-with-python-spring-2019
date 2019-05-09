#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

#import scipy.cluster.hierarchy
from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
#import scipy.spatial.distance
import scipy.stats
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label= scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

NUCLEOTIDE_AS_NUM = dict(zip(['A', 'C', 'G', 'T'], range(0, 4)))
numerize_seq = lambda seq: [NUCLEOTIDE_AS_NUM[base] for base in seq]

def toint(seqs):
    return np.array([numerize_seq(list(seq)) for seq in seqs])

def get_features_and_labels(filename):
    data = pd.read_csv(get_path(filename), sep='\t')
    return (np.array(toint(data.X)), np.array(data.y))

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle("Hierarchical clustering using %s linkage and %s affinity" % (method, affinity))
    plt.show()

def cluster_euclidean(filename):
    [X, y] = get_features_and_labels(filename)
    model = AgglomerativeClustering(linkage='average', affinity='euclidean')
    predicted = model.fit_predict(X)
    acc = accuracy_score(y, predicted)
    return acc

def cluster_hamming(filename):
    [X, y] = get_features_and_labels(filename)
    n_clusters = np.unique(y).shape[0]
    model = AgglomerativeClustering(linkage='average', affinity='precomputed')
    predicted = model.fit_predict(pairwise_distances(X, metric='hamming'))

    permutation = find_permutation(n_clusters, y, predicted)
    predicted = [ permutation[label] for label in predicted]

    acc = accuracy_score(y, predicted)
    return acc

def main():
    print(cluster_euclidean('data.seq'))
    print(cluster_hamming('data.seq'))

    #print("Accuracy score with Euclidean affinity is", cluster_euclidean("data.seq"))
    #print("Accuracy score with Hamming affinity is", cluster_hamming("data.seq"))

if __name__ == "__main__":
    main()
