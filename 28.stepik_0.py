from math import sqrt, exp, sin, log, cos, acos, degrees

# x_a = float(input("x_a = "))
#
# y_a = float(input("y_a = "))
#
# x_b = float(input("x_b = "))
#
# y_b = float(input("y_b = "))
#
# x_c = float(input("x_c = "))
#
# y_c = float(input("y_c = "))


# def compute_len(x_0, y_0, x_1, y_1):
#     len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
#     return len_line
#
#
# # Площадь
# def compute_area(a_1, a_2, a_3):
#     p = (a_1 + a_2 + a_3) / 2
#     area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
#     return area
#
#
# # вычисление угла треугольниа
# def compute_angle(a_1, a_2, a_3):
#     angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2) /
#                      (2 * a_1 * a_2))
#
#     return degrees(angle_rad)
#
#
# # Длина строны AB
# c = compute_len(x_a, y_a, x_b, y_b)
# # Длина строны BC
# a = compute_len(x_b, y_b, x_c, y_c)
# # Длина строны AC
# b = compute_len(x_a, y_a, x_c, y_c)
#
# # Периметр
# p = a + b + c
#
# if a + b <= c or b + c <= a or a + c <= b:
#     print("Треугольник не существует")
# else:
#     s = compute_area(a, b, c)
#     # Периметр
#     p = a + b + c
#
#     angle_A = compute_angle(c, b, a)
#     angle_B = compute_angle(c, a, b)
#     angle_C = compute_angle(a, b, c)
#
#     print("Стороны : ", round(a, 3), round(b, 3), round(c, 3))
#
#     print("Площадь : ", round(s, 3))
#
#     print("Периметр : ", round(p, 3))
#
#     print("Углы : ", round(angle_A, 3), round(angle_B, 3), round(angle_C, 3))


#
# x_a = float(input("x_a = "))
#
# y_a = float(input("y_a = "))
#
# x_b = float(input("x_b = "))
#
# y_b = float(input("y_b = "))
#
# x_c = float(input("x_c = "))
#
# y_c = float(input("y_c = "))
#
#
# def compute_len(x_0, y_0, x_1, y_1):
#     len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
#     return len_line
#
#
# # Площадь
# def compute_area(a_1, a_2, a_3):
#     p = (a_1 + a_2 + a_3) / 2
#     area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
#     return area
#
#
# # Длина строны AB
# c = compute_len(x_a, y_a, x_b, y_b)
# # Длина строны BC
# a = compute_len(x_b, y_b, x_c, y_c)
# # Длина строны AC
# b = compute_len(x_a, y_a, x_c, y_c)
#
#
# # радиус вписанной окружности
# def r_in(a_1, a_2, a_3):
#     p = a + b + c
#     r = sqrt((p / 2 - a_1) * (p / 2 - a_2) * (p / 2 - a_3) / (p / 2))
#     return r
#
#
# # радиус описанной окружности
# def r_out(a_1, a_2, a_3):
#     s = compute_area(a_1, a_2, a_3)
#     r = (a_1 * a_2 * a_3) / (4 * s)
#     return r
#
#
# # medians
# def median(a_1, a_2, a_3):
#     m = 0.5 * sqrt(2 * (a_1 ** 2 + a_2 ** 2) - a_3 ** 2)
#     return m
#
#
# if a + b <= c or b + c <= a or a + c <= b:
#     print("error")
# else:
#
#     sum_med = median(c, b, a) + median(a, c, b) + median(a, b, c)
#
#     print(round(r_in(a, b, c), 4), round(r_out(a, b, c), 4), round(sum_med, 4))


"""Задача
Ракета запускается с точки на экваторе и развивает скорость v км/с. Каков результат запуска?

Указание: если v ≤ 7.8 км/с, то ракета упадет на Землю (вывести 0), если 7.8 <v <11.2, то ракета станет спутником Земли (вывести 1), если  11.2 ≤ v ≤ 16.4 , то ракета станет спутником Солнца (вывести 2), если v > 16.4, то ракета покинет Солнечную Систему (вывести 3).

Если будет введено значение, меньшее или равное 0, то вывести "error".

Входные данные:

скорость ракеты.
Выходные данные:

число 0, 1, 2, 3 или error."""
#  ---------------1.4----------------------------
# v = float(input())
#
#
# if 0 < v <= 7.8:
#     print(0)
# elif 7.8 < v < 11.2:
#     print(1)
# elif 11.2 <= v <= 16.4:
#     print(2)
# elif v > 16.4:
#     print(3)
# else:
#     print('error')

