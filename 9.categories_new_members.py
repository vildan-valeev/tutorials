"""
Список списков - возраст, рейтинг
Сеньором клуба может быть тот кто не старше 55 и рейтинг выше 7. Остальные Open

"""

def openOrSenior(data):
    members = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            members.append('Senior')
        else:
            members.append('Open')
    return members


print(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]))
print(openOrSenior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
