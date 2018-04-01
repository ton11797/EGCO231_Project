#import
from pymongo import MongoClient
import random
import string

from datetime import datetime, time as datetime_time, timedelta
import pprint
import json

from flask import Flask, url_for,Response,request,json
from time import gmtime, strftime
#print(json.dumps(json_data,sort_keys=True,indent=2)) 
def Jprint(JSON):
	print(json.dumps(JSON,sort_keys=True,indent=2))

# ////////////////////////////////////////////////////////
# load config
def load_config():
	file_config = open("config.conf","r")
	read_config = {}
	print(file_config)
	for line in file_config:
		buf = line.strip().split("=")
		read_config[buf[0]] = buf[1]
	return read_config
# ///////////////////////////////////////////////////////
# log
def printdata(data):
    file = open("log.txt","a")
    print(data)
    file.write(data+"\n")
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
			self.user.insert_one({"username":username,"password":password})
			respond = {"status":"sucess","error":"none"}
			return json.dumps(respond)

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
		self.random = self.random + strftime("%m%d%H%M%S",gmtime())
		printdata("[login]: "+ username + " login at "  + strftime("%Y/%m/%d %H:%M:%S",gmtime()))
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

	def whois(self,cookies):
		return self.session.find_one({"cookies":cookies})['username']
	
	def insert_schedule(self,room,json):
		roomdata = self.room.find_one({'Room':room})
		schedule = roomdata['schedule']
		schedule.append(json)
		self.room.update_one({'room':room},{'$set':{'schedule':schedule}})
		return True

	def remove_schedule(self,room,username,data_time):
		roomdata = self.room.find_one({'Room':room})
		schedule = roomdata['schedule']
		for i in range(len(schedule)):
			if schedule[i]['Username'] == username and schedule[i]['Data_Time'] == data_time:
				del schedule[i]
				break
		self.room.update_one({'room':room},{'$set':{'schedule':schedule}})
		

DB = database()
DB.remove_schedule("meeting room",'toasdfn','25/4/2561 12:00-16:00')
# ///////////////////////////////////////////////////////
# book
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

def checkBook(data):# can Book or not
	room = data['Room']
	date = data['Data_Time']

	room_db = list(findkeys(DB.get_room(), "Room"))
	date_db = list(findkeys(DB.get_room(), "Data_Time"))
	# print(room,date)
	# print(room_db,date_db)

	if room in room_db :
		if date in date_db :
			return False
		else:
			for d in date_db:
				date_time1 = d.split()
				date_time2 = date.split()
				if date_time2[0] in date_time1[0]: #date check
					db_s,db_e = [datetime.strptime(t, '%H:%M') for t in date_time1[1].split('-')]
					s,e = [datetime.strptime(t, '%H:%M') for t in date_time2[1].split('-')]
					if ( (s < db_s and e <= db_s) or (s >= db_e and e > db_e) ) :
						return True
	return True

def Book(JSONINPUT):
	data = JSONINPUT['Data']
	username = DB.whois(JSONINPUT['cookie_session'])	
	respond = {"status":"sucess","error":"none"}
	respond_err = {"status":"fail","error":"Have reservations !!"}
	set_return = []
	Res = {}
	for d in data:
		json = {'Username': username,
				'Data_Time':d['Data_Time']}
		#Jprint(json)
		if checkBook(d) :
			DB.insert_schedule(d['Room'],json)
			set_return.append(respond)
		else:
			set_return.append(respond_err)
	Res['respond'] = set_return
	return Res

JSONINPUT = json.load(open('egco231_putroom.json'))
#print(list(findkeys(JSONINPUT , "Room")))
Jprint(Book(JSONINPUT))

# # ///////////////////////////////////////////////////////
# # login
# def Login(input):
# 	return DB.login(input["Username"],input["Password"])
# # # ///////////////////////////////////////////////////////
# # # cancel


# # # ///////////////////////////////////////////////////////
# # # register
# def Register(data):
# 	if (DB.have_user(data["Username"])):
# 		respond = {"status":"fail","error":"This username is already in use"}
# 		return json.dumps(respond)
# 	else:
# 		if(len(data["Password"])<17 and len(data["Password"])>7):
# 			return DB.register(str(data["Password"]),str(data["Password"]))
# 		else:
# 			respond = {"status":"fail","error":"your password must contain between 8 and 15 letters and numbers"}
# 			return json.dumps(respond)
# # # ///////////////////////////////////////////////////////
# # # get room
# def Get_room():
# 	return DB.get_room()

# # # ///////////////////////////////////////////////////////
# # # Route

# app = Flask(__name__)

# @app.route('/login', methods = ['POST'])
# def api_login():
# 	if request.method =='POST':
# 		if request.headers['Content-Type'] == 'application/json':
# 			return Login(request.json)
# 		else:
# 			return "415 Unsupported Media Type ;)"
# 	else: return "fail_POST_LOGIN"

# @app.route('/regis', methods = ['POST'])
# def api_regis():
# 	if request.method =='POST':
# 		if request.headers['Content-Type'] == 'application/json':
# 			return Register(request.json)
# 		else:
# 			return "415 Unsupported Media Type ;)"
# 	else: return "fail_POST_REGIS"

# @app.route('/book', methods = ['POST'])
# def api_book():
# 	if request.method =='POST':
# 		if (request.headers['Content-Type'] == 'application/json'):
# 				return Book(request.json)
# 		else:
# 			return "415 Unsupported Media Type ;)"
# 	else: return "fail_POST_BOOK"

# @app.route('/cancel', methods = ['POST'])
# def api_cancel():
# 	if request.method =='POST':
# 		if (request.headers['Content-Type'] == 'application/json'):
# 				return "JSON Message: " + json.dumps(request.json)
# 		else:
# 			return "415 Unsupported Media Type ;)"
# 	else: return "fail_POST_CANCEL"
# @app.route('/list', methods = ['GET'])
# def api_list():
# 	if request.method =='GET': return Get_room()
# 	else: return "fail_POST_CANCEL"
# if __name__ == '__main__':
# 	app.run()

# # ///////////////////////////////////////////////////////
