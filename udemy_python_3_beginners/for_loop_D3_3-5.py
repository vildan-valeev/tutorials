"""построить цикл от 0 до ввденееного числа и посчитать сумму всех чисел, делимых без остатка на 3 или 5"""

# n = 15
#
# s = 0
# for i in range(0, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         s += i
#     else:
#         continue
#
# print(s)
# print(sum(i for i in range(0, n + 1) if i % 3 == 0 or i % 5 == 0))


"""взять из первого списка все нечетные числа, из второго четные и объединить их в новом списке"""
# first_lst = [1, 3, 5, 6, 8, 9, 1, 5, 6, 4, 2, 3]
# second_lst = [0, 5, 9, 8, 6, 5, 3, 2, 4, 7]
# res = []
# for f in first_lst:
#     if f % 2 != 0:
#         res.append(f)
# for s in second_lst:
#     if s % 2 == 0:
#         res.append(s)
# print(res)
#
# print([x for x in first_lst if x % 2 != 0] + [x for x in second_lst if x % 2 == 0])

"""посчитать веса карт"""
plus_one = [2, 3, 4, 5, 6]
zero = [7, 8, 9]
minus_one = [10, 'J', 'Q', 'K', 'A']

# current_hand = [2, 3, 4, 10, 'Q', 5]
current_hand = [2, 7, 4, 9, 3, 5]
result = 0
for i in current_hand:
    if i in plus_one:
        result += 1
    elif i in zero:
        result += 0
    elif i in minus_one:
        result -= 1

print(result)
# второй способ
cards = {
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 0,
    8: 0,
    9: 0,
    10: -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1
}
cards_sum = sum([cards[x] for x in current_hand])
print(cards_sum)
