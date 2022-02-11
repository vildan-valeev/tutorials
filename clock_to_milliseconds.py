"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

"""
import unittest


def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000


class TestOrder(unittest.TestCase):

    def test_descending_order(self):
        self.assertEqual(past(0, 1, 1), 61000)
        self.assertEqual(past(1, 1, 1), 3661000)
        self.assertEqual(past(0, 0, 0), 0)
        self.assertEqual(past(1, 0, 1), 3601000)
        self.assertEqual(past(1, 0, 0), 3600000)

# python -m unittest -v clock_to_milliseconds.py
