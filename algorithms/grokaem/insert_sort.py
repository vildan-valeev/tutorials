"""
Алгоритм сортировки вставками:

    нерекурсивный;
    устойчивый;
    преобразует входные данные без использования вспомогательной структуры данных (in place);
    имеет сложность O(n2);
"""

def insert_sort(A):
    """сортировка списка А вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1
    return A


# def insert_sort(arr):
#     for i in range(len(arr)):
#         cursor = arr[i]
#         pos = i
#
#         while pos > 0 and arr[pos - 1] > cursor:
#             # Меняем местами число, продвигая по списку
#             arr[pos] = arr[pos - 1]
#             pos = pos - 1
#         # Остановимся и сделаем последний обмен
#         arr[pos] = cursor
#
#     return arr

def min_move(a):
    """Обратная сортировка - с конца"""
    counter = 0
    for pos, cursor in reversed(list(enumerate(a))):
        print(pos, cursor)

        while pos > 0 and a[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            a[pos] = a[pos - 1]
            pos = pos - 1
            counter += 1
        # Остановимся и сделаем последний обмен
        a[pos] = cursor
    print(counter)
    return a

print(insert_sort([1,3,5,30,12,4,60,18]))
