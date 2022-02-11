"""
Алгоритм падежей при выводе ЦЕЛЫХ чисел от 1 до 99
...рубля
...рублей
...рубль

"""

k = float(input())

if 1 <= k and k.is_integer():
    last = k % 10
    if int(last) == 1 and not k == 11:
        print(f'{int(k)} поездка')
    elif 1 < last < 5 and not 11 < k < 15:
        print(f'{int(k)} поездки')
    else:
        print(f'{int(k)} поездок')
else:
    print('ошибка')

# async def suffix_text(value: int, one_value, some_value, many_value):
#     result = ''
#     if not value:
#         return result
#
#     last = abs(value) % 10
#     if int(last) == 1 and not value == 11:
#         result = f'{int(value)} {one_value}'
#     elif 1 < last < 5 and not 11 < value < 15:
#         result = f'{int(value)} {some_value}'
#     else:
#         result = f'{int(value)} {many_value}'
#
#     if value < 0:
#         result = "-" + result
#     return result