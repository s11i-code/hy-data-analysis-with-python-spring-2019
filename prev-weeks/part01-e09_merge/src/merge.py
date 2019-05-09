#!/usr/bin/env python3

def merge(L1, L2):
    if(L1[-1] < L2[0]):
        return L1 + L2
    elif(L2[-1] < L2[0]):
        return L2 + L1
    else: 
     return []

def main():
    print(merge([2], [1]))
    print(merge([], []))
    print(merge([4], []))
    print(merge([4, 38, 69], [5, 12]))
    print(merge([4, 7, 10], [12, 13]))
    print(merge([14], [5, 12, 13]))

    
if __name__ == "__main__":
    main()
