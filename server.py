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
		self.URI = "mongodb+srv://root:root@egco231-ettdb.mongodb.net" 
		self.client = MongoClient(self.URI)
		self.db = self.client['EGCO231']
		self.user = self.db['userData']
		self.room = self.db['Room']
		self.session = self.db['loginSession ']

	def have_user(self,username):
		
		if str(self.user.find_one({"username":username})) == "None":
			return False
		else:
			return True

	def register(self,username,password):
		if self.have_user(username):
			respond = {"status":"Fail","error":"username exist"}
			return json.dumps(respond)
		else:
			self.user.insert_one({"Username":username,"Password":password})
			respond = {"status":"sucess","error":"username exist"}
			return json.dumps(respond)

	def rand_string(self,length, char_set=10):
		output = ''
		for _ in range(length): output += random.choice(char_set)
		return output

	def get_room(self):
		collect = self.room.find({})
		array =[]
		for c in collect:
			del c['_id']
			array.append(c)
		respond = {"available-room":array}
		return respond

	def genCookies(self,username):
		self.random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
		self.session.insert_one({"username":username,"cookies":self.random})
		return self.random

	def login(self,username,password):
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

	def insert(self,json):
		self.room.insert_one(json)


JSONINPUT = json.load(open('EGCO231_getroom.json'))
DB = database()
#DB.insert(JSONINPUT)
# print(DB.have_user("admin"))

#print(DB.login("admin","123"))
#printdata("test\n")




# ///////////////////////////////////////////////////////
# book

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

def findkeys(node, kv):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, kv):
               yield x
    elif isinstance(node, dict):
        if kv in node:
            yield node[kv]
        for j in node.values():
            for x in findkeys(j, kv):
                yield x

# s,e = [datetime.strptime(t, '%H:%M') for t in dateTime[1].split('-')]
# iss,ie = [datetime.strptime(t, '%H:%M') for t in d[1].split('-')]

def checkBook(input):


	for data in input:
		room = data['Room']
		date = data['Data_Time']

		room_db = list(findkeys(DB.get_room(), "Room"))
		date_db = list(findkeys(DB.get_room(), "Data_Time"))

		if room in room_db :
			if date in date_db :
				return False
			else:
				for d in date_db:
					date_time1 = d.split()
					date_time2 = date.split()
					if date_time2[0] in date_time1[0]: #date check
						db_s,db_e = [datetime.strptime(t, '%H:%M') for t in date_time1[1].split('-')]
						# timedb_diff = time_diff(db_s, db_e)
						s,e = [datetime.strptime(t, '%H:%M') for t in date_time2[1].split('-')]
						# time_diff = time_diff(s, e)

						if ( (s < db_s and e <= db_s) or (s >= db_e and e > db_e) ) :
							return True
			
		return True

#checkBook('JSONINPUT')
def Book(JSONINPUT):
	data = JSONINPUT['Data']
	cs = JSONINPUT['cookie_session']
	respond = {"status":"sucess","error":"none"}
	respond_err = {"status":"fail","error":"Have reservations !!"}

	if checkBook(data) :
		DB.insert(JSONINPUT) 
		return json.dumps(respond)
	return json.dumps(respond_err)

JSONINPUT = json.load(open('egco231_putroom.json'))
#print(list(findkeys(JSONINPUT , "Room")))
print(Book(JSONINPUT))
	

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
		if request.headers['Content-Type'] == 'application/json' : return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_LOGIN"

@app.route('/regis', methods = ['POST'])
def api_regis():
	if request.method =='POST':
		if (request.headers['Content-Type'] == 'application/json'):
			return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_REGIS"

@app.route('/book', methods = ['POST'])
def api_book():
	if request.method =='POST':
		if (request.headers['Content-Type'] == 'application/json'):
				return "JSON Message: " + json.dumps(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_BOOK"

@app.route('/cancel', methods = ['POST'])
def api_cancel():
	if request.method =='POST':
		if (request.headers['Content-Type'] == 'application/json'):
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
