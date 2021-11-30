"""функция make_adder - фабрика для функций суммирования,

захватывает локальное состояние
"""


def make_adder(n):
    def add(x):
        return x + n

    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4))
print(plus_5(4))


### объекты как вызываемы функции

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x, *args, **kwargs):
        return self.n + x

plus_3 = Adder(3)

print(plus_3(4))

print(callable(plus_3))
print(callable(5))