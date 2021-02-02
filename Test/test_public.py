import unittest

import Resource.directory_reader as d_r


class TestF(unittest.TestCase):
    def test_DirReader(self):
        for file in d_r.DirReader("test"):
            self.assertEqual(file, "Test"+"\\test.txt")
