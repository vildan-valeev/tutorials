"""
Алгоритм падежей при выводе ЦЕЛЫХ чисел от 1 до 99
...рубля
...рублей
...рубль

"""

k = float(input())

if 1 <= k <= 99 and k.is_integer():
    last = k % 10
    if int(last) == 1 and not k == 11:
        print(f'{int(k)} рубль')
    elif 1 < last < 5 and not 11 < k < 15:
        print(f'{int(k)} рубля')
    else:
        print(f'{int(k)} рублей')
else:
    print('ошибка')

