"""You are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    import math
    digit_list = list(map(int, str(num)))  # num to list
    result = ''
    for i in digit_list:
        result += str(math.ceil(math.pow(i, 2)))
    return int(result)


if __name__ == '__main__':
    print(square_digits(9119))
