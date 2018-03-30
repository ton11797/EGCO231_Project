from pymongo import MongoClient
import datetime
import pprint
import json
from bson.objectid import ObjectId

#Variable
URI = "mongodb+srv://root:root@egco231-ettdb.mongodb.net"
json_data = json.load(open('primer-dataset.json')) 
#print(json.dumps(json_data,sort_keys=True,indent=2)) 


def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})


#main

client = MongoClient(URI)
db  = client['EGCO231']
userData = db['userData']
Rooms = db['Room']

userData.insert_one(json_data)






