#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import functools

from tmc import points

from tmc.utils import load, get_out, patch_helper

module_name="src.matrix_power"
matrix_power = load(module_name, "matrix_power")
main = load(module_name, "main")
ph = patch_helper(module_name)

# This solution to wrap a patched method comes originally from
# https://stackoverflow.com/questions/25608107/python-mock-patching-a-method-without-obstructing-implementation
def spy_decorator(method_to_decorate):
    mock = MagicMock()
    def wrapper(self, *args, **kwargs):
        mock(*args, **kwargs)
        return method_to_decorate(self, *args, **kwargs)
    wrapper.mock = mock
    return wrapper

class MatrixPower(unittest.TestCase):

    @points('p03-04.1')
    def test_one(self):
        a = np.array([[1,2], [3,4]])
        np.testing.assert_array_equal(a, matrix_power(a, 1),
                                      err_msg="Raising to power one should not change the matrix!")
        
    @points('p03-04.1')
    def test_zero(self):
        a = np.array([[1,2], [3,4]])
        np.testing.assert_array_equal(np.eye(2), matrix_power(a, 0),
                                      err_msg="Raising to power 0 should produce identity matrix!")
        
    @points('p03-04.1')
    def test_multiply(self):
        a = np.array([[1,2], [3,4]])
        for i in range(1,4):
            a1 = matrix_power(a, i)
            a2 = matrix_power(a, -i)
            np.testing.assert_array_almost_equal(np.eye(2), a1@a2,
                                                 err_msg="Multiplying a matrix and its inverse should produce identity matrix! "
                                                 "Input was matrix_power(a, %i) @ matrix_power(a, -%i), where a=\n%s" %(i,i,a))
            
    @points('p03-04.1')
    def test_called(self):
        a = np.array([[1,2], [3,4]])
        with patch(ph("functools.reduce"), wraps=functools.reduce) as preduce,\
             patch(ph("np.linalg.inv"), wraps=np.linalg.inv) as inv:
            p = matrix_power(a, -2)
            preduce.assert_called()
            inv.assert_called()
        


if __name__ == '__main__':
    unittest.main()
    
