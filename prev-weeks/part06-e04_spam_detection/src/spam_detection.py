#!/usr/bin/env python3
import gzip
import math
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import metrics

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def read_gzip(file_name, fraction):
    with gzip.open(get_path(file_name)) as f:
        lines = f.readlines()
    cutoff = math.ceil(len(lines) * fraction)
    return lines[0:cutoff]

def spam_detection(random_state=0, fraction=1.0):
    spam = read_gzip('spam.txt.gz', fraction)
    ham = read_gzip('ham.txt.gz', fraction)
    vec = CountVectorizer()
    X = vec.fit_transform(np.array(ham + spam))
    y = np.hstack([[0]*len(ham), [1]*len(spam)])
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.25, random_state=random_state)

    model = MultinomialNB().fit(X_train, y_train)

    predictions = model.predict(X_test)
    acc = metrics.accuracy_score(y_test, predictions)
    misclassified_count = np.sum(y_test != predictions)

    return acc, len(y_test), misclassified_count

def main():
    accuracy, total, misclassified = spam_detection()
    print(accuracy, total, misclassified )

if __name__ == "__main__":
    main()
