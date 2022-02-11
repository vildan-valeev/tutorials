"""Посчитать гласные буквы"""


def count_vowels(word):
    vowels = 0
    for i in word:
        if i in 'aeiou':
            vowels += 1
    return vowels


print(count_vowels('abcd'))


# Короткое решение
def count_vowels(txt):
    return sum([1 for x in txt.lower() if x in 'aeiou'])
