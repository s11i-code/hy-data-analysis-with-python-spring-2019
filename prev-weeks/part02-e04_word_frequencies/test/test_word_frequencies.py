#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_out

module_name="src.word_frequencies"
word_frequencies = load(module_name, "word_frequencies")

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

@points('p02-04.1')
class WordFrequencies(unittest.TestCase):

    
    def test_first(self):
        d = word_frequencies(get_path("alice.txt"))
        self.assertEqual(d['creating'], 3)
        self.assertEqual(d['Carroll'], 3)
        self.assertEqual(d['sleepy'], 2)
        self.assertEqual(d['Rabbit'], 28)
        self.assertEqual(len(d), 2580)

    def test_calls(self):
        with patch('builtins.open', wraps=open) as o:
            d = word_frequencies(get_path("alice.txt"))
            o.assert_called()
            
if __name__ == '__main__':
    unittest.main()
    
