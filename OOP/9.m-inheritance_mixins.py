# Порядок наследования имеет значение

# class Person:
#     def hello(self):
#         print('I am Person')
#
#
# class Student(Person):
#     def hello(self):
#         print('I am Student')
#
#
# class Prof(Person):
#     def hello(self):
#         print('I am Prof')
#
#
# class Someone(Student, Prof):
#     pass
#
#
# s = Someone()


# s.hello()

# s.__class__.mro()

# ---------- Mixins -------------
class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I like {self.food}')


class Person:
    def hello(self):
        print('I am Person')


class Student(FoodMixin, Person):
    food = 'Pizza'

    def hello(self):
        print('I am Student')


s = Student()
