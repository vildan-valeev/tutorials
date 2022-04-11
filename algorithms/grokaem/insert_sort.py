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

print(insert_sort([1,3,5,30,12,4,60,18]))
