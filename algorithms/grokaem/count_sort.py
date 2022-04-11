"""
Сортировка подсчетом

Этот алгоритм не производит сравнение элементов. Для сортировки используются математические свойства целых чисел.
Мы подсчитываем вхождения числа в массиве и сохраняем результат во вспомогательном массиве, где индексу соответствует
значение ключа.

Алгоритм сортировки подсчетом:

    нерекурсивный;
    устойчивый;
    преобразует входные данные без использования вспомогательной структуры данных (in place), но все же требует дополнительной памяти;
    имеет сложность O(n);
"""
from typing import List


def sortArray(self, nums: List[int]) -> List[int]:
    i_lower_bound, upper_bound = min(nums), max(nums)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item + lb for item in nums]
        lower_bound, upper_bound = min(nums), max(nums)

    counter_nums = [0] * (upper_bound - lower_bound + 1)
    for item in nums:
        counter_nums[item - lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_nums):
        num = idx + lower_bound
        for i in range(item):
            nums[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item - lb for item in nums]
    return nums
