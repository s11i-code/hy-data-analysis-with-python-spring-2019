#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np
#from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, KFold
#from sklearn.model_selection import ShuffleSplit

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)


# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        #        lines.append(str(line))
        doc="".join(lines)
    else:
        with open(get_path(filename), "rb") as data:
            doc=data.read()
    #print("Lines: %i" % len(lines))
    #print(lines[0])
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    #english_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/words"
    #words="/usr/share/dict/words"
    with open(get_path("words"), encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())

    return list(lines)


#def is_latin(s):
#    return "å" not in s and "ä" not in s and "ö" not in s
def get_occurrences_vec(word):
    unique, counts = np.unique(list(word), return_counts=True)
    counts = dict(zip(unique, counts))
    return np.array([counts.get(letter, 0) for letter in alphabet])

def get_features(words):
    vecs = [get_occurrences_vec(word) for word in words]
    return np.array(vecs)

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)
upcase_set = set(alphabet.upper())

def contains_valid_chars(s):
    return all(letter in alphabet_set or letter in upcase_set for letter in s)

# Print fitted parameters of a model
# def print_parameters(model):
#     for key in dir(model):
#         if key[0] != '_' and key[-1] == '_':
#             print(key, getattr(model, key))


def get_features_and_labels():
    fin_words = load_finnish()
    eng_words = load_english()

    fin_words = [word.lower() for word in fin_words if contains_valid_chars(word)]
    eng_words = [word.lower() for word in eng_words if contains_valid_chars(word) and word[0].islower()]
    fin_y = np.repeat(0, len(fin_words))
    eng_y = np.repeat(1, len(eng_words))
    features = np.vstack((get_features(fin_words), get_features(eng_words)))
    y =  np.concatenate((fin_y, eng_y), axis=None)
    return np.array(features), y

def word_classification():
    data = get_features_and_labels()
    model = MultinomialNB()
    acc = cross_val_score(model, data[0], data[1], cv= KFold(n_splits=5, shuffle=True, random_state=0))
    return acc

def main():
    #print(get_features(np.array(["abc", "zaka"])))
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
