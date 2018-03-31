#import
from pymongo import MongoClient
from datetime import datetime, time as datetime_time, timedelta
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

def time_diff(start, end):
    if isinstance(start, datetime_time): # convert to datetime
        assert isinstance(end, datetime_time)
        start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
    if start <= end: # e.g., 10:33:26-11:15:49
        return end - start
    else: # end < start e.g., 23:55:00-00:25:00
        end += timedelta(1) # +day
        assert end > start
        return end - start

def Time_diff(Bound):
    s,e = [datetime.strptime(t, '%H:%M') for t in Bound.split('-')]
    return time_diff(s,e)


def checkBook(JSONINPUT):
    #input = json.load(open(in)) 
    inJson = {
    'Username': 'nar',
    'Room':'6272',
    'Date_Time':"25/4/2561 12:00-15:00"
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
                
                if dateTime != d:                   
                    s,e = [datetime.strptime(t, '%H:%M') for t in dateTime[1].split('-')]
                    iss,ie = [datetime.strptime(t, '%H:%M') for t in d[1].split('-')]
                    time = Time_diff(dateTime[1])
                    itime = Time_diff(d[1])
                    if(iss < s and ie > e and itime < time):
                        #insert(Json) 
                        print('in')
                        # print(json.dumps(Json,sort_keys=True,indent=2))
                        return True
                return False
        #insert(Json) 
        # print(json.dumps(Json,sort_keys=True,indent=2))
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