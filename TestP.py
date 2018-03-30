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

#Response login
Response = {
            "status":"success",
            "cookie_session":"KFIOGMREOIVK439050I",
            "admin":"yes"
}


def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)}) 

def insert(room,Name,date,start,end):
    data = {
            "available-room": [
                {
                "Room": "6272",
                "schedule": [
                    {
                    "Username": "narit",
                    "Data_Time": "25/4/2561 12:00-16:00"
                    },
                    {
                    "Username": "narit",
                    "Data Time": "28/4/2561 12:00-16:00"
                    }
                ]
                },
                {
                "Room": "6273",
                "schedule": []
                },
                {
                "Room": "6274",
                "schedule": []
                }
            ]
            }
    room.insert_one(data)


def insert(username,password):
    data = {
            'username':username,
            'password':password
    }
    userData.insert_one(data)

def insert(JSON):
    userData.insert_one(JSON)



#main
import requests
r = requests.get('serverport')
jsondata = json.loads( r.json() )
username = jsondata['username']
#username = json.loads(r.json())['username']

if userData.find_one({'username' : username}) == None:
    insert(r.json)
    r = requests.post(url, Response)









