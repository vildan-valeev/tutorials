"""
Итератор Iter

Применение:
1. Необходимо скрыть детали реализации сложной структуры данных от клиента
2. Необходимо предоставить возможность осуществлять обход одной и той же структуры данных несколькими способами
3. Обход различный структур данных должен осуществляться в рамках единого интерфейса

Достоинства:
1. Позволяет организовать различные способы и направления обхода структур данных
2.

Недостаки:
1. Если достаточно цикла for, то его применение не оправдано


"""
# from abc import ABC, abstractmethod
# from typing import List
#
#
# class PizzaItem:
#     def __init__(self, number):
#         self.number = number
#
#     def __str__(self):
#         return f"кусочек пиццы под номером: {self.number}"
#
#
# class Iterator(ABC):
#
#     @abstractmethod
#     def next(self) -> PizzaItem:
#         ...
#
#     @abstractmethod
#     def has_next(self) -> bool:
#         ...
#
#
# class PizzaSliceIterator(Iterator):
#     def __init__(self, pizza: List[PizzaItem]):
#         self._pizza = pizza
#         self._index = 0
#
#     def next(self) -> PizzaItem:
#         pizza_item = self._pizza[self._index]
#         self._index += 1
#         return pizza_item
#
#     def has_next(self) -> bool:
#         return False if self._index >= len(self._pizza) else True
#
#
# class PizzaAggregate:
#     def __init__(self, amount_slices: int = 10):
#         self.slices = [PizzaItem(it + 1) for it in range(amount_slices)]
#         print(f"Приготовили пиццу и порезали на {amount_slices} кусочков")
#
#     def amount_slices(self) -> int:
#         return len(self.slices)
#
#     def iterator(self) -> Iterator:
#         return PizzaSliceIterator(self.slices)
#
#
# if __name__ == '__main__':
#     pizza = PizzaAggregate(5)
#
#     iterator = pizza.iterator()
#
#     while iterator.has_next():
#         item = iterator.next()
#         print("Это" + str(item))
#
#     print("*" * 20)
#
#     iterator = pizza.iterator()
#     iterator.next()
#     while iterator.has_next():
#         item = iterator.next()
#         print("Это" + str(item))


from typing import List
from collections.abc import Iterable, Iterator


class PizzaItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"кусочек пиццы под номером: {self.number}"


class PizzaSliceIterator(Iterator):
    def __init__(self, pizza: List[PizzaItem],
                 reverse: bool = False):
        self._pizza = pizza
        self._index: int = -1 if reverse else 0
        self._reverse = reverse

    def __next__(self) -> PizzaItem:
        try:
            pizza_item = self._pizza[self._index]
            self._index += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return pizza_item


class PizzaAggregate(Iterable):
    def __init__(self, amount_slices: int = 10):
        self._slices = [PizzaItem(it+1) for it in range(amount_slices)]
        print(f"Приготовили пиццу и порезали "
              f"на {amount_slices} кусочков")

    def amount_slices(self) -> int:
        return len(self._slices)

    def __iter__(self) -> PizzaSliceIterator:
        return PizzaSliceIterator(self._slices)

    def get_reverse_iterator(self) -> PizzaSliceIterator:
        return PizzaSliceIterator(self._slices, True)


if __name__ == "__main__":
    pizza = PizzaAggregate(5)
    for item in pizza:
        print("Это " + str(item))
    print("*" * 8 + "Обход в обратную сторону" + "*"*8)
    iterator = pizza.get_reverse_iterator()
    for item in iterator:
        print("Это " + str(item))
