#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    a = np.array([[1, -a1, -b1], [1, -a2, -b2], [1, -a3, -b3]])
    b = np.array([c1, c2, c3])
    return np.linalg.solve(a, b)

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    z, y, x = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print("Planes meet at z=%f, y=%f and x=%f" % (z, y, x))

if __name__ == "__main__":
    main()
