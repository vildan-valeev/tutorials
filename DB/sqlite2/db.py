#  база данных или гугл таблица
from peewee import JOIN

from DB.sqlite2.models import DoctorType, Doctor, ServiceType, Price


def put_data():
    """Згрузка данных в базу"""
    try:
        doc1 = Doctor.create(last_name='Байбурина', first_name='Замира', middle_name='Зигануровна',
                             callback='baiburina_doctor')
        doc2 = Doctor.create(last_name='Даутова', first_name='Земфира', middle_name='Альфредовна',
                             callback='dautova_doctor')
        doctype1 = DoctorType.create(title='Кардиолог', callback='cardiolog_doctortype')
        doctype2 = DoctorType.create(title='Эндокринолог', callback='endokrinolog_doctortype')
        servicetype1 = ServiceType.create(title='Консультация', callback='consultation_servicetype')
        servicetype2 = ServiceType.create(title='Процедура', callback='procedure_servicetype')

        price1 = Price.create(service_type=servicetype1, doctor=doc1, doctor_type=doctype1, duration="0.5", price=1000)
        price2 = Price.create(service_type=servicetype2, doctor=doc2, doctor_type=doctype2, duration="0.5", price=1000)
        return "Добавлено!"
    except:
        return "Ошибка!"


def menu_get_doctors():
    """список докторов"""
    print('--------получаем список докторов имена----------')
    doctor_type_callback = 'cardiolog_doctortype'
    service_type_callback = 'consultation_servicetype'
    query = (Doctor
             .select()
             .join(Price)
             .join(DoctorType)
             .switch(Price)
             .join(ServiceType)
             .where(DoctorType.callback == doctor_type_callback, ServiceType.callback == service_type_callback)
             )
    for doctor in query:
        print(doctor.last_name[0].upper())
    # for doctor in Doctor.select():
    #     print(doctor)
    #     print(f"{doctor.last_name} {doctor.first_name} {doctor.middle_name}", doctor.callback)


def menu_get_doctor_type():
    print('--------получаем список докторов профессий----------')
    query = DoctorType.select()
    for doctortype in query:
        print(doctortype.title, doctortype.callback)


def menu_get_service_type():
    print('-------получаем тип услуги отфильтрованному по колбеку профессии доктора------')
    doctor_type_callback = 'cardiolog_doctortype'

    query = (ServiceType
             .select(ServiceType)
             .join(Price)
             .join(DoctorType)
             .where(DoctorType.callback == doctor_type_callback)
             )
    for i in query:
        print(i.title, i.callback)


# ----
# put_data()
menu_get_doctors()
# menu_get_doctor_type()
# menu_get_service_type()
