from models import House, Area


# принтуем количество и все записи
def show_houses():
    print('----Дома-------')

    print('Количество:', House.select().where(House.status == True).count())  # Person.status is True
    for house in House.select():
        if house.status is True:
            print(f'{house.id} :', house.title, house.descr)
        else:
            print(f'{house.id} :', house.title, house.descr, ' - статус False')


def show_areas():
    print('Количество:', Area.select().where(Area.status == True).count())  # Person.status is True

    for area in Area.select():
        if area.status is True:
            print(f'{area.id} :', area.title)
        else:
            print(f'{area.id} :', area.title, ' - статус False')

def show():
    print('----Дома-------')

    print('Количество:', House.select().where(House.status == True).count())  # Person.status is True
    for house in House.select():
        if house.status is True:
            print(f'{house.id} :', house.title, house.descr)
        else:
            print(f'{house.id} :', house.title, house.descr, ' - статус False')

    print('---------------------')


    print('----Районы-------')
    # x = Area.select().where(Area.status == True)
    # # print('Районы с строку:', Area.select().where(Area.status == True))
    a = []
    for area in Area.select().where(Area.status == True):
        x = f'{area.title}'
        a.append(x)
    # print('a', a)
    b = '\n'.join(a)
    print('b', b)


    print('---------------------')
    print('Количество:', Area.select().where(Area.status == True).count())  # Person.status is True

    for area in Area.select():
        if area.status is True:
            print(f'{area.id} :', area.title)
        else:
            print(f'{area.id} :', area.title, ' - статус False')

    print('---------------------')
    print('----квартиры по районам-------')
    # print('Количество:', Area.select().where(Area.houses.id == 1).count())  # Person.status is True
    for area in Area.select():
        print(f'{area.id} :', area.title, area.houses.count(), 'квартир')

        for house in area.houses:
            print('   ', f'{house.id} :', house.title)
    else:
        print('    нет квартир')

    print('---------------------')


    print('----квартиры определенного района с id==2 -------')

    houses = House.select(House.id, House.title).join(Area).where(Area.id == 2)
    print(len(houses))
    print(House.select(House.id, House.title).join(Area).where(Area.id == 2).count())
    print(houses[0].title)
    for house in enumerate(houses):
        print(house)
        # print('id:', house.id, house.title)



def create_house():
    # прием записи одной
    print('Введите название дома')
    title = input()
    print('Введите описание')
    descr = input()
    print('Введите название района')
    inp = input()
    area = Area.get(Area.title == inp)
    print(area)
    # добавление в базу
    House.create(title=title, descr=descr, area=area
                 )
    print('сохранено')


def create_area():
    # прием записи одной
    print('Введите название района')
    title = input()
    # добавление в базу
    res = Area.create(title=title)
    return print(res)

def delete():
    print('Введите id для удаления записи')
    del_id = input()

    House[del_id].delete_instance()
    print('Удалено')
    print('Количество осталось:', House.select().count())


def update_house():
    print('Введите id для изменения записи')
    update_id = input()

    try:
        status = House.get(House.id == update_id).status
    except:
        print("Вы ввели не то число похоже")

    try:
        if status:
            res = House.update(status=False).where(House.id == update_id).execute()
            print('Изменено\n', res)
        elif status is False:
            res = House.update(status=True).where(House.id == update_id).execute()
            print(res)
            print('Изменено\n', res)
        else:
            print("Статус не сменился, где-то ошибка...")
    except:
        print("Статус не сменился, где-то ошибка")
    # print(res)

    # Person[del_id].age = 222
    # Person[del_id].save()

    print('Изменено')
    print('Количество осталось:', House.select().where(House.status == True).count())


if __name__ == '__main__':
    # show()
    # main()
    #  delete()
    # update()
    # create_area()
    # show_houses()
    # show_areas()
    create_house()
