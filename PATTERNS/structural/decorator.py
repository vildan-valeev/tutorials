
"""
1. Если имеется необходимость динамически и незаметно для клиентского кода добавлять обязанности к существующим объектам
2. Если нет возможности использовать наследование для расширения функциональности объекта
3. Обязанности накладываемы на объект могут быть с него сняты

Достоинства:
1. Позволяет динамически добавлять как одну, так и несколько обязанностей объекту
2. Предоставляет больше гибкости, по сравнению с наследованием

Недостатки:
1. Разрастается кодовая база проекта из-за наличия большого числа маленьких классов
2. Появляются трудности с конфигурированием многократно оборачиваемых объектов


"""
from abc import ABC, abstractmethod


class IPizzaBase(ABC):
    """Интерфейс декорируемого объекта"""
    @abstractmethod
    def cost(self) -> float:
        pass


class PizzaBase(IPizzaBase):
    """ Класс декорируемого объекта"""
    def __init__(self, cost):
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost


class IDecorator(IPizzaBase):
    """Интерфейс декоратора"""
    @abstractmethod
    def name(self) -> str:
        pass

class PizzaMargarita(IDecorator):

    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Маргарита"

    def cost(self) -> float:
        return self.__cost+self.__wrapped.cost()

    def name(self) -> str:
        return self.__name


class PizzaSalami(IDecorator):

    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Салями"

    def cost(self) -> float:
        return (self.__cost + self.__wrapped.cost())*2

    def name(self) -> str:
        return self.__name


if __name__ == '__main__':
    def print_pizza(pizza: IDecorator) -> None:
        print(f'Стоимость пиццы "{pizza.name()}" = {pizza.cost()}')

    pizza_base = PizzaBase(3.4)
    print(f'Стоимость основы пиццы {pizza_base.cost()}')

    margarita = PizzaMargarita(pizza_base, 10)
    print_pizza(margarita)

    salami = PizzaSalami(pizza_base, 7)
    print_pizza(salami)
