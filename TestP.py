from pymongo import MongoClient
import datetime
import pprint
import json
from bson.objectid import ObjectId
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

#Variable
URI = "mongodb+srv://root:root@egco231-ettdb.mongodb.net"
client = MongoClient(URI)
db       = client['EGCO231']
room     = db['Room']
userData = db['userData']

app = Flask(__name__)
api = Api(app)

#json_data = json.load(open('primer-dataset.json')) 
#print(json.dumps(json_data,sort_keys=True,indent=2)) 


#Response login 
Response = { 
            "status":"success", 
            "cookie_session":"KFIOGMREOIVK439050I", 
            "admin":"yes" 
} 



def print(posts):
    for post in posts.find():
        pprint.pprint(post) 

#for Test
def insert(username,password):
    data = {
            'username':username,
            'password':password
    }
    userData.insert_one(data)

#Register
def Jinsert(JSON):
    userData.insert_one(JSON)


#main
Name = 'oat'

r = requests.get(url)  
username = json.loads(r.json())['username'] 
password = json.loads(r.json())['username'] 
 
 
#Login case 
if userData.find_one({"$and":[{'username' : username,'password' : password}]}) : 
    print("in") 
    #r = requests.post(url, Response) 
else: 
    #r = requests.post(url, Response) 
    









