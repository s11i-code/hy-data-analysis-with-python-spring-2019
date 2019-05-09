#!/usr/bin/env python3

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split
#from sklearn import model_selection
#from sklearn import cross_validation

#from sklearn.naive_bayes import GaussianNB
from sklearn import naive_bayes

#from sklearn.metrics import accuracy_score
from sklearn import metrics
import numpy as np
from sklearn.naive_bayes import GaussianNB

def plant_classification():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], train_size=0.80, random_state=0)
    model = GaussianNB().fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = metrics.accuracy_score(y_test, predictions)
    return acc

def main():
    print("Accuracy is %f" % plant_classification())

if __name__ == "__main__":
    main()
