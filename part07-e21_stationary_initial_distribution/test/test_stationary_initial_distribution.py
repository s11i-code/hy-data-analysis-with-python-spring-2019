#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock

import numpy as np

from tmc import points
from tmc.utils import load, get_out, patch_helper

module_name="src.stationary_initial_distribution"
get_stationary_distributions = load(module_name, "get_stationary_distributions")
main = load(module_name, "main")
MarkovChain = load(module_name, "MarkovChain")
kullback_leibler = load(module_name, "kullback_leibler")
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

@points('p07-21.1')
class StationaryInitialDistribution(unittest.TestCase):

    def test_correctness(self):
        transition=np.array([[0.3, 0, 0.7, 0],
                             [0, 0.4, 0, 0.6],
                             [0.35, 0, 0.65, 0],
                             [0, 0.2, 0, 0.8]])
        distributions = get_stationary_distributions(transition)
        np.testing.assert_allclose(distributions[0], [0.33333333, 0., 0.66666667,  0], atol=1e-04)
        np.testing.assert_allclose(distributions[1], [ 0., 0.25, 0., 0.75], atol=1e-04)

    def test_calls(self):
        generate_method = spy_decorator(MarkovChain.generate)
        with patch(ph("np.linalg.eig"), wraps=np.linalg.eig) as eig,\
             patch.object(MarkovChain, "generate", new=generate_method),\
             patch(ph("MarkovChain"), wraps=MarkovChain) as mc,\
             patch(ph("kullback_leibler"), wraps=kullback_leibler) as kl,\
             patch(ph("get_stationary_distributions"), wraps=get_stationary_distributions) as gsd:
            main()
            eig.assert_called()
            gsd.assert_called()
            mc.assert_called()
            generate_method.mock.assert_called_with(10000)
            self.assertEqual(kl.call_count, 5)

if __name__ == '__main__':
    unittest.main()
    
