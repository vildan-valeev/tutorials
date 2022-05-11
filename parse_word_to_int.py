from typing import List

import unittest

"""
n this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

Additional Notes:

    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
    All tested numbers are valid, you don't need to validate them


"""
NUM = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,

    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,

    "hundred": 100,
    "thousand": 1000,
    "million": 1000000

}


def parse_int(s):
    for i in s.split():
        print(NUM[i])
    return 0


parse_int('two hundred forty-six')

# class TestRGB(unittest.TestCase):
#
#     def test_rgb(self):
#         """"""
#
#         self.assertEqual(parse_int('one'), 1)
#         self.assertEqual(parse_int('twenty'), 20)
#         self.assertEqual(parse_int('twenty thousand four'), 20004)
#         self.assertEqual(parse_int('two hundred forty-six'), 246)
#         self.assertEqual(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'), 783919)

# python -m unittest -v parse_word_to_int.py