"""
Дана длина ребра основания правильной треугольной пирамиды а и ее высота h. Найти объем пирамиды и площадь ее полной поверхности.

При вводе неверных данных (длина и высота не должны иметь нулевые или отрицательные значения) - вывести "error".

Формулы для вычисления:



Входные данные:

длина ребра a (вещественное число);
высота h (вещественное число).
Выходные данные:

объем пирамиды;
площадь ее полной поверхности.
При выводе значения округлить до 3-х знаков после запятой
"""
# a_a = float(input("a = "))
# h_h = float(input("h = "))
#
#
# def value(a, h):
#     v = (a ** 2 * h) / (4 * sqrt(3))
#     return v
#
#
# def area(a, h):
#     s = (a ** 2 * sqrt(3)) / 4 + (3 * a) / 2 * sqrt(h ** 2 + a ** 2 / 12)
#     return s
#
#
# if a_a <= 0 or h_h <= 0:
#     print("error")
# else:
#
#     print(round(value(a_a, h_h), 3), round(area(a_a, h_h), 3))

"""
Задача
По номеру года найти число дней в этом году (вывести 365, если это не високосный год, или 366, если високосный).

Указание. В современном (григорианском) календаре каждый год, номер которого делится на 4, является високосным, за исключением тех, которые делятся на 100 и не делятся на 400. Например, 1900 год - не високосный, 2000 год - високосный.

Григорианский календарь был веден в 1582 году, поэтому если пользователь введет значение, меньшее 1582, то вывести "error".

Входные данные:

год (целое число).
Выходные данные:

количество дней в году или error.
"""
# year = float(input())
#
# # print(year.is_integer())
#
# if year >= 1582 and year.is_integer():
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             print(365)
#         else:
#             print(366)
#     else:
#         print(365)
#
# else:
#     print('error')

"""
Задача
Напишите программу, которая для целого числа k (от 1 до 99) напечатает фразу «k рублей», учитывая при этом, что при некоторых значениях слово «рублей» заменяется на «рубль» или «рубля».

Например: 2 рубля, 13 рублей, 41 рубль.

Если введено значение вне интервала от 1 до 99, то вывести "ошибка".

Входные данные:

сумма в рублях (целое число).
Выходные данные:

число и слово рубль  в нужном падеже (строка текста) или ошибка.
"""
# k = float(input())
#
# if 1 <= k <= 99 and k.is_integer():
#     last = k % 10
#     if int(last) == 1 and not k == 11:
#         print(f'{int(k)} рубль')
#     elif 1 < last < 5 and not 11 < k < 15:
#         print(f'{int(k)} рубля')
#     else:
#         print(f'{int(k)} рублей')
# else:
#     print('ошибка')


"""
Задача
Посчитать, сколько банок краски необходимо, чтобы окрасить внутреннюю площадь бассейна кубической формы со стороной а метров, если расход краски на 1 квадратный метр  составляет b миллилитров, а в банке содержится v литров краски.

При вводе неверных данных  вывести '"error".

Входные данные:

сторона бассейна a в метрах (вещественное число);
расход краски b в миллилитрах (вещественное число);
объем банки с краской v литров (целое число).
Выходные данные:

количество банок краски или error.
"""
# from math import ceil
# a = input()
# b = input()
# v = input()
#
# if float(a) > 0 and float(b) > 0 and int(v) > 0:
#     # площадь
#     s = 5 * (float(a) ** 2)
#     # общий расход
#     r = s * (float(b) / 1000)
#     # количество банок
#     t = r / int(v)
#     print(ceil(t))
# else:
#     print('error')


