# class MoneyBox:
#     def __init__(self, capacity=0):
#         self.capacity = capacity
#         self.counter = 0
#         # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         if self.counter + v <= self.capacity:
#             return True
#         else:
#             return False
#         # True, если можно добавить v монет, False иначе
#
#     def add(self, v):
#         if self.can_add(v):
#             self.counter += v
#         # положить v монет в копилку


# x = MoneyBox(15)
# x.add(5)
# print(x.counter, x.capacity)
# x.add(9)
# print(x.counter, x.capacity)
# x.add(3)
# print(x.counter, x.capacity)
# x.add(5)
# print(x.counter, x.capacity)


# class Buffer:
#
#     def __init__(self):
#         self.lst = []
#
#     def add(self, *a):
#         self.lst.extend(a)
#         while len(self.lst) - 5 >= 0:
#             print(sum(self.lst[0:5]))
#             self.lst = self.lst[5:]
#
#     def get_current_part(self):
#         return self.lst
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# print(buf.get_current_part())
# print(buf.add(4, 5, 6))
# print(buf.get_current_part())
# print(buf.add(7, 8, 9, 10))
# print(buf.get_current_part())
# print(buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
# print(buf.get_current_part())
#
# from datetime import datetime
#
# time = '31.11.2020 23:59'
# c = lambda time: datetime.strptime(time, '%d.%m.%Y %H:%M')
# print(c)

text = '123456789'


c = text[:5]
print(c)
