"""
Прототип - позволяет копировать объекты не обращая внимания на детали ее реализации
В каких случаях?
1. код не должен зависеть от классов копируемых объектов
2. Необходимо избежать иерархии классов или фабрик, а также параллельных иерархий классов продуктов
3. Необходимо избежать множества производных классов, которые отличаются друг от друга начальным значением их атрибутов
4.

ДостоинстваЖ
1. клонирование объектов без привязки к их конкретным классам
2. Ускорение создания объектов и уменьшение повторяющегося кода при инициализации объектов
Неодстатки
1. Сложно осуществить процесс клонирования составных объектов, имеющих ссылки на другие объекты
"""
from abc import ABC, abstractmethod
from typing import List
import copy
from builder import (PizzaSauceType,
                     PizzaBase,
                     PizzaDoughDepth,
                     PizzaDoughType,
                     PizzaTopLevelType)


class IPrototype(ABC):
    @abstractmethod
    def clone(self): pass


"""
Класс компонуемого продукта
"""


class Pizza(IPrototype):
    def __init__(self,
                 name,
                 dough: PizzaBase = PizzaBase(PizzaDoughDepth.THICK,
                                              PizzaDoughType.WHEAT),
                 sauce: PizzaSauceType = PizzaSauceType.TOMATO,
                 topping: List[PizzaTopLevelType] = None,
                 cooking_time: int = 10
                 ):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.cooking_time = cooking_time  # in minute

    def __str__(self):
        info: str = f"Pizza name: {self.name} \n" \
                    f"dough type: {self.dough.DoughDepth.name} & " \
                    f"{self.dough.DoughType.name}\n" \
                    f"sauce type: {self.sauce} \n" \
                    f"topping: {[it.name for it in self.topping] if self.topping is not None else 'None'} \n" \
                    f"cooking time: {self.cooking_time} minutes\n" \
                    f"-----------------------------------------"

        return info

    def clone(self):
        topping = self.topping.copy() if self.topping is not None else None
        return type(self)(
            self.name,
            self.dough,
            self.sauce,
            topping,
            self.cooking_time
        )


if __name__ == "__main__":
    pizza = Pizza("Margarita", topping=[PizzaTopLevelType.MOZZARELLA,
                                        PizzaTopLevelType.MOZZARELLA,
                                        PizzaTopLevelType.BACON])

    print(pizza)
    new_pizza = pizza.clone()  # клонируем объект
    new_pizza.name = "New_Margarita"
    print(new_pizza)
    salami_pizza = copy.deepcopy(new_pizza)
    salami_pizza.name = "Salami"
    salami_pizza.sauce = PizzaSauceType.BARBEQUE
    salami_pizza.topping.append(PizzaTopLevelType.SALAMI)
    print(salami_pizza)
