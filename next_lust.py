"""
Вводить next или lust.

"""

a = [1, 2, 3, 4]
index = -len(a)
count = 1

item = a[index]
print(index)
# показываем первую


print(f'объект по индексу = {item}/{len(a)}\n'
      f'счетчик           = {count}/{len(a)}')

while True:
    inp = input()
    if inp == 'next':
        if index >= -1:
            index = -len(a)
            count = 1
        else:
            index += 1
            count += 1
    elif inp == 'last':
        if index <= -len(a):
            index = -1
            count = len(a)
        else:
            index -= 1
            count -= 1
    else:
        print('Ошибка')

    print('index', index)
    item = a[index]
    print(f'объект по индексу = {item}/{len(a)}\n'
          f'счетчик           = {count}/{len(a)}')
