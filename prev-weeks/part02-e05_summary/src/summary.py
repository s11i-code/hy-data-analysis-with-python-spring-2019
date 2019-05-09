#!/usr/bin/env python3
import re
import math
import sys
def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def parse_line(line):
    try:
        return float(line.strip('\n'))           
    except ValueError:
        return None
 

def summary(filename):
    f = open(get_path(filename), 'r')
    lines = f.readlines()
    values = [parse_line(line) for line in lines if parse_line(line) != None]
    summed = sum(values)
    n = len(values)
    avg = summed/n
    squared_diffs = [(val - avg)**2 for val in values]
    stdev = math.sqrt(sum(squared_diffs)/(n-1))
    return (summed, avg, stdev)

def main():
    files =  sys.argv[1:]
    for file in files:
        fsummary = summary(file)
        print("File: {} Sum: {:.6f} Average: {:.6f} Stddev: {:.6f}".format(file, fsummary[0], fsummary[1], fsummary[2]))

if __name__ == "__main__":
    main()
