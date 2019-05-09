#!/usr/bin/env python3

def main():
    nums = list(range(1, 7))
    [ print("({},{})".format(a, b)) for a in nums
                    for b in nums
                    if a + b == 5]
    

if __name__ == "__main__":
    main()
