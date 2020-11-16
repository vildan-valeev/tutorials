import datetime

from peewee import *

db = SqliteDatabase("google_calendar.db")


########################################################################
class BaseModel(Model):
    class Meta:
        database = db


class Doctor(BaseModel):
    """Имена докторов"""
    last_name = CharField()  # фамилия
    first_name = CharField()  # имя
    middle_name = CharField()  # отчество
    callback = CharField()


class DoctorType(BaseModel):
    """Профессии докторов"""
    title = CharField()
    callback = CharField()


class ServiceType(BaseModel):
    """Тип услуги: консультация узи и тд"""
    title = CharField()
    callback = CharField()


class Price(BaseModel):
    """Связанная таблица - доктора, фамилии, услуги"""
    service_type = ForeignKeyField(ServiceType)
    doctor = ForeignKeyField(Doctor)
    doctor_type = ForeignKeyField(DoctorType)
    duration = CharField()
    price = IntegerField()


class Order(BaseModel):
    """Заявка на запись - в календарь, на оплату и тд """
    price = ForeignKeyField(Price)
    date = DateTimeField(default=datetime.datetime.now)


class UserStatus(BaseModel):
    """Присваивание статуса юзерам - админ, врач, пользователь, владелец ..."""
    title = CharField()
    callback = CharField()


class User(BaseModel):
    """Пользователи - сохранение, личный кабинет итд"""
    tg_id = IntegerField()
    tg_username = CharField()
    orders = ManyToManyField(Order)
    status = ForeignKeyField


if __name__ == "__main__":  # для локального запуска - создание, отладка, миграции и тд
    try:
        db.create_tables([ServiceType, DoctorType, Doctor, Order, Price, User, UserStatus])

    except OperationalError:
        print("Tables already exists!")
