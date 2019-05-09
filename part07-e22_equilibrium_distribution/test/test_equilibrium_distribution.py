#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock

import numpy as np

from tmc import points
from tmc.utils import load, get_out, patch_helper

module_name="src.equilibrium_distribution"
equilibrium_distribution = load(module_name, "equilibrium_distribution")
main = load(module_name, "main")
MarkovChain = load(module_name, "MarkovChain")
kullback_leibler = load(module_name, "kullback_leibler")
get_stationary_distributions = load(module_name, "get_stationary_distributions")
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

@points('p07-22.1')
class EquilibriumDistribution(unittest.TestCase):

    def test_correctness(self):
        transition=np.array([[0.3, 0.1, 0.5, 0.1],
                             [0.2, 0.3, 0.15, 0.35],
                             [0.25, 0.15, 0.2, 0.4],
                             [0.35, 0.2, 0.4, 0.05]])
        distributions = get_stationary_distributions(transition)
        np.testing.assert_allclose(distributions[0], [0.27803345, 0.17353238, 0.32035021, 0.22808396], atol=1e-04)

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
            self.assertEqual(mc.call_count, 2)
            generate_method.mock.assert_called_with(10000)
            self.assertEqual(kl.call_count, 10)


if __name__ == '__main__':
    unittest.main()
    
