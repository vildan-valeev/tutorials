from typing import List

import unittest

"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character
of the final pair with an underscore ('_').
"""

# import re
#
# def solution(s:str):
#     return re.findall(".{2}", s + "_")


def solution(s:str) -> List[str]:
    """ """
    n = 2
    return [s[i:i + n] if len(s[i:i + n]) == n else s[i:i + n] + '_' for i in range(0, len(s), n)]


class TestAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.tests = (
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
        )

    def test_solition(self):
        """"""
        for s, result in self.tests:
            self.assertEqual(solution(s), result)

# python -m unittest -v split_strings.py
