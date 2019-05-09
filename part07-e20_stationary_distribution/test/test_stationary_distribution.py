#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock

import numpy as np

from tmc import points
from tmc.utils import load, get_out, patch_helper

module_name="src.stationary_distribution"
get_stationary_distributions = load(module_name, "get_stationary_distributions")
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

@points('p07-20.1')
class StationaryDistribution(unittest.TestCase):

    
    def test_first(self):
        transition=np.array([[0.3, 0, 0.7, 0],
                             [0, 0.4, 0, 0.6],
                             [0.35, 0, 0.65, 0],
                             [0, 0.2, 0, 0.8]])
        distributions = get_stationary_distributions(transition)
        np.testing.assert_allclose(distributions[0], [0.33333333, 0., 0.66666667,  0], atol=1e-04)
        np.testing.assert_allclose(distributions[1], [ 0., 0.25, 0., 0.75], atol=1e-04)

    def test_calls(self):
        with patch(ph("np.linalg.eig"), wraps=np.linalg.eig) as eig,\
             patch(ph("get_stationary_distributions"), wraps=get_stationary_distributions) as gsd:
            main()
            eig.assert_called()
            gsd.assert_called()
                
if __name__ == '__main__':
    unittest.main()
    
