name = 'world'
s = 'hello {}'
result = s.format(name)
print('1', result)

# -----2-------
name = 'LEON'
number = '100'
pattern = '{} - {}'
result = '{} - {}'.format(name, number)
print('2', result)

# -----3-------
name = 'LEON'
number = '100'
patt = '{movie} - {rating}'
result = patt.format(movie=name, rating=number)
print('3', result)

# -----4-------
name = 'LEON'
number = '100'
result = f'{name} - {number}'
print('4', result)

# -----5-------
from string import Template

t = Template('$name - $number')
name = 'LEON'
number = '100'
result = t.substitute(name=name, number=number)
print('5', result)


#  --- Hack test ----
secret = 'secret'
class Hack:
    def __init__(self):
        pass


hack = Hack()
user_input = '{error.__init__.__globals__[secret]}'
print(user_input.format(error=hack))


user_input = '${error.__init__.__globals__[secret]}'
print(Template(user_input).substitute(error=hack))

"""если форматирующие строки поступают от польователей, то использовать шаблонные строки, чтобы избежать 
проблем с безопасностью!!!
В других случаях - интерполяция литеральных строк (f'{}')
"""