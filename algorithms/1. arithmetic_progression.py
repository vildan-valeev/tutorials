"""
Жители племени «Тумба-Юмба» единственные в долине, которые умеют правильно отвечать на один особенный вопрос.
По правильному ответу их можно отличить от жителей других племён.
Вот этот вопрос: назовите сумму целых чисел от 1 (включительно) до N (включительно).
"""


def arithmetic_progression(b, a=1):
    if b < 0:  # если меньше, то наоборот
        a, b = b, a
    return sum(range(a, b + 1))


print(arithmetic_progression(1))
print(arithmetic_progression(3))
print(arithmetic_progression(-3))
print(arithmetic_progression(5))
