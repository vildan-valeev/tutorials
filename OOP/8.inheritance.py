# python -i 8.inheritance.py


# class Person:
#     def hello(self):
#         print('I am Person')
#
#
# class Student(Person):
#     def hello(self):
#         print('I am Student')
#
# s = Student()


class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}')


class Student(Person):
    pass


s = Student('Ivan')
