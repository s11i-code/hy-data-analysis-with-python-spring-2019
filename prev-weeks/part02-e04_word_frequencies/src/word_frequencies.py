#!/usr/bin/env python3
import re
def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def word_frequencies(filepath):
    f = open(filepath, 'r')
    text = f.read()
    words = re.split(r'\s', text)[0:-2]
    freqs = {}
    for word in words: 
        word = word.strip('"[],.:?!')
        if word in freqs:
            freqs[word] = freqs[word] + 1
        else:
            freqs[word] = 1
    return freqs
    
def main():
    d = word_frequencies(get_path("alice.txt"))
    for word in d:
        print("%s\t%s" % (word, d[word]))

if __name__ == "__main__":
    main()
