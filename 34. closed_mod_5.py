"""Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:

y больше или равно x
y делится нацело на 5
"""
# def closest_mod_5(x):
#     return x if x % 5 == 0 else closest_mod_5(x + 1)



def closest_mod_5(x):
    while x % 5 != 0:
        x += 1
    return x



print(closest_mod_5(37))