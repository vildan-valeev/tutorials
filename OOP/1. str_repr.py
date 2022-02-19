# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#
#     def __str__(self):
#         return f'{self.color} автомобиль'
#
#     # def __repr__(self):
#     #     return f'{self.__class__.__name__}({self.color!r} {self.mileage!r})'
#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.color!r} {self.mileage!r})'
#
# my_car = Car('красный', 345)
#
# print(my_car)
# print(repr(my_car))


class ReCheck:
    version_re = '22'
    date_re = '(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-(?:20[12345][0-9])'

    def __init__(self):
        self.version_re = '33'



