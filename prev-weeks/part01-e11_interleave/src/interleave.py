#!/usr/bin/env python3

def interleave(*lists):
    lists = list(zip(*lists))
    print(lists)
    ret = []
    for lst in lists:
        ret.extend(list(lst))
    return ret

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
