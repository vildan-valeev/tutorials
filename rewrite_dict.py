import unittest


def convert_key(other):
    # разбиваем ключ на ключи (подразумевается что ключ только один - 0)
    keys = list(other.keys())[0].split('.')
    # проверяем ключ с точкой или нет (точка выхода с рекурсии)
    if len(keys) == 1:
        return other
    return {f"{keys[0]}": convert_key({'.'.join(keys[1:]): list(other.values())[0]})}


class TestConvert(unittest.TestCase):

    def test_convert_key(self):
        """"""

        self.assertEqual(convert_key({"channel.id": "12123424354"}), {"channel": {"id": "12123424354"}})
        self.assertEqual(convert_key({"extras.org_region.oblast": 'выпва'}), {"extras": {"org_region": {'oblast': "выпва"}}})


# python -m unittest -v rewrite_dict.py
