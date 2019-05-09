#!/usr/bin/env python3

def find_matching(L, pattern):
    res = []
    for index, word in enumerate(L):
        if pattern in word:
            res.append(index)
    return res

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
