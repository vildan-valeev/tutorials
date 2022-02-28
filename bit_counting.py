from typing import List

import unittest

"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary 
representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

"""


# import re
#
# def solution(s:str):
#     return re.findall(".{2}", s + "_")


def count_bits(n: int) -> int:
    """ """
    # return sum([int(x) for x in f'{n:b}'])
    # return f'{n:b}'.count('1')
    return bin(n).count("1")


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.tests = (
            (0, 0),
            (4, 1),
            (7, 3),
            (9, 2),
            (10, 2),
        )

    def test_scount_bitsn(self):
        """"""
        for n, result in self.tests:
            self.assertEqual(count_bits(n), result)

# python -m unittest -v bit_counting.py
