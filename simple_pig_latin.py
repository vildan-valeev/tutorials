from typing import List

import unittest

"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.
"""


def pig_it(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)

    return ' '.join(res)

def ttt(text):
    result = []
    for i in text.split():
        tmp_word = ''
        tmp = ''
        for s in i:
            if s.isalpha() and not tmp:
                tmp = s
            else:
                tmp_word += s
        if i.isalpha():
            result.append(tmp_word + tmp + "ay")
        else:
            result.append(tmp_word + tmp)
    return " ".join(result)


print(ttt('Pig latin is cool !'))

# class TestSum(unittest.TestCase):
#
#     def test_sum(self):
#         """"""
#
#         self.assertEqual(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
#         self.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')
#         self.assertEqual(pig_it('Hi, I am pizza!'), 'iHay, Iay maay izzapay!')

# python -m unittest -v simple_pig_latin.py
