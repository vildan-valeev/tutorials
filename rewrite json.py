import json


video_id = input()


#   открытие
try:  # открытие на дозапись
    data = json.load(open('20.json'))
except:   # если нет, то создать  пустой список для записи
    data = ''


data.append(video_id)


with open('20.json', 'w') as file:
     json.dump(data, file, indent=2, ensure_ascii=False)

try:
    data = json.load(open('20.json'))
    print(data[-1])
except:
    print('No data')