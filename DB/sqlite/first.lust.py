from peewee import *

db = SqliteDatabase('base.db')


class homes(Model):
    own_area = IntegerField()
    owner = TextField()

    class Meta:
        database = db
        db_table = 'homes'

homes.create_table()





from agwa import *

last_kv = []

def check_kv_first(own_id, *args):
    if not args:
        m = homes.select().where(homes.own_area == own_id).limit(1).get()
        last_kv.append(m.id)
        return m
    else:
        m = homes.select().where((homes.id > args[0]) & (homes.own_area == own_id)).limit(1).get()
	last_kv.append(m.id)
        return m


print(check_kv_first(5).owner)
print(check_kv_first(5, last_kv[0]).owner)

print(check_kv_first(5, 22).owner)