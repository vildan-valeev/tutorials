from typing import List

import unittest

"""
Complete the solution so that it reverses all of the words within the string passed in.
"""


# import re
#
# def solution(s:str):
#     return re.findall(".{2}", s + "_")


def reverse_words(s: str) -> str:
    """
    1. Разъединяем в список - split
    2. Обратный срез от -1
    3. Собираем обратно в строку - join
    """
    # return ' '.join(reversed(str.split(' ')))
    return ' '.join(s.split(' ')[::-1])


class TestReverse(unittest.TestCase):

    def setUp(self) -> None:
        self.tests = (
            ("The greatest victory is that which requires no battle",
             'battle no requires which that is victory greatest The'),
        )

    def test_solition(self):
        """"""
        for s, result in self.tests:
            self.assertEqual(reverse_words(s), result)

# python -m unittest -v reversed_words.py
