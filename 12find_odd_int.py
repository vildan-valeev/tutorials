"""
По заданному массиву найдите целое число, которое встречается нечетное количество раз.

Всегда будет только одно целое число, которое встречается нечетное количество раз.

"""

seq = [20, 1, 1, 2, 2, 3, 3, 5, 5, 1, 2, 4, 20, 4, 1, 2, 5]


# def find_it(seq):
#     b = {}
#     for i in seq:
#         if i in b:
#             b[i] += 1
#         else:
#             b[i] = 1
#
#     for odd in b:
#         if b[odd] % 2 != 0:
#             return odd
#         else:
#             'None'


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_it(seq))
