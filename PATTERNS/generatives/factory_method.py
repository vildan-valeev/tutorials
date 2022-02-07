# Фабричный метод.
# В каких случаях?
# 1. Если классу заранее неизвестно объекты каких классов ему придется создавать
# 2. Объекты, создаваемые классом должны специфицироваться его производными классами
# 3. Базовый класс, делегирует свои обязанности одному из производных, и эти данные необходимо инкапсулировать
#
# Достоинства:
# 1. позволяет избежать привязки к конкретным классам продуктов;
# 2. Выделить весь код для создания продуктов в одно место(классб модель). 3.
# Недостатки:
# 1. Если большое количество продуктов, то создается большое количество параллельных иерархий классов

from enum import Enum


class PizzaType(Enum):
    """
    Перечисление текущих рецептов пицц в пиццерии, которые можно приготовить.
    """
    MARGARITA = 0,
    MEXICO = 1,
    STELLA = 2,


class Pizza:
    def __init__(self, price: float):
        self.__price = price

    def get_price(self):
        return self.__price


class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(3.5)


class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(17.5)


class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(5.5)


def create_pizza(pizza_type: PizzaType) -> Pizza:
    factory_dict = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.MEXICO: PizzaMexico,
        PizzaType.STELLA: PizzaStella,
    }
    return factory_dict[pizza_type]()


if __name__ == "__main__":
    for pizza in PizzaType:
        my_pizza = create_pizza(pizza)
        print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')
