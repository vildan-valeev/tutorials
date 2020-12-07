from collections import namedtuple

Person = namedtuple('Person', 'name age')

jake = Person(name='Jake', age=22)

print(jake)
print(jake.name, jake.age)
jake._replace(name='JAKE')

print(jake)
print(type(Person))