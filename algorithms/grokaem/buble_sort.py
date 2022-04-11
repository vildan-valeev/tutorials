"""
Алгоритм сортировки пузырьком:

    нерекурсивный;
    устойчивый;
    преобразует входные данные без использования вспомогательной структуры данных (in place);
    имеет сложность O(n2);
"""


def bubbleSort(array):
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array
