"""
сумма вводимых строк...

Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.

Выведите одно число – сумму данных n чисел.
"""
# print(sum([int(input()) for i in range(int(input()))]))


n = int(input())
i = 1
x = 0
while i <= n:
    i += 1
    x += int(input())

print(x)

print(sum([int(input()) for i in range(int(input()))]))