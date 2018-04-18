#import
from pymongo import MongoClient
import random
import string
from datetime import datetime, time as datetime_time, timedelta
import pprint
import json
from flask import Flask, url_for,Response,request,json
from time import gmtime, strftime

# ////////////////////////////////////////////////////////
# load config
class config:
	def __init__(self):
		file_config = open("config.conf","r")
		self.read_config = {}
		for line in file_config:
			buf = line.strip().split("=")
			self.read_config[buf[0]] = buf[1]
	def get_config(self):
		return self.read_config

CONFIG = config()
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
		config = CONFIG.get_config()
		login = config['dbuser']+config['dbpass']
		if not(login==""):
			login=login+'@'
		else:
			printdata("[Warning]: database no auth")
		printdata("[info]:connection database "+'mongodb://'+ login + config['db_address']+':'+config['db_port'])
		self.client = MongoClient('mongodb://'+ login + config['db_address']+':'+config['db_port'])
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
		print(str(self.user.find_one({"$and":[{"username":username},{"password":password}]}))=="None")
		print((self.user.find_one({"$and":[{"username":username},{"password":password}]})))
		if str(self.user.find_one({"$and":[{"username":username},{"password":password}]}))=="None":
			print("tewt")
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
		roomdata = self.room.find_one({'room':room})
		schedule = roomdata['schedule']
		schedule.append(json)
		self.room.update_one({'room':room},{'$set':{'schedule':schedule}})
		return True
	def remove_schedule(self,room,username,data_time):
		roomdata = self.room.find_one({'room':room})
		schedule = roomdata['schedule']
		for i in range(len(schedule)):
			if schedule[i]['Username'] == username and schedule[i]['Data_Time'] == data_time:
				del schedule[i]
				break
		self.room.update_one({'room':room},{'$set':{'schedule':schedule}})

 
DB = database()

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

def checkBook(username,data):# can Book or not
	date = data['Data_Time']
	cell = {'Username':username,'Data_Time':date}

	#room_db = list(findkeys(DB.get_room(), "room"))
	#date_db = list(findkeys(DB.get_room(), "Data_Time"))
	thisroom = DB.room.find_one({'room':data['Room']})#checkroom
	schedule = thisroom['schedule']
	if not schedule:
		schedule.append(cell)
		DB.room.update_one({'room':data['Room']},{'$set':{'schedule':schedule}})
		return True
	if cell in schedule :
		return False
	date_time2 = date.split()
	for i in range(len(schedule)) :
		date_time1 = schedule[i]['Data_Time'].split()
		print(date_time1[0],'====',date_time2[0])
		if date_time2[0] == date_time1[0]: #date check
			db_s,db_e = [datetime.strptime(t, '%H:%M') for t in date_time1[1].split('-')]
			s,e = [datetime.strptime(t, '%H:%M') for t in date_time2[1].split('-')]
			if not ( (s < db_s and e <= db_s) or (s >= db_e and e > db_e) ) :
				return False
	schedule.append(cell)
	DB.room.update_one({'room':data['Room']},{'$set':{'schedule':schedule}})
	return True

def Book(JSONINPUT):
	data = JSONINPUT['Data']
	DB.whois(JSONINPUT['cookie_session'])
	username = DB.whois(JSONINPUT['cookie_session'])
	respond = {"status":"sucess","error":"none"}
	respond_err = {"status":"fail","error":"Have reservations !!"}
	set_return = []
	Res = {}
	for d in data:
		jsond = {'Username': username,'Data_Time':d['Data_Time']}
		if checkBook(username,d) :
			#DB.insert_schedule(d['Room'],jsond)
			set_return.append(respond)
		else:
			set_return.append(respond_err)
	Res['respond'] = set_return
	return json.dumps(Res)

# ///////////////////////////////////////////////////////
# login
def Login(input):
	return DB.login(input["Username"],input["Password"])
# # ///////////////////////////////////////////////////////
# # cancel


# # ///////////////////////////////////////////////////////
# # register
def Register(data):
	if (DB.have_user(data["Username"])):
		respond = {"status":"fail","error":"This username is already in use"}
		return json.dumps(respond)
	else:
		return DB.register(str(data["Username"]),str(data["Password"]))
# # ///////////////////////////////////////////////////////
# # get room
def Get_room():
	return json.dumps(DB.get_room())

# # ///////////////////////////////////////////////////////
# # Route

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
				return Book(request.json)
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

runat = CONFIG.get_config()
if __name__ == '__main__':
	app.run(host=runat['server_address'],port=int(runat['server_port']))

# # ///////////////////////////////////////////////////////
