"""
*args - упаковка входящих именованных аргументов в кортеж
Аккуратно использовать с генераторами

*kwargs - упаковка входящих именованных аргументов в словарь
"""


def test(*args, **kwargs):
      a = kwargs['year']
      print(a)

li = [2, 3, 4, 6]

test(*li, year=1990, name='Bob')


# li = [{'id': 123, 'point_a': 'Москва', 'point_b': 'Уфа'}, {'id': 209, 'point_a': 'Москва', 'point_b': 'Уфа'}, {'id': 304, 'point_a': 'Москва', 'point_b': 'Уфа'}, {'id': 383, 'point_a': 'Москва', 'point_b': 'Уфа'}, {'id': 549, 'point_a': 'Москва', 'point_b': 'Уфа'}, {'id': 695, 'point_a': 'Москва', 'point_b': 'Уфа'}, {'id': 1012, 'point_a': 'Москва', 'point_b': 'Уфа'}]
#
# print(len(li))

# ci = {'id': 4,
#       'point_a': 'Магнитогорск',
#       'region_a': 'обл Челябинская',
#       'city_a': 'г Челябинск',
#       'lat_a': '61.7130801',
#       'lon_a': '28.7328336',
#       'point_b': 'Екатеринбург',
#       'region_b': 'обл Свердловская',
#       'city_b': 'г Екатеринбург',
#       'lat_b': '53.1950306',
#       'lon_b': '50.1069518',
#       'date_start': '2020-10-01T00:00:00',
#       'text': 'dfgdfg',
#       'cost': 5500,
#       'telephone': '+79565662356',
#       'tg_id': None,
#       'tg_username': 22,
#       'published': '2020-08-25T10:34:02.806715'}
#
# if ci['tg_username'] is not None:
#     print(ci['tg_username'])
#     print('ok')
