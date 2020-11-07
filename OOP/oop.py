# class Restaurant():
#     """Ресторан"""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         """Инициализируем атрибуты - имя и возраст"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """Описание ресторана"""
#         print(self.restaurant_name, ', ', self.cuisine_type)
#
#     def open_restaurant(self):
#         """Сообщение об открытии ресотарана"""
#         print(f"Ресторан {self.restaurant_name.title()} открыт")
#
#
# r1 = Restaurant('H2O', 'кафе')
# r2 = Restaurant('McD', 'макдак')
#
# r1.describe_restaurant()
# r2.describe_restaurant()

class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()

b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)