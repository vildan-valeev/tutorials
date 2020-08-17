#!C:\Users\Admin\PycharmProjects\tutorial\venv\Scripts\python.exe
# -*- coding: utf-8 -*-

# from importlib import reload
from sqlite3.dbapi2 import Cursor
from sys import getdefaultencoding
from models import Item, main
from peewee import fn, SQL
import sys

# reload(sys)
# sys.setdefaultencoding('utf8')


from DB.sqlite.models import db


class DB:

    def get_item(self, id):
        item = Item.select().where(Item.id == id).get()
        return item

    def count_items(self) -> int:
        total = Item.select().count
        return total

    def add_item(self, **kwargs):
        pass

    def update_item(self):
        pass

    def delete_item(self):
        pass


# # принтуем количество и все записи
# def show_houses():
#     print('----Дома-------')
#
#     print('Количество:', House.select().where(House.status == True).count())  # Person.status is True
#     for house in House.select():
#         if house.status is True:
#             print(f'{house.id} :', house.title, house.descr)
#         else:
#             print(f'{house.id} :', house.title, house.descr, ' - статус False')
#
#
# def show_areas():
#     print('Количество:', Area.select().where(Area.status == True).count())  # Person.status is True
#
#     for area in Area.select():
#         if area.status is True:
#             print(f'{area.id} :', area.title)
#         else:
#             print(f'{area.id} :', area.title, ' - статус False')
#
# def show():
#     print('----Дома-------')
#
#     print('Количество:', House.select().where(House.status == True).count())  # Person.status is True
#     for house in House.select():
#         if house.status is True:
#             print(f'{house.id} :', house.title, house.descr)
#         else:
#             print(f'{house.id} :', house.title, house.descr, ' - статус False')
#
#     print('---------------------')
#
#
#     print('----Районы-------')
#     # x = Area.select().where(Area.status == True)
#     # # print('Районы с строку:', Area.select().where(Area.status == True))
#     a = []
#     for area in Area.select().where(Area.status == True):
#         x = f'{area.title}'
#         a.append(x)
#     # print('a', a)
#     b = '\n'.join(a)
#     print('b', b)
#
#
#     print('---------------------')
#     print('Количество:', Area.select().where(Area.status == True).count())  # Person.status is True
#
#     for area in Area.select():
#         if area.status is True:
#             print(f'{area.id} :', area.title)
#         else:
#             print(f'{area.id} :', area.title, ' - статус False')
#
#     print('---------------------')
#     print('----квартиры по районам-------')
#     # print('Количество:', Area.select().where(Area.houses.id == 1).count())  # Person.status is True
#     for area in Area.select():
#         print(f'{area.id} :', area.title, area.houses.count(), 'квартир')
#
#         for house in area.houses:
#             print('   ', f'{house.id} :', house.title)
#     else:
#         print('    нет квартир')
#
#     print('---------------------')
#
#
#     print('----квартиры определенного района с id==2 -------')
#
#     houses = House.select(House.id, House.title).join(Area).where(Area.id == 2)
#     print(len(houses))
#     print(House.select(House.id, House.title).join(Area).where(Area.id == 2).count())
#     print(houses[0].title)
#     for house in enumerate(houses):
#         print(house)
#         # print('id:', house.id, house.title)


def create_house():
    # прием записи одной
    print('Введите название дома')
    title = input()
    print('Введите описание')
    descr = input()

    # добавление в базу
    Item.create(title=title, descr=descr)
    print('сохранено')
import sqlite3

def search():
    query = Item.select().where(Item.title.contains('house'))
    query2 = Item.select().where(Item.title ** '%house%')
    query3 = Item.select().where(Item.title.contains('дом'))
    query4 = Item.select().where(Item.title ** '%дом%')

    cur = db.execute_sql('SELECT * FROM items WHERE title LIKE "дом"')
    # print(cur.count())
    for i in cur:
        print(i)

    print('query:  ', query.count())
    print('query2: ', query2.count())
    print('query3: ', query3.count())
    print('query4: ', query4.count())






def create_items():
    Item.create(title='House', descr='sdfsdfsdf')
    Item.create(title='HoUSE', descr='dsfgdfgghhgf')
    Item.create(title='house', descr='ds234rfdghhgf')
    Item.create(title='дом', descr='ds234rfdghhgf')
    Item.create(title='ДОМ', descr='ds2ываываdghhgf')
    Item.create(title='Дом', descr='ds2ываываdghhgf')


if __name__ == '__main__':
    # getdefaultencoding()
    # main()
    search()
    # create_items()
    # create_house()
