# STDLIB
import unittest

# THIRDPARTY
from Task5 import change_dict, change_list


class TestTask5(unittest.TestCase):
    def test_change_list(self):
        self.assertEqual(change_list([1, 2, 3]), [1, 4, 9])
        self.assertRaises(TypeError, change_list("abrakadabra"))

    def test_change_dict(self):
        self.assertEqual(change_dict({"key1": 1, "key2": 2, "key3": 3}), {"key1": 1, "key2": 4, "key3": 9})
        self.assertRaises(TypeError, change_dict([1, 2, 3]))
