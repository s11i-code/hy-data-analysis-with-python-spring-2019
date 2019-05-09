#!/usr/bin/python3

import unittest

from tmc import points

from tmc.utils import load, get_out

random_event = load('src.random_event', 'random_event')

@points('p07-07.1')
class TestRandomEvent(unittest.TestCase):

    def test_first(self):
        for _ in range(10):
            distribution=dict(zip("ACGT", [0.10, 0.35, 0.15, 0.40]))
            self.assertIn(random_event(distribution), "ACGT")
        
    def test_second(self):
        events="First Second Third Fourth Fifth".split()
        for _ in range(10):
            distribution=dict(zip(events,
                              [0.5, 0.05, 0.20, 0.15, 0.10]))
            self.assertIn(random_event(distribution), events)
        
        

if __name__ == '__main__':
    unittest.main()
    
