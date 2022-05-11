from typing import List

import unittest

"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal 
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must 
be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

"""


def rgb(r, g, b):
    def check(a):
        if a < 0:
            return 0
        elif a > 255:
            return 255
        else:
            return a
    return f"{check(r):02x}{check(g):02x}{check(b):02x}".upper()


class TestRGB(unittest.TestCase):

    def test_rgb(self):
        """"""

        self.assertEqual(rgb(0,0,0),"000000")
        self.assertEqual(rgb(1,2,3),"010203")
        self.assertEqual(rgb(255,255,255), "FFFFFF")
        self.assertEqual(rgb(254,253,252), "FEFDFC")
        self.assertEqual(rgb(-20,275,125), "00FF7D")

# python -m unittest -v rgb_to_hex.py
