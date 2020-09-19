# x = [1, 2, 3]
# y = x
# y.append(4)
#
# s = "123"
# t = s
# t = t + "4"
#
# print(str(x) + " " + s)

"""
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
"""
objects = [1, 2, 1, 5, True, False, True, 'false', [], [1, 2], [1, 2]]

ans = 0
a = set()
for obj in objects:
    a.add(id(obj))


print(a)
print(len(a))
