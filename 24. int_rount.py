"""Округление чисел"""
import math


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


n = [42, 18, 5, 60, 10, 14, 38]

for i in n:
    x = roundup(i)
    print(x)
