#!/usr/bin/env python3

def positive_list(L):
    positives = list(filter(lambda elem: elem > 0, L))
    return positives
    
def main():
    assert(positive_list([2,-2,0,1,-7]) == [2,1])
    
if __name__ == "__main__":
    main()
