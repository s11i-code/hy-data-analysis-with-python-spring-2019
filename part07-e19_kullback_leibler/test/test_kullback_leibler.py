#!/usr/bin/python3

import unittest


from tmc import points

from tmc.utils import load, get_out

kullback_leibler = load('src.kullback_leibler', 'kullback_leibler')

@points('p07-19.1')
class TestKullbackLeibler(unittest.TestCase):

    
    def test_first(self):
        p = dict(zip("ACGT", [0.25]*4))
        self.assertAlmostEqual(kullback_leibler(p, p), 0.0, places=3)

    def test_second(self):
        p = dict(zip("ACGT", [1.0, 0.0, 0.0, 0.0]))
        q = dict(zip("ACGT", [0.25]*4))
        self.assertAlmostEqual(kullback_leibler(p, q), 2.0, places=3)

    def test_exception(self):
        p = dict(zip("ACGT", [1.0, 0.0, 0.0, 0.0]))
        q = dict(zip("ACGT", [0.25]*4))
        #self.assertAlmostEqual(kullback_leibler(q, p), 2.0, places=3)
        self.assertRaises(ZeroDivisionError, kullback_leibler, q, p)

    def test_single(self):
        p = { "A" : 1.0 }
        self.assertAlmostEqual(kullback_leibler(p, p), 0.0, places=3)
        

if __name__ == '__main__':
    unittest.main()
    
