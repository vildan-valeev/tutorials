from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

new_user = {
    "name": "Becky"
}

db = client.test
db.users.insert_one(new_user)

for a in db.users.find():
    pprint.pprint(a)