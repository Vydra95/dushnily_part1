# STDLIB
import unittest

# THIRDPARTY
from Task2 import find_evens


class TestTask2(unittest.TestCase):
    def test_find_evens(self):
        self.assertEqual(find_evens(1, 5), [2, 4])
        self.assertRaises(TypeError, find_evens("love", 100))
