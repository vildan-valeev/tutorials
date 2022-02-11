"""Если повторов нет то "(", если есть то ")" """

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


print(duplicate_encode('test'))


# def duplicate_encode(word):
#     """a new string where each character in the new string is '('
#     if that character appears only once in the original word, or ')'
#     if that character appears more than once in the original word.
#     Ignores capitalization when determining if a character is a duplicate. """
#     word = word.upper()
#     result = ""
#     for char in word:
#         if word.count(char) > 1:
#             result += ")"
#         else:
#             result += "("
#
#     return result