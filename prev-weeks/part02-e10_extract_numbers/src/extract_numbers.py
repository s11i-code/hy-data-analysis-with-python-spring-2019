#!/usr/bin/env python3

def as_number(str):
    try:
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            return None
    

def extract_numbers(s):
    elems = s.split(' ')
    nums = [as_number(elem) for elem in elems]
    nums = [num for num in nums if num != None]
    return nums

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
