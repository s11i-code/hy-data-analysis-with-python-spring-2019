#!/usr/bin/env python3
from functools import reduce
import numpy as np

def array_gen(a, n, inv=False):
    for num in range(1, n+1):
        yield (np.linalg.inv(a) if inv else a)

def matrix_power(a, n):
    shape = np.shape(a)
    assert shape[0] == shape[1], "The array is not a square matrix"
    if(n == 0):
        return np.eye(shape[0])
    elif(n == 1):
        return a
    elif(n > 0):
        return reduce(np.matmul, array_gen(a, n))
    else:
        return reduce(np.matmul, array_gen(a, abs(n), inv=True))

def main():
    array = np.array([[1,2], [3,4]])
    print('n is 0')
    print(matrix_power(array, 0))
    print(np.linalg.matrix_power(array, 0))
    print('n is 1')
    print(matrix_power(array, 1))
    print(np.linalg.matrix_power(array, 1))
    print('n is 2')
    print(matrix_power(array, 2))
    print(np.linalg.matrix_power(array, 2))
    print('n is -2')
    print(matrix_power(array, -2))
    print(np.linalg.matrix_power(array, -2))



if __name__ == "__main__":
    main()
