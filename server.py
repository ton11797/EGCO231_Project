#import
from pymongo import MongoClient
import random
import uuid
import hashlib
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
		self.user.delete_one({"username":"admin"}) 
		self.user.insert_one({"username":"admin","password":self.hash_password(config['adminpassword'])})
	
	def hash_password(self,password):
		return hashlib.sha256(password.encode()).hexdigest()

	def have_user(self,username):
		if str(self.user.find_one({"username":username})) == "None":
			return False
		else:
			return True
 
	def register(self,username,password):
		if self.have_user(username):
			respond = {"status":"Fail","error":"username exist"}
			return json.dumps(respond,sort_keys=True,indent=2)
		else:
			self.user.insert_one({"username":username,"password":password})
			respond = {"status":"sucess","error":"none"}
			return json.dumps(respond,sort_keys=True,indent=2)
 
	def get_room(self):
		collect = self.room.find({})
		array =[]
		for c in collect:
			del c['_id']
			array.append(c)
		respond = {"available-room":array}
		return json.dumps(respond,sort_keys=True,indent=2)

	def genCookies(self,username):
		self.random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
		self.random = self.random + strftime("%m%d%H%M%S",gmtime())
		printdata("[login]: "+ username + " login at "  + strftime("%Y/%m/%d %H:%M:%S",gmtime()))
		self.session.insert_one({"username":username,"cookies":self.random})
		return self.random
 
	def login(self,username,password):
		print(username)
		print(password)
		if str(self.user.find_one({"username":username,"password":password}))=="None":
			respond = {"status":"Fail","error":"username or password not match"}
			return json.dumps(respond,sort_keys=True,indent=2)
		else:
			self.cookies = self.genCookies(username)
			self.admin = "no"
		if username=="admin":
			self.admin = "yes"
		respond = {"status":"sucess","error":"none","cookie_session":self.cookies,"admin":self.admin}
		return json.dumps(respond,sort_keys=True,indent=2)
 
	def whois(self,cookies):
		return self.session.find_one({"cookies":cookies})['username']
	
	def get_schedule(self,room):
		return self.room.find_one({'room':room})['schedule']

	def insert_schedule(self,room,json):
		schedule = self.get_schedule(room)
		schedule.append(json)
		self.room.update_one({'room':room},{'$set':{'schedule':schedule}})
		return True

	def remove_schedule(self,room,json):
		schedule = self.get_schedule(room)
		for i in range(len(schedule)):
			if schedule[i] == json:
				del schedule[i]
				break
		self.room.update_one({'room':room},{'$set':{'schedule':schedule}})
		return True

 
DB = database()
def Cancel(data):
    booklist = DB.get_room()
    array=[]
    for book in booklist["available-room"]:
        for cancel in data["Data"]:
            if cancel["Room"]==book["Room"]:
                status = False
                for schedule in book["schedule"]:
                    if cancel["Data_Time"]==book["Data_Time"]:
                        if DB.whois(data["cookie_session"])=="admin" or DB.whois(data["cookie_session"])==schedule["Username"]:
                            array.append({"Room":cancel["Room"],"Data_time":cancel["Data_Time"],"status":"success","error":"none"})
                            status = True
                        else:
                            array.append({"Room":cancel["Room"],"Data_time":cancel["Data_Time"],"status":"fail","error":"Permission denied"})
                if status:
                    array.append({"Room":cancel["Room"],"Data_time":cancel["Data_Time"],"status":"fail","error":"Room available"})
    respond = {"Data":array}
    return json.dumps(respond)

# ///////////////////////////////////////////////////////
# book
class Book:
	def __init__(self):
		self.respond 	= {"status":"sucess","error":"none"}
		self.respond_err = {"status":"fail","error":"Have reservations !!"}
		self.respond_cerr = {"status":"fail","error":"Not Have Book on this requests !!"}
		self.respond_cerr2 = {"status":"fail","error":"Error time Book"}
		self.Res = {}
	
	def JsonForm(self,cookie,date,time):
		jsond = {
			'username': DB.whois(cookie),
			'date': date,'time': time
		}
		return jsond

	def checkBook(self,room,data):# can Book or not
		schedule = DB.get_schedule(room)
		if not schedule: 
			return True
		if  data in schedule :
			return False
		for i in range(len(schedule)) :
			if data['date'] == schedule[i]['date'] :
				if data['time'] == schedule[i]['time']:
					return False
				db_s,db_e 	= [datetime.strptime(t,'%H:%M') for t in schedule[i]['time'].split('-')]
				s,e 		= [datetime.strptime(t,'%H:%M') for t in data['time'].split('-')]
				if not ( (s < db_s and e <= db_s) or (s >= db_e and e > db_e) ) :
					return False
		return True

	def At(self,JSONINPUT):
		set_return = []
		for data in JSONINPUT['Data']:
			s,e  = [datetime.strptime(t,'%H:%M') for t in data['time'].split('-')]
			if(s >= e):
				set_return.append(self.respond_cerr2)
			else:
				Json_Form = self.JsonForm(JSONINPUT['cookie_session'],
									data['date'],data['time'])
				if self.checkBook(data['room'],Json_Form ) :
					DB.insert_schedule(data['room'],Json_Form )
					set_return.append(self.respond)
				else:
					set_return.append(self.respond_err)
		self.Res['respond'] = set_return
		return json.dumps(self.Res,sort_keys=True,indent=2)

	def Cancel(self,JSONINPUT):
		set_return = []
		print(JSONINPUT['cookie_session'])
		username = DB.whois(JSONINPUT['cookie_session'])
		for data in JSONINPUT['Data']:
			schedule = DB.get_schedule(data['room'])
			Json_Form = self.JsonForm(JSONINPUT['cookie_session'],data['date'],data['time'])
			
			if username == 'admin':
				for d in schedule :
					if d['date']== data['date'] and d['time'] == data['time']:
						Json_Form = d
						break
			if not schedule:
				set_return.append(self.respond_cerr)
			elif Json_Form in schedule :
				DB.remove_schedule(data['room'],Json_Form)
				set_return.append(self.respond)
			else:
				set_return.append(self.respond_cerr)
		
		self.Res['respond'] = set_return
		return json.dumps(self.Res,sort_keys=True,indent=2)

BK = Book()

# ///////////////////////////////////////////////////////
# login
def Login(input):
	return DB.login(input["Username"],input["Password"])
# # ///////////////////////////////////////////////////////
# # register
def Register(data):
	if (DB.have_user(data["Username"])):
		respond = {"status":"fail","error":"This username is already in use"}
		return json.dumps(respond,sort_keys=True,indent=2)
	else:
			return DB.register(str(data["Username"]),str(data["Password"]))
# # ///////////////////////////////////////////////////////
# # get room
def Get_room():
	return DB.get_room()

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
				return BK.At(request.json)
		else:
			return "415 Unsupported Media Type ;)"
	else: return "fail_POST_BOOK"

@app.route('/cancel', methods = ['POST'])
def api_cancel():
	if request.method =='POST':
		if (request.headers['Content-Type'] == 'application/json'):
				return BK.Cancel(request.json)#"JSON Message: " + json.dumps(request.json)
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
