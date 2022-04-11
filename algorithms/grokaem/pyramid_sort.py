"""
Пирамидальная сортировка («сортировка кучей»)

Как и в двух предыдущих алгоритмах, мы создаем два сегмента списка: отсортированный и несортированный.
В данном алгоритме для эффективного нахождения максимального элемента в неотсортированной части списка мы
используем структуру данных «куча».
Метод heapify в примере кода использует рекурсию для получения элемента с максимальным значением на вершине.

Алгоритм пирамидальной сортировки:

    нерекурсивный;
    неустойчивый;
    преобразует входные данные без использования вспомогательной структуры данных (in place);
    имеет сложность O(nlog(n));
"""


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array
