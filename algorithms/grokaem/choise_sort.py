"""
Алгоритм сортировки выбором:

    нерекурсивный;
    может быть как устойчивым, так и неустойчивым;
    преобразует входные данные без использования вспомогательной структуры данных (in place);
    имеет сложность O(n2);
"""


def choise_sort(A):
    """сортировка списка А выбором"""
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

# def selectionSort(array):
#     for i in range(len(array)-1):
#         min_idx = i
#         for idx in range(i + 1, len(array)-1):
#             if array[idx] < array[min_idx]:
#                 min_idx = idx
#         array[i], array[min_idx] = array[min_idx], array[i]
#     return array
