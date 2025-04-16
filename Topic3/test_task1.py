# STDLIB
import unittest

# THIRDPARTY
from Task1 import mean_list


class TestTask1(unittest.TestCase):
    def test_mean_list(self):
        self.assertEqual(mean_list([1, 2, 3]), "Среднее арифметическое: 2.0")
