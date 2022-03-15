from typing import List

import unittest
import re

"""
Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


# def increment_string(strng):
# """без регулярки"""
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))


def increment_string(strng):
    """C регуляркой"""
    if strng.isalpha():
        strng += '1'
    elif strng.isdigit():
        strng = str(int(strng) + 1).zfill(len(strng))
    elif strng:
        r = re.findall('^(.+\D)(\d+)$', strng)
        word = r[0][0]
        num = r[0][1]
        strng = f'{word}{str(int(num) + 1).zfill(len(num))}'
    return '1' if not strng else strng


class TestSolution(unittest.TestCase):

    def test_increment_string(self):
        """"""
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string(""), "1")
        self.assertEqual(increment_string("1"), "2")
        self.assertEqual(increment_string("tM653TD<99.ciRKa2784864077339"), "tM653TD<99.ciRKa2784864077340")
        self.assertEqual(increment_string("l|(9fkk_|544997sP2p65106249"), "l|(9fkk_|544997sP2p65106250")
        self.assertEqual(increment_string("r1"), "r2")
