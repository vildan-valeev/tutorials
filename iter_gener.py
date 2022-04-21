"""
Итератор – более общая концепция, чем генератор.
Генератор – это итератор, но не наоборот. Не любой итератор является генератором.

"""
import time


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# 1.  генератор однострочный
g = (2 * i for i in range(5))
# print(type(g))
# print(next(g))


# 2. генератор в виде функции
def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


# 3. Бесконечный итератор
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater = Repeater("Привет")
for item in repeater:
    print(item)
    time.sleep(1)
