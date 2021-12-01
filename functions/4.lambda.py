add = lambda x, y: x + y
print(add(5,3))

# сортировка по произвоьному ключу
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x: x[1]))
