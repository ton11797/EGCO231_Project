from pymongo import MongoClient
import datetime
import pprint
import json
from bson.objectid import ObjectId

#Variable
URI = "mongodb+srv://root:root@egco231-ettdb.mongodb.net"
client = MongoClient(URI)
db       = client['EGCO231']
room     = db['Room']
userData = db['userData']


#json_data = json.load(open('primer-dataset.json')) 
#print(json.dumps(json_data,sort_keys=True,indent=2)) 


def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)}) 

def insert(room,Name,date,start,end):
    room = room["available-room"]
    data = {
            'room': room,
            'username':Name,
            'Datetime':{'date':date,
                        'start': start,
                        'End': end
                        }
    }
    room.insert_one(data)

def insert(username,password):
    data = {
            'username':username,
            'password':password
    }
    userData.insert_one(data)



#main

insert('narit1',77624)







