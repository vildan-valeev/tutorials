"""Create a function that takes a positive integer and returns the next bigger number that can be formed
by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071

5432 => 5


"""
from itertools import permutations


# def test(n):
#     lst = []
#     for i in permutations(str(n)):
#         lst.append(int(''.join(map(str, i))))
#     c = sorted(lst)
#     print(c)
#     print(c.index(n))
#     print(len(c))
#     if (c.index(n) + 1) == len(c):
#         return c[c.index(n)]
#     else:
#         return c[(c.index(n) + 1)]

# def test(n):
#     lst = sorted([int(''.join(map(str, i))) for i in permutations(str(n))])
#     return lst[(lst.index(n) + 1)] if lst.index(n) != len(lst) else lst[lst.index(n)]


# def test(n):
#     lst = sorted([int(''.join(map(str, i))) for i in permutations(str(n))])
#     if (lst.index(n) + 1) == len(lst):
#         return lst[lst.index(n)]
#     else:
#         return lst[(lst.index(n) + 1)]

def test(n):
    lst = sorted([int(''.join(map(str, i))) for i in permutations(str(n))])
    return lst[(lst.index(n) + 1)] if lst.index(n) != len(lst) else lst[lst.index(n)]

print(test(12))
print(test(513))
print(test(2017))
print(test(5432))
