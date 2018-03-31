#import
from pymongo import MongoClient
import random
import string

from datetime import datetime, time as datetime_time, timedelta
import pprint
import json

from flask import Flask, url_for,Response,request,json


# ////////////////////////////////////////////////////////
# load config


# ///////////////////////////////////////////////////////
# log
def printdata(data):
    file = open("log.txt","a")
    print(data,end="")
    file.write(data)
    file.close
# ///////////////////////////////////////////////////////
# database
class database:
	def __init__(self):
		self.client = MongoClient('localhost', 27017)
		self.db = self.client['EGCO']
	def have_user(self,username):
		self.user = self.db['userData']
		if str(self.user.find_one({"username":username})) == "None":
			return False
		else:
			return True

	def register(self,username,password):
		if self.have_user(username):
			respond = {"status":"Fail","error":"username exist"}
			return json.dumps(respond)
		else:
			self.user.insert_one({"username":username,"password":password})
			respond = {"status":"sucess","error":"username exist"}
			return json.dumps(respond)

	def rand_string(self,length, char_set=10):
		output = ''
		for _ in range(length): output += random.choice(char_set)
		return output

	def get_room(self):
		self.room = self.db['room']
		collect = self.room.find({})
		array =[]
		for c in collect:
			del c['_id']
			array.append(c)
		respond = {"available-room":array}
		return json.dumps(respond)

	def genCookies(self,username):
		self.session = self.db['loginSession ']
		self.random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
		self.session.insert_one({"username":username,"cookies":self.random})
		return self.random

	def login(self,username,password):
		self.user = self.db['userData']
		if self.user.find_one({"username":username,"password":password})=="None":
			respond = {"status":"Fail","error":"username or password not match"}
			return json.dumps(respond)
		else:
			self.cookies = self.genCookies(username)
			self.admin = "no"
			if username=="admin":
				self.admin = "yes"
			respond = {"status":"sucess","error":"none","cookie_session":self.cookies,"admin":self.admin}
			return json.dumps(respond)



DB = database()
# print(DB.have_user("admin"))
# print(DB.get_room())
print(DB.login("admin","123"))
printdata("test\n")
printdata("test\n")
printdata("test\n")
printdata("test\n")
printdata("test\n")

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
    
    respond = {"status":"sucess","error":"none"}
    respond_err = {"status":"fail","error":"Have reservations !!"}

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
                        
                        return json.dumps(respond)
                return json.dumps(respond_err)
        #insert(Json) 
        # print(json.dumps(Json,sort_keys=True,indent=2))
        return json.dumps(respond)

checkBook('JSONINPUT')
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

app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def api_login():
    if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
			return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_LOGIN"

@app.route('/regis', methods = ['POST'])
def api_regis():
	if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
			return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_REGIS"

@app.route('/book', methods = ['POST'])
def api_book():
	if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
				return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_BOOK"

@app.route('/cancel', methods = ['POST'])
def api_cancel():
	if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
				return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_CANCEL"
@app.route('/list', methods = ['GET'])
def api_list():
	if request.method =='GET': return "list of Room"
	else: return "fail_POST_CANCEL"
if __name__ == '__main__':
	app.run()

# ///////////////////////////////////////////////////////
