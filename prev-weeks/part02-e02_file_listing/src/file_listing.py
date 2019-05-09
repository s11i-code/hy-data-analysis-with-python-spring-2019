#!/usr/bin/env python3
import sys
import os 
import re
import calendar


def process_line(line):
    months = "|".join(calendar.month_abbr[1:])
    parts = re.findall(r"hyad-all\s+(\d+)\s+(%s)\s+(\d+)\s+(\d{2}):(\d{2}) (.+)" % months, line)[0]
    
    return [int(part) if part.isdigit() else part for part in parts]

def read_lines(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + file_name, 'r')
    return f.readlines()

def file_listing():
    lines = read_lines('/listing.txt')
    return [process_line(line) for line in lines]
    
def main():
    print(file_listing())
        
if __name__ == "__main__":
    main()
