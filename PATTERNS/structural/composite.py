"""
Компоновщик

В каких случаях?
1. Объект может быть структурирован в виде дерева
2. В клиентском коде необходимо единообразно трактовать как составные, так и индивидуальные объекты

Достоинства:
Позволяет определять иерархии классов, в состав которых входят примитивные и составные объекты.
Упрощает архитектуру клиента и облегчает добавление новых видов компонентов

Недостатки:
слишком общий интерфейс классов

"""

from abc import ABC, abstractmethod


class IProduct(ABC):
    """
    Интерфейс продуктов входящих в пиццу
    """

    def cost(self) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Product(IProduct):
    """Класс продукта"""

    def __init__(self, name: str, cost: float):
        self.__cost = cost
        self.__name = name

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class CompountProduct(IProduct):
    """
    Класс компонуемый продукт
    """

    def __init__(self, name: str):
        self.__name = name
        self.product = []

    def cost(self):
        cost = 0
        for it in self.product:
            cost += it.cost()
        return cost

    def name(self) -> str:
        return self.__name

    def add_product(self, product: IProduct):
        self.product.append(product)

    def remove_product(self, product: IProduct):
        self.product.remove(product)

    def clear(self):
        self.product = []


class Pizza(CompountProduct):
    def __init__(self, name: str):
        super().__init__(name)

    def cost(self):
        cost = 0
        for it in self.product:
            cost_it = it.cost()
            print(f'Стоимость "{it.name()}" = {cost_it} тугриков')
            cost += cost_it
        print(f'Стоимость "{self.name()}" = {cost} тугриков')
        return cost


if __name__ == '__main__':
    dough = CompountProduct('тесто')
    dough.add_product(Product('мука', 3))
    dough.add_product(Product('яйцо', 2.3))
    dough.add_product(Product('соль', 1))
    dough.add_product(Product('соль', 1))

    sauce = Product('барбекю', 12.1)

    topping = CompountProduct('топпинг')
    topping.add_product(Product('Дор блю', 14))
    topping.add_product(Product('Пармезан', 12.3))
    topping.add_product(Product('Моцарелла', 9.54))
    topping.add_product(Product('Маасдам', 7.27))

    pizza = Pizza('4 сыра')
    pizza.add_product(dough)
    pizza.add_product(sauce)
    pizza.add_product(topping)
    print(pizza.cost())

