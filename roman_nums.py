"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
Examples

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

"""
import unittest


class RomanNumerals:
    num_from = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    num_to = {

    }
    @staticmethod
    def to_roman(val: int) -> str:
        num_from = __class__.__dict__.get("num_from")
        inv_nums = {v: k for k, v in num_from.items()}
        string_num = str(val)
        result = ''
        for i, s in enumerate(string_num):
            r: str = '0' * len(string_num[i + 1:])  # рядность
            if int(s) == 4:
                result += (inv_nums[int('1' + r)] + inv_nums[int('5' + r)])
            elif int(s) == 9:
                result += (inv_nums[int('1' + r)] + inv_nums[int('1' + r + '0')])
            elif 0 <= int(s) < 4:  # 1 - 3
                result += inv_nums[int('1' + r)] * int(s)
            else:  # 5, 6 - 8
                result += (inv_nums[int('5' + r)] + inv_nums[int('1' + r)] * (int(s) - 5))
        return result

    @staticmethod
    def from_roman(roman_num: str) -> int:
        num_from = __class__.__dict__.get("num_from")
        result = 0
        for i, c in enumerate(roman_num):
            if i + 1 < len(roman_num) and num_from[roman_num[i]] < num_from[roman_num[i + 1]]:
                result -= num_from[roman_num[i]]
            else:
                result += num_from[roman_num[i]]
        return result


class TestSum(unittest.TestCase):

    def test_to(self):
        """"""

        self.assertEqual(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
        self.assertEqual(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
        self.assertEqual(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
        self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
        self.assertEqual(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')

    def test_from(self):

        self.assertEqual(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
        self.assertEqual(RomanNumerals.from_roman('I'), 1, 'I should == 1')
        self.assertEqual(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
        self.assertEqual(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
        self.assertEqual(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')

# python -m unittest -v roman_nums.py

#
# import string
# from collections import OrderedDict
#
#
# class RomanNumerals:
#     @classmethod
#     def to_roman(self, num):
#         conversions = OrderedDict(
#             [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
#              ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)])
#         out = ''
#         for key, value in conversions.iteritems():
#             while num >= value:
#                 out += key
#                 num -= value
#         return out
#
#     @classmethod
#     def from_roman(self, roman):
#         conversions = OrderedDict(
#             [('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9), ('IV', 4), ('M', 1000), ('D', 500),
#              ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)])
#         out = 0
#         for key, value in conversions.iteritems():
#             out += value * roman.count(key)
#             roman = string.replace(roman, key, "")
#         return out

