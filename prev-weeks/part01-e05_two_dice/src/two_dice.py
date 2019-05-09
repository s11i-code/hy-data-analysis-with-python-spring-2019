#!/usr/bin/env python3

def main():
    nums = list(range(1, 7))
    for outer in nums:
        for inner in nums:
            if(inner + outer == 5):
                print("({},{})".format(outer, inner))

if __name__ == "__main__":
    main()
