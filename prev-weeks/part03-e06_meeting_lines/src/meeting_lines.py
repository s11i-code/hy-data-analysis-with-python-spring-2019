#!/usr/bin/python3

import numpy as np

def meeting_lines(a1, b1, a2, b2):
    a = [[1, -a1], [1, -a2]]
    b = [b1, b2]
    return np.linalg.solve(a, b)

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    y, x = meeting_lines(a1, b1, a2, b2)
    print("Lines meet at y=%f and x=%f" % (y, x))

if __name__ == "__main__":
    main()
