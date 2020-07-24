name = 'world'

s = 'hello {}'

result = s.format(name)

print(result)


#-----2-------


name = 'LEON'
number = '100'

pattern = '{} - {}'

result = '{} - {}'.format(name, number)

print(result)

#-----3-------

name = 'LEON'
number = '100'

pattern = '{movie} - {rating}'

result = pattern.format(movie=name, rating=number)

print(result)

#-----4-------

name = 'LEON'
number = '100'


result = f'{name} - {number}'

print(result)

