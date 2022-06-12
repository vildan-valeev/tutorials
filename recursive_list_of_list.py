"""
Дано: [1, 2, [5], 3, [4, 5, 6, 7, 8, 9, 10, [7, 8, 11]]]
1. Получить из него простой список, убрать дубли ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
2. Оставить только нечетные числа ([1, 3, 5, 7, 9, 11])
3. Сортировка в обратном порядке ([11, 9 ,7, 5, 3, 1])

"""

data = [1, 2, [5], 3, [4, 5, 6, 7, 8, 9, 10, [7, 8, 11]]]


def one(inner) -> list:
    if not inner:
        return inner
    if isinstance(inner[0], list):
        return one(inner[0]) + one(inner[1:])
    return list(set(inner[:1] + one(inner[1:])))


def two(inner) -> list:
    return [i for i in one(inner) if i % 2 != 0]


def three(inner) -> list:
    return sorted([i for i in two(inner)], reverse=True)


print(one(data))

print(two(data))

print(three(data))
