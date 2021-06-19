# from typing import Union
#
#
# def normalize_price(income: Union[float, int, str]) -> str:
#     # если str, то переводим в float и делаем дальнейшие проверки
#     if isinstance(income, str):
#         income = float(income)
#     # если без точки
#     if isinstance(income, int):
#         return str(abs(income))
#     # если с точкой
#     if isinstance(income, float):
#         # является ли float целым
#         if float.is_integer(income):
#             return str(abs(int(income)))
#         else:
#             # сколько чисел после запятой- если больше двух то оставляем как есть
#             if len(str(income).split('.')[1]) <= 2:
#                 return f'{abs(income):.2f}'
#             return str(abs(income))
#
#
# test = [100.0, 12.345, 12.34500000, 12.3, -12.23, 10, -100.000, -12.345, -65.0, -75, '10', '12.345']
# for i in test:
#     print(normalize_price(i))

def normalize_price(income):
    # если str, то переводим в float и делаем дальнейшие проверки
    if isinstance(income, str):
        # print('это строка')
        income = float(income)
    # если без точки
    if isinstance(income, int):
        # print('это целое число')
        return str(income)
    # если с точкой
    if isinstance(income, float):
        # является ли float целым
        # print('это вещественное число')
        if float.is_integer(income):
            return str(int(income))
        else:
            # сколько чисел после запятой- если больше двух то оставляем как есть
            if len(str(income).split('.')[1]) <= 2:
                return f'{income:.2f}'
            return str(income)


test = [100.0, 12.345, 12.34599999999900000, 12.3, 12.23, 10, -100.000, -12.345, -65.0, -75, '10', '12.345']
for i in test:
    print(normalize_price(i))

print(normalize_price('123'))