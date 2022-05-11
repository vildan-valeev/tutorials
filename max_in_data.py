"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns
the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects,
can be considered as 0.
"""

from typing import List

import unittest

# def cakes(recipe, available):
#     return min(available.get(k, 0)/recipe[k] for k in recipe)


def cakes(recipe, available):
    """Проверка ингридиентов"""
    # проверяем само наличие ингридиентов
    dif = set(recipe).difference(set(available))
    # определяем целое количество по минимальному из значений - это и будет количество cakes
    count = []
    if not dif:
        for i in recipe:
            count.append(available[i] // recipe[i])
    return min(count, default=0)


class TestCake(unittest.TestCase):

    def test_Cake_1(self):
        """Ингридиентов достаточно"""
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEqual(cakes(recipe, available), 2, 'example #1')

    def test_Cake_2(self):
        """Не хватает ингридиентов"""
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        self.assertEqual(cakes(recipe, available), 0, 'example #2')

    def test_Cake_3(self):
        """Не хватает ингридиентов"""
        recipe = {"flour": 500, "sugar": 200, "eggs": 2}
        available = {"flour": 1200, "sugar": 1200, "eggs": 1, "milk": 200}
        self.assertEqual(cakes(recipe, available), 0, 'example #3')

    def test_Cake_4(self):
        """Нету ингридиентов"""
        recipe = {"flour": 500, "sugar": 200, "eggs": 2}
        available = {"flour": 1200, "sugar": 1200, "milk": 200}
        self.assertEqual(cakes(recipe, available), 0, 'example #4')


# python -m unittest -v max_in_data.py
if __name__ == '__main__':
    print(cakes({"flour": 500, "sugar": 200, "eggs": 1},
                {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
