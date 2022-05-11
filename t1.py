from collections import namedtuple


City = namedtuple('City', 'name population')

c1 = City('Bratislava', 432000)
c2 = City('Budapest', 1759000)

print(c1, c1.name)
print(c2)
