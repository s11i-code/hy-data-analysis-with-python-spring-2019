#!/usr/bin/env python3


def main():
    nums = list(range(1, 11))
    for outer in nums:
        for inner in nums:
            product = outer * inner
            print(product, " ", end="")
        print("")
    

if __name__ == "__main__":
    main()
