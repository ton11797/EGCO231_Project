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

def checkBook():
    #input = json.load(open(in)) 
    inJson = {
    'Username': 'nar',
    'Room':'6272',
    'Date_Time':"25/4/2561 12:00-13:00"
    }

    input = inJson
    user = input['Username']
    room = input['Room']
    date = input['Date_Time']

    Json = {
    'Username' : user,
    'Room': room,
    'Data_Time' : date
    }

    for r in get_room() :
        #print(r['Room'])
        #print(r['schedule'])
        if room == r['Room'] :
            for s in r['schedule']:
                #print(s['Data_Time'])
                dateTime = s['Data_Time'].split()
                d = date.split()
                if dateTime == d:
                    return False
                else:
                    time = dateTime[1].split('-')
                    st = time[0]
                    et = time[1]
                    #hr = et-st

                    inputtime = d[1].split('-')
                    sit = inputtime[0]
                    eit = inputtime[1]
                    #ihr = eit -sit
                    
                    if sit < st and eit > et :#and ihr < hr:
                        #insert(Json) 
                        print('in')
                        print(json.dumps(Json,sort_keys=True,indent=2))
        #print(json.dumps(Json,sort_keys=True,indent=2))
        return True

checkBook()
 


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