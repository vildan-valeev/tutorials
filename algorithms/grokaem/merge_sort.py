"""
Сортировка слиянием

Этот алгоритм работает по принципу «разделяй и властвуй».
Здесь мы делим список ровно пополам и продолжаем это делать, пока в нем не останется только один элемент.
Затем мы объединяем уже упорядоченные части нашего списка. Мы продолжаем это делать, пока не получим
отсортированный список со всеми элементами несортированного входного списка.

Алгоритм сортировки слиянием:

    рекурсивный;
    устойчивый;
    требует дополнительной памяти;
    имеет сложность O(nlog(n));
"""


def mergeSort(nums):
    if len(nums) == 1:
        return nums
    mid = (len(nums) - 1) // 2
    lst1 = mergeSort(nums[:mid + 1])
    lst2 = mergeSort(nums[mid + 1:])
    result = merge(lst1, lst2)
    return result


def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while (i <= len(lst1) - 1 and j <= len(lst2) - 1):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i > len(lst1) - 1:
        while (j <= len(lst2) - 1):
            lst.append(lst2[j])
            j += 1
    else:
        while (i <= len(lst1) - 1):
            lst.append(lst1[i])
            i += 1
    return lst
