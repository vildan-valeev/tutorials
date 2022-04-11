# def countdown(i):
#     print(i)
#     return countdown(i-1)
#
#
# countdown(5)


def recursion_sum(lst, i=0):
    if i >= len(lst):
        return 0
    return lst[i] + recursion_sum(lst, i + 1)


z = recursion_sum([1, 5, 6, 12, 15])
print(z)
