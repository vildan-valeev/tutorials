import requests

# ---------
r = requests.get('http://127.0.0.1:8000/api/tours/')
response = r.json()
print(response)
print(len(response))

for i in response:
    print('id ', i['id'])

# -----
data = {
        "id": 3,
        "point_a": "Выборг",
        "region_a": "обл Ленинградская, р-н Выборгский",
        "city_a": "г Выборг",
        "lat_a": "60.7130801",
        "lon_a": "28.7328336",
        "point_b": "Самара",
        "region_b": "обл Самарская",
        "city_b": "г Самара",
        "lat_b": "53.1950306",
        "lon_b": "50.1069518",
        "date_start": "2020-09-30T08:30:00",
        "text": "ываываыва",
        "cost": 5466,
        "telephone": "+79565662355",
    }

id = 3,
point_a = "Выборг"
region_a = "обл Ленинградская, р-н Выборгский",
city_a = "г Выборг",
lat_a = "60.7130801",
lon_a = "28.7328336",
point_b = "Самара",
region_b = "обл Самарская",
city_b = "г Самара",
lat_b = "53.1950306",
lon_b = "50.1069518",
date_start = "2020-09-30T08:30:00",
text = "ываываыва",
cost = 5466,
telephone = "+79565662355",

r = requests.post('http://127.0.0.1:8000/api/tours/create/', data=data)
resp = r.status_code
print(resp)