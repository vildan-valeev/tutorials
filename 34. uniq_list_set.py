"""
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
"""
# print(len(set(map(id, objects))))

objects = [1, 2, 1, 5, True, False, True, 'false', [], [1, 2], [1, 2]]

ans = 0
a = set()
for obj in objects:
    a.add(id(obj))

print(a)
print(len(a))
