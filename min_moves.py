from typing import List

import unittest

"""
Minimum number of moves

There're two list:

    [5, 1, 3, 2, 4]
    [4, 5, 2, 1, 3]

Your goal is to change the first list to the second list

Each modification consists of choosing a single number and moving it some number of positions to the left.

Your task is to write a function min_move, which has 2 argument a and b(list) and calculate the minimum moves to change
 the first list to the second list.
 
 1, 3, 5, 2, 4
--> 1, 3, 4, 5, 2  # The position of 4 is changed
--> 1, 2, 3, 4, 5  # The position of 2 is changed, and now it's in correct order.
"""


def min_move(a, b):
    """Сортировка вставками - с конца"""
    counter = 0
    n = len(a)
    for i in range(n - 1, -1, -1):
        print(i, a[i], b[i], a, b)

    return counter


# def min_move(a):
#     counter = 0
#     for i in range(len(a)):
#         cursor = a[i]
#         pos = i
#
#         while pos > 0 and a[pos - 1] > cursor:
#             # Меняем местами число, продвигая по списку
#             a[pos] = a[pos - 1]
#             pos = pos - 1
#             counter +=1
#         # Остановимся и сделаем последний обмен
#         a[pos] = cursor
#     print(counter)
#     return a


min_move([1, 3, 5, 2, 4], [1, 2, 3, 4, 5])
# min_move([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# min_move([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
#
# class TestSolution(unittest.TestCase):
#
#     def test_move_zeros(self):
#         """"""
#
#         self.assertEqual(min_move([1, 3, 5, 2, 4], [1, 2, 3, 4, 5]), 2)
#         self.assertEqual(min_move([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 0)
#         self.assertEqual(min_move([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), 4)

# python -m unittest -v min_moves.py
