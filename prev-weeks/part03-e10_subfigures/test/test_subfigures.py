#!/usr/bin/env python3

import unittest
from unittest.mock import patch, Mock, DEFAULT
import numpy as np
import matplotlib.pyplot as plt

from tmc import points

from tmc.utils import load, get_out, patch_name

module_name="src.subfigures"
subfigures = load(module_name, "subfigures")

def mysubplots(*arg, **kwarg):
    return Mock(), (Mock(), Mock())

class MockSubplots(object):

    def __call__(self, *x, **kw):
        self.fig = Mock()
        shape = x[:2]
        if shape[0] == 1 or shape[1] == 1:
            n = max(shape)
            self.ax = np.array([Mock() for _ in range(n)])
        else:
            self.ax = np.empty(shape, dtype=Mock)
            for (r,c), x in np.ndenumerate(self.ax):
                self.ax[r,c] = Mock()
        return self.fig, self.ax
        
@points('p03-10.1')
class Subplots(unittest.TestCase):

    
    def test_calls(self):
        n = 10
        a = np.random.randint(0, 10, (n, 3))
        a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)

        with patch(patch_name(module_name, "plt.show")) as pshow:
            with patch(patch_name(module_name, "plt.subplots"), side_effect=plt.subplots) as psubplots:
                subfigures(a)
                pshow.assert_called_once()
                psubplots.assert_called_once()
                self.assertEqual(psubplots.call_args[0][:2], (1,2), msg="Wrong shape of subplot grid")


    def test_method_calls(self):
        n = 10
        a = np.random.randint(0, 10, (n, 3))
        a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)

        mysub = MockSubplots()
        with patch(patch_name(module_name, "plt.show")) as pshow:
            with patch(patch_name(module_name, "plt.subplots"), side_effect=mysub) as psubplots:
                subfigures(a)
                pshow.assert_called_once()
                psubplots.assert_called_once()
                self.assertEqual(psubplots.call_args[0][:2], (1,2), msg="Wrong shape of subplot grid")
                mysub.ax[0].plot.assert_called_once()
                mysub.ax[1].scatter.assert_called_once()
                np.testing.assert_array_equal(mysub.ax[0].plot.call_args[0][0], a[:,0])
                np.testing.assert_array_equal(mysub.ax[0].plot.call_args[0][1], a[:,1])
                positional = mysub.ax[1].scatter.call_args[0]
                kwargs = mysub.ax[1].scatter.call_args[1]
                if len(positional) >= 2:
                    np.testing.assert_array_equal(positional[0], a[:,0],
                                                  err_msg="x-coordinates were not correct for scatter call!")
                    np.testing.assert_array_equal(positional[1], a[:,1],
                                                  err_msg="y-coordinates were not correct for scatter call!")
                elif "x" in kwargs and "y" in kwargs:
                    np.testing.assert_array_equal(kwargs["x"], a[:,0],
                                                  err_msg="x-coordinates were not correct for scatter call!")
                    np.testing.assert_array_equal(kwargs["y"], a[:,1],
                                                  err_msg="y-coordinates were not correct for scatter call!")
                else:
                    self.assertTrue(False, msg="Give x and y for scatter call as position "
                                    "either as positional arguments or as keyword arguments!")

                self.assertIn("c", kwargs, msg="Give the 'c' keyword argument to scatter method call!")
                np.testing.assert_array_equal(kwargs["c"], a[:,2],
                                              err_msg="You did not give correct values to the 'c' parameter of the scatter function")
                self.assertIn("s", kwargs, msg="Give the 's' keyword argument to scatter method call!")
                np.testing.assert_array_equal(kwargs["s"], a[:,3],
                                              err_msg="You did not give correct values to the 's' parameter of the scatter function")


    # def test_calls2(self):
    #     n = 10
    #     a = np.random.randint(0, 10, (n, 3))
    #     a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)
    #     with patch.multiple("src.subplots.plt",
    #                         show=DEFAULT, subplots=DEFAULT) as mocks:
    #         subfigures(a)
    #         mocks["show"].assert_called_once()



if __name__ == '__main__':
    unittest.main()
    