"""
Задача
Дано значение времени в 12-ти часовом формате h:m:s. Определить угол в градусах между положением часовой стрелки в начале суток и ее положением в h часов, m минут и s секунд.

Допустимыми значениями считать целое число часов от 0 до 11, минут и секунд от 0 до 59. Если введены другие значения - вывести "error".

Входные данные:

количество часов h (целое число);
количество минут m (целое число);
количество секунд s (целое число).
Выходные данные:

значение угла в градусах или error.
Результат округлить до двух знаков после запятой.
"""
from math import degrees

# h = int(input())
# m = int(input())
# s = int(input())
#
# # if 0 <= h <= 11 and 0 <= (m or s) <= 59 :
# if 0 <= h <= 11 and 0 <= m <= 59 and 0 <= s <= 59:
#     # total_s = h * 3600 + m * 60 + s
#     # one_sec_gr = 360 / (12 * 60 * 60)
#     total = (h * 3600 + m * 60 + s) / 120
#
#     print(round(total, 2))
# else:
#     print("error")


# def f_x(x):
#     y = 1 / (x + 1) + x / (x - 3)
#     return y
#
#
# t = float(input("t = "))
# y = f_x(t)
#
# print("f(", t, ") = ", y)


"""
Вы положили некоторую сумму x в банк на n месяцев под k% годовых с капитализацией процентов. Расчет итоговой суммы осуществляется по формуле:

s=x\cdot (1+{k\over 12\cdot100})^n
s=x⋅(1+ 
12⋅100
k
​	
 ) 
n
 
Посчитать прибыль от вложения (разницу между конечной и исходной суммой), результат округлить до целого.

Реализовать задачу на основе предложенного шаблона. Проверку входных данных не делать.

Входные данные:

сумма вклада x руб;
процент k;
количество месяцев n.
Выходные данные:

прибыль от вложения, округленная до целого числа.
Пояснение:

Для округления выходных данных использовать round()
"""
# x = float(input())
# k = float(input())
# n = int(input())
#
#
# # deposit - сумма вклада, interest_rate -процентная ставка,
# # amount_months - количество месяцев
# def compute_income(deposit, interest_rate, amount_months):
#     inc = deposit * (1 + (interest_rate / (12 * 100))) ** amount_months
#     return inc
#
#
# # вычислить прибыль с помощью функции
#
# s = compute_income(x, k, n) - x
#
# # вывести результат
# print(round(s))


"""Подобрать такое ЦЕЛОЕ значение исходного вклада, чтобы за 5.0 месяцев получить прибыль 1969.0 рублей, если годовая 
процентная ставка составляет 7.0%. """

# def compute_income(deposit, interest_rate, amount_months):
#     z = deposit * (1 + (interest_rate / (12 * 100))) ** amount_months
#     return z
#
#
# k = float(input())   # занести процент вклада
# n = float(input())  # занести количество месяцев
# s = float(input())  # занести прибыль
#
# a = []
#
# for x in range(1000, 300000):
#     # вычислить прибыль для вклада x с помощью функции  compute_income(x, ..., ...)
#     income = compute_income(x, k, n) - x
#
#     if round(income) == s:
#         a.append(x)
#
# print(min(a))


"""
Для вычисления и прогноза численности населения Земли С. П. Капица предложил следующую формулу:

N(t)={C\over \tau}\cdot {arcctg({{T_1-t}\over \tau}})
N(t)= 
τ
C
​	
 ⋅arcctg( 
τ
T 
1
​	
 −t
​	
 )
где:
 t - год, для которого вычисляется численность населения;
С - 172 миллиарда человек·лет;
T1 -  2000 год;
\tauτ - 45 лет.

Вычислить численность населения в заданные годы.

Реализовать задачу на основе шаблона.

Входные данные:

строка, состоящая из n целых чисел, разделенных пробелами, каждое число - год.   
Выходные данные:

n строк, в каждой из которых выведен год и численность населения в этом году, для вывода использовать формат:
         "%5d - %6.3f миллиард(ов)"
"""

from math import pi, atan


def peoples(t):
    x = (2000 - t) / 45
    arcctg = pi / 2 - atan(x)
    N = 172 / 45 * arcctg
    return N


n = input('n = ')
years = n.split()

for year in years:
    res = peoples(int(year))
    print("%5d - %6.3f миллиард(ов)" % (int(year), res))
