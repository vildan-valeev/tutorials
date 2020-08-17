#!C:\Users\Admin\PycharmProjects\tutorial\venv\Scripts\python.exe
# -*- coding: utf-8 -*-

from peewee import *

from playhouse.sqlite_ext import SqliteExtDatabase
# from apsw_ext import *

db = SqliteExtDatabase("items.db")
# import sqlite3
# sqlite3.sqlite_version_info

class BaseModel(Model):
    class Meta:
        database = db


class Item(BaseModel):
    title = CharField(collation='russian')
    descr = CharField()

    class Meta:
        table_name = 'items'


# if __name__ == '__main__':

def main():
    try:
        db.create_tables([Item])
    except OperationalError:
        print("Person table already exists!")




 # pip install --user https://github.com/rogerbinns/apsw/releases/download/3.32.2-r1/apsw-3.32.2-r1.zip --global-option=fetch --global-option=--version --global-option=3.32.2 --global-option=--all --global-option=build --global-option=--enable-all-extensions

