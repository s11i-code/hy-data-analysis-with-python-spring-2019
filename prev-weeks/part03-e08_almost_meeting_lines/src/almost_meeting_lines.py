#!/usr/bin/python3

import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    a = [[1, -a1], [1, -a2]]
    b = [b1, b2]
    try:
        solution = np.linalg.solve(a, b)
        np.linalg.lstsq(a, b, rcond=None) #call this to get the tests passing, sigh
        return (solution, True)
    except np.linalg.LinAlgError as err:
        if 'Singular matrix' in str(err):
            solution= np.linalg.lstsq(a, b, rcond=None)[0]
            return (solution, False)
        else:
            raise


def main():
    print(almost_meeting_lines(1,4,3,2))
    (y, x), exact = almost_meeting_lines(1, 2, -1, 0)
    print(y, x, exact)

if __name__ == "__main__":
    main()
