#import
from pymongo import MongoClient
import random
import string
from datetime import datetime, time as datetime_time, timedelta
import pprint
import json
from flask import Flask, url_for,Response,request,json
#print(json.dumps(json_data,sort_keys=True,indent=2)) 
def Jprint(JSON):
  print(json.dumps(JSON,sort_keys=True,indent=2))
 
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
		return json.dumps(respond)

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
	
	def find_room(self,room):
		return self.room.find_one({'room':room})

	def insert_schedule(self,room,json):
		roomdata = self.find_room(room)
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
def checkBook(room,jsond):# can Book or not
	date = jsond['Data_Time']
	thisroom = DB.find_room(room)
	schedule = thisroom['schedule']
	if not schedule:
		return True
	if jsond in schedule :
		return False
	date_time2 = date.split()
	for i in range(len(schedule)) :
		date_time1 = schedule[i]['Data_Time'].split()
		if date_time2[0] == date_time1[0]: #date check
			db_s,db_e = [datetime.strptime(t, '%H:%M') for t in date_time1[1].split('-')]
			s,e = [datetime.strptime(t, '%H:%M') for t in date_time2[1].split('-')]
			if not ( (s < db_s and e <= db_s) or (s >= db_e and e > db_e) ) :
				return False
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
		if checkBook(d['Room'],jsond) :
			DB.insert_schedule(d['Room'],jsond)
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
		if(len(data["Password"])<17 and len(data["Password"])>7):
			return DB.register(str(data["Password"]),str(data["Password"]))
		else:
			respond = {"status":"fail","error":"your password must contain between 8 and 15 letters and numbers"}
			return json.dumps(respond)
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
