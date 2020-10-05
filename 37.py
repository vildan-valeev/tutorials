# import datetime
#
# t = '2020-10-08T15:25:00'
#
# date_time_obj = datetime.datetime.strptime(t, '%Y-%m-%dT%H:%M:%S')
#
# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)
#
# x = date_time_obj.strftime('%H:%M:%S %Y-%m-%d')
# print('New Date-time:', x)


# def test(*args):
#     if args:
#         return args
#     else:
#         return 'No args'
#
#
# # print(test({'idd': 123}))
# print(test(123))


import requests

code = 300


def save_item():
    try:
        response = code + 1
        if response == 201:
            return 10
        else:
            return False
    except:
        return False


def post_vk(*args):
    print('args vk', args)
    if args:
        return f'в вк c id = {args[0]}'
    else:
        return 'в вк без id'


def post_tg(*args):
    print('args tg', args)
    if args:
        return f'в тг c id = {args[0]}'
    else:
        return 'в тг без id'


id_item = save_item()
print(id_item)


if id_item:
    vk = post_vk(id_item)
    print('vk', vk)
    tg = post_tg(id_item)
    print('tg', tg)
    if vk and tg:
        print('Сохранено в бд, опубликовано в тг и вк')
    elif vk:
        print('Опубликовано в вк!')
    elif tg:
        print('Опубликовано в тг!')
    else:
        print('Ошибка.')
else:
    vk = post_vk()
    print('vk', vk)
    tg = post_tg()
    print('tg', tg)
    if vk and tg:
        print('Опубликовано в тг и вк, но в бд не сохранено!')
    elif vk:
        print('Опубликовано только в вк!')
    elif tg:
        print('Опубликовано только в тг!')
    else:
        print('Ошибка.')

    print(False)
