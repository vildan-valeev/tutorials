import unittest

test = {
    "ID": "werui-32e32iuh-ewpir30",
    "passport": {
        "first_name": "Олег",
        "last_name": "Минаев",
        "middle_name": "Александрович"
    },
    "channel": {
        "name": "Vkontakte",
        "namespace": "",
        "id": "123456789"
    },
    "extras": {
        "role": "user",
        "group_id": 2051234,
        "phone": "+79169161122",
        "email": "client@mail.com",
        "inn": 989129823749827,
        "kpp": 982193610928790000008,
        "org_region": "Moscow",
        "is_vip": False
    }
}

test2 = {"channel.id": "12123424354"}


def convert_key(other):
    keys = list(other.keys())[0].split('.')  # разбиваем ключ на ключи (подразумевается что ключ только один - 0)
    if len(keys) == 1:  # проверяем ключ с точкой или нет (точка выхода с рекурсии)
        return other
    return {f"{keys[0]}": convert_key({'.'.join(keys[1:]): list(other.values())[0]})}


print(convert_key({"extras.org_region.oblast.gorod.ulica": 'выпва'}))

# for k, v in other.items():
#     print(k)
#     if '.' not in k:
#         d.update({k: v})
#     else:
#         key, kk = k.split('.')
#         print(key)
#         d.update({
#             key: {
#                 kk: other[k]
#             }
#         })
# return d


# class TestSolution(unittest.TestCase):
#
#     def test_move_zeros(self):
#         """"""
#
#         self.assertEqual(convert_key({"channel.id": "12123424354"}), {"channel": {"id": "12123424354"}})
#         self.assertEqual(convert_key({"extras.org_region.oblast": 'выпва'}), {"extras": {"org_region": {'oblast': "выпва"}}})


# python -m unittest -v moving_zeros_to_the_end.py
