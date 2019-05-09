#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_out

module_name="src.file_extensions"
file_extensions = load(module_name, "file_extensions")
main = load(module_name, "main")

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

class FileExtensions(unittest.TestCase):

    @points('p02-07.1')
    def test_first(self):
        correct_d = {'txt': ['file1.txt', 'file2.txt'],
                     'pdf': ['mydocument.pdf'],
                     'gz': ['archive.tar.gz']}
        no_extension, d = file_extensions(get_path("filenames.txt"))
        self.assertEqual(no_extension, ["test"],
                         msg="There should be exactly one filename without an extension!")
        self.assertEqual(d, correct_d, msg="The dictionary of files with an extension is incorrect!")

    @points('p02-07.1')
    def test_calls(self):
        with patch('builtins.open', side_effect=open) as o:
            file_extensions(get_path("filenames.txt"))
            o.assert_called_once()

    @points('p02-07.2')
    def test_main(self):
        with patch('src.file_extensions.file_extensions', side_effect=[([], {})]) as fe:
            main()
            self.assertEqual(fe.call_count, 1,
                             msg="You should call function 'file_extensions' from main!")
            result = get_out().split('\n')
            self.assertEqual(len(result), 1, msg="Expected one line of output!")
            self.assertEqual(result[0], "0 files with no extension")

if __name__ == '__main__':
    unittest.main()
    
