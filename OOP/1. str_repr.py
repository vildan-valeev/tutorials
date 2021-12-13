class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'{self.color} автомобиль'

    # def __repr__(self):
    #     return f'{self.__class__.__name__}({self.color!r} {self.mileage!r})'
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r} {self.mileage!r})'

my_car = Car('красный', 345)

print(my_car)
print(repr(my_car))
