#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points
import re
from tmc.utils import load, get_out, patch_name

module_name="src.red_green_blue"
red_green_blue = load(module_name, "red_green_blue")

@points('p02-03.1')
class RedGreenBlue(unittest.TestCase):

    
    def test_size(self):
        result=red_green_blue()
        
        self.assertEqual(len(result), 753)
        for s in result:
            self.assertEqual(len(s.split("\t")), 4, msg=s)

    def test_content(self):
        result=red_green_blue()
        for s in result:
            t=s.split("\t")
            r=int(t[0])
            g=int(t[1])
            b=int(t[2])
            name=t[3]
            self.assertGreaterEqual(r, 0, msg="The value of a component should be in the range [0,255]!")
            self.assertLessEqual(r, 255, msg="The value of a component should be in the range [0,255]!")
            self.assertGreaterEqual(g, 0, msg="The value of a component should be in the range [0,255]!")
            self.assertLessEqual(g, 255, msg="The value of a component should be in the range [0,255]!")
            self.assertGreaterEqual(b, 0, msg="The value of a component should be in the range [0,255]!")
            self.assertLessEqual(b, 255, msg="The value of a component should be in the range [0,255]!")
        t = result[1].split("\t")
        r=int(t[0])
        g=int(t[1])
        b=int(t[2])
        name=t[3]
    
        self.assertEqual(r, 248)
        self.assertEqual(g, 248)
        self.assertEqual(b, 255)
        self.assertEqual(name, "ghost white")


    def test_called(self):
        with patch('builtins.open', side_effect=open) as o,\
             patch(patch_name(module_name, 're.match'), side_effect=re.match) as m,\
             patch(patch_name(module_name, 're.search'), side_effect=re.search) as s,\
             patch(patch_name(module_name, 're.findall'), side_effect=re.findall) as fa,\
             patch(patch_name(module_name, 're.finditer'), side_effect=re.finditer) as fi:
            result=red_green_blue()
            o.assert_called()
            self.assertTrue(m.called or s.called or fa.called or fi.called)

if __name__ == '__main__':
    unittest.main()
    
