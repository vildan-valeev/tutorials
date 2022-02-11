"""
Позиционные аргументы
"""


def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res


print(s(1, b=2))
print(s(1, 5,55,555, b=2))