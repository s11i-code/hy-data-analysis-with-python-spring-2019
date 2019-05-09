#!/usr/bin/env python3
import sys
import re

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)


def file_count(filename):
    f = open(get_path(filename), 'r')
    lines = f.readlines()
    linecount = len(lines)
    wordcount, charcount = 0, 0 # len(text.split(" "))
    charcount
    for line in lines:
         charcount += len(line)
         wordcount += len(line.split())      
    return (linecount, wordcount, charcount)

def main():
    files =  sys.argv[1:]
    for file in files:
        linecount, wordcount, charcount = file_count(file)
        print("{}\t{}\t{}\t{}".format(linecount, wordcount, charcount, file))

if __name__ == "__main__":
    main()        