import unittest

"""
Your task is to make a function that can take any non-negative integer as an argument
and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.
"""


def descending_order(num: int) -> int:
    """42145 -> 54421"""
    # tmp = list(map(int, list(str(num))))
    # tmp.sort(reverse=True)
    # return int(''.join(map(str, tmp)))
    return int("".join(sorted(str(num), reverse=True)))


class TestOrder(unittest.TestCase):

    def test_descending_order(self):
        self.assertEqual(descending_order(42145), 54421)
        self.assertEqual(descending_order(145263), 654321)
        self.assertEqual(descending_order(123456789), 987654321)


# python -m unittest -v descending_order.py


