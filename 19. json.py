import json
from datetime import datetime, date, time, timedelta
#
#
# user = {
#     'user_id': input(),   #  message from id
#     'date': input()   #   message date
# }
#
# #   открытие
# try:  # открытие на дозапись
#     data = json.load(open('users.json'))
# except:   # если нет, то создать  пустой список для записи
#     data = []
#
#
#
# #  добавляем объект в список
# data.append(user)
#
#
# # дозапись
# with open('users.json', 'w') as file:
#     json.dump(data, file, indent=2, ensure_ascii=False)
#
# # количество элементов в списке
# day_count = 0
from time import sleep

users = json.load(open('users.json'))
# for i in users:
#     if datetime.now() >= i['date']:
#         day_count += 1
#         print(i['date'])
#
#
#
# count = len(users)
# print(count)
#
# print('Done!')
#
#
# --------------------
# количество за последние сутки
day_count = 0
for i in users:
    date_str = i['date']
    date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    sleep(5)
    date_delta = datetime.now() - timedelta(days=1)
    print(date_delta)
    if date_obj >= date_delta:
        day_count += 1
    else:
        day_count += 0
print(day_count)
# --------------------

#
# data = json.load(open('users.json'))
# # print(len(data))
# user = {
#         "user_id": 6175653232,
#         "date": "2020-05-13 01:43:29"
#         }
#
# # print(data['user_id'].count(user['user_id']))
# #     data.append(user)  # добавляем объект в список
# # else:
# #     None
#
# data_list_id = []
# for i in data:
#     data_list_id.append(i['user_id'])
#
# print(data_list_id)
# print(data_list_id.count(user['user_id']))

