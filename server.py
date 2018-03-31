#import
from pymongo import MongoClient
import datetime
import pprint
import json


#Variable 
URI = "mongodb+srv://root:root@egco231-ettdb.mongodb.net" 
client = MongoClient(URI) 
db       = client['EGCO231'] 
room     = db['Room'] 
userData = db['userData'] 



# ////////////////////////////////////////////////////////
# load config


# ///////////////////////////////////////////////////////
# log


# ///////////////////////////////////////////////////////
# database


# ///////////////////////////////////////////////////////
# book
def get_room():
    json_data = json.load(open('EGCO231_getroom.json')) 
    return json_data['available-room']
#print(json.dumps(get_room(),sort_keys=True,indent=2))

def checkBook(rm,date):
    for r in get_room() :
        #print(r['Room'])
        #print(r['schedule'])
        if rm == r['Room'] :
            for s in r['schedule']:
                #print(s['Data_Time'])
                dateTime = s['Data_Time'].split()
                
                if dateTime == d:
                    return False
                else:
                    time = dateTime[1].split('-')

                
checkBook('6272','25/4/2561 12:00-16:00')
    


 
        
    


# ///////////////////////////////////////////////////////
# login


# ///////////////////////////////////////////////////////
# cancel


# ///////////////////////////////////////////////////////
# register


# ///////////////////////////////////////////////////////
# get room


# ///////////////////////////////////////////////////////
# Route


# ///////////////////////////////////////////////////////