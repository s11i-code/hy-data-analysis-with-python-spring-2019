#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import re
from tmc import points

from tmc.utils import load, get_out, patch_name

module_name="src.file_listing"
file_listing = load(module_name, "file_listing")

@points('p02-02.1')
class FileListing(unittest.TestCase):

    
    def test_size(self):
        result=file_listing()
        self.assertEqual(len(result), 47)

        for t in result:
            self.assertEqual(len(t), 6)

    def test_content(self):
        result=file_listing()
        for t in result:
            self.assertIsInstance(t[0], int)
            self.assertIsInstance(t[1], str)
            self.assertIsInstance(t[2], int)
            self.assertIsInstance(t[3], int)
            self.assertIsInstance(t[4], int)
            self.assertIsInstance(t[5], str)

            self.assertTrue(t[1] in "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())

            self.assertTrue(t[2] in range(1,32))
            self.assertTrue(t[3] in range(0,24))
            self.assertTrue(t[3] in range(0,60))



    def test_called(self):
        with patch('builtins.open', side_effect=open) as o,\
             patch(patch_name(module_name, 're.compile'), side_effect=re.compile) as c,\
             patch(patch_name(module_name, 're.match'), side_effect=re.match) as m,\
             patch(patch_name(module_name, 're.search'), side_effect=re.search) as s,\
             patch(patch_name(module_name, 're.findall'), side_effect=re.findall) as fa,\
             patch(patch_name(module_name, 're.finditer'), side_effect=re.finditer) as fi:
            result=file_listing()
            o.assert_called()
            self.assertTrue(c.called or m.called or s.called or fa.called or fi.called,
                            msg="Expected that one of the following was called: "
                            "re.search, re.findall, re.finditer!")


if __name__ == '__main__':
    unittest.main()
    
