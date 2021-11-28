import re


# def valid_ISBN10(isbn):
#     v = str(isbn)
#     result = 0
#     if re.match(r'(\d{9})([0-9]|X|x)', str(isbn)):
#         for n, i in enumerate(v, 1):
#             if n == 10:
#                 if i == 'X':
#                     i = 10
#             result += abs(n * int(i))
#             print(n, i, result, n * int(i))
#         if result % 11 == 0:
#             return True
#
#     return False

def valid_ISBN10(isbn):
    v = str(isbn)
    result = 0
    if len(v) != 10:
        return False

    for n, i in enumerate(v[0:9], 1):
        if i.isdigit():
            result += n * int(i)
        else:
            return False
        print(n, i, result)
    if v[-1] == 'X':
        result += 100
    else:
        result += int(v[-1]) * 10

    if result % 11 == 0:
        return True
    return False

# import re
#
# def valid_ISBN10(isbn):
#     return bool(re.match("\d{9}[\dX]$", isbn)) and sum("0123456789X".index(d) * i for i, d in enumerate(isbn, 1)) % 11 == 0
#

if __name__ == '__main__':
    print(valid_ISBN10('1112223339'))
