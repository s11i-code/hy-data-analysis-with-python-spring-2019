#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
import numpy as np

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    iris = load_iris()
    num_of_clusters = np.unique(iris.target).shape[0]
    model = KMeans(num_of_clusters, random_state=0)
    model.fit(iris.data)
    permutation = find_permutation(num_of_clusters, iris.target, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    acc = accuracy_score(iris.target, new_labels)
    return acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
