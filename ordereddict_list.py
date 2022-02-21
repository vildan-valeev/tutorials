a = [
    {
        "code": "469",
        "summary": "Summary text 1",
        "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
    },
    {
        "code": "445",
        "summary": "Summary text 1",
        "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
    },
    {
        "code": "445",
        "summary": "Summary text 3",
        "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
    }
]
b = [
    {
        "code": "469",
        "summary": "Summary text 1",
        "manual": "35c55e7f-8d6d-46ff-bc84-64c4c6e22a3b"
    }
]

from collections import OrderedDict
a = [OrderedDict(i) for i in a]
# print(a)
# b = [OrderedDict(i) for i in b]
#
# print(b[0]['code'])
# print(all(x in a for x in b))



class ValidateItems:
    """ Валидация элементов заданного справочника текущей версии """
    print(__doc__)
