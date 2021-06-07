# class Person:
#     def __init__(self, name):
#         self.name =name
#
#
# class Student(Person):
#     def __init__(self, surname, name):
#         super().__init__(name)
#         self.surname = surname
#
# s = Student('Ivanov', 'Ivan')


class Person:
    def hello(self):
        print(f'Bound with {self}')


class Student(Person):
    def hello(self):
        print('Student obj.hello() is called')
        super().hello()


s = Student()
print(s.hello())
