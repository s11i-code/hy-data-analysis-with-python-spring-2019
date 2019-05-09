#!/usr/bin/env python3
import os
import re

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def read_lines(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + '/' + file_name, 'r')
    return f.readlines()

def parse_color(line):
    values = list(re.findall(r"\A\s*(\d+)\s*(\d+)\s*(\d+)", line)[0])
    name = re.findall(r"\t\t(.+?)\n", line)
    return "\t".join(values+name)


def red_green_blue():
    lines = read_lines('rgb.txt')[1:]
    colors = [parse_color(line) for line in lines]
    return colors

def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
