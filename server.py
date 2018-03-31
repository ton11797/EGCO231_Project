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
    print(data,end="")
    file.write(data)
    file.close
# ///////////////////////////////////////////////////////
# database
class database:
	def __init__(self):
		config = load_config()
		login = config['dbuser']+config['dbpass']
		if not(login==""):
			login=login+'@'
		# self.client = MongoClient('localhost', 27017)
		self.client = MongoClient('mongodb://'+ login + config['server_address']+':'+config['port'])
		self.db = self.client['EGCO']
		self.room = self.db['Room']
		self.session = self.db['loginSession']
		self.user = self.db['userData']
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
		return json.dumps(respond)

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

	def whois(self,cookies):
		return self.session.find_one({"cookies":cookies})['username']

DB = database()
print(DB.whois("WcIiXtzWCxVvo3Hwl33C9EPThCLbafpq"))
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

def checkBook(input):# can Book or not
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
						s,e = [datetime.strptime(t, '%H:%M') for t in date_time2[1].split('-')]
						if ( (s < db_s and e <= db_s) or (s >= db_e and e > db_e) ) :
							return True
		return True

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
def Login(input):
	return DB.login(input["Username"],input["Password"])
# ///////////////////////////////////////////////////////
# cancel


# ///////////////////////////////////////////////////////
# register
def Register(data):
	if (DB.have_user(data["Username"])):
		respond = {"status":"fail","error":"This username is already in use"}
		return json.dumps(respond)
	else:
		if(len(data["Password"])<17 and len(data["Password"])>7):
			return DB.register(str(data["Password"]),str(data["Password"]))
		else:
			respond = {"status":"fail","error":"your password must contain between 8 and 15 letters and numbers"}
			return json.dumps(respond)

# ///////////////////////////////////////////////////////
# get room
def Get_room():
	return DB.get_room()

# ///////////////////////////////////////////////////////
# Route

app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def api_login():
	if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
			return Login(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_LOGIN"

@app.route('/regis', methods = ['POST'])
def api_regis():
	if request.method =='POST':
		if request.headers['Content-Type'] == 'application/json':
			return Register(request.json)
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
	if request.method =='GET': return Get_room()
	else: return "fail_POST_CANCEL"
if __name__ == '__main__':
	app.run()

# ///////////////////////////////////////////////////////
