from random import randint

x = []
# сгенерируем массив список
while len(x) < 10:
    z = randint(1, 10)
    if z not in x:
        x.append(z)
    # print(z, x)

print(x)

# удалим любой элемент из списка
index = randint(0, 9)
print(f'Удалим число - {x[index]}')
print(f'-----\n')
x.pop(index)
print(f'Найти недостающее число из массива от 1 до 10 \n{x}')

a_1 = 1
a_n = 10
n = 10

S = (a_1 + a_n) / 2 * n

print(S - sum(x))
