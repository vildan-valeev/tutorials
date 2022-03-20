from typing import List

import unittest

"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""


# def move_zeros(array):
#     return sorted(array, key=lambda x: x==0 and type(x) is not bool)


def move_zeros(array):
    x = [i for i in array if i != 0]
    return x + [0] * (len(array) - len(x))


# move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])

class TestSolution(unittest.TestCase):

    def test_move_zeros(self):
        """"""

        self.assertEqual(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros(
            [0, 0]),
            [0, 0])
        self.assertEqual(move_zeros(
            [0]),
            [0])
        self.assertEqual(move_zeros(
            []),
            [])

# python -m unittest -v moving_zeros_to_the_end.py
