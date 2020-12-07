"""Выбираем самое сладкое"""


class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles

    @staticmethod
    def sweetest_icecream(lst):
        flavor_values = {
            'Plain': 0,
            'Vanilla': 5,
            'ChocolateChip': 5,
            'Strawberry': 10,
            'Chocolate': 10
        }
        max([icecream.sprinkles + flavor_values[icecream.flavor] for icecream in lst])


ice1 = IceCream('Chovcolate', 13)
ice2 = IceCream('Vanilla', 0)
ice3 = IceCream('Strawberry', 7)
ice4 = IceCream('Plain', 18)
ice5 = IceCream('ChocolateChip', 3)

print(IceCream.sweetest_icecream([ice1, ice2, ice3, ice4, ice5, ]))
print(IceCream.sweetest_icecream([ice3, ice1, ]))
print(IceCream.sweetest_icecream([ice3, ice5, ]))
