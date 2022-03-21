from typing import List

import unittest

"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.
"""


def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0




class TestSum(unittest.TestCase):

    def test_sum(self):
        """"""

        self.assertEqual(sum_array([6, 2, 1, 8, 10]), 16)
        self.assertEqual(sum_array([-6, -20, -1, -10, -12]), -28)
        self.assertEqual(sum_array([6, 0, 1, 10, 10]), 17)
        self.assertEqual(sum_array([-6, 20, -1, 10, -12]), 3)
        self.assertEqual(sum_array([-3, -5]), 0)
        self.assertEqual(sum_array([3, 5]), 0)
        self.assertEqual(sum_array([-3]), 0)
        self.assertEqual(sum_array([3]), 0)
        self.assertEqual(sum_array(None), 0)
        self.assertEqual(sum_array([]), 0)

# python -m unittest -v sum_without_higest_and_lowest.py
