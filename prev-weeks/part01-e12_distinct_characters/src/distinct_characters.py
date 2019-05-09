#!/usr/bin/env python3

def distinct_characters(L):
    counts = {}
    for word in L:
        distinct_chars = len(set(word))
        counts[word] = distinct_chars
    return counts

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
