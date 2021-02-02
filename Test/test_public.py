import sys
import unittest
from Resource.directory_reader import DirReader


class TestF(unittest.TestCase):
    def test_DirReader(self):
        for file in DirReader("Test"):
            self.assertEqual(file, "Test" + "\\test.txt")
