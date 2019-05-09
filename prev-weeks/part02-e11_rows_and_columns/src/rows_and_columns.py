#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    return [row for row in a]
    
def get_columns(a):
    return [row for row in a.T]

    
def main():
    a = np.array([[5, 0, 3, 3],
            [7, 9, 3, 5],
            [2, 4, 7, 6],
            [8, 8, 1, 6]])
    print(get_rows(a))
    print(get_columns(a))        
       

if __name__ == "__main__":
    main()
