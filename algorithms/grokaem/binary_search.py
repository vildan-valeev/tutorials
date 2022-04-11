from array import array


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = low + high
        guess = lst[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    return


my_list = [1, 3, 5, 7, 9, 11, 16]

# print(binary_search(my_list, 3))


v = array(i, [1,2,3])
