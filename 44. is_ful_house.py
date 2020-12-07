"""Определить фул хуас - 2 одинаковых значения и 3 одинаковых значения"""


def is_full_house(carts: list):
    carts.sort()
    print(carts)
    if len(set(carts)) == 2:
        if carts[0] == carts[1] and carts[3] == carts[4]:
            return True
        else:
            return False
    else:
        return False


print(is_full_house(['A', 'A', 'A', 'K', 'K']))

print(is_full_house(['3', 'J', 'J', '3', '3']))

print(is_full_house(['10', 'J', '10', '10', '10']))

print(is_full_house(['7', 'J', '3', '4', '2']))


# Короткое решение
def is_full_house(hand):
    return all([hand.count(i) >= 2 for i in hand])