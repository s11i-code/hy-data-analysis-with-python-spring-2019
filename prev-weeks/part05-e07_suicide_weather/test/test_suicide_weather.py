#!/usr/bin/env python3

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from tmc import points

from tmc.utils import load, get_out, patch_helper

module_name="src.suicide_weather"
suicide_weather = load(module_name, "suicide_weather")
suicide_fractions = load(module_name, "suicide_fractions")
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

@points('p05-07.1')
class SuicideWeather(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.tup = suicide_weather()

    def setUp(self):
        self.tup = suicide_weather()

    def test_return_value(self):
        suicide_n, temperature_n, common_n, corr = self.tup
        self.assertEqual(suicide_n, 141, msg="Incorrect size of suicide Series!")
        self.assertEqual(temperature_n, 191, msg="Incorrect size of temperature Series!")
        self.assertEqual(common_n, 108, msg="Incorrect size of common Series!")
        self.assertAlmostEqual(corr, -0.5580402318136322, places=4,
                               msg="Incorrect Spearman correlation!")

    def test_calls(self):
        method = spy_decorator(pd.core.series.Series.corr)
        with patch(ph("suicide_fractions"), wraps=suicide_fractions) as psf,\
             patch(ph("pd.read_html"), wraps=pd.read_html) as phtml,\
             patch.object(pd.core.series.Series, "corr", new=method),\
             patch(ph("suicide_weather"), wraps=suicide_weather) as psw:
            main()
            psf.assert_called_once()
            psw.assert_called_once()
            phtml.assert_called_once()
            method.mock.assert_called()
        out = get_out()
        self.assertRegex(out, r"Suicide DataFrame has \d+ rows",
                         msg="Output line about Suicide was incorrect!")
        self.assertRegex(out, r"Temperature DataFrame has \d+ rows",
                         msg="Output line about Temperature was incorrect!")
        self.assertRegex(out, r"Common DataFrame has \d+ rows",
                         msg="Output line about Common was incorrect!")
        self.assertRegex(out, r"Spearman correlation:\s+[+-]?\d+\.\d+",
                         msg="Output line about correlation was incorrect!")

if __name__ == '__main__':
    unittest.main()

