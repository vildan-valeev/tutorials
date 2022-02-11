"""Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each other and
preserving the original order of elements.


Убрать подряд повторяющиеся символы
"""


def unique_in_order(iterable):
    # a = list(iterable)
    # b = len(a) - 1
    # iterated = []
    # for i in range(0, b):
    #
    #     if a[i] != a[i + 1]:
    #         iterated.append(a[i])
    #     elif a[i] == a[b]:
    #         iterated.append(a[b])
    #     else:
    #         # print(a[i], '- дубликат')
    #         pass
    # return iterated
    newList = []
    for item in iterable:
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    return newList

print(unique_in_order('AAAABBBCCDAABBB'))  # ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD'))  # ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1, 2, 2, 3, 3]))  # [1,2,3]
