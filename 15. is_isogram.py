"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore
letter case.

Проверка являются ли буквы в строке повторяющимися

"""


def is_isogram(string):

    if len(set(string.lower())) == len(string.lower()):
        return True
    else:
        return False


# def is_isogram(string):
#     return len(string) == len(set(string.lower()))


is_isogram("Dermatoglyphics")
is_isogram("isogram")
is_isogram("aba")
is_isogram("moOse")
is_isogram("isIsogram")
is_isogram("")
