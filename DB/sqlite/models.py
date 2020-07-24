from peewee import *

db = SqliteDatabase("houses.db")


########################################################################
class Area(Model):
    title = CharField()
    status = BooleanField(default=True)

    class Meta:
        database = db


class House(Model):
    title = CharField()
    descr = CharField()
    area = ForeignKeyField(Area, backref='houses')
    status = BooleanField(default=True)

    class Meta:
        database = db

class Photo(Model):
    file_id = CharField()
    house_id = ForeignKeyField(House, backref='photos')

    class Meta:
        database = db


if __name__ == "__main__":
    try:
        db.create_tables([House, Area, Photo])
    except OperationalError:
        print("Person table already exists!")
